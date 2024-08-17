

if '__u_blox_structs_h__' not in locals():
    __ublox_structs_h_ = None

import SparkFun_u_blox_GNSS_Arduino_Library

if 'DEF_NUM_SENS' not in locals():
    DEF_NUM_SENS:int = 7 #max num of ESF sensors

if 'DEF_MAX_NUM_ESF_RAW_REPEATS' not in locals():
    DEF_MAX_NUM_ESF_RAW_REPEATS:int = 10

if 'DEF_MAX_NUM_ESF_MEAS' not in locals():
    DEF_MAX_NUM_ESF_MEAS:int = 31


class bits1:
    def __init__(self, automatic, implicitUpdate, addToFileBuffer, callbackCopyValid):
        self.automatic = automatic
        self.implicitUpdate = implicitUpdate
        self.addToFileBuffer = addToFileBuffer
        self.callbackCopyValid = callbackCopyValid


class flags:
    def __init__(self, all:int, Bits:bits1):
        self.all = all
        self.Bits = Bits


class ubxAutomaticFlags:
    def __init__(self, Flags:flags):
        self.Flags = Flags



UBX_NAV_POSECEF_LEN = 20

class UBX_NAV_POSECEF_data_t:
    def __init__(self, iTOW, ecefX, ecefY, ecefZ, pAcc) -> None:
        self.iTOW = iTOW
        self.ecefX = ecefX
        self.ecefY = ecefY
        self.ecefZ = ecefZ
        self.pAcc = pAcc

class bits2:
    def __init__(self, all, iTOW, ecefX, ecefY, ecefZ, pAcc) -> None:
        self.all = all
        self.iTOW = iTOW
        self.ecefX = ecefX
        self.ecefY = ecefY
        self.ecefZ = ecefZ
        self.pAcc = pAcc


class moduleQueried:
    def __init__(self, all, bits:bits2):
        self.all = all
        self.bits = bits

class UBX_NAV_POSECEF_moduleQueried_t:
    def __init__(self, all:int, module:moduleQueried):
        self.all = all
        self.module = module

class UBX_NAV_POSECEF_t:
    def __init__(self, automaticFlags: ubxAutomaticFlags, data:UBX_NAV_POSECEF_data_t, callbackData: UBX_NAV_POSECEF_data_t, callBackPointer :UBX_NAV_POSECEF_data_t, callBackPointerPtr:UBX_NAV_POSECEF_data_t ):
        self.automaticFlags = automaticFlags
        self.data = data
        self.callBackData = callbackData
        self.callBackPointer = callBackPointer
        self.callBackPointerPtr = callBackPointerPtr


UBX_NAV_POSLLH_LEN = 28

class UBX_NAV_POSLLH_data_t:
    def __init__(self, iTOW:int, lon:int, lat:int, height:int, hMSL:int, hAcc:int, vAcc:int) -> None:
        self.iTOW = iTOW
        self.lon = lon
        self.lat = lat
        self.height = height
        self.hMSL = hMSL
        self.hAcc = hAcc
        self.vAcc = vAcc

class bits3:
    def __init__(self, all:int, lon:int, lat:int, heigth:int, hMSL:int, hAcc:int, vAcc:int) -> None:
        self.all = all
        self.lon = lon
        self.lat = lat
        self.heigth = heigth
        self.hMSL = hMSL
        self.hAcc = hAcc
        self.vAcc = vAcc



class UBX_NAV_POSLLH_moduleQueried_t:
    def __init__(self, all:int, bits:bits3) -> None:
        self.all = all
        self.bits = bits

class UBX_NAV_POSLLH_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags,data:UBX_NAV_POSLLH_data_t, callbackPointer:UBX_NAV_POSLLH_data_t, callBackPointerPtr: UBX_NAV_POSLLH_data_t, callbackData:UBX_NAV_POSLLH_data_t) -> None:
        self.automaticFlags = automaticFlags
        self.data = data
        self.callBackPointer = callbackPointer
        self.callBackPointerPtr = callBackPointerPtr
        self.callbackData = callbackData


UBX_NAV_STATUS_LEN = 16
class bits4:
    def __init__(self, gpsFixOk, diffSoln, wknSet, towSet) -> None:
        self.gpsFixOk = gpsFixOk
        self.wknSet = wknSet
        self.towSet = towSet

class flags2:
    def __init__(self, all, bits:bits4) -> None:
        self.all = all
        self.bits = bits

class bits5:
    def __init__(self, gpsFixOk, diffSoln, wknSet, towSet) -> None:
        self.gpsFixOk = gpsFixOk
        self.diffSoln = diffSoln
        self.wknSet = wknSet
        self.towSet = towSet

   


class flags3:
    def __init__(self,all, bits:bits5) -> None:
        self.all = all
        self.bits = bits

class bits6:
    def __init__(self, diffCorr, carrSolnValid, reserved, mapMatching):
        self.diffCorr = diffCorr
        self.carrSolnValid = carrSolnValid
        self.reserved = reserved
        self.mapMatching = mapMatching

  

