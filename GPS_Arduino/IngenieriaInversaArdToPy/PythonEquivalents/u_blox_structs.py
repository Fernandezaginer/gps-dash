

if '__u_blox_structs_h__' not in locals():
    __ublox_structs_h_ = None

from ast import List
from inspect import ismodule
from json import JSONDecoder
from pydoc import allmethods
from sys import version
from tkinter import NO
# import SparkFun_u_blox_GNSS_Arduino_Library

DEF_NUM_SENS:int = 7 #max num of ESF sensors


DEF_MAX_NUM_ESF_RAW_REPEATS:int = 10


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

        if reserved1.__len__() != 5:
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

    reserved = [None,None,None]

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

        if reserved.__len__() != 3:
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
        self.reserved = [0] * 2

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

        if reserved1.__len__() != 2:
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

        if reserved2.__len__() != 4:
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

        if reserved3.__len__() != 4:
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
        if reserved1.__len__() != 3:
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
        if reserved2.__len__() != 3:
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
        self.all = all
        self.iTOW = iTOW
        self.version = version
        self.srcOfCurrls = srcOfCurrls
        self.currLs = currLs
        self.srcOfLsChange = srcOfLsChange
        self.lsChange = lsChange
        self.timeToLsEvent = timeToLsEvent
        self.dateOfGpsWn = dateOfGpsWn
        self.dateOfLsGpsDn = dateOfLsGpsDn
        self.valirCurrLs = valirCurrLs
        self.validTimeToLsEvent = validTimeToLsEvent


class UBX_NAV_TIMELS_moduleQueried_t:
    def __init__(self, all, bits:bits27) -> None:
        self.all = all
        self.bits = bits


class   UBX_NAV_TIMELS_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, data:UBX_NAV_TIMELS_data_t, moduleQueried:UBX_NAV_TIMELS_moduleQueried_t, callbackPointer:UBX_NAV_TIMELS_data_t, callbackPointerPtr:UBX_NAV_TIMELS_data_t, callbackData:UBX_NAV_TIMELS_data_t) -> None:
        self.automaticFlags = automaticFlags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callbackPointer = callbackPointer
        self.callbackPointerPtr = callbackPointerPtr
        self.callbackData = callbackData

UBX_NAV_SAT_MAX_BLOCKS = 225
UBX_NAV_SAT_MAX_LEN = 8 + (12*UBX_NAV_SAT_MAX_BLOCKS)

class UBX_NAV_SAT_header_t:
    def __init__(self, iTOW, version, numSvs, reserved1:list) -> None:
        self.iTOW = iTOW
        self.version = version
        self.numSvs = numSvs
        self.reserved = reserved1

        if reserved1.__len__() != 2:
            reserved1 = [None,None]
        else:
            pass


class flags12:
    def __init__(self, qualityInd, svUsed, health, diffCorr, smoothed, orbitSource, ephAvail, almAvail, anoAvail, aopAvail, reserved1, sbasCorrUsed, rtcmCorrUsed, slasCorrUsed, spartnCorrUsed, prCorrUsed, crCorrUsed, doCorrUsed, reserved2) -> None:
        self.qualityInd = qualityInd
        self.svUsed = svUsed
        self.health = health
        self.diffCorr = diffCorr
        self.smoothed = smoothed
        self.orbitSource = orbitSource
        self.ephAvail = ephAvail
        self.almAvail = almAvail
        self.anoAvail = anoAvail
        self.aopAvail = aopAvail
        self.reserved1 = reserved1
        self.sbasCorrUsed = sbasCorrUsed
        self.rtcmCorrUsedd = rtcmCorrUsed
        self.slasCorrUsed = slasCorrUsed
        self.spartnCorrUsed = spartnCorrUsed
        self.prCorrUsed = prCorrUsed
        self.crCorrUsed = crCorrUsed
        self.reserved2 = reserved2

class UBX_NAV_SAT_block_t:
    def __init__(self, gnssId, svId, cno, elev, azim, prRes,flags:flags12) -> None:
        self.gnssId = gnssId
        self.svId = svId
        self.cno = cno
        self.elev = elev
        self.azim = azim
        self.prRes = prRes
        self.flags = flags

bar:UBX_NAV_SAT_block_t = None

class UBX_NAV_SAT_data_t:
    def __init__(self, header:UBX_NAV_SAT_header_t, blocks:list) -> None:
        self.header = header
        self.blocks = blocks



        #blocks tiene que contener UBX_NAV_SAT_BLOCKS
        for i in range(UBX_NAV_SAT_MAX_BLOCKS):
            blocks.append(bar)


class UBX_NAV_SAT_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, data:UBX_NAV_SAT_data_t, moduleQueried:bool, callbackPointer:UBX_NAV_SAT_data_t, callbackPointerPtr:UBX_NAV_SAT_data_t, callbackData:UBX_NAV_SAT_data_t) -> None:
        self.automaticFlags = automaticFlags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callbackPonter = callbackPointer
        self.callbackPonterPtr = callbackPointerPtr
        self.callbackData = callbackData

UBX_NAV_SVIN_LEN = 40

class UBX_NAV_SVIN_data_t:
    def __init__(self, version, reserved1:list, iTOW, dur, meanX, meanY, meanZ, meanXHP, meanYHP, meanZHP, reserved2, meanAcc, obs, valid, active, reserved3:list) -> None:
        self.version = version
        self.reserved1 = reserved1

        reserved1 = [None, None, None]
        self.iTOW = iTOW
        self.dur = dur
        self.meanX = meanX
        self.meanY = meanY
        self.meanZ = meanZ
        self.meanXHP = meanXHP
        self.meanYHP = meanYHP
        self.meanZHP = meanZHP
        self.reserved2 = reserved2
        self.meanAcc = meanAcc
        self.obs = obs
        self.valid = valid
        self.active = active
        self.reserved3 = reserved3
        reserved3 = [None,None]

class bits28:
    def __init__(self, all, version, iTOW, dur, meanX, meanY, meanZ, meanXHP, meanYHP, meanZHP, meanAcc, obs, valid, active):
        self.all = all
        self.version = version
        self.iTOW = iTOW
        self.dur = dur
        self.meanX = meanX
        self.meanY = meanY
        self.meanZ = meanZ
        self.meanXHP = meanXHP
        self.meanYHP = meanYHP
        self.meanZHP = meanZHP
        self.meanAcc = meanAcc
        self.obs = obs
        self.valid = valid
        self.active = active

class UBX_NAV_SVIN_moduleQueried_t:
    def __init__(self, all, bits:bits28):
        self.all = all
        self.bits = bits

class UBX_NAV_SVIN_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, data:UBX_NAV_SVIN_data_t, moduleQueried:UBX_NAV_SVIN_moduleQueried_t,callbackPointer:UBX_NAV_SVIN_data_t, callbackPointerPtr:UBX_NAV_SVIN_data_t, callbackData:UBX_NAV_SVIN_data_t) -> None:
        self.automaticFlags = automaticFlags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callbackPointer = callbackPointer
        self.callbackPointerPtr


UBX_NAV_RELPOSNED_LEN = 40
UBX_NAV_RELPOSNED_LEN_F9 = 64

class bits29:
    def __init__(self, gnssFixOk, diffSoln, relPosValid, carrSoln, isMoving, refPosMiss, refObsMiss, relPosHeadingValid, relPosNormallized) -> None:
        self.gnssFixOk = gnssFixOk
        self.diffSoln = diffSoln
        self.relPosValid = relPosValid
        self.carrSoln = carrSoln
        self.isMoving = isMoving
        self.refPosMiss = refPosMiss
        self.refObsMiss = refObsMiss
        self.relPosHeadingValid = relPosHeadingValid
        self. relPosNormalized = relPosNormallized

