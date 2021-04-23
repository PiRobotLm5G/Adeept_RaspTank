import RPi.GPIO as GPIO
import time 

class CallBack:
	"""
		CallBack class
					pin:call back trigger GPIO pin
					call_func: call back function to execute when call back event occur.
				my_callback_one
					execute call back function.
		comments:this class doesn't know the detail of the call back function.
	"""
    def __init__(self, pin, call_func):

        # pin is call back torigger, set pull up
        self.pin = pin
		self.call_func = call_func
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP) 

        # Chattering measures 1000ms
        GPIO.add_event_detect(pin, GPIO.RISING, bouncetime=1000)
        # call back func set
        GPIO.add_event_callback(pin, self.my_callback_one) 
                    
    def my_callback_one(self):
        self.call_func
