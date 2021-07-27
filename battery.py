from tkinter import *
import psutil

def battery():
    battery= psutil.sensors_battery()
    percentage=battery.percent
    return percentage

x=0

while(x<95):
    x=battery()
window=Tk()
lbl=Label(window, text="Please unplug", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
window.title('Battery')
window.geometry("300x200+10+10")
window.mainloop()





