import PySimpleGUI as sg

sg.theme("Default1")
tab1 = sg.Tab("時間割", [[sg.Text("時間割を表示")]])
tab2 = sg.Tab("授業開始", [[sg.Text("授業を開始")]])
tab3 = sg.Tab("授業終了", [[sg.Text("授業を終了")]])

layout = [[sg.TabGroup([[tab1, tab2, tab3]])]]

window = sg.Window("ClassCode", layout=layout,)

while True:
    event, values = window.read()
    if event == None:
        print(event, values)
        break
    else:
        print(event, values)
window.close()
