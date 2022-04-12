def loading():
    import PySimpleGUI as sg
    import time
    sg.theme('Dark Red')
    BAR_MAX = 1000
    layout = [[sg.Text('Loading')],
            [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,20), key='-PROG-')],
            [sg.Cancel()]]
    window = sg.Window('Loading', layout)
    for i in range(500):
        event, values = window.read(timeout=10)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        window['-PROG-'].update(i+2)
    time.sleep(3)
    window.close()
loading()