class fixStat:
    def __init__(self,all, bits:bits6):
        self.all = all
        self.bits = bits

class flags4:
    def __init__(self, all, stats:fixStat):
        self.all = all
        self.stats = stats

class UBX_NAV_STATUS_data_t:
    def __init__(self, iTOW, gpsFix, flags:flags3, FixStat:fixStat, flags2:flags4, ttff, msss):
        self.iTOW = iTOW
        self.gpsFix = gpsFix
        self.flags = flags
        self.FixStat = FixStat
        self.flags2 = flags2
        self.ttff = ttff
        self.msss = msss

class bits7:
    def __init__(self, all, iTOW, gpsFix, gpsFixOk, diffSoln, wknSet, towSet, diffCor, carrSolnValid, mapMatching, psmState, spoofDetState, carrSoln, ttff, msss) -> None:
        self.all = all
        self.iTOW = iTOW
        self.gpsFix = gpsFix
        self.gpsFixOk = gpsFixOk
        self.diffSoln = diffSoln
        self.carrSolnValid = carrSolnValid
        self.mapMatching = mapMatching
        self.psmState = psmState
        self.spoofDetState = spoofDetState
        self.carrSoln = carrSoln
        self.ttff = ttff
        self.msss = msss

 

class UBX_NAV_STATUS_moduleQueried_t:
    def __init__(self, all:int , bits:bits7) -> None:
        self.all = all
        self.bits = bits


class UBX_NAV_STATUS_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, data:UBX_NAV_STATUS_data_t, moduleQueried:UBX_NAV_STATUS_moduleQueried_t, callBackPointer:UBX_NAV_STATUS_data_t, callbackPointerPtr:UBX_NAV_STATUS_data_t, callBackdata:UBX_NAV_STATUS_data_t) -> None:
        self.automaticFlags = automaticFlags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callBackPointer = callBackPointer
        self.callbackPointerPtr = callbackPointerPtr
        self.callBackdata = callBackdata

UBX_NAV_DOP_LEN = 18

class UBX_NAV_DOP_data_t:
    def __init__(self, iTOW, gDOP, pDOP, tDOP, vDOP, hDOP, nDOP, eDOP) -> None:
        self.iTOW = iTOW
        self.gDOP = gDOP
        self.pDOP = pDOP
        self.tDOP = tDOP
        self.vDOP = vDOP
        self.hDOP = hDOP
        self.nDOP = nDOP
        self.eDOP = eDOP

class bits8:
    def __init__(self, all, iTOW, gDOP, pDOP, tDOP, vDOP, hDOP, nDOP, eDOP) -> None:
        self.all = all
        self.iTOW = iTOW
        self.gDOP = gDOP
        self.pDOP = pDOP
        self.tDOP = tDOP
        self.vDOP = vDOP
        self.hDOP = hDOP
        self.nDOP = nDOP
        self.eDOP = eDOP



class moduleQueried2:
    def __init__(self, all, bits:bits8) -> None:
        self.all = all
        self.bits = bits


class UBX_NAV_DOP_moduleQueried_t:
    def __init__(self, module:moduleQueried2):
        self.moduleQueried = module


class UBX_NAV_DOP_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, data:UBX_NAV_DOP_data_t, moduleQueried: UBX_NAV_DOP_data_t, callbackPointer: UBX_NAV_DOP_data_t, callbackPointerPtr: UBX_NAV_DOP_data_t) -> None:
        self.automaticFlags = automaticFlags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callbackPointer = callbackPointer
        self.callbackPointerPtr = callbackPointerPtr


UBX_NAV_ATT_LEN = 32

class UBX_NAV_ATT_data_t:
    def __init__(self, iTOW, version, reserved:list, roll, pitch, heading, accRoll, accPitch, accHeading):
        self.iTOW = iTOW
        self.version = version
        self.reserved = reserved
        self.roll = roll
        self.pitch = pitch
        self.heading = heading
        self.accRoll = accRoll
        self.accPitch = accPitch
        self.accHeading = accHeading

    reserved = [3]

class bits9:
    def __init__(self, all, iTOW, version, roll, pitch, heading, accRoll, accPitch, accHeading):
        self.all = all
        self.iTOW = iTOW
        self.version = version
        self.roll = roll
        self.pitch = pitch
        self.heading = heading
        self.accRoll = accRoll
        self.accPitch = accPitch
        self.accHeading = accHeading

   

class moduleQueried3:
    def __init__(self, all, bits:bits9):
        self.all = all
        self.bits = bits

class UBX_NAV_ATT_moduleQueried_t:
    def __init__(self, Module:moduleQueried3, all):
        self.Module = Module
        self.all = all

class UBX_NAV_ATT_t:
    def __init__(self, autoMaticFlags:ubxAutomaticFlags, data:UBX_NAV_ATT_data_t, moduleQueried:UBX_NAV_ATT_moduleQueried_t) -> None:
        self.autoMaticFlags = autoMaticFlags
        self.data = data
        self.moduleQueried = moduleQueried

UBX_NAV_PVT_LEN = 92

