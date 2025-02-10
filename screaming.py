from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 1
speed = 0.5

while True:        
    if cp.shake(shake_threshold=20):
        cp.start_tone(3000)
    else:
        cp.stop_tone()
