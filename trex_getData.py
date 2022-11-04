import keyboard
import uuid
import time
from PIL import Image
from mss import mss

"""
https://fivesjs.skipser.com/trex-game/
"""

mon = {"top": 380, "left": 740, "width": 280, "height": 115}
sct = mss()

i = 0

def record_screen(record_id, key):
    global i
    
    i += 1
    print("{}: {}".format(key, i))
    img = sct.grap(mon)
    im = Image.frombytes("RGB", img.size, img.rgb)
    im.save("./img/{}_{}_{}.png".format(key, record_id, i))
    
    
is_exit = False

def exit():
    global is_exit
    is_exit = True
    
keyboard.add_hotkey("esc", exit)

record_id = uuid.uuid4()

while True:
    
    if is_exit: break

    try:
        if keyboard.is_pressed(keyboard.KEY_UP):
            record_screen(record_id, "up")
            time.sleep(0.1)
            
        else if keyboard.is_pressed(keyboard.KEY_DOWN):
            record_screen(record_id, "down")
            time.sleep(0.1)
            
        else if keyboard.is_pressed("right"):
            record_screen(record_id, "right")
            time.sleep(0.1)
            
    except RuntimeError: continue
            