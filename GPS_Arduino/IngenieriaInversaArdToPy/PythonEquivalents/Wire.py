

    #include <inttypes.h>
    #include "Stream.h"

        #if !defined(NO_GLOBAL_INSTANCES) && !defined(NO_GLOBAL_TWOWIRE)
            extern TwoWire Wire;
        #endif


        #ifndef I2C_BUFFER_LENGTH
            #define I2C_BUFFER_LENGTH 128
        #endif

    class TwoWire: public Stream {
        private:
            static uint8_t rxBuffer[];
            static size_t  rxBufferIndex;
            static size_t  rxBufferLength;

            static uint8_t txAddress;
            static uint8_t txBuffer[];
            static size_t  txBufferIndex;
            static size_t  txBufferLength;

            static uint8_t transmitting;
            static void (*user_onRequest)(void);
            static void (*user_onReceive)(size_t);
            static void onRequestService(void);
            static void onReceiveService(uint8_t*, size_t);

        public:
            TwoWire();
            void   begin(int sda, int scl);
            void   begin(int sda, int scl, uint8_t address);
            void   pins(int sda, int scl) __attribute__((deprecated));  // use begin(sda, scl) in new code
            void   begin();
            void   begin(uint8_t);
            void   begin(int);
            void   setClock(uint32_t);
            void   setClockStretchLimit(uint32_t);
            void   beginTransmission(uint8_t);
            void   beginTransmission(int);
            uint8_t endTransmission(void);
            uint8_t endTransmission(uint8_t);
            size_t  requestFrom(uint8_t address, size_t size, bool sendStop);
            uint8_t status();

            uint8_t requestFrom(uint8_t, uint8_t);
            uint8_t requestFrom(uint8_t, uint8_t, uint8_t);
            uint8_t requestFrom(int, int);
            uint8_t requestFrom(int, int, int);

            virtual size_t write(uint8_t);
            virtual size_t write(const uint8_t*, size_t);
            virtual int    available(void);
            virtual int    read(void);
            virtual int    peek(void);
            virtual void   flush(void);
            void           onReceive(void (*)(int));     // arduino api
            void           onReceive(void (*)(size_t));  // legacy esp8266 backward compatibility
            void           onRequest(void (*)(void));

            using Print::write;
    };

       