class flags13:
    def __init__(self, all, bits:bits29) -> None:
        self.all = all
        self.bits = bits

class UBX_NAV_RELPOSNED_data_t:
    def __init__(self, version, reserved0, refStationId, iTOW, relPosN, relPosE, relPosD, relPosLenght, relPosHeading, reserved1:list, relPosHPN, relPosHPE, relPosHPD, relPosHPLenght, accN, accE, accD, accLenght, accHeading, reserved2:list, flags:flags13) -> None:
       self.version = version
       self.reserved0 = reserved0
       self.refStationId = refStationId
       self.iTOW = iTOW
       self.relPosN = relPosN
       self.relPosE = relPosE
       self.relPosD = relPosD
       self.relPosLenght = relPosLenght
       self.relPosHeading = relPosHeading
       self.reseved1 = reserved1
       self.relPosHPE = relPosHPE
       self.relPosHPN = relPosHPN
       self.relPosHPD = relPosHPD
       self.relPosHPLenght = relPosHPLenght
       self.accN = accN
       self.accE = accE
       self.accD = accD
       self.accLenght = accLenght
       self.accHeading = accHeading
       self.reserved2 = reserved2
       self.flags = flags

class bits30:
    def __init__(self, all, version, refStationId, iTOW, relPosN, relPosE, relPosLenght, relPosHeading, relPosHPN, relPosHPE, relPosHPD, relPosHPLenght, accN, accE, accD, accLenght, accHeading, gnssFixOk, diffSoln, relPosValid, carrSoln, isMoving, refPosMiss, refObsMiss, refPosHeadingValid, refPosNormalized):
        self.all = all
        self.version = version
        self.refStationId = refStationId
        self.iTOW = iTOW
        self.relPosN = relPosN
        self.relPosE = relPosE
        self.relPosLenght = relPosLenght
        self.relPosHeading = relPosHeading
        self.relPosHPN = relPosHPN
        self.relPosHPE = relPosHPE
        self.relPosHPD = relPosHPD
        self.relPosHPLenght = relPosHPLenght
        self.accN = accN
        self.accE = accE
        self.accD = accD
        self.accLenght = accLenght
        self.accHeading = accHeading
        self.gnssFixOk = gnssFixOk
        self.diffSoln = diffSoln
        self.relPosValid = relPosValid
        self.carrSoln = carrSoln
        self.isMoving = isMoving
        self.refPosMiss = refPosMiss
        self.refObsMiss = refObsMiss
        self.refPosHeadingValid = refPosHeadingValid
        self.relPosNormalized = refPosNormalized

class UBX_NAV_RELPOSNED_moduleQueried_t:
    def __init__(self, all, bits:bits30):
        self.all = all
        self.bits = bits

class UBX_NAV_RELPOSNED_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, data:UBX_NAV_RELPOSNED_data_t, moduleQueried:UBX_NAV_RELPOSNED_moduleQueried_t, callbackPointer:UBX_NAV_RELPOSNED_data_t, callbackPointerPtr:UBX_NAV_RELPOSNED_data_t, callbackData:UBX_NAV_RELPOSNED_data_t):
        self.automaticFlags = automaticFlags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callbackPointer = callbackPointer
        self.callbackPointerPtr = callbackPointerPtr
        self.callbackData = callbackData

UBX_NAV_AOPSTATUS_LEN = 16

class bits31:
    def __init__(self, useAOP):
        self.useAOP = useAOP

class aopCFG:
    def __init__(self, all, bits:bits31):
        self.all = all
        self.bits = bits

class UBX_NAV_AOPSTATUS_data_t:
    def __init__(self, iTOW, aopCFG:aopCFG, status, reserved1:list):
        self.iTOW = iTOW
        self.aopCFG = aopCFG
        self.reserved1 = reserved1

        if reserved1.__len__() != 10:
            for i in range(10):
                reserved1.append(None)

        self.status = status

class bits32:
    def __init__(self, all, iTOW, useAOP, status):
        self.all = all
        self.iTOW = iTOW
        self.useAOP = useAOP
        self.status = status

class UBX_NAV_AOPSTATUS_moduleQueried_t:
    def __init__(self, all, bits:bits32):
        self.all = all
        self.bits = bits

class UBX_NAV_AOPSTATUS_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, data:UBX_NAV_AOPSTATUS_data_t, moduleQueried:UBX_NAV_AOPSTATUS_moduleQueried_t, callbackPointer:UBX_NAV_AOPSTATUS_data_t, callbackPointerPtr:UBX_NAV_AOPSTATUS_data_t, callbackData:UBX_NAV_AOPSTATUS_data_t):
        self.automaticFlags = automaticFlags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callbackPointer = callbackPointer
        self.callbackPointerPtr = callbackPointerPtr
        self.callbackData = callbackData

UBX_NAV_EOE_LEN = 4

class UBX_NAV_EOE_data_t:
    def __init__(self, iTOW):
        self.iTOW = iTOW

class moduleQueried14:
    def __init__(self, all, iTOW):
        self.all = all
        self.iTOW = iTOW

class UBX_NAV_EOE_moduleQueried_t:
    def __init__(self, all, moduleQueried:moduleQueried14):
        self.all = all
        self.moduleQueried = moduleQueried

class UBX_NAV_EOE_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags,moduleQueried:UBX_NAV_EOE_moduleQueried_t,data:UBX_NAV_EOE_data_t, callbackPointer:UBX_NAV_EOE_data_t, callbackPointrPtr:UBX_NAV_EOE_data_t, callbackData:UBX_NAV_EOE_data_t):
        self.automaticFlags = automaticFlags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callbackPointer = callbackPointer
        self.callbackPointerPtr = callbackPointrPtr
        self.callbackData = callbackData


UBX_RXM_SFRBX_MAX_WORDS = 16
UBX_RXM_SFRBX_MAX_LEN = 8 + (4 * UBX_RXM_SFRBX_MAX_WORDS)

class UBX_RXM_SFRBX_data_t:
    def __init__(self, gnssId, svId, reserved1, freqId, numWords, chn, version, reserved2, dwrd:list):
        self.gnssId = gnssId
        self.svId = svId
        self.reserved1 = reserved1
        self.freqId = freqId
        self.numWords = numWords
        self.chn = chn
        self.version = version
        self.reserved2 = reserved2
        self.drwd = dwrd

        if dwrd.__len__() != UBX_RXM_SFRBX_MAX_WORDS:
            for i in range(UBX_RXM_SFRBX_MAX_WORDS):
                dwrd.append(None)

class UBX_RXM_SFRBX_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, data:UBX_RXM_SFRBX_data_t, moduleQueried:bool, callbackPointer:UBX_RXM_SFRBX_data_t, callbackPointerPtr:UBX_RXM_SFRBX_data_t, callbackData:UBX_RXM_SFRBX_data_t) -> None:
        self.automaticFlags = automaticFlags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callbackPointer = callbackPointer
        self.callbackPointerPtr = callbackPointerPtr
        self.callbackData = callbackData

UBX_RXM_RAWX_MAX_BLOCKS = 92
RAWX_MAX_LEN = 16 + (32 * UBX_RXM_RAWX_MAX_BLOCKS)

class bits33:
    def __init__(self, leapSec, clkReset) -> None:
        self.leapSec = leapSec
        self.clkReset = clkReset