class bits10:
    def __init__(self, validDate, validTime, fullyResolved, validMag):
        self.validDate = validDate
        self.validTime = validTime
        self.fullyResolved = fullyResolved
        self.validMag = validMag
  


class valid:
    def __init__(self, all, bits:bits10) -> None:
        self.all = all
        self.bits = bits

class bits11:
    def __init__(self, gnssFixOK, diffSoln, psmState, headVehValid, carrSoln) -> None:
        self.gnssFixOK = gnssFixOK
        self.diffSoln = diffSoln
        self.psmState = psmState
        self.headVehValid = headVehValid
        self.carrSoln = carrSoln
    

class flags5:
    def __init__(self, all, bits:bits11) -> None:
        self.all = all
        self.bits = bits

class bits12:
    def __init__(self, reserved, confirmedAvai, confirmedDate, confirmedTime) -> None:
        self.reserved = reserved
        self.confirmedAvai = confirmedAvai
        self.confirmedDate = confirmedDate
        self.confirmedTime = confirmedTime


class flags6:
    def __init__(self, all, bits:bits12) -> None:
        self.all = all
        self.bits = bits

class bits13:
    def __init_(self, indalidLlh) -> None:
        self.invalidLlh = indalidLlh
    invalidLlh = 3

class flags7:
    def __init__(self, all, bits:bits13) -> None:
        self.all = all
        self.bits = bits

class UBX_NAV_PVT_data_t:
    def __init__(self, iTOW, year, month, day, hour, min, sec, Valid:valid, tAcc, nano, fixType, flags:flags5, flags2:flags6, numSV, lon, lat, height, hMSL, hAcc, velN, velE, velD, gSpeed, headMot, sAcc, headAcc, pDOP, flags3:flags7, reserved1:list, headVeh, magDec, magAcc) -> None:
        self.iTOW = iTOW
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.min = min
        self.sec = sec
        self.Valid = Valid
        self.tAcc = tAcc
        self.nano = nano
        self.fixType = fixType
        self.flags = flags
        self.flags2 = flags2
        self.numSV = numSV
        self.lon = lon
        self.lat = lat
        self.height = height
        self.hMSL = hMSL
        self.hAcc = hAcc
        self.velN = velN
        self.velE = velE
        self.velD = velD
        self.gSpeed = gSpeed
        self.headMot = headMot
        self.sAcc = sAcc
        self.headAcc = headAcc
        self.pDOP = pDOP
        self.flags3 = flags3
        self.reserved1 = reserved1
        self.headVeh = headVeh
        self.magDec = magDec
        self.magAcc = magAcc
        
        if reserved1.__len__() is not 5:
            if reserved1.__len__() > 5:
                while reserved1.__len__() > 5:
                    reserved1.pop()

            elif reserved1.__len__() < 5:
                while reserved1.__len__() < 5:
                    reserved1.append(None)
        
        else: 
            for i in range(reserved1.__len__()):
                reserved1[i] = None

class bits14:
    def __init__(self, all, iTOW, year, month, day, hour, min, sec, validDate, validTime, fullyResolved, validMag, tAcc, nano, fixType, gnssFixOk, diffSoln, psmState, headVehValid, carrSoln, confirmedAvai, confirmedDate, confirmedTime, numSV, lon, lat, height, hMSL, hAcc, vAcc, velN, velE) -> None:
        self.all = all
        self.iTOW = iTOW
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.min = min
        self.sec = sec
        self.validTime = validTime
        self.validDate = validDate
        self.fullyResolved = fullyResolved
        self.validMag = validMag
        self.tAcc = tAcc
        self.nano = nano
        self.fixType = fixType
        self.gnssFixOk = gnssFixOk
        self.diffSoln = diffSoln
        self.psmState = psmState
        self.headVehValid = headVehValid
        self.carrSoln = carrSoln
        self.confirmedAvai = confirmedAvai
        self.confirmedDate = confirmedDate
        self.confirmedTime = confirmedTime
        self.numSV = numSV
        self.lon = lon
        self.lat = lat
        self.height = height
        self.hMSL = hMSL
        self.hAcc = hAcc
        self.vAcc = vAcc
        self.velN = velN
        self.velE = velE




class moduleQueried4:
    def __init__(self, all, bits:bits14) -> None:
        self.all = all
        self.bits = bits

class bits15:
    def __init__(self, velD, gSpeed, headMot, sAcc, headAcc, pDOP, invalidLlh, headVeh, magDec, magAcc) -> None:
        self.velD = velD
        self.gSpeed = gSpeed
        self.headMot = headMot
        self.sAcc = sAcc
        self.headAcc = headAcc
        self.pDOP = pDOP
        self.invalidLlh = invalidLlh
        self.headVeh = headVeh
        self.magDec = magDec
        self.magAcc = magAcc

   

class moduleQueried5:
    def __init__(self,all, bits:bits15) -> None:
        self.all = all
        self.bits = bits

class UBX_NAV_PVT_moduleQueried_t:
    def __init__(self,module:moduleQueried4,module2:moduleQueried5) -> None:
        self.module = module
        self.module2 = module2

