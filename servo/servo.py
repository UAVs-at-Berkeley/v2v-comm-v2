import RPi.GPIO as GPIO
import time

control = [5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
servo = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)

p = GPIO.PWM(servo, 50)
p.start(5)

try:
	while True:
		"""
		for i in control:
			p.ChangeDutyCycle(x)
			time.sleep(0.1)
			print x

		for i in reversed(control):
			p.ChangeDutyCycle(control[x])
			time.sleep(0.1)
			print x
		"""
		p.ChangeDutyCycle(5)
		time.sleep(1)
		p.ChangeDutyCycle(11)
		time.sleep(1)
		'''
		p.ChangeDutyCycle(7.5)
		time.sleep(1)
		p.ChangeDutyCycle(2.5)
		time.sleep(1)
		'''

except KeyboardInterrupt:
	GPIO.cleanup()