class recStat:
    def __init__(self, all, bits:bits33) -> None:
        self.all = all
        self.bits = bits


class UBX_RXM_RAWX_header_t:
    def __init__(self, rcvTow:list, week, leapS, numMeas, version, reserved1) -> None:
        self.rcvTow = rcvTow
        for i in range(8):
            rcvTow.append(None)
        self.week = week
        self.LeapS = leapS
        self.numMeas = numMeas
        self.version = version
        self.reserved1 = reserved1
        reserved1 = [None, None]

class bitsTrkstat:
    def __init__(self, prValid, cpVAlid, halfCyc, subHalfCyc):
        self.prValid = prValid
        self.cpValid = cpVAlid
        self.halfCyc = halfCyc
        self.subHalfCyc = subHalfCyc
class trkstat:
    def __init__(self, all, bits:bitsTrkstat):
        self.all =  all
        self.bits = bits


class UBX_RXM_RAWX_block_t:
    def __init__(self, prMes:list, cpMes:list, doMes:list, gnssId, svId, sigId, freqId, lockTime, cno, prStdev, cpStdev, doStdev, trk:trkstat, reserved2):
        self.prMes = prMes
        prMes = []
        for i in range(8):
            prMes.append(None)


        self.cpMes = cpMes
        cpMes = []
        for i in range(8):
            cpMes.append(None)

        self.doMes = doMes
        doMes = []
        for i in range(8):
            doMes.append(None)

        self.gnssId = gnssId
        self.svId = svId
        self.freqId = freqId
        self.lockTime = lockTime
        self.cno = cno
        self.prStdev = prStdev
        self.cpStdev = cpStdev
        self.doStdev = doStdev
        self.trk = trk
        self.reserved2 = reserved2

class UBX_RXM_RAWX_data_t:
    def __init__(self, header:UBX_RXM_RAWX_header_t, blocks:list):
        for i in range(UBX_RXM_RAWX_MAX_BLOCKS):
            blocks.append(UBX_RXM_RAWX_block_t())

class UBX_RXM_RAWX_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, data:UBX_RXM_RAWX_data_t, moduleQueried:bool, callbackPointer:UBX_RXM_RAWX_data_t, callbackPointerPtr:UBX_RXM_RAWX_data_t, callbackData:UBX_RXM_RAWX_data_t):
        self.automaticFlags = automaticFlags
        self.data = data
        self.moduleQueried = moduleQueried
        self.callbackPointer = callbackPointer
        self.callnackData = callbackData

UBX_RXM_COR_LEN = 12
class bits34:
    def __init__(self,protocol, errStatus, msgUsed, correctionId, msgTypeValid, msgSubTypeValid, msgInputHandle, msgEncrypted, msgDecrypted) -> None:
        self.protocol = protocol
        self.errStatus = errStatus
        self.msgUsed = msgUsed
        self.correctionId = correctionId
        self.msgTypeValid = msgTypeValid
        self.msgSubTypeValid = msgSubTypeValid
        self.msgInputHandle = msgInputHandle
        self.msgEcrypted = msgEncrypted
        self.msgDecrypted = msgDecrypted



class statusinfo:
    def __init__(self, all, bits:bits34):
        self.all = all
        self.bits = bits1


class UBX_RXM_COR_data_t:
    def __init__(self, version, ebno, reserved0:list, statusinfo:statusinfo, msgType, msgSybType) -> None:
        self.version = version
        self.ebno = ebno
        self.reserved0 = reserved0
        for i in range(2):
            reserved0.append(None)
        self.statusinfo = statusinfo
        self.msgType = msgType
        self.msgSubType = msgSybType

class UBX_RXM_COR_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, callbackPointer:UBX_RXM_COR_data_t, callbackPointerPtr:UBX_RXM_COR_data_t, callbackData:UBX_RXM_COR_data_t):
        self.automaticFlags = automaticFlags
        self.callbaclPointers = callbackPointer
        self.callbackPointerPtr = callbackPointerPtr
        self.callbacdata = callbackData

UBX_RXM_PMP_MAX_USER_DATA = 504
UBX_RXM_PMP_MAX_LEN = UBX_RXM_PMP_MAX_USER_DATA + 24

class UBX_RXM_PMP_data_t:
    def __init__(self, version, reserved0, numBytesUserData, timeTag, uniqueWord:list, serviceIdentifier, spare, uniqueWordBitErrors, fecBits, ebno, reserved1, userData:list):
        self.version = version
        self.reserved0 = reserved0
        self.numBytesUserData = numBytesUserData
        self.timeTag = timeTag
        self.uniqueWord = uniqueWord
        for i in range(2):
            uniqueWord.append(None)

        self.serviceIdentifier = serviceIdentifier
        self.spare = spare
        self.uniqueWordBitErrors = uniqueWordBitErrors
        self.fecBits = fecBits
        self.ebno = ebno
        self.reserved1 = reserved1
        self.userData = userData
        for i in range(UBX_RXM_PMP_MAX_USER_DATA):
            userData.append(None)


class UBX_RXM_PMP_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, callbackPointerPtr:UBX_RXM_PMP_data_t, callbackData:UBX_RXM_PMP_data_t):
        self.automaticFlags = automaticFlags
        self.callbackPointerPtr = callbackPointerPtr
        self.callbackData = callbackData

class UBX_RXM_PMP_message_data_t:
    def __init__(self, sync1, sync2, cls, ID, lenghtLSB, lenghtMSB, payload:list, checksumA, checksumB):
        self.sync1 = sync1
        self.sync2 = sync2
        self.cls = cls
        self.ID =  ID
        self.lenghtLSB = lenghtLSB
        self.lenghtMSB = lenghtMSB
        self.payload = payload

        for i in range(UBX_RXM_PMP_MAX_LEN):
            payload.append(None)

        self.checksumA = checksumA
        self.checksumB = checksumB

class UBX_RXM_PMP_message_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, callbackPointerPtr:UBX_RXM_PMP_message_data_t, callbackData:UBX_RXM_PMP_message_data_t ):
        self.automaticFlags = automaticFlags
        self.callBackPointerPtr = callbackPointerPtr
        self.callbackData = callbackData

UBX_RXM_QZSSL6_NUM_CHANNELS = 2
UBX_RXM_QZSSL6_DATALEN = 250
UBX_RXM_QZSSL6_MAX_LEN = UBX_RXM_QZSSL6_DATALEN + 14

class UBX_RXM_QZSSL6_data_t:
    def __init__(self, version, svId, cno, timeTag, groupDelay, bitErrCorr, chInfo, reserved0:list, msgBytes:list):
        self.version = version
        self.svId = svId
        self.cno = cno
        self.timeTag = timeTag
        self.groupDelay = groupDelay
        self.bitErrCorr = bitErrCorr
        self.chInfo = chInfo
        self.reserved0 = reserved0
        for i in range(2):
            reserved0.append(None)

        self.msgBytes = msgBytes
        for j in range(UBX_RXM_QZSSL6_DATALEN):
            msgBytes.append(None)

class bits35:
    def __init__(self, automatic, implicitUpdate, addToFileBuffer, callbackCopyValid):
        self.automatic = automatic
        self.implicitUpdate = implicitUpdate
        self.addToFileBuffer = addToFileBuffer
        self.callbackCopyValid = callbackCopyValid

class ubxQZSSL6AutomaticFlags:
    def __init__(self, all, bits:bits35):
        self.all = all
        self.bits = bits

