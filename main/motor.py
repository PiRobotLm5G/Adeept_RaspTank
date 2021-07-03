import RPi.GPIO as GPIO, time


GPIO.setmode(GPIO.BCM)

class motor:
    """
    motor class
            AIN1:DC motor power from 5.0 A source
            AIN2:DC motor power to 
            PWMA:Correspond to PWM
            POWER:Correspond to duty?
            forward
            motor cycle forward
            backward
            motor cycle backward
            stop
            motor stop
            change_power
            change duty
            change_direction
            change motor cycle direction
    """
    __direction = 'forward'
    def __init__(self, AIN1,AIN2,PWMA, POWER):
        GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(AIN2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(PWMA, GPIO.OUT, initial=GPIO.LOW)
        self.p= GPIO.PWM(PWMA, 100)
        self.p.start(0)
        self.ain1 = AIN1
        self.ain2 = AIN2
        self.pwma = PWMA
        self.power = POWER

    def forward(self):
        GPIO.output(self.ain1, GPIO.HIGH)
        GPIO.output(self.ain2, GPIO.LOW)
        self.p.ChangeDutyCycle(self.power)
        self.__direction = 'forward'
        
    def backward(self):
        GPIO.output(self.ain1, GPIO.LOW)
        GPIO.output(self.ain2, GPIO.HIGH)
        self.p.ChangeDutyCycle(self.power)
        self.__direction = 'backward'
        
    def stop(self):
        GPIO.output(self.ain1, GPIO.LOW)
        GPIO.output(self.ain2, GPIO.LOW)
        
    def change_power(self, power):
        self.power = power
        if self.__direction == 'forward':
            self.forward()
        else:
            self.backward()
    def change_direction(self):
        if self.__direction == 'forward':
            self.backword()
            self.__direction = 'backward'
        else:
            self.forward()
            self.__direction = 'forward'


        
#forward_motor(75)
if __name__ == "__main__":
    PWMA = 25
    AIN1 = 22
    AIN2 = 23
    c_step = 10
    POWER = 50
    GPIO.setmode(GPIO.BCM)
    motor_1 = motor(AIN1, AIN2, PWMA, POWER)
    print('stop:1')
    print('forward:2')
    print('backward:4')
    print('change power:3')
    i = 0
    while True:
        i=i+1
        if(i>50):
            break
        try:
            cont = input()
        except:
            pass
        print('channel')
        #print(cont)
        if(cont == '1'):
            print('stop')
            motor_1.stop()
            break

        elif(cont == '2'):
            print('forward')
            motor_1.forward()
            direct = 'forward'
        elif(cont == '3'):
            print('change power')
            print('input duty cycle: 0~100')
            motor_power =int(input())
            if(motor_power < 100):
                motor_1.change_power(motor_power)
            else:
                print('error')
                cont ='1'
        elif(cont == '4'):
            print('backward')
            motor_1.backward()
            direct = 'back'
    GPIO.cleanup()
