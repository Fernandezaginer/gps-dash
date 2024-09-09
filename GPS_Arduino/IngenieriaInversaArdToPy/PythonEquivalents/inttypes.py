from typing import NewType

if '__INTTYPES_H' not in locals():
    __INTTYPES_H_ = None

int_farptr_t = NewType('int_farptr_t',int)

uint_farptr_t = NewType('uint_farptr_t', int)

PRId8:chr = 'd'
PRIdLEAST8:chr = 'd'
PRIdFAST8:chr = 'd'
PRId16:chr = 'd'
PRIdLEAST16:chr = 'd'
PRIdFAST16:chr = "d"

PRIi16:chr = "i"
PRIiLEAST16:chr = "i"
PRIiFAST16:chr = "i"

PRId32:str = "ld"
PRIdLEAST32:str = "ld"
PRIdFAST32:str = "ld"

PRIi32:str = "li"
PRIiLEAST32:str = "li"
PRIiFAST32:str = "li"

PRId64: str = "lld"
PRIdLEAST64: str = "lld"
PRIdFAST64: str = "lld"

PRIi64: str = "lli"
PRIiLEAST64: str = "lli"
PRIiFAST64: str = "lli"

PRIdMAX: str = "lld"
PRIiMAX: str = "lli"

PRIdPTR = NewType('PRIdPTR', PRId16)
PRIiPTR = NewType('PRIiPTR', PRIi16)
PRIo8:chr = 'o'
PRIoLEAST8:chr = 'o'
PRIoFAST8:chr = 'o'
PRIu8:chr = 'u'
PRIuLEAST8:chr = 'u'
PRIuFAST8:chr = 'u'
PRIx8:chr = 'x'
PRIxLEAST8:chr = 'x'
PRIxFAST8:chr = 'x'
PRIX8:chr = 'X'
PRIXLEAST8:chr = 'X'
PRIXFAST8:chr = 'X'
PRIo16:chr = 'o'
PRIoFAST16:chr = 'o'
PRIoLEAST16:chr = 'o'

PRIu16:str = "u"
PRIuLEAST16:str = "u"
PRIuFAST16: str = "u"

PRIx16: str = "x"
PRIxLEAST16: str = "x"
PRIxFAST16: str = "x"

PRIX16: str = "X"
PRIXLEAST16: str = "X"
PRIXFAST16: str = "X"

PRIo32: str = "lo"
PRIoLEAST32: str = "lo"
PRIoFAST32: str = "lo"

PRIu32: str = "lu"
PRIuLEAST32: str = "lu"
PRIuFAST32: str = "lu"

PRIx32: str = "lx"
PRIxLEAST32: str = "lx"
PRIxFAST32: str = "lx"

PRIX32: str = "lX"
PRIXLEAST32: str = "lX"
PRIXFAST32: str = "lX"

PRIo64: str = "llo"
PRIoLEAST64: str = "llo"
PRIoFAST64: str = "llo"

PRIu64: str = "llu"
PRIuLEAST64: str = "llu"
PRIuFAST64: str = "llu"

PRIx64: str = "llx"
PRIxLEAST64: str = "llx"
PRIxFAST64: str = "llx"

PRIX64: str = "llX"
PRIXLEAST64: str = "llX"
PRIXFAST64: str = "llX"

PRIoMAX: str = "llo"
PRIuMAX: str = "llu"
PRIxMAX: str = "llx"
PRIXMAX: str = "llX"


PRIoPTR = NewType('PRIoPTR', PRIo16)
PRIuPTR = NewType('PRIuPTR', PRIu16)
PRIxPTR = NewType('PRIxPTR', PRIx16)
PRIXPTR = NewType('PRIXPTR', PRIX16)

SCNd8: str = "hhd"
SCNdLEAST8: str = "hhd"
SCNdFAST8: str = "hhd"

SCNi8: str = "hhi"
SCNiLEAST8: str = "hhi"
SCNiFAST8: str = "hhi"
    
SCNd16: str = "d"
SCNdLEAST16: str = "d"
SCNdFAST16: str = "d"

SCNi16: str = "i"
SCNiLEAST16: str = "i"
SCNiFAST16: str = "i"

SCNd32: str = "ld"
SCNdLEAST32: str = "ld"
SCNdFAST32: str = "ld"

SCNi32: str = "li"
SCNiLEAST32: str = "li"
SCNiFAST32: str = "li"

if '__avr_libc_does_not_implement_long_long_in_printf_or_scanf' not in locals():
    SCNd64: str = "lld"
    SCNdLEAST64: str = "lld"
    SCNdFAST64: str = "lld"
    SCNi64: str = "lli"
    SCNiLEAST64: str = "lli"
    SCNiFAST64: str = "lli"

    SCNdMAX: str = "lld"
    SCNiMAX: str = "lli"

SCNdPTR = NewType('SCNdPTR', SCNd16)
SCNiPTR = NewType('SCNiPTR', SCNi16)

if '__avr_libc_does_not_implement_hh_in_scanf' not in locals():
    SCNo8: str = "hho"
    SCNoLEAST8: str = "hho"
    SCNoFAST8: str = "hho"

    SCNu8: str = "hhu"
    SCNuLEAST8: str = "hhu"
    SCNuFAST8: str = "hhu"

    SCNx8: str = "hhx"
    SCNxLEAST8: str = "hhx"
    SCNxFAST8: str = "hhx"

# Octal scanf formats
SCNo16: str = "o"
SCNoLEAST16: str = "o"
SCNoFAST16: str = "o"

SCNo32: str = "lo"
SCNoLEAST32: str = "lo"
SCNoFAST32: str = "lo"

# Decimal scanf formats
SCNu16: str = "u"
SCNuLEAST16: str = "u"
SCNuFAST16: str = "u"

SCNu32: str = "lu"
SCNuLEAST32: str = "lu"
SCNuFAST32: str = "lu"

# Hexadecimal scanf formats
SCNx16: str = "x"
SCNxLEAST16: str = "x"
SCNxFAST16: str = "x"

SCNx32: str = "lx"
SCNxLEAST32: str = "lx"
SCNxFAST32: str = "lx"


if '__avr_libc_does_not_implement_long_long_in_printf_or_scanf' not in locals():
    SCNo64: str = "llo"
    SCNoLEAST64: str = "llo"
    SCNoFAST64: str = "llo"

    # Decimal scanf formats
    SCNu64: str = "llu"
    SCNuLEAST64: str = "llu"
    SCNuFAST64: str = "llu"

    # Hexadecimal scanf formats
    SCNx64: str = "llx"
    SCNxLEAST64: str = "llx"
    SCNxFAST64: str = "llx"

    # Maximum scanf formats
    SCNoMAX: str = "llo"
    SCNuMAX: str = "llu"
    SCNxMAX: str = "llx"
    
    SCNoPTR = NewType('SCNoPTR', SCNo16)
    SCNuPTR = NewType('SCNuPTR',SCNu16)
    SCNxPTR = NewType('SCNxPTR', SCNx16)