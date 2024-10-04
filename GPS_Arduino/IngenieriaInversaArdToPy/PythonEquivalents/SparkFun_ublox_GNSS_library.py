
import GPS_Arduino.IngenieriaInversaArdToPy.PythonEquivalents.Wire as i2c
import u_blox_structs
import u_blox_config_keys
from enum import Enum
import struct

debugPin = -1

class sfe_ublox_status_e(Enum):
    SFE_UBLOX_STATUS_SUCCESS = 1
    SFE_UBLOX_STATUS_FAIL = 2
    SFE_UBLOX_STATUS_CRC_FAIL = 3
    SFE_UBLOX_STATUS_TIMEOUT = 4
    SFE_UBLOX_STATUS_COMMAND_NACK = 5
    SFE_UBLOX_STATUS_OUT_OF_RANGE = 6
    SFE_UBLOX_STATUS_INVALID_ARG = 7
    SFE_UBLOX_STATUS_INVALID_OPERATION = 8
    SFE_UBLOX_STATUS_MEM_ERR = 9
    SFE_UBLOX_STATUS_HW_ERR = 10
    SFE_UBLOX_STATUS_DATA_SENT = 11
    SFE_UBLOX_STATUS_DATA_RECEIVED = 12
    SFE_UBLOX_STATUS_I2C_COMM_FAILURE = 13
    SFE_UBLOX_STATUS_DATA_OVERWRITTEN = 14

class sfe_ublox_packet_validity_e(Enum):
    SFE_UBLOX_PACKET_VALIDITY_NOT_VALID = 1
    SFE_UBLOX_PACKET_VALIDITY_VALID = 2
    SFE_UBLOX_PACKET_VALIDITY_NOT_DEFINED = 3
    SFE_UBLOX_PACKET_NOTACKNOWLEDGED = 4


class sfe_ublox_packet_buffer_e(Enum):
    SFE_UBLOX_PACKET_PACKETCFG = 1
    SFE_UBLOX_PACKET_PACKETACK = 2
    SFE_UBLOX_PACKET_PACKETBUF = 3
    SFE_UBLOX_PACKET_PACKETAUTO = 4

class bits:
    def __init__(self, all, UBX_NMEA_DTM, UBX_NMEA_GAQ, UBX_NMEA_GBQ, UBX_NMEA_GBS, UBX_NMEA_GGA, UBX_NMEA_GLL, UBX_NMEA_GLQ, UBX_NMEA_GNQ,UBX_NMEA_GNS, UBX_NMEA_GPQ ,UBX_NMEA_GQQ, UBX_NMEA_GRS, UBX_NMEA_GSA, UBX_NMEA_GST, UBX_NMEA_GSV, UBX_NMEA_RLM, UBX_NMEA_RMC, UBX_NMEA_TXT, UBX_NMEA_VLW, UBX_NMEA_VTG, UBX_NMEA_ZDA):
            self.all = all
            self.UBX_NMEA_DTM = UBX_NMEA_DTM
            self.UBX_NMEA_CAQ = UBX_NMEA_GAQ
            self.UBX_NMEA_GBQ = UBX_NMEA_GBQ
            self.UBX_NMEA_GBS = UBX_NMEA_GBS
            self.UBX_NMEA_GGA = UBX_NMEA_GGA
            self.UBX_NMEA_GLL = UBX_NMEA_GLL
            self.UBX_NMEA_GLQ = UBX_NMEA_GLQ
            self.UBX_NMEA_GNQ = UBX_NMEA_GNQ
            self.UBX_NMEA_GNS = UBX_NMEA_GNS
            self.UBX_NMEA_GPQ = UBX_NMEA_GPQ
            self.UBX_NMEA_GQQ = UBX_NMEA_GQQ
            self.UBX_NMEA_GRS = UBX_NMEA_GRS
            self.UBX_NMEA_GSA = UBX_NMEA_GSA
            self.UBX_NMEA_GST = UBX_NMEA_GST
            self.UBX_NMEA_GSV = UBX_NMEA_GSV
            self.UBX_NMEA_RLM = UBX_NMEA_RLM
            self.UBX_NMEA_RMC = UBX_NMEA_RMC
            self.UBX_NMEA_TXT = UBX_NMEA_TXT
            self.UBX_NMEA_VLW = UBX_NMEA_VLW
            self.UBX_NMEA_VTG= UBX_NMEA_VTG
            self.UBX_NMEA_ZDA = UBX_NMEA_ZDA



class sfe_ublox_nmea_filtering_t:
    def __init__(self, all, bits:bits):
        self.all = all
        self.bits = bits


class sfe_ublox_nmea_filtering_e(Enum):
    SFE_UBLOX_FILTER_NMEA_ALL = 0x00000001
    SFE_UBLOX_FILTER_NMEA_DTM = 0x00000002
    SFE_UBLOX_FILTER_NMEA_GAQ = 0x00000004
    SFE_UBLOX_FILTER_NMEA_GBQ = 0x00000008
    SFE_UBLOX_FILTER_NMEA_GBS = 0x00000010
    SFE_UBLOX_FILTER_NMEA_GGA = 0x00000020
    SFE_UBLOX_FILTER_NMEA_GLL = 0x00000040
    SFE_UBLOX_FILTER_NMEA_GLQ = 0x00000080
    SFE_UBLOX_FILTER_NMEA_GNQ = 0x00000100
    SFE_UBLOX_FILTER_NMEA_GNS = 0x00000200
    SFE_UBLOX_FILTER_NMEA_GPQ = 0x00000400
    SFE_UBLOX_FILTER_NMEA_GQQ = 0x00000800
    SFE_UBLOX_FILTER_NMEA_GRS = 0x00001000
    SFE_UBLOX_FILTER_NMEA_GSA = 0x00002000
    SFE_UBLOX_FILTER_NMEA_GST = 0x00004000
    SFE_UBLOX_FILTER_NMEA_GSV = 0x00008000
    SFE_UBLOX_FILTER_NMEA_RLM = 0x00010000
    SFE_UBLOX_FILTER_NMEA_RMC = 0x00020000
    SFE_UBLOX_FILTER_NMEA_TXT = 0x00040000
    SFE_UBLOX_FILTER_NMEA_VLW = 0x00080000
    SFE_UBLOX_FILTER_NMEA_VTG = 0x00100000
    SFE_UBLOX_FILTER_NMEA_ZDA = 0x00200000