class UBX_NAV_PVT_t:
    def __init__(self, automaTicFlags:ubxAutomaticFlags, data:UBX_NAV_PVT_data_t, moduleQueried:UBX_NAV_PVT_moduleQueried_t, callBackpointer:UBX_NAV_PVT_data_t, callbackPointerPtr: UBX_NAV_PVT_data_t, callbackData: UBX_NAV_PVT_data_t) -> None:
        self.automaticFlags = automaTicFlags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callbackPointer = callBackpointer
        self.callbackPointerPtr = callbackPointerPtr
        self.callbackData = callbackData

UBX_NAV_ODO_LEN = 20

class UBX_NAV_ODO_data_t:
    def __init__(self, version, reserved:list, iTOW, distance, totalDistance, distanceStd) -> None:
        self.version = version
        self.reserved = reserved
        self.iTOW = iTOW
        self.distance = distance
        self.totalDistance = totalDistance
        self.distanceStd = distanceStd

    reserved = [3]

class bits16:
    def __init__(self, all, version, iTOW, distance, totalDistance, distanceStd) -> None:
        self.all = all
        self.version = version
        self.iTOW = iTOW
        self.distance = distance
        self.totalDistance = totalDistance
        self.distanceStd = distanceStd

  
class moduleQueried6:
    def __init__(self, bits:bits16, all) -> None:
        self.bits = bits
        self.all  = all

class UBX_NAV_ODO_moduleQueried_t:
    def __init__(self, all, module:moduleQueried6) -> None:
        self.all = all
        self.module = moduleQueried6


class UBX_NAV_ODO_t:
    def __init__(self, AutomaticFlags:ubxAutomaticFlags, data:UBX_NAV_ODO_data_t, moduleQueried: UBX_NAV_ODO_moduleQueried_t, callbackPointer:UBX_NAV_ODO_data_t, callBackPointerPtr: UBX_NAV_ODO_data_t, callBackData: UBX_NAV_ODO_data_t) -> None:
        self.automaticFlags = AutomaticFlags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callbackPointer = callbackPointer
        self.callBackPointerPtr = callBackPointerPtr
        self.callBackdata = callBackData

UBX_NAV_VELECEF_LEN = 20

class UBX_NAV_VELECEF_data_t:
    def __init__(self, iTow, ecefVX, ecefVY, ecefVZ, sAcc) -> None:
        self.iTOW = iTow
        self.ecefVX = ecefVX
        self.ecefVY = ecefVY
        self.ecefVZ = ecefVZ
        self.sAcc = sAcc
class bits17:
    def __init__(self, all, iTOW, ecefVX, ecefVY, ecefVZ, sAcc) -> None:
        self.all = all
        self.iTOW = iTOW
        self.ecefVX = ecefVX
        self.ecefVY = ecefVY
        self.ecefVZ = ecefVZ
        self.sAcc = sAcc

    all, iTOW, ecefVX, ecefVY, ecefVZ, sAcc = 1
class moduleQueried7:
    def __init_(self, bits:bits17, all) -> None:
        self.bits = bits
        self.all = all

class UBX_NAV_VELECEF_moduleQueried_t:
    def __init__(self, module:moduleQueried) -> None:
        self.module = module


class UBX_NAV_VELCEF_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, data:UBX_NAV_VELECEF_data_t,moduleQueried: UBX_NAV_VELECEF_moduleQueried_t, callBackPointer:UBX_NAV_VELECEF_data_t, callBackPointerPtr: UBX_NAV_ODO_data_t, callbackData:UBX_NAV_ODO_data_t) -> None:
        self.automaticFlags = automaticFlags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callBackPointer = callBackPointer
        self.callBackPointerPtr = callBackPointer

UBX_NAV_VELNED_LEN = 36

class UBX_NAV_VELNED_data_t:
    def __init__(self, iTOW, velN, velE, velD, speed, gSpeed, heading, sAcc, cAcc) -> None:
        self.iTOW = iTOW
        self.velN = velN
        self.velE = velE
        self.velD = velD
        self.speed = speed
        self.gSpeed = gSpeed
        self.heading = heading
        self.sAcc = sAcc

class bits18:
    def __init__(self, all, iTOW, velN, velE, velD, speed, gSpeed, heading, sAcc, cAcc) -> None:
        self.all = all
        self.iTOW = iTOW
        self.velN = velN
        self.velE = velE
        self.velD = velD
        self.speed = speed
        self.gSpeed = gSpeed
        self.heading = heading
        self.sAcc = sAcc
        self.cAcc = cAcc

    all,iTOW,velN,velE, velD, speed, gSpeed, heading, sAcc, cAcc = 1


class UBX_NAV_VELNED_moduleQueried:
    def __init__(self, all, bits:bits18) -> None:
        self.all = all
        self.bits = bits