class UBX_RXM_QZSSL6_message_data_t:
    def __init__(self, sync1,  sync2, cls, ID, lenghtLSB, lenghtMSB, payload:list, checksumA, checksumB):
        self.sync1 = sync1 # 0xB5
        self.sync2 = sync2 # 0x62
        self.cls = cls
        self.ID = ID
        self.lenghtLSB = lenghtLSB
        self.lenghtMSB = lenghtMSB
        self.payload = payload
        for i in range(UBX_RXM_QZSSL6_MAX_LEN):
            payload.append(None)

        self.checksumA = checksumA
        self.checksumB = checksumB

class UBX_RXM_QZSSL6_message_t:
    def __init__(self, automaticFlags:ubxQZSSL6AutomaticFlags, callbackPointerPtr:UBX_RXM_QZSSL6_message_data_t,callbackData:UBX_RXM_QZSSL6_message_data_t):
        self.automaticFlags = automaticFlags
        self.callbackPointerPtr = callbackPointerPtr
        self.callbackData = callbackData

# CFG Structs
# UBX-CFG-PRT (0x06 0x00): Port configuration
# The content changes depending on which port type is being configured
# This struct defines the common structure

UBX_CFG_PRT_LEN = 20

class bits36:
    def __init__(self, inUbx, inNmea, inRtcm, reserved, inRtcm3, inSPARTN):
        self.inUbx = inUbx
        self.inNmea = inNmea
        self.inRtcm = inRtcm
        self.reserved = reserved
        self.inRtcm3 = inRtcm3
        self.inSPARTN = inSPARTN


class inProtoMask:
    def __init__(self, all, bits:bits36):
        self.all = all
        self.bits = bits

class outProtoMask:
    def __init__(self, outUbx, outNmea, reserved, outRtcm3, outSPARTN):
        self.outUbx = outUbx
        self.outNmea = outNmea
        self.reserved = reserved
        self.outRtcm3 = outRtcm3
        self.outSPARTN = outSPARTN

class UBX_CFG_PTR_data_t:
    def __init__(self, all, inprotomask:inProtoMask, outprotomask:outProtoMask, flags, reserved1):
        self.all = all
        self.inprotomask = inprotomask
        self.outprotomask = outprotomask
        self.flags = flags
        self.reserved1 = reserved1

class UBX_CFG_PRT_t:
    def __init__(self, data:UBX_CFG_PTR_data_t, dataValid:bool):
        self.data = data
        self.dataValid = dataValid

UBX_CFG_RATE_LEN = 6

class UBX_CFG_RATE_data_t:
    def __init__(self, measRate, navRate, timeRef):
        self.measRate = measRate
        self.navRate = navRate
        self.timeRef = timeRef

class bits37:
    def __init__(self, all, measRate, navRate, timeRef):
        self.all = all
        self.measRate = measRate
        self.navRate = navRate
        self.timeRef = timeRef

class moduleQueried15:
    def __init__(self, all, bits:bits37):
        self.all = all
        self.bits = bits

class UBX_CFG_RATE_moduleQueried_t:
    def __init__(self, all, moduleQueried:moduleQueried15):
        self.all = all
        self.moduleQueried = moduleQueried

class UBX_CFG_RATE_t:
    def __init__(self, automaticFlags:ubxAutomaticFlags, data:UBX_CFG_RATE_data_t, moduleQueried:UBX_CFG_RATE_moduleQueried_t):
        self.automaticFlags = automaticFlags
        self.data = data
        self.moduleQueried = moduleQueried

UBX_CFG_TP5_LEN = 32

class Flags_tp5_data:
    def __init__(self):
        self.all = 0
        self.active = False  # If set enable time pulse; if pin assigned to another function, other function takes precedence.
        self.lockGnssFreq = False  # If set, synchronize time pulse to GNSS as soon as GNSS time is valid.
        self.lockedOtherSet = False  # If set the receiver switches between the timepulse settings given by 'freqPeriodLocked' & 'pulseLenLocked' and those given by 'freqPeriod' & 'pulseLen'.
        self.isFreq = False  # If set 'freqPeriodLock' and 'freqPeriod' are interpreted as frequency, otherwise interpreted as period.
        self.isLength = False  # If set 'pulseLenRatioLock' and 'pulseLenRatio' interpreted as pulse length, otherwise interpreted as duty cycle.
        self.alignToTow = False  # Align pulse to top of second (period time must be integer fraction of 1s).
        self.polarity = False  # Pulse polarity: 0: falling edge at top of second; 1: rising edge at top of second
        self.gridUtcGnss = 0  # Timegrid to use: 0: UTC; 1: GPS; 2: GLONASS; 3: BeiDou; 4: Galileo
        self.syncMode = 0  # Sync Manager lock mode to use


class UBX_CFG_TP5_data_t:
    def __init__(self):
        self.tpIdx = 0  # Time pulse selection (0 = TIMEPULSE, 1 = TIMEPULSE2)
        self.version = 0x01  # Message version (0x01 for this version)
        self.reserved1 = [0, 0]  # Reserved bytes
        self.antCableDelay = 0  # Antenna cable delay: ns
        self.rfGroupDelay = 0  # RF group delay: ns
        self.freqPeriod = 0  # Frequency or period time, depending on setting of bit 'isFreq': Hz_or_us
        self.freqPeriodLock = 0  # Frequency or period time when locked to GNSS time, only used if 'lockedOtherSet' is set: Hz_or_us
        self.pulseLenRatio = 0  # Pulse length or duty cycle, depending on 'isLength': us_or_2^-32
        self.pulseLenRatioLock = 0  # Pulse length or duty cycle when locked to GNSS time, only used if 'lockedOtherSet' is set: us_or_2^-32
        self.userConfigDelay = 0  # User-configurable time pulse delay: ns
        self.flags = Flags_tp5_data()  # Flags union

UBX_CFG_ITFM_LEN = 8 # UBX-CFG-ITFM (0x06 0x39): Jamming/interference monitor configuration

class Config:
        def __init__(self):
            self.bbThreshold = 0  # Broadband jamming detection threshold (4 bits)
            self.cwThreshold = 0  # CW jamming detection threshold (5 bits)
            self.algorithmBits = 0  # Reserved algorithm settings (22 bits)
            self.enable = 0  # Enable interference detection (1 bit)

        @property
        def all(self):
            return (self.bbThreshold << 27) | (self.cwThreshold << 22) | (self.algorithmBits << 0) | (self.enable << 31)

class Config2:
    def __init__(self):
        self.generalBits = 0  # General settings (12 bits)
        self.antSetting = 0  # Antenna setting (2 bits)
        self.enable2 = 0  # Set to 1 to scan auxiliary bands (1 bit)

    @property
    def all(self):
        return (self.generalBits << 20) | (self.antSetting << 18) | (self.enable2 << 31)

class UBX_CFG_ITFM_data_t:
    def __init__(self):
        self.config = Config()
        self.config2 = Config2()

BX_CFG_TMODE3_LEN = 40

class Flags_Cfg_tmode3:
        def __init__(self):
            self.mode = 0  # Receiver Mode: 0 Disabled; 1 Survey In; 2 Fixed Mode (true ARP position information required); 3-255 Reserved
            self.lla = 0  # Position is given in LAT/LON/ALT (default is ECEF)

        @property
        def all(self):
            mode_mask = 0xFF << 0
            lla_mask = 0x1 << 8

            return (self.mode & 0xFF) | (self.lla << 8)