UBX_SYNCH_1 = 0xB5
UBX_SYNCH_2 = 0x62

# The following are UBX Class IDs. Descriptions taken from ZED-F9P Interface Description Document page 32, NEO-M8P Interface Description page 145
UBX_CLASS_NAV = 0x01  # Navigation Results Messages: Position, Speed, Time, Acceleration, Heading, DOP, SVs used
UBX_CLASS_RXM = 0x02  # Receiver Manager Messages: Satellite Status, RTC Status
UBX_CLASS_INF = 0x04  # Information Messages: Printf-Style Messages, with IDs such as Error, Warning, Notice
UBX_CLASS_ACK = 0x05  # Ack/Nak Messages: Acknowledge or Reject messages to UBX-CFG input messages
UBX_CLASS_CFG = 0x06  # Configuration Input Messages: Configure the receiver.
UBX_CLASS_UPD = 0x09  # Firmware Update Messages: Memory/Flash erase/write, Reboot, Flash identification, etc.
UBX_CLASS_MON = 0x0A  # Monitoring Messages: Communication Status, CPU Load, Stack Usage, Task Status
UBX_CLASS_AID = 0x0B  #(NEO-M8P ONLY!!!) AssistNow Aiding Messages: Ephemeris, Almanac, other A-GPS data input
UBX_CLASS_TIM = 0x0D  # Timing Messages: Time Pulse Output, Time Mark Results
UBX_CLASS_ESF = 0x10  #(NEO-M8P ONLY!!!) External Sensor Fusion Messages: External Sensor Measurements and Status Information
UBX_CLASS_MGA = 0x13  # Multiple GNSS Assistance Messages: Assistance data for various GNSS
UBX_CLASS_LOG = 0x21  # Logging Messages: Log creation, deletion, info and retrieval
UBX_CLASS_SEC = 0x27  # Security Feature Messages
UBX_CLASS_HNR = 0x28  #(NEO-M8P ONLY!!!) High Rate Navigation Results Messages: High rate time, position speed, heading
UBX_CLASS_NMEA = 0xF0 # NMEA Strings: standard NMEA strings
UBX_CLASS_PUBX = 0xF1 # Proprietary NMEA-format messages defined by u-blox

# Class: CFG
# The following are used for configuration. Descriptions are from the ZED-F9P Interface Description pg 33-34 and NEO-M9N Interface Description pg 47-48
UBX_CFG_ANT = 0x13       # Antenna Control Settings. Used to configure the antenna control settings
UBX_CFG_BATCH = 0x93     # Get/set data batching configuration.
UBX_CFG_CFG = 0x09       # Clear, Save, and Load Configurations. Used to save current configuration
UBX_CFG_DAT = 0x06       # Set User-defined Datum or The currently defined Datum
UBX_CFG_DGNSS = 0x70     # DGNSS configuration
UBX_CFG_ESFALG = 0x56    # ESF alignment
UBX_CFG_ESFA = 0x4C      # ESF accelerometer
UBX_CFG_ESFG = 0x4D      # ESF gyro
UBX_CFG_GEOFENCE = 0x69  # Geofencing configuration. Used to configure a geofence
UBX_CFG_GNSS = 0x3E      # GNSS system configuration
UBX_CFG_HNR = 0x5C       # High Navigation Rate
UBX_CFG_INF = 0x02       # Depending on packet length, either: poll configuration for one protocol, or information message configuration
UBX_CFG_ITFM = 0x39      # Jamming/Interference Monitor configuration
UBX_CFG_LOGFILTER = 0x47 # Data Logger Configuration
UBX_CFG_MSG = 0x01       # Poll a message configuration, or Set Message Rate(s), or Set Message Rate
UBX_CFG_NAV5 = 0x24      # Navigation Engine Settings. Used to configure the navigation engine including the dynamic model.
UBX_CFG_NAVX5 = 0x23     # Navigation Engine Expert Settings
UBX_CFG_NMEA = 0x17      # Extended NMEA protocol configuration V1
UBX_CFG_ODO = 0x1E       # Odometer, Low-speed COG Engine Settings
UBX_CFG_PM2 = 0x3B       # Extended power management configuration
UBX_CFG_PMS = 0x86       # Power mode setup
UBX_CFG_PRT = 0x00       # Used to configure port specifics. Polls the configuration for one I/O Port, or Port configuration for UART ports, or Port configuration for USB port, or Port configuration for SPI port, or Port configuration for DDC port
UBX_CFG_PWR = 0x57       # Put receiver in a defined power state
UBX_CFG_RATE = 0x08      # Navigation/Measurement Rate Settings. Used to set port baud rates.
UBX_CFG_RINV = 0x34      # Contents of Remote Inventory
UBX_CFG_RST = 0x04       # Reset Receiver / Clear Backup Data Structures. Used to reset device.
UBX_CFG_RXM = 0x11       # RXM configuration
UBX_CFG_SBAS = 0x16      # SBAS configuration
UBX_CFG_TMODE3 = 0x71    # Time Mode Settings 3. Used to enable Survey In Mode
UBX_CFG_TP5 = 0x31       # Time Pulse Parameters
UBX_CFG_USB = 0x1B       # USB Configuration
UBX_CFG_VALDEL = 0x8C    # Used for config of higher version u-blox modules (ie protocol v27 and above). Deletes values corresponding to provided keys/ provided keys with a transaction
UBX_CFG_VALGET = 0x8B    # Used for config of higher version u-blox modules (ie protocol v27 and above). Configuration Items
UBX_CFG_VALSET = 0x8A    # Used for config of higher version u-blox modules (ie protocol v27 and above). Sets values corresponding to provided key-value pairs/ provided key-value pairs within a transaction.

