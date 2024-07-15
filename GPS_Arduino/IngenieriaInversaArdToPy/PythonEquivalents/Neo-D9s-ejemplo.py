import secrets.py
import SparkFunUbloxGpsv3.py
import serial
import RPi.GPIO as GPIO#para sustituir PINMODE del propio arduino 
import time



#pines GPIO de rpi5
GPIO.setmode(GPIO.BOARD)





#clases de otra libreria
SFE_UBLOX_GNSS_SPI myGNSS
SFE_UBLOX_GNSS_SPI myLBand


#clase SPI de otra libreria
mySPI = "SPI" # usar otra si se requiere
mySpeed:int = 2000000

#pines de arduino
gnssCS:int = 4
lbandCS:int = 17

myLBandFreq:int = 556290000

def OK(ok:bool) -> str:
    if ok == True:
        return " -> OK"
    else:
        return " -> ERROR!"

#UBX_RXM_PMP_message_data_t *pmpData, es un puntero a un tipo de dato, se puede hacer como clase
def pushRXMPMP(pmpData:str):
    #inizializacion del puerto serial 
    Serial = serial.Serial('devttyACM0', 11250)

    payloadLen:int = (pmpData.LenghtMSB << 8)|(pmpData.LenghtMSB)
    Serial.write(F("New RXM-PMP data received. Message payload length is "))
    Serial.write(payLoadLen)
    #myGNSS es otra funcion definida en SparkFunUbloxGpsv3.py
    myGNSS.pushRawData(pmpData.sync1, sys.getsizeof(payLoadLen) + 6)
    myGNSS.pushRawData(pmpData.Sync1, 2)

#ubxDataStruct inicializar como clase
def writePVTdata(UBX_NAV_PVT_data_t:ubxDataStruct):
    Serial = serial.Serial('devttyACM0', 11250)

    latitude:float = ubxDataStruct.lat
    Serial.write("Lat: ")
    Serial.write(latitude /1000000.0,7)

    longuitude:float = ubxDataStruct.hMSL
    Serial.write("Height: ")
    Serial.write(longuitude/10000000.0,7)

    altitude:float = ubxDataStruct.fixType
    Serial.write("Fix: ")
    Serial.write(altitude / 1000.0,3)

    fixType:int = ubxDataStruct.fixType
    Serial.write(" Fix ")
    Serial.write(fixType)

    if fixType == 0:
        Serial.write(" (None) ")
    elif fixType == 1:
        Serial.write(" (Dead Reconing) ")
    elif fixType == 2:
        Serial.write(" (2D) ")
    elif fixType == 3:
        Serial.write(" (3D) ")
    else:
        Serial.write(" (UNKNOWN) ")
        
    
    carrSoln:int = ubxDataStruct.flags.bits.carrSoln
    Serial.write(" (Carrier Solution: ) ")
    Serial.write(carrSoln)

    if(carrSoln == 0)
        Serial.write(" (None ) ")
    elif (carrSoln == 1):
        Serial.write(F(" (Floating)"));
    elif (carrSoln == 2):
        Serial.write(F(" (Fixed)"));
    else:
        Serial.write(F(" (UNKNOWN)"));

    hAcc = ubxDataStruct.hAcc
    Serial.write(" Horizontal Accuracy Estimate:  ")
    Serial.write(hAcc)
    Serial.write(" (mm)")
    
    Serial.write("\n")

#Clase UBX RMX COR data t, buscar definicion
def printRXMCOR(ubxDataStruct:UBX_RXM_COR_data_t):
  Serial = serial.Serial('devttyACM0', 11250)
  Serial.write("UBX-RXM-COR:  ebno: ")
  Serial.write(ubxDataStruct.ebno / 8, 3) #Convert to dB
  Serial.write("  protocol: ")
  if ubxDataStruct.statusInfo.bits.protocol == 1:
    Serial.write("RTCM3")
  elif ubxDataStruct.statusInfo.bits.protocol == 2:
    Serial.write("SPARTN")
  elif ubxDataStruct.statusInfo.bits.protocol == 29:
    Serial.write("PMP (SPARTN)")
  elif ubxDataStruct.statusInfo.bits.protocol == 30:
    Serial.write("QZSSL6")
  else:
    Serial.write("Unknown")

  Serial.write("  errStatus: ")
  if ubxDataStruct.statusInfo.bits.errStatus == 1:
    Serial.write("Error-free")
  elif ubxDataStruct.statusInfo.bits.errStatus == 2:
    Serial.write("Erroneous")
  else:
    Serial.write("Unknown")

  Serial.write("  msgUsed: ")
  if ubxDataStruct.statusInfo.bits.msgUsed == 1:
    Serial.write("Not used")
  elif ubxDataStruct.statusInfo.bits.msgUsed == 2:
    Serial.write("Used")
  else:
    Serial.write("Unknown")

  Serial.write("  msgEncrypted: ")
  if ubxDataStruct.statusInfo.bits.msgEncrypted == 1:
    Serial.write("Not encrypted")
  elif ubxDataStruct.statusInfo.bits.msgEncrypted == 2:
    Serial.write("Encrypted")
  else:
    Serial.write("Unknown")

  Serial.write("  msgDecrypted: ")
  if ubxDataStruct.statusInfo.bits.msgDecrypted == 1:
    Serial.write("Not decrypted")
  elif ubxDataStruct.statusInfo.bits.msgDecrypted == 2:
    Serial.write("Successfully decrypted")
  else:
    Serial.write("Unknown")

  Serial.write("\n")

def setup():
   Serial = serial.Serial('devttyACM0', 11250)
  #configuracion de los pines

   GPIO.setup(gnssCS,GPIO.OUT)
   GPIO.setup(gnssCS, GPIO.HIGH)
   GPIO.setup(lbandCS, GPIO.OUT)
   GPIO.setup(lbandCS, GPIO.HIGH)

   time.sleep(1)
   Serial.write("NEO_D9S SPARTN Corrections")
   
   # mySPI.begin() activar SPI 
   # Inicializar y Configurar ZED-f9x
   # myGNSS.enableDebugging() log en el terminal


## derivado de aqui ##


   

   

   
   
  

    
    
