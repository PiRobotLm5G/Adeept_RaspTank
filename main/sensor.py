#!/usr/bin/python
import time
import smbus
bus = smbus.SMBus(1)
 
VL6180X_SYSTEM_FRESH_OUT_OF_RESET = 0x0016
VL6180X_SYSRANGE_MAX_CONVERGENCE_TIME = 0x001C
VL6180X_SYSRANGE_RANGE_CHECK_ENABLES = 0x002D
VL6180X_SYSRANGE_EARLY_CONVERGENCE_ESTIMATE = 0x0022
VL6180X_SYSALS_INTEGRATION_PERIOD = 0x0040
VL6180X_SYSALS_ANALOGUE_GAIN = 0x3F
VL6180X_FIRMWARE_RESULT_SCALER = 0x0120
VL6180X_SYSRANGE_START = 0x0018
VL6180X_RESULT_RANGE_VAL = 0x0062
VL6180X_SYSTEM_INTERRUPT_CLEAR = 0x0015
VL6180X_SYSALS_START = 0x0038
VL6180X_RESULT_ALS_VAL = 0x0050




class sensor:
    """
    sensor class
    addr:address for I2C control
        __read
        I2C value read
    __WriteByte
        write C value from A address to B address 
    __WriteByte16
        hex write?
    get_sensor_status()
        get sensor values only distance
    comment: before using multi sensor, must change address of sensor registor address
    """
    def __init__(self, addr):
        if self.__read(addr,VL6180X_SYSTEM_FRESH_OUT_OF_RESET) == 1:
            self.__WriteByte(addr,0x0207, 0x01)
            self.__WriteByte(addr,0x0208, 0x01)
            self.__WriteByte(addr,0x0096, 0x00)
            self.__WriteByte(addr,0x0097, 0xfd)
            self.__WriteByte(addr,0x00e3, 0x00)
            self.__WriteByte(addr,0x00e4, 0x04)
            self.__WriteByte(addr,0x00e5, 0x02)
            self.__WriteByte(addr,0x00e6, 0x01)
            self.__WriteByte(addr,0x00e7, 0x03)
            self.__WriteByte(addr,0x00f5, 0x02)
            self.__WriteByte(addr,0x00d9, 0x05)
            self.__WriteByte(addr,0x00db, 0xce)

            self.__WriteByte(addr,0x00dc, 0x03)
            self.__WriteByte(addr,0x00dd, 0xf8)
            self.__WriteByte(addr,0x009f, 0x00)
            self.__WriteByte(addr,0x00a3, 0x3c)
            self.__WriteByte(addr,0x00b7, 0x00)
            self.__WriteByte(addr,0x00bb, 0x3c)
            self.__WriteByte(addr,0x00b2, 0x09)
            self.__WriteByte(addr,0x00ca, 0x09)
            self.__WriteByte(addr,0x0198, 0x01)
            self.__WriteByte(addr,0x01b0, 0x17)
            self.__WriteByte(addr,0x01ad, 0x00)
            self.__WriteByte(addr,0x00ff, 0x05)
            self.__WriteByte(addr,0x0100, 0x05)
            self.__WriteByte(addr,0x0199, 0x05)
            self.__WriteByte(addr,0x01a6, 0x1b)
            self.__WriteByte(addr,0x01ac, 0x3e)
            self.__WriteByte(addr,0x01a7, 0x1f)
            self.__WriteByte(addr,0x0030, 0x00)
        #default_settings
        # Recommended : Public registers - See data sheet for more detail
        self.__WriteByte(addr,0x0011, 0x10); # Enables polling for 'New Sample ready' when measurement completes
        self.__WriteByte(addr,0x010a, 0x30); # Set the averaging sample period (compromise between lower noise and increased execution time)
        self.__WriteByte(addr,0x003f, 0x46); # Sets the light and dark gain (upper nibble). Dark gain should not be changed.
        self.__WriteByte(addr,0x0031, 0xFF); # sets the # of range measurements after which auto calibration of system is performed
        self.__WriteByte(addr,0x0040, 0x63); # Set ALS integration time to 100ms DocID026571 Rev 1 25/27 AN4545 SR03 settings27
        self.__WriteByte(addr,0x002e, 0x01); # perform a single temperature calibration of the ranging sensor
 
        #Optional: Public registers - See data sheet for more detail
        self.__WriteByte(addr,0x001b, 0x09); # Set default ranging inter-measurement period to 100ms
        self.__WriteByte(addr,0x003e, 0x31); # Set default ALS inter-measurement period to 500ms
        self.__WriteByte(addr,0x0014, 0x24); # Configures interrupt on 'New Sample Ready threshold event' 
        self.__WriteByte(addr,0x016, 0x00); #change fresh out of set status to 0

        # Additional settings defaults from community
        self.__WriteByte(addr,VL6180X_SYSRANGE_MAX_CONVERGENCE_TIME, 0x32)
        self.__WriteByte(addr,VL6180X_SYSRANGE_RANGE_CHECK_ENABLES, 0x10 | 0x01)
        self.__WriteByte16(addr,VL6180X_SYSRANGE_EARLY_CONVERGENCE_ESTIMATE, 0x7B)
        self.__WriteByte16(addr,VL6180X_SYSALS_INTEGRATION_PERIOD, 0x64) #100ms
        self.__WriteByte(addr,VL6180X_SYSALS_ANALOGUE_GAIN, 0x20) #x40
        self.__WriteByte(addr,VL6180X_FIRMWARE_RESULT_SCALER, 0x01)
        self.addr = addr
        
    def get_sensor_status(self):
        self.__WriteByte(self.addr,VL6180X_SYSRANGE_START, 0x01) #0x03 renzoku
        time.sleep(0.1)
        distance = self.__read(self.addr,VL6180X_RESULT_RANGE_VAL)
        self.__WriteByte(self.addr,VL6180X_SYSTEM_INTERRUPT_CLEAR, 0x07)
        return distance
    def __read(self, addr,register16):
        a1 = (register16 >> 8) & 0xFF
        a0 = register16 & 0xFF
        bus.write_i2c_block_data(addr, a1, [a0])
        return bus.read_byte(addr)
 
    def __WriteByte(self, addr,register16, data):
        a1 = (register16 >> 8) & 0xFF
        a0 = register16 & 0xFF
        bus.write_i2c_block_data(addr, a1, [a0, (data & 0xFF)])
     
    def __WriteByte16(self, addr,register16, data16):
        a1 = (register16 >> 8) & 0xFF
        a0 = register16 & 0xFF
        d1 = (data16 >> 8) & 0xFF
        d0 = data16 & 0xFF
        bus.write_i2c_block_data(addr, a1, [a0, d1, d0])
    
 
#main
if __name__ == "__main__":
    tof_orig_addr = 0x29
    tof_right_addr = tof_orig_addr
    tof_left_addr = 0x2a
    tof_front_addr = 0x2b

    sens_1 = sensor(tof_right_addr)
    sens_2 = sensor(tof_left_addr)
    sens_3 = sensor(tof_front_addr)
    for i in range (0, 100):
        print(sens_1.get_sensor_status(), sens_2.get_sensor_status(), sens_3.get_sensor_status())
#Copyright (c) 2014-2015 Arnie Weber. All rights reserved.

