import datetime
import math
import time

import pygame
import RPi.GPIO as GPIO
import speakerphat

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.mixer.music.load('/home/pi/projects/big-green-button/sounds/car_horn.wav')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # High state when button is pressed

# Show that everything ready using speakerphat's LEDs
speed = 4
for i in range(125):
	offset = int((math.sin(time.time() * speed) * 5) + 5)
	speakerphat.clear()
	speakerphat.set_led(offset, 255)
	speakerphat.show()

history_value = GPIO.LOW

try:
	while True:
		with open('times.dat', 'a') as f_out:
			current_value = GPIO.input(10)  # avoid weird race conditions?
			if current_value != history_value:
				history_value = current_value
				if current_value == GPIO.HIGH:
					f_out.write(f'{datetime.datetime.now().time()}\n ')
					pygame.mixer.music.play()
				history_value = current_value
except KeyboardInterrupt:
	print('Bye!')

