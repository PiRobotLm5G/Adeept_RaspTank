import sensor
import change
import motor
import switch
import PySimpleGUI as sg
import Screen
import Callback
#first sensor address
addr=0x29
#second sensor newaddress
new_addr=0x2a

#first switch input GPIO num
switch_1_num = 20
#second switch input GPIO num
switch_2_num = 26
#switch outpit GPIO num
switch_out = 19
#init switch
sensor.init_switch_output(switch_num)
sensor.switch_read_on(switch_num)
#motor PWM
PWMA = 18
#AIN1
AIN1 = 27
#AIN2
AIN2 = 22
#PWM ratio
POWER = 50
#change addr of sensor
change.change_addr(new_addr)



#make instanse sensor
sens_1 = sensor.sensor(addr)
sens_2 = sensor.sensor(new_addr)
# if the sensor detect less than 10 mm, the event will occur.
closed_value = 10

#motor instanse
mt = motor.motor(AIN1, AIN2, PWMA, POWER)

#make switch instanse
switch_1 = switch.switch(switch_1_num)
switch_2 = switch.switch(switch_2_num)

def call_back_event():
	#change motor direction
	#è¨î‰âÍÇ≥ÇÒë´
	print("call back event")

#make callback instanse 
cb_1 = CallBack.Callback(switch_1_num, call_back_event)
cb_2 = CallBack.Callback(switch_2_num, call_back_event)


#Screen layout
battery_bottun = [sg.Button('ON', key = 'on'), sg.Button('OFF', key = 'off')]
input_value = [sg.Button('Get Sensor', key = 'sensor'), sg.Button('Get Switch', key = 'switch')]
motor_pwm = [sg.Slider((0,  100),0,1,orientation='h',size=(45, 15),key='motor',
                    enable_events=True)]
slider_value = [sg.InputText('0', size =(10,1), key = 'input'), sg.Button('set', key = 'set')]




frame_battery = sg.Frame('Engine', layout =[battery_bottun])
frame_debug = sg.Frame('Debug', layout =[input_value])
frame_motor = sg.Frame('Motor', layout = [motor_pwm, slider_value])
layout = [[frame_battery], [frame_debug], [frame_motor]]
title = 'Simple Screen'

#make screen instanse
gui = Screen.GUI(title, layout)

#main task
while True:
	request, event = gui.show()
	#power on key
	if request == 'on':
		motor.forward()
	#power off key
	elif request == 'off':
		gui.close()
		motor.stop()
		break
	#get sensor value
	elif request == 'sensor':
		print(sens_1.get_sensor_status())
		print(sens_2.get_sensor_status())
	#get switch value
	elif request == 'switch':
		print(switch_1.get_sensor_status())
		print(switch_2.get_sensor_status())
	#change scroll bar
	elif request == 'motor':
		gui.update('input', values['motor'])
	#change input Text value
	elif request == 'input':
		gui.update('motor', values['input'])
	#change motor power
	elif request == 'set':
		gui.update('motor', values['input'])
		motor.change_power(values['input'])
	#timeout event. always monitor sensor values.
	#switch values change event can be detected through call back function.
	elif request == 'timeout':
		if(sens_1.get_sensor_status() < closed_value):
			#motor change derection
			#è¨î‰âÍÇ≥ÇÒë´
		elif(sens_2.get_sensor_status() < closed_value):
			#motor change derection
			#è¨î‰âÍÇ≥ÇÒë´
		
		
	
	
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
