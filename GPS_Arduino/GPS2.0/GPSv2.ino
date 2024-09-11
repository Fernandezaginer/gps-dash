
#include <Wire.h> //Needed for I2C to GNSS

#include <SparkFun_u-blox_GNSS_v3.h> //http://librarymanager/All#SparkFun_u-blox_GNSS_v3
SFE_UBLOX_GNSS myGNSS;
void setup()
{
  delay(1000);
  
  Serial.begin(115200);
  Serial.println("SparkFun u-blox Example");

  Wire.begin();

  if (myGNSS.begin() == false) //Connect to the u-blox module using Wire port
  {
    Serial.println(F("u-blox GNSS not detected at default I2C address. Please check wiring. Freezing."));
    while (1);
  }

  myGNSS.setI2COutput(COM_TYPE_UBX); //Set the I2C port to output UBX only (turn off NMEA noise)
  //myGNSS.saveConfiguration(); //Optional: Save the current settings to flash and BBR
}

void loop()
{
  //Query module. The module only responds when a new position is available
  if (myGNSS.getPVT())
  {
    long latitude = myGNSS.getLatitude();
    Serial.print(F("Lat: "));
    Serial.print(latitude/10^7);
    Serial.print(F(" (degrees)"));

    long longitude = myGNSS.getLongitude();
    Serial.print(F(" Long: "));
    Serial.print(longitude/10^7);
    Serial.print(F(" (degrees)"));

    long altitude = myGNSS.getAltitude();
    Serial.print(F(" Alt: "));
    Serial.print(altitude/10^3);
    Serial.println(F(" (m)"));
  }
  
  if (myGNSS.getNAVHPPOSECEF())
  {
    long accuracy = myGNSS.getPositionAccuracy();
    Serial.print(F("3D Positional Accuracy: "));
    Serial.print(accuracy);
    Serial.println(F(" (mm)"));
  }
}
