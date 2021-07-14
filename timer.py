import tkinter, win32api, win32con, pywintypes
from PIL import Image
import pyautogui
import time
import d3dshot
from win32api import GetSystemMetrics



d = d3dshot.create()
X = GetSystemMetrics(0)/1.95519348269#982
Y = GetSystemMetrics(1)/27#40


s = 45
loopVar = 0
detected = 0
firstTime = 0

def main():
    global s, detected, loopVar, firstTime
    #determine if spike is down
    img = d.screenshot()
    pix = img.load()
    r,g,b = pix[X, Y]  # Get the RGBA Value of the a pixel of an image
    if(g == 0 and b == 0):
        detected = 1
    #determine if spike is down
    if(detected == 0):
        label.config(text=str(45.0), fg="white", bg = "#fffcff")
        label.master.wm_attributes("-transparentcolor", "#fffcff")
    if(detected  == 1):
        if(loopVar == 0):
            firstTime = time.time()
        loopVar = loopVar +  1
        if (g > 0 and b > 0):
            detected = 0
        elapsedTime = time.time()-firstTime
        s = round(45-elapsedTime, 1)
        label.config(text=str(s))
        if(s <= 0):
            s = 45
            label.config(text=str(s))
            loopVar = 0
            detected = 0
        if(s <= 15 and s > 7):
            label.config(fg = 'yellow')
        elif(s <= 7):
            label.config(fg = 'red', bg="#f50000")
            label.master.wm_attributes("-transparentcolor", "#f50000")

        #Send Messages to Tm8's

    label.after(50, main)
print("Init")
label = tkinter.Label(text='45.0', font=('Consolas','40'), fg='white', bg='#fffcff')
label.master.overrideredirect(True)
label.master.geometry("+1600+15")
label.master.lift()
label.master.wm_attributes("-topmost", True)
label.master.wm_attributes("-disabled", True)
label.master.wm_attributes("-transparentcolor", "#fffcff")

hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
# http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
# The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

label.pack()
label.after(1, main)
label.mainloop()
"""
#Standard Response
Hey Guys! I'm a software developer and I just finished the Alpha of a spike timer program!
It allows you to see the exact milliseconds in the future when the spike will go open

If you are interested the source code is below:
https://repl.it/@c4syner/SpikeTimer#main.py
"""