# Class: NMEA
# The following are used to enable NMEA messages. Descriptions come from the NMEA messages overview in the ZED-F9P Interface Description
UBX_NMEA_MSB = 0xF0 # All NMEA enable commands have 0xF0 as MSB. Equal to UBX_CLASS_NMEA
UBX_NMEA_DTM = 0x0A # GxDTM (datum reference)
UBX_NMEA_GAQ = 0x45 # GxGAQ (poll a standard message (if the current talker ID is GA))
UBX_NMEA_GBQ = 0x44 # GxGBQ (poll a standard message (if the current Talker ID is GB))
UBX_NMEA_GBS = 0x09 # GxGBS (GNSS satellite fault detection)
UBX_NMEA_GGA = 0x00 # GxGGA (Global positioning system fix data)
UBX_NMEA_GLL = 0x01 # GxGLL (latitude and long, whith time of position fix and status)
UBX_NMEA_GLQ = 0x43 # GxGLQ (poll a standard message (if the current Talker ID is GL))
UBX_NMEA_GNQ = 0x42 # GxGNQ (poll a standard message (if the current Talker ID is GN))
UBX_NMEA_GNS = 0x0D # GxGNS (GNSS fix data)
UBX_NMEA_GPQ = 0x40 # GxGPQ (poll a standard message (if the current Talker ID is GP))
UBX_NMEA_GQQ = 0x47 # GxGQQ (poll a standard message (if the current Talker ID is GQ))
UBX_NMEA_GRS = 0x06 # GxGRS (GNSS range residuals)
UBX_NMEA_GSA = 0x02 # GxGSA (GNSS DOP and Active satellites)
UBX_NMEA_GST = 0x07 # GxGST (GNSS Pseudo Range Error Statistics)
UBX_NMEA_GSV = 0x03 # GxGSV (GNSS satellites in view)
UBX_NMEA_RLM = 0x0B # GxRMC (Return link message (RLM))
UBX_NMEA_RMC = 0x04 # GxRMC (Recommended minimum data)
UBX_NMEA_TXT = 0x41 # GxTXT (text transmission)
UBX_NMEA_VLW = 0x0F # GxVLW (dual ground/water distance)
UBX_NMEA_VTG = 0x05 # GxVTG (course over ground and Ground speed)
UBX_NMEA_ZDA = 0x08 # GxZDA (Time and Date)

# The following are used to configure the NMEA protocol main talker ID and GSV talker ID
UBX_NMEA_MAINTALKERID_NOTOVERRIDDEN = 0x00 # main talker ID is system dependent
UBX_NMEA_MAINTALKERID_GP = 0x01            # main talker ID is GPS
UBX_NMEA_MAINTALKERID_GL = 0x02            # main talker ID is GLONASS
UBX_NMEA_MAINTALKERID_GN = 0x03            # main talker ID is combined receiver
UBX_NMEA_MAINTALKERID_GA = 0x04            # main talker ID is Galileo
UBX_NMEA_MAINTALKERID_GB = 0x05            # main talker ID is BeiDou
UBX_NMEA_GSVTALKERID_GNSS = 0x00           # GNSS specific Talker ID (as defined by NMEA)
UBX_NMEA_GSVTALKERID_MAIN = 0x01           # use the main Talker ID

# Class: PUBX
# The following are used to enable PUBX messages with configureMessage
# See the M8 receiver description & protocol specification for more details
UBX_PUBX_CONFIG = 0x41   # Set protocols and baud rate
UBX_PUBX_POSITION = 0x00 # Lat/Long position data
UBX_PUBX_RATE = 0x40     # Set/get NMEA message output rate
UBX_PUBX_SVSTATUS = 0x03 # Satellite status
UBX_PUBX_TIME = 0x04     # Time of day and clock information

# Class: HNR
# The following are used to configure the HNR message rates
UBX_HNR_ATT = 0x01 # HNR Attitude
UBX_HNR_INS = 0x02 # HNR Vehicle Dynamics
UBX_HNR_PVT = 0x00 # HNR PVT

# Class: INF
# The following are used to configure INF UBX messages (information messages).  Descriptions from UBX messages overview (ZED_F9P Interface Description Document page 34)
UBX_INF_CLASS = 0x04   # All INF messages have 0x04 as the class
UBX_INF_DEBUG = 0x04   # ASCII output with debug contents
UBX_INF_ERROR = 0x00   # ASCII output with error contents
UBX_INF_NOTICE = 0x02  # ASCII output with informational contents
UBX_INF_TEST = 0x03    # ASCII output with test contents
UBX_INF_WARNING = 0x01 # ASCII output with warning contents

