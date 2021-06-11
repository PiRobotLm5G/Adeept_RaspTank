import PySimpleGUI as sg


battery_bottun = [sg.Button('ON', key = 'on'), sg.Button('OFF', key = 'off')]
input_value = [sg.Button('Get Sensor', key = 'sensor'), sg.Button('Get Switch', key = 'switch')]
motor_pwm = [sg.Slider((0,  100),0,1,orientation='h',size=(45, 15),key='motor',
                    enable_events=True)]
slider_value = [sg.InputText('0', size =(10,1), key = 'input'), sg.Button('set', key = 'set')]




frame_battery = sg.Frame('��d��', layout =[battery_bottun])
frame_debug = sg.Frame('�f�o�b�O', layout =[input_value])
frame_motor = sg.Frame('���[�^�[���x', layout = [motor_pwm, slider_value])
layout = [[frame_battery], [frame_debug], [frame_motor]]
title = '�ȒP����'
