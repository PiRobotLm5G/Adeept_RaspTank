import time
import board
import busio
import adafruit_vl6180x
import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)


AIN1 = 4
AIN2 = 13

def init_gpio():
    GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(AIN2, GPIO.OUT, initial=GPIO.LOW)

#Create I2C bus.
def set_i2c(x):
    if(x == AIN1):
        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)
    elif (x == AIN2):
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)



def read_distance():
    return sensor.range


def read_lux():
    return sensor.read_lux(adafruit_vl6180x.ALS_GAIN_1)


i = 0
init_gpio()
set_i2c(AIN1)
i2c = busio.I2C(board.SCL, board.SDA, 0x29)
i2c_2 = busio.I2C(board.SCL, board.SDA, 0x2a)
sensor = adafruit_vl6180x.VL6180X(i2c)
sensor_2 = adafruit_vl6180x.VL6180X(i2c_2)
while i < 100:
    range_mm = sensor.range
    range_mm_2 = sensor_2.range
    print(range_mm, range_mm_2)
#    light_lux = sensor.read_lux(adafruit_vl6180x.ALS_GAIN_1)
#    print("Light (1x gain):{0}lux".format(light_lux))
#    delay
    time.sleep(0.1)
    i= i+1
GPIO.cleanup()