# Class: LOG
# The following are used to configure LOG UBX messages (loggings messages).  Descriptions from UBX messages overview (ZED_F9P Interface Description Document page 34)
UBX_LOG_CREATE = 0x07           # Create Log File
UBX_LOG_ERASE = 0x03            # Erase Logged Data
UBX_LOG_FINDTIME = 0x0E         # Find index of a log entry based on a given time, or response to FINDTIME requested
UBX_LOG_INFO = 0x08             # Poll for log information, or Log information
UBX_LOG_RETRIEVEPOSEXTRA = 0x0F # Odometer log entry
UBX_LOG_RETRIEVEPOS = 0x0B      # Position fix log entry
UBX_LOG_RETRIEVESTRING = 0x0D   # Byte string log entry
UBX_LOG_RETRIEVE = 0x09         # Request log data
UBX_LOG_STRING = 0x04           # Store arbitrary string on on-board flash

# Class: MGA
# The following are used to configure MGA UBX messages (Multiple GNSS Assistance Messages).  Descriptions from UBX messages overview (ZED_F9P Interface Description Document page 34)
UBX_MGA_ACK_DATA0 = 0x60      # Multiple GNSS Acknowledge message
UBX_MGA_ANO = 0x20            # Multiple GNSS AssistNow Offline assistance - NOT SUPPORTED BY THE ZED-F9P! "The ZED-F9P supports AssistNow Online only."
UBX_MGA_BDS_EPH = 0x03        # BDS Ephemeris Assistance
UBX_MGA_BDS_ALM = 0x03        # BDS Almanac Assistance
UBX_MGA_BDS_HEALTH = 0x03     # BDS Health Assistance
UBX_MGA_BDS_UTC = 0x03        # BDS UTC Assistance
UBX_MGA_BDS_IONO = 0x03       # BDS Ionospheric Assistance
UBX_MGA_DBD = 0x80            # Either: Poll the Navigation Database, or Navigation Database Dump Entry
UBX_MGA_GAL_EPH = 0x02        # Galileo Ephemeris Assistance
UBX_MGA_GAL_ALM = 0x02        # Galileo Almanac Assitance
UBX_MGA_GAL_TIMOFFSET = 0x02  # Galileo GPS time offset assistance
UBX_MGA_GAL_UTC = 0x02        # Galileo UTC Assistance
UBX_MGA_GLO_EPH = 0x06        # GLONASS Ephemeris Assistance
UBX_MGA_GLO_ALM = 0x06        # GLONASS Almanac Assistance
UBX_MGA_GLO_TIMEOFFSET = 0x06 # GLONASS Auxiliary Time Offset Assistance
UBX_MGA_GPS_EPH = 0x00        # GPS Ephemeris Assistance
UBX_MGA_GPS_ALM = 0x00        # GPS Almanac Assistance
UBX_MGA_GPS_HEALTH = 0x00     # GPS Health Assistance
UBX_MGA_GPS_UTC = 0x00        # GPS UTC Assistance
UBX_MGA_GPS_IONO = 0x00       # GPS Ionosphere Assistance
UBX_MGA_INI_POS_XYZ = 0x40    # Initial Position Assistance
UBX_MGA_INI_POS_LLH = 0x40    # Initial Position Assitance
UBX_MGA_INI_TIME_UTC = 0x40   # Initial Time Assistance
UBX_MGA_INI_TIME_GNSS = 0x40  # Initial Time Assistance
UBX_MGA_INI_CLKD = 0x40       # Initial Clock Drift Assitance
UBX_MGA_INI_FREQ = 0x40       # Initial Frequency Assistance
UBX_MGA_INI_EOP = 0x40        # Earth Orientation Parameters Assistance
UBX_MGA_QZSS_EPH = 0x05       # QZSS Ephemeris Assistance
UBX_MGA_QZSS_ALM = 0x05       # QZSS Almanac Assistance
UBX_MGA_QZAA_HEALTH = 0x05    # QZSS Health Assistance

# Class: MON
# The following are used to configure the MON UBX messages (monitoring messages). Descriptions from UBX messages overview (ZED_F9P Interface Description Document page 35)
UBX_MON_COMMS = 0x36 # Comm port information
UBX_MON_GNSS = 0x28  # Information message major GNSS selection
UBX_MON_HW2 = 0x0B   # Extended Hardware Status
UBX_MON_HW3 = 0x37   # HW I/O pin information
UBX_MON_HW = 0x09    # Hardware Status
UBX_MON_IO = 0x02    # I/O Subsystem Status
UBX_MON_MSGPP = 0x06 # Message Parse and Process Status
UBX_MON_PATCH = 0x27 # Output information about installed patches
UBX_MON_RF = 0x38    # RF information
UBX_MON_RXBUF = 0x07 # Receiver Buffer Status
UBX_MON_RXR = 0x21   # Receiver Status Information
UBX_MON_SPAN = 0x31  # Signal characteristics
UBX_MON_SYS = 0x39   # Current system performance information
UBX_MON_TXBUF = 0x08 # Transmitter Buffer Status. Used for query tx buffer size/state.
UBX_MON_VER = 0x04   # Receiver/Software Version. Used for obtaining Protocol Version.

