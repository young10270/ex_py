import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
 
TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
motor = GPIO.PWM(17, 50)
motor.start(2.5)

#GPIO.output(TRIG, GPIO.LOW)
#time.sleep(0.3)


while True:
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.3)


    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
	pulse_start = time.time()
    while GPIO.input(ECHO)==1:
	pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*17150
    distance = round(distance, 2)
    print "Distance: ", distance, "cm"
    time.sleep(0.00001)
    
    if (distance > 10):
	motor.ChangeDutyCycle(2.5)
	time.sleep(1) 
	
    if (distance < 10):
	motor.ChangeDutyCycle(7.5)
        time.sleep(1)
	exit()
