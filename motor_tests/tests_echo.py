import time
import Jetson.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

trigPin = 18  # GPIO 24
echoPin = 16  # GPIO 23

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

def get_distance():
    print('пускаем пинг')
    GPIO.output(trigPin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigPin, GPIO.LOW)
    print('Конец пинга')

    while GPIO.input(echoPin) == GPIO.HIGH:
        pulse_start = time.time()
        print('pulse start = ', pulse_start)

    while GPIO.input(echoPin) == GPIO.LOW:
        pulse_end = time.time()
        print('pulse end = ', pulse_end)

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

try:
    while True:
        distance = get_distance()
        print("Расстояние: {} см".format(distance))
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
