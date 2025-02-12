from adafruit_circuitplayground import cp
import time
import random

num = random.randint(1, 7)

while True:               
    if cp.button_a:
        cp.play_file("examples_rise.wav")
