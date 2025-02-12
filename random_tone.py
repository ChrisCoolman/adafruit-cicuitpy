from adafruit_circuitplayground import cp
import time
import random

num = random.randint(1, 7)

while True:               
    if num == 1:
        if cp.touch_A1:
            cp.start_tone(3000)
    elif num == 2:
        if cp.touch_A2:
            cp.start_tone(3000)
    elif num == 3:
        if cp.touch_A3:
            cp.start_tone(3000)
    elif num == 4:
        if cp.touch_A4:
            cp.start_tone(3000)
    elif num == 5:
        if cp.touch_A5:
            cp.start_tone(3000)
    elif num == 6:
        if cp.touch_A6:
            cp.start_tone(3000)
    elif num == 7:
        if cp.touch_A7:
            cp.start_tone(3000)
    
    if cp.button_a or cp.button_b:
        cp.stop_tone()
