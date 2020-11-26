import PySimpleGUI as sg
from built import executable,images,full_executable,full_images
import os
c="echo \"not run properly\""
shouldi=False

sg.theme('SystemDefault1')   # Add a touch of color
# All the stuff inside your window.
layout = [  
    [sg.Text('Program:', pad=(10,0)) ,sg.Combo(executable,size=(40,0))],
    [sg.Text('Image:', pad=(10,0)) ,sg.Combo(images,size=(40,0))],
    [sg.Text('XPX:', pad=(10,0)),sg.InputText(size=(40,0))],
    [sg.Text('YPX:', pad=(10,0)),sg.InputText(size=(40,0))],
    [sg.Text('Additional:', pad=(10,0)),sg.InputText(size=(40,0))],

    [sg.Button('Run'), sg.Button('Cancel')] 
    ]

# Create the Window
window = sg.Window('Window Title', layout, element_justification='r',return_keyboard_events=True)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        print("canceled")
        break
    if event == 'Run':
        shouldi = True
        c='\"{}\" \"{}\" {} {} {}'.format(full_executable[values[0]],full_images[values[1]],values[2],values[3],values[4])
        break
    
    

window.close()


if shouldi:
    os.system('cmd /k "{}"'.format(c))