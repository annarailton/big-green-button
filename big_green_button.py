import RPi.GPIO as GPIO
import pifacecad


cad = pifacecad.PiFaceCAD()
cad.lcd.backlight_on()
cad.lcd.write("Hello, world!")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # High state when button is pressed

while True:
	if GPIO.input(10) == GPIO.HIGH:
		print("Button was pushed!")