class UBX_CFG_TMODE3_data_t:
    def __init__(self):
        self.version = 0  # Message version (0x00 for this version)
        self.reserved1 = 0
        self.flags = Flags_Cfg_tmode3()
        self.ecefXOrLat = 0  # WGS84 ECEF X coordinate (or latitude) of the ARP position, depending on flags above: cm or deg*1e-7
        self.ecefYOrLon = 0  # WGS84 ECEF Y coordinate (or latitude) of the ARP position, depending on flags above: cm or deg*1e-7
        self.ecefZOrAlt = 0  # WGS84 ECEF Z coordinate (or altitude) of the ARP position, depending on flags above: cm
        self.ecefXOrLatHP = 0  # High-precision WGS84 ECEF X coordinate (or latitude) of the ARP position, depending on flags above: 0.1 mm or deg*1e-9
        self.ecefYOrLonHP = 0  # High-precision WGS84 ECEF Y coordinate (or longitude) of the ARP position, depending on flags above: 0.1 mm or deg*1e-9
        self.ecefZOrAltHP = 0  # High-precision WGS84 ECEF Z coordinate (or altitude) of the ARP position, depending on flags above: 0.1 mm
        self.reserved2 = 0
        self.fixedPosAcc = 0  # Fixed position 3D accuracy: 0.1 mm
        self.svinMinDur = 0  # Survey-in minimum duration: s
        self.svinAccLimit = 0  # Survey-in position accuracy limit: 0.1 mm
        self.reserved3 = [0] * 8  # array of reserved bits


UBX_MON_HW_LEN = 60



class Flags_mon_hw:
    def __init__(self):
        self.rtcCalib = 0  # RTC is calibrated
        self.safeBoot = 0  # Safeboot mode (0 = inactive, 1 = active)
        self.jammingState = 0  # Output from jamming/interference monitor (0 = unknown or feature disabled,
                                # 1 = ok - no significant jamming,
                                # 2 = warning - interference visible but fix OK,
                                # 3 = critical - interference visible and no fix)
        self.xtalAbsent = 0  # RTC xtal has been determined to be absent

    @property
    def all(self):
        rtc_calib_mask = 0x1 << 0
        safe_boot_mask = 0x1 << 1
        jamming_state_mask = 0x3 << 2
        xtal_absent_mask = 0x1 << 4

        return (self.rtcCalib & 0x1) | (self.safeBoot << 1) | (self.jammingState << 2) | (self.xtalAbsent << 4)

class UBX_MON_HW_data_t:
    def __init__(self):
        self.pinSel = 0  # Mask of pins set as peripheral/PIO
        self.pinBank = 0  # Mask of pins set as bank A/B
        self.pinDir = 0  # Mask of pins set as input/output
        self.pinVal = 0  # Mask of pins value low/high
        self.noisePerMS = 0  # Noise level as measured by the GPS core
        self.agcCnt = 0  # AGC monitor (counts SIGHI xor SIGLO, range 0 to 8191)
        self.aStatus = 0  # Status of the antenna supervisor state machine (0=INIT, 1=DONTKNOW, 2=OK, 3=SHORT, 4=OPEN)
        self.aPower = 0  # Current power status of antenna (0=OFF, 1=ON, 2=DONTKNOW)
        self.flags = Flags_mon_hw()
        self.reserved1 = 0  # Reserved
        self.usedMask = 0  # Mask of pins that are used by the virtual pin manager
        self.VP = [0] * 17  # Array of pin mappings for each of the 17 physical pins
        self.jamInd = 0  # CW jamming indicator, scaled (0 = no CW jamming, 255 = strong CW jamming)
        self.reserved2 = [0] * 2  # Reserved
        self.pinIrq = 0  # Mask of pins value using the PIO Irq
        self.pullH = 0  # Mask of pins value using the PIO pull high resistor
        self.pullL = 0  # Mask of pins value using the PIO pull low resistor

UBX_MON_HW2_LEN = 28

class UBX_MON_HW2_data_t:
    def __init__(self):
        self.ofsI = 0
        self.magI = 0
        self.ofsQ = 0
        self.magQ = 0
        self.cfgSource = 0
        self.reserved0 = [0]*3
        self.lowlevelCfg = 0
        self.reserved1 = [0]*8
        self.postStatus = 0
        self.reserved2 = [0]*4

UBX_MON_RF_MAX_BLOCKS = 2
UBX_MON_RF_MAX_LEN = 4 + (24 * UBX_MON_RF_MAX_BLOCKS)

class UBX_MON_RF_header_t:
    def __init__(self):
        self.version = 0x00 #Message version
        self.nBlocks = 0 #number of rf blocks included
        self.reserved0 = [0]*0 #Reserved bits

class Flags_MON_RF_block:
        def __init__(self):
            self.jammingState = 0  # output from Jamming/Interference Monitor (0 = unknown or feature disabled,
                                   # 1 = ok - no significant jamming,
                                   # 2 = warning - interference visible but fix OK,
                                   # 3 = critical - interference visible and no fix)

        @property
        def all(self):
            jamming_state_mask = 0x3 << 0

            return self.jammingState & 0x3

class UBX_MON_RF_block_t:
    def __init__(self):
        self.blockId = 0  # RF block ID (0 = L1 band, 1 = L2 or L5 band depending on product configuration)
        self.flags = Flags_MON_RF_block()
        self.antStatus = 0  # Status of the antenna supervisor state machine (0x00=INIT, 0x01=DONTKNOW, 0x02=OK, 0x03=SHORT, 0x04=OPEN)
        self.antPower = 0  # Current power status of antenna (0x00=OFF, 0x01=ON, 0x02=DONTKNOW)
        self.postStatus = 0  # POST status word
        self.reserved1 = [0] * 4  # Reserved
        self.noisePerMS = 0  # Noise level as measured by the GPS core
        self.agcCnt = 0  # AGC Monitor (counts SIGHI xor SIGLO, range 0 to 8191)
        self.jamInd = 0  # CW jamming indicator, scaled (0=no CW jamming, 255 = strong CW jamming)
        self.ofsI = 0  # Imbalance of I-part of complex signal, scaled (-128 = max. negative imbalance, 127 = max. positive imbalance)
        self.magI = 0  # Magnitude of I-part of complex signal, scaled (0 = no signal, 255 = max.magnitude)
        self.ofsQ = 0  # Imbalance of Q-part of complex signal, scaled (-128 = max. negative imbalance, 127 = max. positive imbalance)
        self.magQ = 0  # Magnitude of Q-part of complex signal, scaled (0 = no signal, 255 = max.magnitude)
        self.reserved2 = [0] * 3  # Reserved


class UBX_MON_RF_data_t:
    def __init__(self):
        self.header = UBX_MON_RF_header_t()
        self.blocks = [UBX_MON_RF_block_t()] * UBX_MON_RF_MAX_BLOCKS

UBX_TIM_TM2_LEN = 28

class flags_tim_tm2_data:
    def __init__(self):
        self.all = 0
        self.mode = 0
        self.run = 0
        self.new_falling_edge = 0
        self.time_base = 0
        self.utc = 0
        self.time = 0
        self.new_rising_edge = 0

class UBX_TIM_TM2_data:
    def __init__(self):
        self.ch = 0  # Channel
        self.flags = flags_tim_tm2_data()
        self.count = 0  # Rising edge counter
        self.wn_r = 0  # Week number of last rising edge
        self.wn_f = 0  # Week number of last falling edge
        self.tow_ms_r = 0  # TOW of rising edge: ms
        self.tow_sub_ms_r = 0  # Millisecond fraction of tow of rising edge: ns
        self.tow_ms_f = 0  # TOW of falling edge: ms
        self.tow_sub_ms_f = 0  # Millisecond fraction of tow of falling edge: ns
        self.acc_est = 0  # Accuracy estimate: ns

