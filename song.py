from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 1
speed = 0.5

while True:               
    for i in range(10):
        cp.pixels[i-1] = (0, 0, 0)
        cp.pixels[i] = (1, 1, 1)
        if i == 0:
            cp.stop_tone()
            cp.start_tone(700)
            #cp.play_file("click.wav")
        elif i == 1:
            cp.stop_tone()
            cp.start_tone(800)
        elif i == 2:
            cp.stop_tone()
            cp.start_tone(900)
        elif i == 3:
            cp.stop_tone()
            cp.start_tone(800)
        elif i == 4:
            cp.stop_tone()
            cp.start_tone(700)
        elif i == 5:
            cp.stop_tone()
            cp.start_tone(900)
        elif i == 6:
            cp.stop_tone()
            cp.start_tone(300)
        elif i == 7:
            cp.stop_tone()
            cp.start_tone(200)
        elif i == 8:
            cp.stop_tone()
            cp.start_tone(900)
        elif i == 9:
            cp.stop_tone()
            cp.start_tone(1000)

        time.sleep(speed)
