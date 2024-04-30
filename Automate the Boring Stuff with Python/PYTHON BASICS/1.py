import PySimpleGUI as ags
ags.theme('DarkAmber')

layout = [
    [ags.Text('something 1')],
    [ags.Text('something 2'), ags.InputText()],
    [ags.Button('ok'), ags.Button('cancel')],
    [ags.Sizer(800,600)]
    
] 

window = ags.Window("hi", layout)

while True:
    event, values = window.read()
    if  event == ags.WIN_CLOSED or event == 'cancel':
        break
    print('you entered values:', values[0])
    
window.close()