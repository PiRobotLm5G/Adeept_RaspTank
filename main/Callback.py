import RPi.GPIO as GPIO
import time 

class Callback:
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
        # Chattering measures 1000ms
        GPIO.add_event_detect(pin, GPIO.FALLING, bouncetime=500)
        # call back func set
        GPIO.add_event_callback(pin, self.my_callback_one) 
                    
    def my_callback_one(self, pin):
        print("call back")
        self.call_func()
        

if __name__ == '__main__':
    import switch
    def call_back_event():
    #change motor direction
    #move.move(speed, 'backward', 'no', 0.6)
    #time.sleep(1)
    #move.move(speed, 'no', 'right', 0.6)
        print("call back event")
    #make switch instanse
    #first switch input GPIO num
    switch_1_num = 20
    #second switch input GPIO num
    switch_2_num = 26
    #switch outpit GPIO num
    switch_out = 19
    switch_1 = switch.switch(switch_1_num)
    switch_2 = switch.switch(switch_2_num)

#make callback instanse 
    cb_1 = Callback(switch_1_num, call_back_event)
    cb_2 = Callback(switch_2_num, call_back_event)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        GIIO.cleanup()
                             