class UBX_NAV_VELNED_t:
    def __init__(self, automaticflags:ubxAutomaticFlags, data:UBX_NAV_VELNED_data_t, moduleQueried: UBX_NAV_VELNED_moduleQueried, callbackPointer: UBX_NAV_VELNED_data_t, callbackPointerPtr:UBX_NAV_VELNED_data_t, callbackData:UBX_NAV_VELNED_data_t) -> None:
        self.automaticFlags = automaticflags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callBackPointer = callbackPointer
        self.callBackPointerPtr = callbackPointer
        self.callBackData = callbackData

 
UBX_NAV_HPPOSECEF = 16

UBX_NAV_HPPOSECEF_LEN = 28

class bits19:
    def __init__(self, invalidEcef) -> None:
        self.invalifEcef = invalidEcef

class flags8:
    def __init__(self, all, bits:bits19) -> None:
        self.all = all
        self.bits = bits


class UBX_NAV_HPPOSECEF_data_t:
    def __init__(self, version, reserved:list, iTOW, ecefX, ecefY, ecefZ, ecefXHp, ecefYHp, ecefZHp, flags:flags8, pAcc) -> None:
        self.version = version 
        self.reserved = reserved
        self.iTOW = iTOW
        self.ecefX = ecefX 
        self.ecefY = ecefY
        self.ecefZ = ecefZ
        self.ecefXHp = ecefXHp
        self.ecefYHp = ecefYHp
        self.ecefZHp = ecefZHp
        self.flags = flags
        self.pAcc = pAcc
    
        if reserved.__len__() is not 3:
            if reserved.__len__() < 3:
                while reserved.len() < 3:
                    reserved.append(None)
            
            elif reserved.__len__() > 3:
                while reserved.len() > 3:
                    reserved.pop()
        
        else:
            for i in range(reserved.__len__()):
                reserved[i] = None

class bits20:
    def __init__(self, all, version, iTOW, ecefX, ecefY, ecefZ, ecefXHp, ecefYHp, ecefZHp, invalidEcef, pAcc) -> None:
        self.all = all 
        self.version = version 
        self.iTOW = iTOW
        self.ecefX = ecefX
        self.ecefY = ecefY
        self.ecefZ = ecefZ
        self.ecefXHp = ecefXHp
        self.ecefYHp = ecefYHp
        self.ecefZHp = ecefZHp
        self.invelidEcef = invalidEcef
        self.pAcc = pAcc
    
    
class moduleQueried8:
    def __init__(self, all, bits:bits20) -> None:
        self.all = all 
        self.bits = bits

class UBX_NAV_HPPOSECEF_moduleQueried_t:
    def __init__(self, all, module:moduleQueried8) -> None:
        self.all = all 
        self.module = module



class UBX_NAV_HPPOSECEF_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, data:UBX_NAV_HPPOSECEF_data_t, mopduleQueried:UBX_NAV_HPPOSECEF_moduleQueried_t, callBackPointer:UBX_NAV_HPPOSECEF_data_t, callBackPointerPtr:UBX_NAV_HPPOSECEF_data_t, callBackData:UBX_NAV_HPPOSECEF_data_t) -> None:
        self.automaticFlags = automaticFlags
        self.data = data
        self.mopduleQueried = mopduleQueried
        self.callbackPointer = callBackPointer
        self.callbackPointerPtr = callBackPointerPtr
        self.callbackData = callBackData

UBX_NAV_HPPOSLLH_LEN = 36

class bits20:
    def __init__(self, invalifEcef) -> None:
        self.invalifEcef = invalifEcef
    invalifEcef = 1


class flags9:
    def __init__(self, all, bits:bits20) -> None:
        self.all = all 
        self.bits = bits

class UBX_NAV_HPPOSECEF_data_t:
    def __init__(self, version, reserved:list, iTOW, ecefX, ecefY, ecefZ, ecefXHp, ecefYHp, ecefZHp, flags:flags9, pAcc) -> None:
        self.version = version 
        self.reserved = reserved 
        self.iTOW = iTOW 
        self.ecefx = ecefX 
        self.ecefy = ecefY
        self.ecefz = ecefZ
        self.ecefxHp = ecefXHp
        self.ecefyHp = ecefYHp
        self.ecefzhp = ecefZHp
        self.flags = flags
        self.pAcc = pAcc

class bits21:
    def __init__(self, all, version, iTOW, ecefX, ecefY, ecefZ, ecefXHp, ecefYHp, ecefZHp, invalidEcef, pAcc) -> None:
        self. all = all 
        self.version = version 
        self.iTOW = iTOW
        self.ecefX = ecefX
        self.ecefY = ecefY
        self.ecefZ = ecefZ
        self.ecefXHp = ecefXHp
        self.ecefYHp = ecefYHp
        self.ecefZHp = ecefZHp
        self. invalidEcef = invalidEcef
        self.pAcc = pAcc
    
    all,version,iTOW,ecefX,ecefXHp,ecefY,ecefYHp,ecefZ,ecefZHp,invalidEcef,pAcc = 1

class moduleQueried9:
    def __init__(self, all, bits:bits21) -> None:
        self.all = all 
        self.bits = bits

