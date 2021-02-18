from tkinter import *
from tkinter import ttk
import Notify
if __name__ == "__main__":
    root = Tk()
    root.title("ClassCode")

    frame1 = ttk.Frame(root, padding=30)
    label1 = ttk.Label(frame1, text="Your name")
    t = StringVar()
    entry1 = ttk.Entry(frame1, textvariable=t)
    button1 = ttk.Button(
        frame1,
        text='OK',
        #command=lambda:print("Hello, %s" % t.get())
        command=lambda: Notify.send_line_notify("ボタンが押されました")
    )
    frame1.pack()
    label1.pack(side=LEFT)
    entry1.pack(side=LEFT)
    button1.pack(side=LEFT)

    root.mainloop()
