import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)



#output 3.3V GPIO pin is common, so can't include class method
def init_switch_output(num):
	GPIO.setup(num, GPIO.OUT)

def switch_read_on(num):
	GPIO.output(num, 1)



class switch:
	"""
		switch class
					input:switch GPIO pin num
				get_switch_status
					get switch values. default is 1, if pushed then value will be 0.
	
	"""
	def __init__(self, input):
		self.input =input
		GPIO.setup(self.input, GPIO.IN)

	def get_switch_status(self):
		return GPIO.input(self.input)
 
 
 
if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)
	switch_1 = 7
	switch_2 = 16
	out_num = 24
	init_switch_output(out_num)
	SW_1 = switch(switch_1)
	SW_2 = switch(switch_2)
	switch_read_on(out_num)
	i = 0
	while i < 100:
		print(SW_1.get_switch_status(), SW_2.get_switch_status())
		time.sleep(0.1)
		i= i+1
	GPIO.cleanup()
