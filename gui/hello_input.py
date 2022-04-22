import PySimpleGUI as sg

layout = [
    [sg.Input(key='-INPUT-'), sg.Button('Confirm', key='-CONFIRM-')],
    [sg.Text('Enter your name', key='-OUTPUT-')]
]

win = sg.Window('Hello World', layout=layout)

while True:
    event, value = win.read()
    
    if event == '-CONFIRM-':
        win['-OUTPUT-'].update(f'Hello {value["-INPUT-"]}!')

    if event == sg.WIN_CLOSED:
        break