from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.1
speed = 0.05

while True:               
    for i in range(10):
        cp.pixels[i] = (255, 0, 0)
        cp.pixels[i - 1] = (255, 35, 0)
        cp.pixels[i - 2] = (255, 75, 0)
        cp.pixels[i - 3] = (225, 150, 0)
        cp.pixels[i - 4] = (100, 100, 0)
        cp.pixels[i - 5] = (0, 225, 0)
        cp.pixels[i - 6] = (0, 255, 0)
        cp.pixels[i - 7] = (25, 0, 255)
        cp.pixels[i - 8] = (50, 0, 200)
        cp.pixels[i - 9] = (100, 0, 100)

        time.sleep(speed)
