#!/usr/bin/python
import time
import smbus
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
bus = smbus.SMBus(1)

def __WriteByte(register16, addr, data):
    a1 = (register16 >> 8) & 0xFF
    a0 = register16 & 0xFF

    try:
        bus.write_i2c_block_data(addr, a1, [a0, (data & 0xFF)])
    except:
        raise


def change_addr(addr, new_addr, reset_pin):
    VL6180X_SLAVE_DEVICE_ADDRESS = 0x0212
    GPIO.setup(reset_pin, GPIO.OUT)
    GPIO.output(reset_pin,0)
    time.sleep(1)
    GPIO.output(reset_pin,1)
    time.sleep(1)
    if addr != new_addr:
        __WriteByte(VL6180X_SLAVE_DEVICE_ADDRESS, addr, new_addr)
    #time.sleep(1)

    #GPIO.output(reset_pin,0)
 
#init

if __name__ == "__main__":
    tof_orig_addr = 0x29
    tof_right_addr = tof_orig_addr
    tof_right_pin = 9
    tof_left_addr = 0x2a
    tof_left_pin = 21
    tof_front_addr = 0x2b
    tof_front_pin = 10 

    #GPIO.setwarnings(False)

    change_addr(tof_orig_addr, tof_left_addr, tof_left_pin)
    change_addr(tof_orig_addr, tof_front_addr, tof_front_pin)
    change_addr(tof_orig_addr, tof_right_addr, tof_right_pin) # power on

    #sda = new_address_read(VL6180X_SLAVE_DEVICE_ADDRESS)
    #print(sda,' id')

    GPIO.cleanup()
        
#if read(VL6180X_SYSTEM_FRESH_OUT_OF_RESET) == 1:
#        print('sensor is ready.')
#        WriteByte(0x0207, 0x01)
#        WriteByte(0x0208, 0x01)
#        WriteByte(0x0096, 0x00)
#        WriteByte(0x0097, 0xfd)
#        WriteByte(0x00e3, 0x00)
#        WriteByte(0x00e4, 0x04)
#        WriteByte(0x00e5, 0x02)
#        WriteByte(0x00e6, 0x01)
#        WriteByte(0x00e7, 0x03)
#        WriteByte(0x00f5, 0x02)
#        WriteByte(0x00d9, 0x05)
#        WriteByte(0x00db, 0xce)
 
#        WriteByte(0x00dc, 0x03)
#        WriteByte(0x00dd, 0xf8)
#        WriteByte(0x009f, 0x00)
#        WriteByte(0x00a3, 0x3c)
#        WriteByte(0x00b7, 0x00)
#        WriteByte(0x00bb, 0x3c)
#        WriteByte(0x00b2, 0x09)
#        WriteByte(0x00ca, 0x09)
#        WriteByte(0x0198, 0x01)
#        WriteByte(0x01b0, 0x17)
#        WriteByte(0x01ad, 0x00)
#        WriteByte(0x00ff, 0x05)
#        WriteByte(0x0100, 0x05)
#        WriteByte(0x0199, 0x05)
#        WriteByte(0x01a6, 0x1b)
#        WriteByte(0x01ac, 0x3e)
#        WriteByte(0x01a7, 0x1f)
#        WriteByte(0x0030, 0x00)
#default_settings
# Recommended : Public registers - See data sheet for more detail
#WriteByte(0x0011, 0x10); # Enables polling for 'New Sample ready' when measurement completes
#WriteByte(0x010a, 0x30); # Set the averaging sample period (compromise between lower noise and increased execution time)
#WriteByte(0x003f, 0x46); # Sets the light and dark gain (upper nibble). Dark gain should not be changed.
#WriteByte(0x0031, 0xFF); # sets the # of range measurements after which auto calibration of system is performed
#WriteByte(0x0040, 0x63); # Set ALS integration time to 100ms DocID026571 Rev 1 25/27 AN4545 SR03 settings27
#WriteByte(0x002e, 0x01); # perform a single temperature calibration of the ranging sensor
# 
##Optional: Public registers - See data sheet for more detail
#WriteByte(0x001b, 0x09); # Set default ranging inter-measurement period to 100ms
#WriteByte(0x003e, 0x31); # Set default ALS inter-measurement period to 500ms
#WriteByte(0x0014, 0x24); # Configures interrupt on 'New Sample Ready threshold event' 
#WriteByte(0x016, 0x00); #change fresh out of set status to 0
# 
## Additional settings defaults from community
#WriteByte(VL6180X_SYSRANGE_MAX_CONVERGENCE_TIME, 0x32)
#WriteByte(VL6180X_SYSRANGE_RANGE_CHECK_ENABLES, 0x10 | 0x01)
#WriteByte16(VL6180X_SYSRANGE_EARLY_CONVERGENCE_ESTIMATE, 0x7B)
#WriteByte16(VL6180X_SYSALS_INTEGRATION_PERIOD, 0x64) #100ms
#WriteByte(VL6180X_SYSALS_ANALOGUE_GAIN, 0x20) #x40
#WriteByte(VL6180X_FIRMWARE_RESULT_SCALER, 0x01)
 
#main
#distance
#WriteByte(VL6180X_SYSRANGE_START, 0x01) #0x03 renzoku
#time.sleep(0.1)
#distance = read(VL6180X_RESULT_RANGE_VAL)
#WriteByte(VL6180X_SYSTEM_INTERRUPT_CLEAR, 0x07)
#print(distance,'mm')
# 
#ambient_light
#WriteByte(VL6180X_SYSALS_START, 0x01)
#time.sleep(0.5)
#light = read16(VL6180X_RESULT_ALS_VAL)
#WriteByte(VL6180X_SYSTEM_INTERRUPT_CLEAR, 0x07)
#print read(VL6180X_SYSALS_ANALOGUE_GAIN)
#print read16(VL6180X_SYSALS_INTEGRATION_PERIOD)
#print(light*0.32*100/(32*100),'lux')
#Copyright (c) 2014-2015 Arnie Weber. All rights reserved.

