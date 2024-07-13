"""
generate_spartnkey.py

This script generates a UBX-RXM-SPARTNKEY message used to transfer dynamic SPARTN keys to a u-blox receiver. 
The UBX-RXM-SPARTNKEY message is structured as follows:

- Header: Sync characters, message class, and ID.
- Length: Specifies the length of the payload.
- Payload: Contains the message content, including version, number of keys, reserved bytes, and key data.
- Checksum: Ensures data integrity.

The payload consists of several parts:
1. Version: Message version (typically 0x01).
2. numKeys: Number of keys in the message (0, 1, or 2).
3. reserved0: Reserved bytes.
4. Repeated group for each key, including reserved1, keyLengthBytes, validFromWno (week number), validFromTow (time of week), and the key value itself.

The script reads a JSON configuration file to retrieve the 'current' and 'next' SPARTN keys. Each key's data is then processed to form its respective payload segment. The final UBX message is constructed by concatenating the header, calculated payload length, payload, and checksum. The output is a hexadecimal string representing the UBX-RXM-SPARTNKEY message.
"""


import json
import struct
import datetime

import serial


# Constants - EDIT THESE
UCENTER_JSON_FILE_PATH = 'device-e0535f2c-093d-4957-8879-cfb48528998d-ucenter-config.json'
PORT = "COM9"
BAUD = "38400"

# DONT TOUCH ANYTHING BELOW THIS LINE
GPS_EPOCH = datetime.datetime(1980, 1, 6, 0, 0, 0)
GPS_TIME_OF_WEEK = 86400


def read_json_file(file_path):
    """
    Read JSON data from a file and return the parsed JSON.

    Args:
        file_path (str): The file path to the JSON file containing the key data.

    Returns:
        dict: Parsed JSON data from the file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def calculate_gps_week_number(timestamp_ms):
    """
    Calculate the GPS week number from a given timestamp.

    Args:
        timestamp_ms (int): The timestamp in milliseconds.

    Returns:
        int: The GPS week number.
    """
    date = datetime.datetime.utcfromtimestamp(timestamp_ms / 1000.0)
    return (date - GPS_EPOCH).days // 7


def create_key_payload(key_data):
    """
    Create the payload part of the key from the given key data.

    Args:
        key_data (dict): Contains 'start' timestamp and 'value' of the key.

    Returns:
        bytes: The binary payload for the key.

    Raises:
        ValueError: If the key value length is not 16 bytes.
    """
    week_number = calculate_gps_week_number(key_data["start"])
    gps_time_of_week = GPS_TIME_OF_WEEK
    key_value = bytes.fromhex(key_data["value"])
    if len(key_value) != 16:
        raise ValueError("Key length is not 16 bytes")
    return struct.pack("<BBHI", 0, 16, week_number, gps_time_of_week) + key_value


def calculate_checksum(data):
    """
    Calculate the UBX checksum which is a 2-byte Fletcher Algorithm checksum.

    Args:
        data (bytes): The data over which the checksum is to be calculated.

    Returns:
        tuple: Two-byte checksum.
    """
    ck_a = 0
    ck_b = 0
    for byte in data:
        ck_a = (ck_a + byte) & 0xFF
        ck_b = (ck_b + ck_a) & 0xFF
    return ck_a, ck_b


def main():
    """
    The main function of the script. It performs the following steps:

    1. Read the JSON data from the specified file path. This file contains key information used
       in the UBX-RXM-SPARTNKEY message.
    2. Extract the 'current' and 'next' keys from the JSON data.
    3. Create payloads for both 'current' and 'next' keys using their respective data.
    4. Construct the complete UBX message by assembling different parts in the correct format.
    5. Print the final UBX message in hexadecimal format.

    The UBX message format is a binary protocol designed for u-blox GNSS receivers. This particular
    script focuses on creating a message that transfers dynamic SPARTN keys to the receiver.
    """

    # Load the JSON data containing key information.
    json_data = read_json_file(UCENTER_JSON_FILE_PATH)

    # Check if the JSON data was successfully loaded.
    if json_data is None:
        print("Failed to load JSON data.")
        return

    # Extract the 'current' and 'next' key data from the JSON file.
    current_key = json_data["MQTT"]["dynamickeys"]["current"]
    next_key = json_data["MQTT"]["dynamickeys"]["next"]

    # Create binary payloads for the 'current' and 'next' keys.
    # This involves converting various key attributes (like start time and key value)
    # into a binary format that can be understood by the GNSS receiver.
    current_key_payload = create_key_payload(current_key)
    next_key_payload = create_key_payload(next_key)

    # Define the header for the UBX message. This is a standard format for UBX messages.
    header = b"\xb5\x62\x02\x36"

    # Calculate the total length of the payload. This is essential as it tells the receiver
    # how much data to expect in the message.
    payload_length = 4 + (
        2 * 24
    )  # Includes bytes for version, numKeys, reserved0, and key payloads

    # Convert the payload length to binary format.
    payload_length_bytes = struct.pack("<H", payload_length)

    # Construct the payload by concatenating different parts:
    # - Version and number of keys (as binary data)
    # - The key payloads (excluding the actual key values)
    # - The key values themselves.
    # This sequence is crucial for the receiver to correctly interpret the message.
    payload = struct.pack(
        "<BB2s", 1, 2, b"\x00\x00"
    )  # Version, number of keys, reserved bytes
    payload += (
        current_key_payload[:-16] + next_key_payload[:-16]
    )  # Add key payloads without key values
    payload += (
        current_key_payload[-16:] + next_key_payload[-16:]
    )  # Add actual key values

    # Calculate the checksum for the message. This is a form of error-checking to ensure data integrity.
    ck_a, ck_b = calculate_checksum(header[2:] + payload_length_bytes + payload)

    # Construct the final UBX message by concatenating the header, payload, and checksum.
    ubx_message = header + payload_length_bytes + payload + bytes([ck_a, ck_b])

    # Convert the final UBX message to a hexadecimal string format for easy reading and debugging.
    formatted_hex = " ".join(f"{byte:02x}" for byte in ubx_message)

    # Print the formatted hexadecimal UBX message.
    print(formatted_hex)

    # convert formatted_hex to bytes
    spartnkey = bytes.fromhex(formatted_hex)
    # Send the byte stream to the GPS device
    with serial.Serial(
        PORT, BAUD, timeout=1
    ) as ser:  # replace 'COM_PORT' with your serial port
        ser.write(spartnkey)


# Ensure that the main function is called when the script is executed directly.
if __name__ == "__main__":
    main()