class moduleQueried_tim_tm2:
    def __init__(self):
        self.all = 0
        self.mode = 0
        self.run = 0
        self.newFallingEdge = 0
        self.timeBase = 0
        self.utc = 0
        self.time = 0
        self.newRisingAngle = 0
        self.count = 0
        self.wnR = 0
        self.wnF = 0
        self.towMsR = 0
        self.towSubMsR = 0
        self.towMsF = 0
        self.towSubMsF = 0
        self.accEst = 0

class UBX_TIM_TM2_moduleQueried:
    def __init__(self):
        self.all = 0
        self.moduleQueried = moduleQueried_tim_tm2()

class UBX_TIM_TM2:
    def __init__(self):
        self.automatic_flags = ubxAutomaticFlags()  # assuming UBX_AutomaticFlags is already defined as a Python class
        self.data = UBX_TIM_TM2_data()
        self.module_queried = UBX_TIM_TM2_moduleQueried()
        self.callback_pointer = None  # function pointer, not directly supported in Python
        self.callback_pointer_ptr = None  # function pointer, not directly supported in Python
        self.callback_data = None  # pointer to UBX_TIM_TM2_data_t, not directly supported in Python

UBX_ESF_ALG_LEN = 16

class flags_ESF_ALG_data:
    def __init__(self):
        self.autoMntAlgOn = 0
        self.status = 0
        self.tiltAlgError = 0
        self.yawAlgError = 0
        self.angleError = 0

class UBX_ESF_ALG_data_t:
    def __init__(self):
        self.iTOW = 0
        self.version = 0
        self.flags = flags_ESF_ALG_data()
        self.reserved1 = 0
        self.yaw = 0
        self.pitch = 0
        self.roll = 0

class UBX_ESF_ALG_moduleQueried_t:
    def __init__(self):
        self.all = 0
        self.iTOW = 0
        self.version =  0
        self.autoMntAlgOn: 0
        self.status = 0
        self.tiltAlgError = 0
        self.yawAlgError = 0
        self.angleError = 0
        self.yaw = 0
        self.pitch = 0
        self.roll = 0


class UBX_ESF_ALG_t:
    def __init__(self):
        self.automaticFlags = ubxAutomaticFlags() # assuming UBX_AutomaticFlags is already defined as a Python class
        self.data = UBX_ESF_ALG_data_t()
        self.moduleQueried = UBX_ESF_ALG_moduleQueried_t()
        self.callbackPointer = None  # function pointer, not directly supported in Python
        self.callbackPointerPtr = None  # function pointer, not directly supported in Python
        self.callbackData = None  # pointer to UBX_ESF_ALG_data_t, not directly supported in Python

class bitfield0:
    def __init__(self):
        self.version = 0
        self.xAngRateValid = 0
        self.yAngRateValid = 0
        self.zAngRateValid = 0
        self.xAccelValid = 0
        self.yAccelValid = 0
        self.zAccelValid = 0

UBX_ESF_INS_LEN = 36

UBX_MGA_ACK_DATA0_RINGBUFFER_LEN = 16


class UBX_ESF_INS_data_t:
    def __init__(self):
        self.bitfield0 = bitfield0()
        self.reserved1 = [0] * 4
        self.iTOW = 0
        self.xAngRate = 0
        self.yAngRate = 0
        self.zAngRate = 0

class UBX_ESF_INS_moduleQueried_t:
    def __init__(self):
        self.all = 0
        self.version = 0
        self.xAngRateValid = 0
        self.yAngRateValid = 0
        self.zAngRateValid = 0
        self.xAccelValid = 0
        self.yAccelValid = 0
        self.zAccelValid = 0
        self.iTOW = 0
        self.xAngRate = 0
        self.yAngRate = 0
        self.zAngRate = 0
        self.xAccel = 0
        self.yAccel = 0
        self.zAccel = 0

class UBX_ESF_INS_t:
    def __init__(self):
        self.automaticFlags = ubxAutomaticFlags()  # ubxAutomaticFlags
        self.data = UBX_ESF_INS_data_t()  # UBX_ESF_INS_data_t
        self.moduleQueried = UBX_ESF_INS_moduleQueried_t()  # UBX_ESF_INS_moduleQueried_t
        self.callbackPointer = UBX_ESF_INS_moduleQueried_t()  # function pointer
        self.callbackPointerPtr = UBX_ESF_INS_moduleQueried_t()  # function pointer
        self.callbackData = UBX_ESF_INS_moduleQueried_t()  # UBX_ESF_INS_data_t pointer


UBX_ESF_MEAS_MAX_LEN = 8 + (4 * DEF_MAX_NUM_ESF_MEAS) + 4

class UBX_ESF_MEAS_sensorData_t:
    def __init__(self):
        self.data = UBX_ESF_MEAS_sensorData_union()

class UBX_ESF_MEAS_sensorData_union:
    def __init__(self):
        self.all = 0
        self.bits = UBX_ESF_MEAS_sensorData_bits()

class UBX_ESF_MEAS_sensorData_bits:
    def __init__(self):
        self.dataField = 0
        self.dataType = 0

class UBX_ESF_MEAS_data_t:
    def __init__(self):
        self.timeTag = 0
        self.flags = UBX_ESF_MEAS_flags_union()
        self.id = 0
        self.data = [UBX_ESF_MEAS_sensorData_t() for i in range(DEF_MAX_NUM_ESF_MEAS)]
        self.calibTtag = 0

class UBX_ESF_MEAS_flags_union:
    def __init__(self):
        self.all = 0
        self.bits = UBX_ESF_MEAS_flags_bits()

class UBX_ESF_MEAS_flags_bits:
    def __init__(self):
        self.timeMarkSent = 0
        self.timeMarkEdge = 0
        self.calibTtagValid = 0
        self.reserved = 0
        self.numMeas = 0

class UBX_ESF_MEAS_t:
    def __init__(self):
        self.automaticFlags = ubxAutomaticFlags()
        self.data = UBX_ESF_MEAS_data_t()
        self.callbackPointer = UBX_ESF_MEAS_data_t()
        self.callbackPointerPtr = UBX_ESF_MEAS_data_t()
        self.callbackData = UBX_ESF_MEAS_data_t()

UBX_ESF_RAW_MAX_LEN = 4 + (8 * DEF_NUM_SENS * DEF_MAX_NUM_ESF_RAW_REPEATS)

class UBX_ESF_RAW_sensorData_t:
    def __init__(self):
        self.data = UBX_ESF_RAW_sensorData_union()
        self.sTag = 0

class UBX_ESF_RAW_sensorData_union:
    def __init__(self):
        self.all = 0
        self.bits = UBX_ESF_RAW_sensorData_bits()

class UBX_ESF_RAW_sensorData_bits:
    def __init__(self):
        self.dataField = 0
        self.dataType = 0

class UBX_ESF_RAW_data_t:
    def __init__(self):
        self.reserved1 = [0] * 4
        self.data = [UBX_ESF_RAW_sensorData_t() for _ in range(DEF_NUM_SENS * DEF_MAX_NUM_ESF_RAW_REPEATS)]
        self.numEsfRawBlocks = 0

class UBX_ESF_RAW_t:
    def __init__(self):
        self.automaticFlags = None  # ubxAutomaticFlags
        self.data = UBX_ESF_RAW_data_t()
        self.callbackPointer = None  # function pointer
        self.callbackPointerPtr = None  # function pointer
        self.callbackData = None  # UBX_ESF_RAW_data_t pointer