# Class: NAV
# The following are used to configure the NAV UBX messages (navigation results messages). Descriptions from UBX messages overview (ZED_F9P Interface Description Document page 35-36)
UBX_NAV_ATT = 0x05       # Vehicle "Attitude" Solution
UBX_NAV_CLOCK = 0x22     # Clock Solution
UBX_NAV_DOP = 0x04       # Dilution of precision
UBX_NAV_EOE = 0x61       # End of Epoch
UBX_NAV_GEOFENCE = 0x39  # Geofencing status. Used to poll the geofence status
UBX_NAV_HPPOSECEF = 0x13 # High Precision Position Solution in ECEF. Used to find our positional accuracy (high precision).
UBX_NAV_HPPOSLLH = 0x14  # High Precision Geodetic Position Solution. Used for obtaining lat/long/alt in high precision
UBX_NAV_ODO = 0x09       # Odometer Solution
UBX_NAV_ORB = 0x34       # GNSS Orbit Database Info
UBX_NAV_PL = 0x62        # Protection Level Information
UBX_NAV_POSECEF = 0x01   # Position Solution in ECEF
UBX_NAV_POSLLH = 0x02    # Geodetic Position Solution
UBX_NAV_PVT = 0x07       # All the things! Position, velocity, time, PDOP, height, h/v accuracies, number of satellites. Navigation Position Velocity Time Solution.
UBX_NAV_PVAT = 0x17      # Navigation position velocity attitude time solution (ZED-F9R only)
UBX_NAV_RELPOSNED = 0x3C # Relative Positioning Information in NED frame
UBX_NAV_RESETODO = 0x10  # Reset odometer
UBX_NAV_SAT = 0x35       # Satellite Information
UBX_NAV_SIG = 0x43       # Signal Information
UBX_NAV_STATUS = 0x03    # Receiver Navigation Status
UBX_NAV_SVIN = 0x3B      # Survey-in data. Used for checking Survey In status
UBX_NAV_TIMEBDS = 0x24   # BDS Time Solution
UBX_NAV_TIMEGAL = 0x25   # Galileo Time Solution
UBX_NAV_TIMEGLO = 0x23   # GLO Time Solution
UBX_NAV_TIMEGPS = 0x20   # GPS Time Solution
UBX_NAV_TIMELS = 0x26    # Leap second event information
UBX_NAV_TIMEUTC = 0x21   # UTC Time Solution
UBX_NAV_VELECEF = 0x11   # Velocity Solution in ECEF
UBX_NAV_VELNED = 0x12    # Velocity Solution in NED
UBX_NAV_AOPSTATUS = 0x60 # AssistNow Autonomous status

# Class: RXM
# The following are used to configure the RXM UBX messages (receiver manager messages). Descriptions from UBX messages overview (ZED_F9P Interface Description Document page 36)
UBX_RXM_COR = 0x34       # Differential correction input status
UBX_RXM_MEASX = 0x14     # Satellite Measurements for RRLP
UBX_RXM_PMP = 0x72       # PMP raw data (NEO-D9S) (two different versions) (packet size for version 0x01 is variable)
UBX_RXM_QZSSL6 = 0x73    # QZSSL6 data (NEO-D9C)
UBX_RXM_PMREQ = 0x41     # Requests a Power Management task (two different packet sizes)
UBX_RXM_RAWX = 0x15      # Multi-GNSS Raw Measurement Data
UBX_RXM_RLM = 0x59       # Galileo SAR Short-RLM report (two different packet sizes)
UBX_RXM_RTCM = 0x32      # RTCM input status
UBX_RXM_SFRBX = 0x13     # Broadcast Navigation Data Subframe
UBX_RXM_SPARTN = 0x33    # SPARTN input status
UBX_RXM_SPARTNKEY = 0x36 # Poll/transfer dynamic SPARTN keys

# Class: SEC
# The following are used to configure the SEC UBX messages (security feature messages). Descriptions from UBX messages overview (ZED_F9P Interface Description Document page 36)
UBX_SEC_UNIQID = 0x03 # Unique chip ID

# Class: TIM
# The following are used to configure the TIM UBX messages (timing messages). Descriptions from UBX messages overview (ZED_F9P Interface Description Document page 36)
UBX_TIM_TM2 = 0x03  # Time mark data
UBX_TIM_TP = 0x01   # Time Pulse Timedata
UBX_TIM_VRFY = 0x06 # Sourced Time Verification

# Class: UPD
# The following are used to configure the UPD UBX messages (firmware update messages). Descriptions from UBX messages overview (ZED-F9P Interface Description Document page 36)
UBX_UPD_SOS = 0x14 # Poll Backup Fil Restore Status, Create Backup File in Flash, Clear Backup File in Flash, Backup File Creation Acknowledge, System Restored from Backup

# The following are used to enable RTCM messages
UBX_RTCM_MSB = 0xF5    # All RTCM enable commands have 0xF5 as MSB
UBX_RTCM_1005 = 0x05   # Stationary RTK reference ARP
UBX_RTCM_1074 = 0x4A   # GPS MSM4
UBX_RTCM_1077 = 0x4D   # GPS MSM7
UBX_RTCM_1084 = 0x54   # GLONASS MSM4
UBX_RTCM_1087 = 0x57   # GLONASS MSM7
UBX_RTCM_1094 = 0x5E   # Galileo MSM4
UBX_RTCM_1097 = 0x61   # Galileo MSM7
UBX_RTCM_1124 = 0x7C   # BeiDou MSM4
UBX_RTCM_1127 = 0x7F   # BeiDou MSM7
UBX_RTCM_1230 = 0xE6   # GLONASS code-phase biases, set to once every 10 seconds
UBX_RTCM_4072_0 = 0xFE # Reference station PVT (ublox proprietary RTCM message)
UBX_RTCM_4072_1 = 0xFD # Additional reference station information (ublox proprietary RTCM message)

