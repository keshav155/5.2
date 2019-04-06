from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = LED(4)
led1 = LED(25)
led2 = LED(12)

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica' , size = 14, weight = "bold")


def ledToggle():
    if led.is_lit:
        led.off()
        ledButton["text"] = "Turn LED 1 on"
    else:
         led.on()
         led1.off()
         led2.off()
         ledButton["text"] = "Turn LED 1 off"
         
def ledToggle1():
    if led1.is_lit:
        led1.off()
        ledButton1["text"] = "Turn LED 2 on"
    else:
         led1.on()
         led.off()
         led2.off()
         ledButton1["text"] = "Turn LED 2 off"
         
         
def ledToggle2():
    if led2.is_lit:
        led2.off()
        ledButton2["text"] = "Turn LED 3 on"
    else:
         led1.off()
         led.off()
         led2.on()
         ledButton2["text"] = "Turn LED 3 off"

def close():
    GPIO.cleanup()
    win.destroy()

ledButton = Button(win,text = 'Turn LED 1 on',font = myFont, command = ledToggle, bg = 'orange', height = 1, width = 24)
ledButton.grid(row=0,column=1)

ledButton1 = Button(win,text = 'Turn LED 2 on',font = myFont, command = ledToggle1, bg = 'yellow', height = 1, width = 24)
ledButton1.grid(row=1,column=1)

ledButton2 = Button(win,text = 'Turn LED 3 on',font = myFont, command = ledToggle2, bg = 'red', height = 1, width = 24)
ledButton2.grid(row=2,column=1)


exitButton = Button(win,text = 'Exit',font = myFont, command = close, bg = 'grey', height = 1, width = 6)
exitButton.grid(row=3,column=1)

win.protocol("WM_DELETE_WINDOW",close)

win.mainloop()