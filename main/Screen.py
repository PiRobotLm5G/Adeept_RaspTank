import PySimpleGUI as sg

class GUI:
        """
        GUI class
        title:Screen title
        layout: Screen layout
        show
        can view Screen according to layout
        can detect key event
        close
        screen close
        comment:We have to modify this class more abstractly.
        """
        def __init__(self, title, layout):
                self.window = sg.Window(title, layout)
        def show(self):
                while True:
                        event, values = self.window.read(timeout=50, timeout_key ='timeout')
                        if event is None:
                                break
                        else:
                                return event, values
                return 'off', values
        def close(self):
                self.window.close()
        def update(self, content, value):
                self.window[content].Update(value)

if __name__ == '__main__':
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
        gui = GUI(title, layout)

        #main task
        while True:
                request, values = gui.show()
                #power on key
                if request == 'on':
                        print('On key action')
                #power off key
                elif request == 'off':
                        print('Off key action')
                        gui.close()
                        break
                #get sensor value
                elif request == 'sensor':
                        print('get sensor status')
                #get switch value
                elif request == 'switch':
                        print('get switch status')
                #change scroll bar
                elif request == 'motor':
                        gui.update('input', values['motor'])
                #change input Text value
                elif request == 'input':
                        print(values['input'])
                #change motor power
                elif request == 'set':
                        gui.update('motor', values['input'])
                        print('set motor duty cicle')
                #timeout event. always monitor sensor values.
                #switch values change event can be detected through call back function.
                elif request == 'timeout':
                        print('event time out')
