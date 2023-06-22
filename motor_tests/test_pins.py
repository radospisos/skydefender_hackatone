import RPi.GPIO as GPIO
import time

output_pins = {
    'JETSON_XAVIER': 18,
    'JETSON_NANO': 33,
    'JETSON_NX': 33,
    'CLARA_AGX_XAVIER': 18,
    'JETSON_TX2_NX': 32,
    'JETSON_ORIN': 18,
    'JETSON_ORIN_NX': 33,
    'JETSON_ORIN_NANO': 33
}
output_pin = output_pins.get(GPIO.model, None)
if output_pin is None:
    raise Exception('PWM not supported on this board')
else:
    print('Everything is OK!')
