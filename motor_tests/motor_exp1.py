import Jetson.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(32, GPIO.OUT)
#GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
i = 0
while True:
	GPIO.output(32, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(32, GPIO.LOW)
	time.sleep(0.0001)
	print(i)
	i+=1

my_pwm = GPIO.PWM(32,100)
my_pwm.ChangeFrequency(1000)
my_pwm.start(10)
time.sleep(100)
print('Done')
GPIO.cleanup()
