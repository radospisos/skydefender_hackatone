import time
import Jetson.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

trigPin = 16  # GPIO 24
echoPin = 18  # GPIO 23

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

def get_distance():
    GPIO.output(trigPin, GPIO.HIGH)
    time.sleep(0.00001)
    #time.sleep(5)
    GPIO.output(trigPin, GPIO.LOW)

    pulse_start = time.time()
    while GPIO.input(echoPin) == GPIO.LOW:
        start_pulse = time.time()
        #print('start_pulse = ', start_pulse)
        #print('echoPin = ', GPIO.input(echoPin))
        GPIO.output(trigPin, GPIO.HIGH)
        time.sleep(0.00001)
        #time.sleep(1)
        GPIO.output(trigPin, GPIO.LOW)


    pulse_end = time.time()
    while GPIO.input(echoPin) == GPIO.HIGH:
        pulse_end = time.time()
        #print('pulse_end = ', pulse_end)
        #print(GPIO.input(echoPin))
        #print('echoPin = ', GPIO.input(echoPin))

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

try:
    while True:
        distance = get_distance()
        print("Расстояние: {} см".format(distance))
        time.sleep(0.001)

except KeyboardInterrupt:
    GPIO.cleanup()
