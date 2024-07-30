

if '__u_blox_structs_h__' not in locals():
    __ublox_structs_h_ = None

import SparkFun_u_blox_GNSS_Arduino_Library.py

if 'DEF_NUM_SENS' not in locals():
    DEF_NUM_SENS:int = 7 #max num of ESF sensors

if 'DEF_MAX_NUM_ESF_RAW_REPEATS' not in locals():
    DEF_MAX_NUM_ESF_RAW_REPEATS:int = 10

if 'DEF_MAX_NUM_ESF_MEAS' not in locals():
    DEF_MAX_NUM_ESF_MEAS:int = 31


class bits1:
    def __init__(self, automatic = 1, implicitUpdate = 1, addToFileBuffer = 1, callbackCopyValid = 1):
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
    def __init__(self, all, iTOW, ecefX, ecefY, ecefZ, pAcc):
        self.all = all
        self.iTOW = iTOW
        self.ecefX = ecefX
        self.ecefY = ecefY
        self.ecefZ = ecefZ
        self.pAcc = pAcc
    all = 1
    iTOW = 1
    ecefX = 1
    ecefY = 1
    ecefZ = 1
    pAcc = 1


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
    
    all = 1
    lon = 1
    lat = 1
    heigth = 1
    hMSL = 1 
    hAcc = 1
    vAcc = 1


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
    
    gpsFixOk = 1
    diffSoln = 1
    wknSet = 1
    towSet = 1


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

    diffCorr = 1
    carrSolnValid = 1
    reserved = 4
    mapMatching = 2

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
    
    all = 1
    iTOW = 1 
    gpsFix = 1
    gpsFixOk = 1
    dipassffSoln = 1
    wknSet = 1
    towSet = 1
    diffCor = 1
    carrSolnValid = 1
    mapMatching = 1
    psmState = 1
    spoofDetState = 1
    carrSoln = 1
    ttff = 1
    msss = 1

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

    all = 1
    iTOW = 1
    gDOP = 1
    pDOP = 1
    tDOP = 1
    vDOP = 1
    hDOP = 1
    nDOP = 1
    eDOP = 1


class moduleQueried2:
    def __init__(self, all, bits:bits8) -> None:
        self.all = all
        self.bits = bits
    

class UBX_NAV_DOP_moduleQueried_t:
    def __init__(self, module:moduleQueried2)
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
    def __init__(self, iTOW, version, reserved:list, roll, pitch, heading, accRoll, accPitch, accHeading)
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


        



