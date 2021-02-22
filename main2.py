import PySimpleGUI as sg

sg.theme("Default1")
layout = [[sg.Text("これはPySimpleGUIを使ったサンプルプログラミングです. ", enable_events=True)],
          [sg.Button("Quit", size=(15, 1)),
           sg.Button("OK", size=(15, 1))]
          ]

window = sg.Window("Sample01", layout)

while True:
    event, values = window.read()
    print("イベント:", event, ", 値:", values)
    if event in (None, "Quit"):
        print("終了します.")
        break
    elif event in ("OK"):
        print("Hello World")
    else:
        print("該当しません.")
        break

window.close()
