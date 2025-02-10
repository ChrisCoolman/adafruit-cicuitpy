from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.3
speed = 0.05
color1 = (255, 0, 0)
color2 = (0, 0, 255)

while True:               
    for i in range(10):
        cp.pixels[i - 1] = (0, 0, 0)
        cp.pixels[i] = color1
        if i <= 4:
            cp.pixels[i + 4] = (0, 0, 0)
            cp.pixels[i + 5] = color2
            cp.stop_tone()
            cp.start_tone(1000)
        elif i > 4:
            cp.pixels[i - 6] = (0, 0, 0)
            cp.pixels[i - 5] = color2
            cp.stop_tone()
            cp.start_tone(2000)

        time.sleep(speed)