# Class: ACK
UBX_ACK_NACK = 0x00
UBX_ACK_ACK = 0x01
UBX_ACK_NONE = 0x02 # Not a real value

# Class: ESF
#  The following constants are used to get External Sensor Measurements and Status
#  Information.
UBX_ESF_MEAS = 0x02
UBX_ESF_RAW = 0x03
UBX_ESF_STATUS = 0x10
UBX_ESF_RESETALG = 0x13
UBX_ESF_ALG = 0x14
UBX_ESF_INS = 0x15 # 36 bytes

SVIN_MODE_DISABLE = 0x00
SVIN_MODE_ENABLE = 0x01

# The following consts are used to configure the various ports and streams for those ports. See -CFG-PRT.
COM_PORT_I2C = 0
COM_PORT_UART1 = 1
COM_PORT_UART2 = 2
COM_PORT_USB = 3
COM_PORT_SPI = 4

COM_TYPE_UBX = (1 << 0)
COM_TYPE_NMEA = (1 << 1)
COM_TYPE_RTCM3 = (1 << 5)
COM_TYPE_SPARTN = (1 << 6)

# Odometer configuration - flags
UBX_CFG_ODO_USE_ODO = (1 << 0)
UBX_CFG_ODO_USE_COG = (1 << 1)
UBX_CFG_ODO_OUT_LP_VEL = (1 << 2)
UBX_CFG_ODO_OUT_LP_COG = (1 << 3)

class odoCfg_e(Enum):
    UBX_CFG_ODO_RUN = 0
    UBX_CFG_ODO_CYCLE = 1
    UBX_CFG_ODO_SWIM = 2
    UBX_CFG_ODO_CAR = 3
    UBX_CFG_ODO_CUSTOM = 4

VAL_CFG_SUBSEC_IOPORT = 0x00000001   # ioPort - communications port settings (causes IO system reset!)
VAL_CFG_SUBSEC_MSGCONF = 0x00000002  # msgConf - message configuration
VAL_CFG_SUBSEC_INFMSG = 0x00000004   # infMsg - INF message configuration
VAL_CFG_SUBSEC_NAVCONF = 0x00000008  # navConf - navigation configuration
VAL_CFG_SUBSEC_RXMCONF = 0x00000010  # rxmConf - receiver manager configuration
VAL_CFG_SUBSEC_SENCONF = 0x00000100  # senConf - sensor interface configuration (requires protocol 19+)
VAL_CFG_SUBSEC_RINVCONF = 0x00000200 # rinvConf - remove inventory configuration
VAL_CFG_SUBSEC_ANTCONF = 0x00000400  # antConf - antenna configuration
VAL_CFG_SUBSEC_LOGCONF = 0x00000800  # logConf - logging configuration
VAL_CFG_SUBSEC_FTSCONF = 0x00001000  # ftsConf - FTS configuration (FTS products only)

# Bitfield wakeupSources for UBX_RXM_PMREQ
VAL_RXM_PMREQ_WAKEUPSOURCE_UARTRX = 0x00000008  # uartrx
VAL_RXM_PMREQ_WAKEUPSOURCE_EXTINT0 = 0x00000020 # extint0
VAL_RXM_PMREQ_WAKEUPSOURCE_EXTINT1 = 0x00000040 # extint1
VAL_RXM_PMREQ_WAKEUPSOURCE_SPICS = 0x00000080   # spics

class dynModel(Enum):
    DYN_MODEL_PORTABLE = 0  #Applications with low acceleration, e.g. portable devices. Suitable for most situations.
    # 1 is not defined
    DYN_MODEL_STATIONARY = 2 # Used in timing applications (antenna must be stationary) or other stationary applications. Velocity restricted to 0 m/s. Zero dynamics assumed.
    DYN_MODEL_PEDESTRIAN = 3     # Applications with low acceleration and speed, e.g. how a pedestrian would move. Low acceleration assumed.
    DYN_MODEL_AUTOMOTIVE = 4  # Used for applications with equivalent dynamics to those of a passenger car. Low vertical acceleration assumed
    DYN_MODEL_SEA = 4            # Recommended for applications at sea, with zero vertical velocity. Zero vertical velocity assumed. Sea level assumed.
    DYN_MODEL_AIRBORNE1g = 5     # Airborne <1g acceleration. Used for applications with a higher dynamic range and greater vertical acceleration than a passenger car. No 2D position fixes supported.
    DYN_MODEL_AIRBORNE2g = 6     # Airborne <2g acceleration. Recommended for typical airborne environments. No 2D position fixes supported.
    DYN_MODEL_AIRBORNE4g = 7     # Airborne <4g acceleration. Only recommended for extremely dynamic environments. No 2D position fixes supported.
    DYN_MODEL_WRIST = 8          # Not supported in protocol versions less than 18. Only recommended for wrist worn applications. Receiver will filter out arm motion.
    DYN_MODEL_BIKE = 9           # Supported in protocol versions 19.2. (not available in all products)
    DYN_MODEL_MOWER = 10          # Added in HPS 1.21 (not available in all products)
    DYN_MODEL_ESCOOTER = 11       # Added in HPS 1.21 (not available in all products)
    DYN_MODEL_UNKNOWN = 255