class UBX_NAV_HPPOSECEF_moduleQueried_t:
    def __init__(self, module:moduleQueried9) -> None:
        self.module = module

class bits22(bits13):
    def __init__(self) -> None:
        self.invalidLlh = 1

class flags10:
    def __init__(self, all , bits:bits22) -> None:
        self.all = all 
        self.bits = bits

class UBX_NAV_HPPOSLLH_data_t:
    def __init__(self, version, reserved1:list, flags:flags10, iTOW, lon, lat, height, hMSL, lonHp, latHp, heightHp, ) -> None: 
        self.version = version 
        self.reserved = reserved1
        self.flags = flags
        self.iTOW = iTOW
        self.lon = lon
        self.lat = lat
        self.height = height
        self.hMSL = hMSL
        self.lonHp = lonHp
        self.latHp = latHp
        self.heightHp = heightHp
        
        #inicializar el vector reserved
        if reserved1.__len__() is not 2:
            if reserved1.__len__() < 2:
                while reserved1.__len__() < 2:
                    reserved1.append(None)
            
            if reserved1.__len__() > 2:
                while reserved1.__len__() > 2:
                    reserved1.pop()

class bits23:
    def __init__(self, all, version, invalidLh, iTOW, lon, lat, height, hMSL, lonHp, latHp, heightHp, hMSLHp, hAcc, vAcc ) -> None:
        self.all = all 
        self.version = version
        self.invalidLh = invalidLh
        self.iTOW = iTOW
        self.lon = lon
        self.lat = lat
        self.height = height
        self.hMSL = hMSL
        self.lonHp = lonHp
        self.latHp = latHp
        self.heightHp = heightHp
        self.hMSLHp = hMSLHp
        self.hAcc = hAcc
        self.vAcc = vAcc
        

class moduleQueried10:
    def __init__(self, all, bits:bits23) -> None:
        self.all = all 
        self.bits = bits

class UBX_NAV_HPPOSLLH_moduleQueried_t:
    def __init__(self, moduleQueried:moduleQueried10) -> None:
        self.moduleQueried = moduleQueried

class UBX_NAV_HPPOSLLH_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, data:UBX_NAV_HPPOSLLH_data_t, moduleQueried:UBX_NAV_HPPOSLLH_moduleQueried_t, callbackPointer:UBX_NAV_HPPOSLLH_data_t, callbackPointerPtr:UBX_NAV_HPPOSLLH_data_t, callbackData:UBX_NAV_HPPOSLLH_data_t) -> None:
        self.automaticFlags = automaticFlags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callbackPointer = callbackPointer
        self.callbackPointerPtr = callbackPointerPtr
        self.callbackData = callbackData

UBX_NAV_PVAT_LEN:int = 116

class valid2:
    def __init__(self, all, validDate, validTime, fullyRestored, valiMag) -> None:
            self.all = all 
            self.validDate = validDate
            self.validTime = validTime
            self.fullyRestored = fullyRestored
            self.valiMag = valiMag

class flags10:
    def __init__(self, gnssFixOk, diffSoln, reserved, vehRollValid, vehPitchValid, vehHeadingValid, carrSoln) -> None:
        self.gnssFixOk = gnssFixOk 
        self.diffSoln = diffSoln
        self.reserved = reserved
        self.vehRollValid = vehRollValid
        self.vehPitchValid = vehPitchValid
        self.vehHeadingValid = vehHeadingValid
        self.carrSoln = carrSoln
        
class  bits24:
    def __init__(self, reserved, confirmedAvai, confirmedDate, confirmedTime) -> None:
        self.reserved = reserved
        self.confirmedAvai = confirmedAvai
        self.confirmedDate = confirmedDate
        self.confirmedTime = confirmedTime
        
class flags11:
    def __init__(self, all, bits:bits24) -> None:
        self.all = all 
        self.bits = bits

