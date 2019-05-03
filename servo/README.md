# Raspberry Pi Servo Control

First need to import RPi.GPIO

Initiallize GPIO using GPIO.setmode(GPIO.BOARD)

Setup GPIO and servo by GPIO.setup(servoPin, GPIO.OUT)

Intiallize PWM with p=GPIO.PWM(servoPin, freq)    //freq usually 50 for servos

Start PWM duty cycle with p.start(percentage)     //middle usually 7.5

Move servo by p.ChangeDutyCycle(newpercentage). A change of 6 points is about 90 degrees. Any duty cycle percentage of less than 2.5 or greater than 12.5 will cause gitters.

Make sure to use time.sleep(t) in order to give enough time for the servo to move. 1 sec is a good amount for large movements

When ending program make sure to GPIO.cleanup to exit

 