class sfe_ublox_gnss_ids_e(Enum):
    SFE_UBLOX_GNSS_ID_GPS = 1
    SFE_UBLOX_GNSS_ID_SBAS = 2
    SFE_UBLOX_GNSS_ID_GALILEO = 3
    SFE_UBLOX_GNSS_ID_BEIDOU = 4
    SFE_UBLOX_GNSS_ID_IMES = 5
    SFE_UBLOX_GNSS_ID_QZSS = 6
    SFE_UBLOX_GNSS_ID_GLONASS = 7

class sfe_ublox_ls_src_e(Enum):
    SFE_UBLOX_LS_SRC_DEFAULT = 1
    SFE_UBLOX_LS_SRC_GLONASS = 2
    SFE_UBLOX_LS_SRC_GPS = 3
    SFE_UBLOX_LS_SRC_SBAS = 4
    SFE_UBLOX_LS_SRC_BEIDOU = 5
    SFE_UBLOX_LS_SRC_GALILEO = 6
    SFE_UBLOX_LS_SRC_AIDED = 7
    SFE_UBLOX_LS_SRC_CONFIGURED = 7
    SFE_UBLOX_LS_SRC_UNKNOWN = 255

class sfe_ublox_mga_assist_ack_e(Enum):
    SFE_UBLOX_MGA_ASSIST_ACK_NO = 1
    SFE_UBLOX_MGA_ASSIST_ACK_YES = 2
    SFE_UBLOX_MGA_ASSIST_ACK_ENQUIRE = 3

class sfe_ublox_mga_ack_infocode_e(Enum):
    SFE_UBLOX_MGA_ACK_INFOCODE_ACCEPTED = 1
    SFE_UBLOX_MGA_ACK_INFOCODE_NO_TIME = 2
    SFE_UBLOX_MGA_ACK_INFOCODE_NOT_SUPPORTED = 3
    SFE_UBLOX_MGA_ACK_INFOCODE_SIZE_MISMATCH = 4
    SFE_UBLOX_MGA_ACK_INFOCODE_NOT_STORED = 5
    SFE_UBLOX_MGA_ACK_INFOCODE_NOT_READY = 6
    SFE_UBLOX_MGA_ACK_INFOCODE_TYPE_UNKNOWN = 7


class sfe_ublox_talker_ids_e(Enum):
    SFE_UBLOX_MAIN_TALKER_ID_DEFAULT = 1
    SFE_UBLOX_MAIN_TALKER_ID_GP = 2
    SFE_UBLOX_MAIN_TALKER_ID_GL = 3
    SFE_UBLOX_MAIN_TALKER_ID_GN = 4
    SFE_UBLOX_MAIN_TALKER_ID_GA = 5
    SFE_UBLOX_MAIN_TALKER_ID_GB = 6
    SFE_UBLOX_MAIN_TALKER_ID_GQ = 7

sfe_ublox_dgnss_mode_e = Enum('sfe_ublox_dgnss_mode_e',['SFE_UBLOX_DGNSS_MODE_FLOAT' , 'SFE_UBLOX_DGNSS_MODE_FIXED'])

class sfe_ublox_pms_mode_e(Enum):
    SFE_UBLOX_PMS_MODE_FULLPOWER = 0
    SFE_UBLOX_PMS_MODE_BALANCED = 1
    SFE_UBLOX_PMS_MODE_INTERVAL = 2
    SFE_UBLOX_PMS_MODE_AGGRESSIVE_1HZ = 3
    SFE_UBLOX_PMS_MODE_AGGRESSIVE_2HZ = 4
    SFE_UBLOX_PMS_MODE_AGGRESSIVE_4HZ = 5
    SFE_UBLOX_PMS_MODE_INVALID = 0xff

sfe_ublox_rxm_mode_e = Enum('sfe_ublox_rxm_mode_e',['SFE_UBLOX_CFG_RXM_CONTINUOUS','SFE_UBLOX_CFG_RXM_POWERSAVE'])

MAX_PAYLOAD_SIZE = 276
SFE_UBLOX_SPI_BUFFER_SIZE = 128
SFE_UBLOX_MAX_NMEA_BYTE_COUNT = 88

class UbxPacket:
    def __init__(self,cls,id,len,counter,starting_spot,payload,checksum_a, checksum_b):
        self.cls = cls
        self.id = id
        self.len = len
        self.counter = counter
        self.starting_spot = starting_spot
        self.payload = payload
        self.checksum_a = checksum_a
        self.checksum_b = checksum_b
        self.valid = sfe_ublox_packet_validity_e()
        self.class_and_id_match = sfe_ublox_packet_validity_e()



class GeofenceState:
    def __init__(self,status,num_fences,comb_state):
        self.status = status
        self.num_fences = num_fences
        self.comb_state = comb_state
        self.states = [0, 0, 0, 0]

class GeofenceParams:
    def __init__(self,num_fences):
        self.num_fences = num_fences
        self.lats = [0, 0, 0, 0]
        self.longs = [0, 0, 0, 0]
        self.rads = [0, 0, 0, 0]

class ModuleSWVersion:
    def __init__(self,version_low, version_high, moduleQueried:bool):
        self.version_low = version_low
        self.version_high = version_high
        self.module_queried = moduleQueried


SFE_UBLOX_DAYS_FROM_1970_TO_2020 = 18262  # Jan 1st 2020 Epoch = 1577836800 seconds