UBX_ESF_STATUS_MAX_LEN = 16 + (4 * DEF_NUM_SENS)

class UBX_ESF_STATUS_sensorStatus_t:
    def __init__(self):
        self.sensStatus1 = UBX_ESF_STATUS_sensorStatus1_union()
        self.sensStatus2 = UBX_ESF_STATUS_sensorStatus2_union()
        self.freq = 0
        self.faults = UBX_ESF_STATUS_faults_union()

class UBX_ESF_STATUS_sensorStatus1_union:
    def __init__(self):
        self.all = 0
        self.bits = UBX_ESF_STATUS_sensorStatus1_bits()

class UBX_ESF_STATUS_sensorStatus1_bits:
    def __init__(self):
        self.type = 0
        self.used = 0
        self.ready = 0

class UBX_ESF_STATUS_sensorStatus2_union:
    def __init__(self):
        self.all = 0
        self.bits = UBX_ESF_STATUS_sensorStatus2_bits()

class UBX_ESF_STATUS_sensorStatus2_bits:
    def __init__(self):
        self.calibStatus = 0
        self.timeStatus = 0

class UBX_ESF_STATUS_faults_union:
    def __init__(self):
        self.all = 0
        self.bits = UBX_ESF_STATUS_faults_bits()

class UBX_ESF_STATUS_faults_bits:
    def __init__(self):
        self.badMeas = 0
        self.badTTag = 0
        self.missingMeas = 0
        self.noisyMeas = 0

class UBX_ESF_STATUS_data_t:
    def __init__(self):
        self.iTOW = 0
        self.version = 0
        self.reserved1 = [0] * 7
        self.fusionMode = 0
        self.reserved2 = [0] * 2
        self.numSens = 0
        self.status = [UBX_ESF_STATUS_sensorStatus_t() for _ in range(DEF_NUM_SENS)]

class UBX_ESF_STATUS_moduleQueried_t:
    def __init__(self):
        self.all = 0
        self.bits = UBX_ESF_STATUS_moduleQueried_bits()

class UBX_ESF_STATUS_moduleQueried_bits:
    def __init__(self):
        self.all = 0
        self.iTOW = 0
        self.version = 0
        self.fusionMode = 0
        self.numSens = 0
        self.status = [0] * DEF_NUM_SENS

class UBX_ESF_STATUS_t:
    def __init__(self):
        self.automaticFlags = ubxAutomaticFlags()  # ubxAutomaticFlags
        self.data = UBX_ESF_STATUS_data_t()
        self.moduleQueried = UBX_ESF_STATUS_moduleQueried_t()
        self.callbackPointer = UBX_ESF_STATUS_data_t()  # function pointer
        self.callbackPointerPtr = UBX_ESF_STATUS_data_t()  # function pointer
        self.callbackData = UBX_ESF_STATUS_data_t()  # UBX_ESF_STATUS_data_t pointer


UBX_MGA_ACK_DATA0_LEN = 8

UBX_MGA_ACK_DATA0_RINGBUFFER_LEN  = 16 # Provide storage for 16 MGA ACK packets

class UBX_MGA_ACK_DATA0_data_t:
    def __init__(self):
        self.type = 0
        self.version = 0
        self.infoCode = 0
        self.msgId = 0
        self.msgPayloadStart = [0] * 4

UBX_MGA_DBD_LEN = 164

class UBX_MGA_DBD_data_t:
    def __init__(self):
        self.dbdEntryHeader1 = 0
        self.dbdEntryHeader2 = 0
        self.dbdEntryClass = 0
        self.dbdEntryID = 0
        self.dbdEntryLenLSB = 0
        self.dbdEntryLenMSB = 0
        self.dbdEntry = [0] * UBX_MGA_DBD_LEN
        self.dbdEntryChecksumA = 0
        self.dbdEntryChecksumB = 0

UBX_MGA_DBD_RINGBUFFER_LEN = 190
UBX_MGA_DBD_RINGBUFFER_LEN = 250

class UBX_MGA_DBD_t:
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.data = [UBX_MGA_DBD_data_t() for _ in range(UBX_MGA_DBD_RINGBUFFER_LEN)]


UBX_HNR_PVT_LEN = 72

class UBX_HNR_PVT_data_t:
    def __init__(self):
        self.iTOW = 0
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour = 0
        self.min = 0
        self.sec = 0
        self.valid = UBX_HNR_PVT_valid_t()
        self.nano = 0
        self.gpsFix = 0
        self.flags = UBX_HNR_PVT_flags_t()
        self.reserved1 = [0] * 2
        self.lon = 0
        self.lat = 0
        self.height = 0
        self.hMSL = 0
        self.gSpeed = 0
        self.speed = 0
        self.headMot = 0
        self.headVeh = 0
        self.hAcc = 0
        self.vAcc = 0
        self.sAcc = 0
        self.headAcc = 0
        self.reserved2 = [0] * 4

class UBX_HNR_PVT_valid_t:
    def __init__(self):
        self.validDate = False
        self.validTime = False
        self.fullyResolved = False

class UBX_HNR_PVT_flags_t:
    def __init__(self):
        self.gpsFixOK = False
        self.diffSoln = False
        self.WKNSET = False
        self.TOWSET = False
        self.headVehValid = False

class UBX_HNR_PVT_moduleQueried_t:
    def __init__(self):
        self.moduleQueried = UBX_HNR_PVT_moduleQueried_bits_t()

class UBX_HNR_PVT_moduleQueried_bits_t:
    def __init__(self):
        self.all = 0

        self.iTOW = 0
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour = 0
        self.min = 0
        self.sec = 0

        self.validDate = 0
        self.validTime = 0
        self.fullyResolved = 0

        self.nano = 0
        self.gpsFix = 0

        self.gpsFixOK = 0
        self.diffSoln = 0
        self.WKNSET = 0
        self.TOWSET = 0
        self.headVehValid = 0

        self.lon = 0
        self.lat = 0
        self.height = 0
        self.hMSL = 0
        self.gSpeed = 0
        self.speed = 0
        self.headMot = 0
        self.headVeh = 0
        self.hAcc = 0
        self.vAcc = 0
        self.sAcc = 0
        self.headAcc = 0

class UBX_HNR_PVT_t:
    def __init__(self):
        self.automaticFlags = ubxAutomaticFlags()
        self.data = UBX_HNR_PVT_data_t()
        self.moduleQueried = UBX_HNR_PVT_moduleQueried_t()
        self.callbackPointer = UBX_HNR_PVT_data_t()
        self.callbackPointerPtr = UBX_HNR_PVT_data_t()
        self.callbackData = UBX_HNR_PVT_data_t()

UBX_HNR_ATT_LEN = 32

class UBX_HNR_ATT_data_t:
    def __init__(self):
        self.iTOW = 0
        self.version = 0
        self.reserved1 = [0]*3
        self.roll = 0
        self.pitch = 0
        self.heading = 0
        self.accRoll = 0
        self.accPitch = 0
        self.accHeading = 0

class UBX_HNR_ATT_moduleQueried_t:
    def __init__(self):
        self.moduleQueried = UBX_HNR_ATT_moduleQueried_bits_t()

class UBX_HNR_ATT_moduleQueried_bits_t:
    def __init__(self):
        self.all = 0

        self.iTOW = 0
        self.version = 0
        self.roll = 0
        self.pitch = 0
        self.heading = 0
        self.accRoll = 0
        self.accPitch = 0
        self.accHeading = 0

