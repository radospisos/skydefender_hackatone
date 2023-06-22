import Jetson.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(32, GPIO.OUT)
#GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
i = 0
while True:
	GPIO.output(18, GPIO.HIGH)
	print('High')
	time.sleep(5)
	GPIO.output(18, GPIO.LOW)
	print('LOW')
	time.sleep(5)
	print(i)
	i+=1

#my_pwm = GPIO.PWM(32,100)
#my_pwm.ChangeFrequency(1000)
#my_pwm.start(10)
#time.sleep(100)
#time.sleep(10)
#GPIO.output(18, GPIO.HIGH)
print('Done')
GPIO.cleanup()