SFE_UBLOX_DAYS_SINCE_2020 = [
    0, 366, 731, 1096, 1461, 1827, 2192, 2557, 2922, 3288,
    3653, 4018, 4383, 4749, 5114, 5479, 5844, 6210, 6575, 6940,
    7305, 7671, 8036, 8401, 8766, 9132, 9497, 9862, 10227, 10593,
    10958, 11323, 11688, 12054, 12419, 12784, 13149, 13515, 13880, 14245,
    14610, 14976, 15341, 15706, 16071, 16437, 16802, 17167, 17532, 17898,
    18263, 18628, 18993, 19359, 19724, 20089, 20454, 20820, 21185, 21550,
    21915, 22281, 22646, 23011, 23376, 23742, 24107, 24472, 24837, 25203,
    25568, 25933, 26298, 26664, 27029, 27394, 27759, 28125, 28490, 28855
]

SFE_UBLOX_DAYS_SINCE_MONTH = [
    [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335],  # Leap Year (Year % 4 == 0)
    [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]  # Normal Year
]



class SFE_UBLOX_GNSS:
    def __init__(self):
        self.defaultMaxWait = 1100
        self.i2cTransactionSize = 32
        self.defaultMGAdelat = 7
        self.defaultMGAINITIMEtAccS = 2
        self.defaultMGAINITIMEtAccNs = 0
        self.defaultMGAINITIMEsource = 0
        self.defaultNavDBDMaxWait = 3100


    sfe_ublox_sentence_types_e = Enum('currentSentence', ['SFE_UBLOX_SENTENCE_TYPE_NONE','SFE_UBLOX_SENTENCE_TYPE_NMEA','SFE_UBLOX_SENTENCE_TYPE_UBX','SFE_UBLOX_SENTENCE_TYPE_RTCM'])


    # bool begin(TwoWire &wirePort = Wire, uint8_t deviceAddress = 0x42, uint16_t maxWait = defaultMaxWait, bool assumeSuccess = false); // Returns true if module is detected
    def begin(self,adress):
        wire = i2c.TwoWire(adress)
        try:
            wire.begin(adress)
            return True
        except Exception as ex:
            return False





    def setI2COutput(self,bus, address, output_protocol):

        # Configure the I2C port to output the specified protocol(s)

        #:param bus: The I2C bus number (e.g. 1 for Raspberry Pi)
        #:param address: The I2C address of the device (e.g. 0x42)
        #:param output_protocol: A string specifying the protocol(s) to output, separated by commas (e.g. "UBX,NMEA" or "RTCM3,SPARTN")

        # Define the protocol codes
        PROTOCOL_CODES = {
            "UBX": 0x01,
            "NMEA": 0x02,
            "RTCM3": 0x04,
            "SPARTN": 0x08
        }

        # Parse the output protocol string
        protocols = [protocol.strip() for protocol in output_protocol.split(",")]
        protocol_code = 0
        for protocol in protocols:
            if protocol in PROTOCOL_CODES:
                protocol_code |= PROTOCOL_CODES[protocol]
            else:
                raise ValueError(f"Invalid protocol: {protocol}")

        # Configure the I2C port using smbus
        bus = i2c.smbus.SMBus(bus)
        bus.write_byte(address, 0x00)  # CFG_PRT (I/O protocol configuration)
        bus.write_byte(address, protocol_code)


    def setNavigationFrecuency(self, freq):
        self.navigationFrecuency = freq


    def getPVT(self, bus, adress):
        self.maxwait = self.defaultMaxWait
        self.pvtBus = bus
        self.pvtAdress = adress
        # Get the current PVT (position, velocity, time) data from the device
        #Get the current PVT (position, velocity, time) data from the device

        #:param bus: The I2C bus number (e.g. 1 for Raspberry Pi)
        #:param address: The I2C address of the device (e.g. 0x42)
        #:return: A dictionary containing the PVT data:
        #   - `latitude`: Latitude in degrees (float)
        #  - `longitude`: Longitude in degrees (float)
        # - `altitude`: Altitude in meters (float)
            #- `velocity_north`: Velocity in meters per second (float)
            # `velocity_east`: Velocity in meters per second (float)
            # `velocity_down`: Velocity in meters per second (float)
            # `time`: Time in seconds since the epoch (int)
        # Define the PVT data structure
        PVT_DATA_STRUCT = struct.Struct("<iiiiiii")

        # Read the PVT data from the device using smbus
        Pvtbus = i2c.smbus.SMBus(bus)
        pvt_data = Pvtbus.read_i2c_block_data(adress, 0x00, 28)  # NAV_PVT (PVT data)

        # Unpack the PVT data
        pvt_data_unpacked = PVT_DATA_STRUCT.unpack(bytes(pvt_data))

        # Extract the PVT data fields
        pvt_data_dict = {
            "latitude": pvt_data_unpacked[0] / 1e7,  # degrees
            "longitude": pvt_data_unpacked[1] / 1e7,  # degrees
            "altitude": pvt_data_unpacked[2] / 1e3,  # meters
            "velocity_north": pvt_data_unpacked[3] / 1e3,  # meters per second
            "velocity_east": pvt_data_unpacked[4] / 1e3,  # meters per second
            "velocity_down": pvt_data_unpacked[5] / 1e3,  # meters per second
            "time": pvt_data_unpacked[6]  # seconds since the epoch
        }
        self.pvt_data_dictionary = pvt_data_dict
        return pvt_data_dict




    def getLatitude(self):
        self.maxwait = self.defaultMaxWait
        return self.pvt_data_dictionary.get('latitude')

    def getLonguitude(self):
        self.maxwait = self.defaultMaxWait
        return self.pvt_data_dictionary.get('longitude')
    def getAltitude(self):
        self.maxwait = self.defaultMaxWait
        return self.pvt_data_dictionary.get('altitude')