class UBX_NAV_PVAT_data_t:
    def __init__(self, iTOW, version, valid:valid2, year, month, day, hour, min, sec, reserved0, reserved1:list, tAcc, nano, fixType, flags:flags10, flags2:flags11, numSV, lon, lat, height, hMSL, hAcc, vAcc, velN, velE, velD, gSpeed, sAcc, vehRoll, vehPitch, vehHeading, motHeading, accRoll, accPitch, accHeading, magDec, magAcc, errEllipseOrient, errEllipseMajor,errElipseMinor,reserved2:list, reserved3:list) -> None:
        self.iTOW = iTOW
        self.version = version
        self.valid = valid
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.min = min
        self.sec = sec
        self.reserved0 = reserved0
        self.reserved1 = reserved1
        
        if reserved1.__len__() is not 2:
            if reserved1.__len__() < 2:
                while reserved1.__len__() < 2:
                    reserved1.append(None)
            
            elif reserved1.__len__() > 2:
                while reserved1.__len__() > 2:
                    reserved1.pop()
        else:
            for i in range(reserved1.__len__()):
                reserved1[i] = None
        
        self.tAcc = tAcc
        self.nano = nano
        self.fixType = fixType
        self.flags = flags
        self.flags2 = flags2
        self.numSV = numSV
        self.lon = lon
        self.lat = lat
        self.height = height
        self.hMSL = hMSL
        self.hAcc = hAcc
        self.vAcc = vAcc
        self.velN = velN
        self.velE = velE
        self.velD = velD
        self.gSpeed = gSpeed
        self.sAcc = sAcc
        self.vehRoll = vehRoll
        self.vehPitch = vehPitch
        self.vehHeading = vehHeading
        self.motHeading = motHeading
        self.accRoll = accRoll
        self.accPitch = accPitch
        self.accHeading = accHeading
        self.magDec = magDec
        self.magAcc = magAcc
        self.errEllipseMajor = errEllipseMajor
        self.errEllipseMinor = errElipseMinor
        self.errEllipseOrient = errEllipseOrient
        self.reserved2 = reserved2
        
        if reserved2.__len__() is not 4:
            if reserved2.__len__() < 4:
                while reserved2.__len__() < 4:
                    reserved2.append(None)
            
            elif reserved2.__len__() > 4:
                while reserved2.__len__() > 4:
                    reserved2.pop()
        
        else:
            for i in range(reserved2.__len__()):
                reserved2[i] = None
        
        self.reserved3 = reserved3
        
        if reserved3.__len__() is not 4:
            if reserved3.__len__() < 4:
                while reserved3.__len__() < 4:
                    reserved3.append(None)
            
            elif reserved3.__len__() > 4:
                while reserved3.__len__() > 4:
                    reserved3.pop()
        
        else:
            for i in range(reserved3.__len__()):
                reserved3[i] = None
        
class moduleQueried11:
    def __init__(self, all, iTOW, version, validDate, validTime, fullyResolved, validMag, year, month, day, hour, min, sec, tAcc, nano, fixType, gnssFixOk, diffSoln, vehRollValid, vehPitchValid, vehHeadValid, carrSoln, confirmedAvai, confirmedDate, confirmedTime, numSV, lon, lat, height, hMSL, hAcc, vAcc) -> None:
        self.all = all 
        self.iTOW = iTOW
        self.version = version
        self.validDate = validDate
        self.validTime = validTime
        self.fullyResolved = fullyResolved
        self.validMag = validMag
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.min = min
        self.sec = sec
        self.tAcc = tAcc
        self.nano = nano
        self.fixType = fixType
        self.gnssFixOk = gnssFixOk
        self.diffSoln = diffSoln
        self.vehRollValid = vehRollValid
        self.vehPitchValid = vehPitchValid
        self.vehHeadingValid = vehHeadValid
        self.carrSoln = carrSoln
        self.confirmedAvai = confirmedAvai
        self.confirmedDate = confirmedDate
        self.numSV = numSV
        self.lon = lon
        self.lat = lat
        self. height = height
        self.hMSL = hMSL
        self.hAcc = hAcc
        
class moduleQueried12:
    def __init__(self, all, velN, velE, velD, gSpeed, sAcc, vehRoll, vehPitch, vehHeading, motHeading, accRoll, accPitch, accHeading, magDec, magAcc, errEllipseOrient, errEllipseMajor, errEllipseMinor) -> None:
        self.all = all
        self.velN = velN
        self.velE = velE
        self.velD = velD
        self.gSpeed = gSpeed
        self .sAcc = sAcc
        self.vehRoll = vehRoll
        self.vehPitch = vehPitch
        self.vehHeading = vehHeading
        self.motHeading = motHeading
        self.accRoll = accRoll
        self.accPitch = accPitch
        self.accHeading = accHeading
        self.magDec = magDec
        self.errEllipseOrient = errEllipseOrient
        self.errEllipseMajor = errEllipseMajor
        self.errEllipseMinor = errEllipseMinor
        
        
class UBX_NAV_PVAT_moduleQueried_t:
    def __init__(self, all, moduleQueried1:moduleQueried11, moduleQueried2:moduleQueried12) -> None:
        self.all = all 
        self.moduleQueried1 = moduleQueried1
        self.moduleQueried2 = moduleQueried2

class UBX_NAV_PVAT_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, data:UBX_NAV_PVAT_data_t, moduleQueried:UBX_NAV_PVAT_moduleQueried_t, callbackPointer:UBX_NAV_PVAT_data_t, callbackPointerPtr:UBX_NAV_PVAT_data_t, callbackData:UBX_NAV_PVAT_data_t) -> None:
        self.automaticFlags = automaticFlags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callbackPointer = callbackPointer
        self.callbackPointerPtr = callbackPointerPtr
        self.callbackData = callbackData

UBX_NAV_TIMEUTC_LEN = 20

class valid3:
    def __init__(self, valitTOW, validWKN, validUTC, reserved, utcStandard) -> None:
        self.validTOW = valitTOW
        self.validWKN = validWKN
        self.validUTC = validUTC
        self.reserved = reserved
        self.utcStandard = utcStandard
        

