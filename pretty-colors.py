import time
import random
from adafruit_circuitplayground import cp

cp.pixels.brightness = 1
speed = 0.01

def grc():
    colors = [
        (255, 0, 0),    # Red
        (0, 255, 0),    # Green
        (0, 0, 255),    # Blue
        (255, 255, 0),  # Yellow
        (255, 165, 0),  # Orange
        (128, 0, 128),  # Purple
        (0, 255, 255),  # Cyan
        (255, 192, 203),# Pink
        (255, 105, 180),# Hot Pink
        (0, 128, 0),    # Dark Green
        (75, 0, 130),   # Indigo
        (255, 20, 147), # Deep Pink
    ]
    return random.choice(colors)
    
while True:
    if cp.button_a:
        cp.start_tone(3000)
        for i in range(10):
            cp.pixels[i] = grc()
            time.sleep(speed)
    else:
        cp.stop_tone()
        for i in range(10):
            cp.pixels[i] = (0, 0, 0)