class UBX_HNR_ATT_t:
    def __init__(self):
        self.automaticFlags = 0
        self.data = UBX_HNR_ATT_data_t()
        self.moduleQueried = UBX_HNR_ATT_moduleQueried_t()
        self.callbackPointer = UBX_HNR_ATT_data_t()
        self.callbackPointerPtr = UBX_HNR_ATT_data_t()
        self.callbackData = UBX_HNR_ATT_data_t()

UBX_HNR_INS_LEN = 36

class UBX_HNR_INS_data_t:
    def __init__(self):
        self.bitfield0 = UBX_HNR_INS_bitfield0_t()
        self.reserved1 = [0]*4
        self.iTOW = 0
        self.xAngRate = 0
        self.yAngRate = 0
        self.zAngRate = 0
        self.xAccel = 0
        self.yAccel = 0
        self.zAccel = 0

class UBX_HNR_INS_bitfield0_t:
    def __init__(self):
        self.version = 0
        self.xAngRateValid = False
        self.yAngRateValid = False
        self.zAngRateValid = False
        self.xAccelValid = False
        self.yAccelValid = False
        self.zAccelValid = False

class UBX_HNR_INS_moduleQueried_t:
    def __init__(self):
        self.moduleQueried = UBX_HNR_INS_moduleQueried_bits_t()

class UBX_HNR_INS_moduleQueried_bits_t:
    def __init__(self):
        self.all = 0

        self.version = 0
        self.xAngRateValid = 0
        self.yAngRateValid = 0
        self.zAngRateValid = 0
        self.xAccelValid = 0
        self.yAccelValid = 0
        self.zAccelValid = 0

        self.iTOW = 0
        self.xAngRate = 0
        self.yAngRate = 0
        self.zAngRate = 0
        self.xAccel = 0
        self.yAccel = 0
        self.zAccel = 0

class UBX_HNR_INS_t:
    def __init__(self):
        self.automaticFlags = 0
        self.data = UBX_HNR_INS_data_t()
        self.moduleQueried = UBX_HNR_INS_moduleQueried_t()
        self.callbackPointer = UBX_HNR_INS_moduleQueried_t()
        self.callbackPointerPtr = UBX_HNR_INS_moduleQueried_t()
        self.callbackData = UBX_HNR_INS_moduleQueried_t()

class nmeaAutomaticFlags:
    def __init__(self):
        self.flags = nmeaAutomaticFlags_bits_t()

class nmeaAutomaticFlags_bits_t:
    def __init__(self):
        self.completeCopyValid = False
        self.completeCopyRead = False
        self.callbackCopyValid = False

NMEA_GGA_MAX_LENGTH = 100

class NMEA_GGA_data:
    def __init__(self, length: int, nmea: bytes):
        self.length = length
        self.nmea = nmea

class NMEA_GPGGA:
    def __init__(self, automatic_flags: nmeaAutomaticFlags, callback_pointer=None, callback_pointer_ptr=None):
        self.automatic_flags = automatic_flags
        self.working_copy = NMEA_GGA_data(0, bytearray(NMEA_GGA_MAX_LENGTH))
        self.complete_copy = NMEA_GGA_data(0, bytearray(NMEA_GGA_MAX_LENGTH))
        self.callback_pointer = callback_pointer
        self.callback_pointer_ptr = callback_pointer_ptr
        self.callback_copy = None

class NMEA_GNGGA:
    def __init__(self, automatic_flags:nmeaAutomaticFlags, callback_pointer=None, callback_pointer_ptr=None):
        self.automatic_flags = automatic_flags
        self.working_copy = NMEA_GGA_data(0, bytearray(NMEA_GGA_MAX_LENGTH))
        self.complete_copy = NMEA_GGA_data(0, bytearray(NMEA_GGA_MAX_LENGTH))
        self.callback_pointer = callback_pointer
        self.callback_pointer_ptr = callback_pointer_ptr
        self.callback_copy = None


NMEA_VTG_MAX_LENGTH = 100

class NMEA_GGA_data:
    def __init__(self, length: int, nmea: bytes):
        self.length = length
        self.nmea = nmea

class NMEA_GPGGA:
    def __init__(self, automatic_flags: nmeaAutomaticFlags, callback_pointer, callback_pointer_ptr):
        self.automatic_flags = automatic_flags
        self.working_copy = NMEA_GGA_data(0, bytearray(NMEA_GGA_MAX_LENGTH))
        self.complete_copy = NMEA_GGA_data(0, bytearray(NMEA_GGA_MAX_LENGTH))
        self.callback_pointer = callback_pointer
        self.callback_pointer_ptr = callback_pointer_ptr
        self.callback_copy = None

class NMEA_GNGGA:
    def __init__(self, automatic_flags: nmeaAutomaticFlags, callback_pointer, callback_pointer_ptr):
        self.automatic_flags = automatic_flags
        self.working_copy = NMEA_GGA_data(0, bytearray(NMEA_GGA_MAX_LENGTH))
        self.complete_copy = NMEA_GGA_data(0, bytearray(NMEA_GGA_MAX_LENGTH))
        self.callback_pointer = callback_pointer
        self.callback_pointer_ptr = callback_pointer_ptr
        self.callback_copy = None


NMEA_RMC_MAX_LENGTH = 100

class NMEA_RMC_data:
    def __init__(self):
        self.length = 0
        self.nmea = [0 for i in range(NMEA_RMC_MAX_LENGTH)]


class NMEA_GPRMC:
    def __init__(self, automatic_flags: nmeaAutomaticFlags):
        self.automatic_flags = automatic_flags
        self.working_copy = NMEA_RMC_data(0, bytearray(NMEA_RMC_MAX_LENGTH))
        self.complete_copy = NMEA_RMC_data(0, bytearray(NMEA_RMC_MAX_LENGTH))
        self.callback_pointer = NMEA_RMC_data()
        self.callback_pointer_ptr = NMEA_RMC_data()
        self.callback_copy = NMEA_RMC_data

class NMEA_GNRMC:
    def __init__(self, automatic_flags: nmeaAutomaticFlags):
        self.working_copy = NMEA_RMC_data(0, bytearray(NMEA_RMC_MAX_LENGTH))
        self.complete_copy = NMEA_RMC_data(0, bytearray(NMEA_RMC_MAX_LENGTH))
        self.callback_pointer = NMEA_RMC_data()
        self.callback_pointer_ptr = NMEA_RMC_data
        self.callback_copy = None


NMEA_ZDA_MAX_LENGTH = 50

class NMEA_ZDA_data:
    def __init__(self, length: int, nmea: bytes):
        self.length = length
        self.nmea = nmea

class NMEA_GPZDA:
    def __init__(self):
        self.automatic_flags = ubxAutomaticFlags()
        self.working_copy = NMEA_ZDA_data(0, bytearray(NMEA_ZDA_MAX_LENGTH))
        self.complete_copy = NMEA_ZDA_data(0, bytearray(NMEA_ZDA_MAX_LENGTH))
        self.callback_pointer = NMEA_ZDA_data()
        self.callback_pointer_ptr = NMEA_ZDA_data()
        self.callback_copy = None

class NMEA_GNZDA:
    def __init__(self, automatic_flags: 'nmeaAutomaticFlags', callback_pointer=None, callback_pointer_ptr=None):
        self.automatic_flags = automatic_flags
        self.working_copy = NMEA_ZDA_data(0, bytearray(NMEA_ZDA_MAX_LENGTH))
        self.complete_copy = NMEA_ZDA_data(0, bytearray(NMEA_ZDA_MAX_LENGTH))
        self.callback_pointer = callback_pointer
        self.callback_pointer_ptr = callback_pointer_ptr
        self.callback_copy = None