class UBX_NAV_TIMEUTC_data_t:
    def __init__(self, iTOW, tAcc, nano, year, month, day, min, sec, valid:valid3) -> None:
        self.iTOW = iTOW
        self.tAcc = tAcc
        self.nano = nano
        self.year = year
        self.month = month
        self.day = day
        self.min = min
        self.sec = sec
        self.valid = valid

class bits25:
    def __init__(self, all, iTOW, tAcc, nano, year, month, day, hour, min, sec, validTOW, validWKN, validUTC, utcStandard) -> None:
        self.all = all
        self.iTOW = iTOW
        self.tAcc = tAcc
        self.nano = nano
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.min = min
        self.sec = sec
        self.validTOW = validTOW
        self.validUTC = validUTC
        self.utcStandard = utcStandard

class UBX_NAV_TIMEUTC_moduleQueried_t:
    def __init__(self, all, bits:bits25) -> None:
        self.all = all
        self.bits = bits


class UBX_NAV_TIMEUTC_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, data:UBX_NAV_TIMEUTC_data_t, moduleQueried:UBX_NAV_ATT_moduleQueried_t, callbackPointer:UBX_NAV_TIMEUTC_data_t, callbackPointerPtr:UBX_NAV_TIMEUTC_data_t, callbackData:UBX_NAV_TIMEUTC_data_t) -> None:
        self.automaticFlags = automaticFlags
        self.data = data
        self.moduleQueried = moduleQueried 
        self.callbackPointer = callbackPointer
        self.callbackPointerPtr = callbackPointerPtr

UBX_NAV_CLOCK_LEN = 20

class UBX_NAV_CLOCK_data_t:
    def __init__(self):
        self.iTOW = 0  # GPS time of week of the navigation epoch: ms
        self.clkB = 0  # Clock bias: ns
        self.clkD = 0  # Clock drift: ns/s
        self.tAcc = 0  # Time accuracy estimate: ns
        self.fAcc = 0  # Frequency accuracy estimate: ps/s

class moduleQueried13:
    def __init__(self, all, iTOW, clkB, clkD, tAcc, fAcc) -> None:
        self.all = all
        self.iTOW = iTOW
        self.clkB = clkB
        self.clkD = clkD
        self.tAcc = tAcc
        self.fAcc = fAcc

class UBX_NAV_CLOCK_moduleQueried_t:
    def __init__(self, all, moduleQueried:moduleQueried13) -> None:
        self.all = all 
        self.moduleQueried = moduleQueried


class UBX_NAV_CLOCK_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags,data:UBX_NAV_CLOCK_data_t,moduleQueried:UBX_NAV_CLOCK_moduleQueried_t,callbackPointer:UBX_NAV_CLOCK_data_t,callbackPointerPtr:UBX_NAV_CLOCK_data_t, callbackData:UBX_NAV_CLOCK_data_t) -> None:
        self.automaticFlags = automaticFlags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callbackPointer = callbackPointer
        self.callbackPointerPtr = callbackPointerPtr
        self.callbackData = callbackData
        
UBX_NAV_TIMELS_LEN = 24

class bits26:
    def __init__(self, validCurrLs, validTimeToLsEvent) -> None:
        self.validCurrls = validCurrLs
        self.validTimeToLsEvent = validTimeToLsEvent

class valid4:
    def __init__(self, all, bits:bits26) -> None:
        self.all = all
        self.bits = bits
        

class UBX_NAV_TIMELS_data_t:
    def __init__(self, iTOW, version, reserved1:list, srcOfCurrLs, currLs, srcOflsChange, lsChange, timeToLsEvent, dateOfLsGpsWn, reserved2:list, valid:valid4) -> None:
        self.iTOW = iTOW
        self.version = version
        self.reserved1 = reserved1
        if reserved1.__len__() is not 3:
            if reserved1.__len__() > 3:
                while reserved1.__len__() > 3:
                    reserved1.pop()
            
            elif reserved1.__len__() < 3:
                while reserved1.__len__() < 3:
                    reserved1.append(None)
        else:
            for i in range(reserved1.__len__()):
                reserved1[i] = None
                
        self.srcOfCurrLs = srcOfCurrLs
        self.currLs = currLs
        self.srcOflsChange = srcOflsChange
        self.lsChange = lsChange
        self.timeToLsEvent = timeToLsEvent
        self.dateOfLsGpsWn = dateOfLsGpsWn
        self.reserved2 = reserved2
        if reserved2.__len__() is not 3:
            if reserved2.__len__() > 3:
                while reserved2.__len__() > 3:
                    reserved2.pop()
            elif reserved2.__len__() < 3:
                while reserved2.__len__() < 3:
                    reserved2.append(None)   
        else:
            for i in range(reserved2.__len__()):
                reserved2[i] = None
        
        self.valid = valid
        
class bits27:
    def __init__(self, all, iTOW, version, srcOfCurrls, currLs, srcOfLsChange, lsChange, timeToLsEvent, dateOfGpsWn, dateOfLsGpsDn, valirCurrLs, validTimeToLsEvent) -> None:
        
        
class UBX_NAV_TIMELS_moduleQueried_t:
    def __init__(self, all, bits:bits27) -> None: