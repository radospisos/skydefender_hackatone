import Jetson.GPIO as GPIO
import time

# Установка режима пинов
GPIO.setmode(GPIO.BOARD)
def calculate_angular_velocity(angle_change, time_change):
    angular_velocity = angle_change / time_change
    return angular_velocity
def angle_change(degree_first, degree_current):
	return degree_current - degree_first	
# Настройка пинов для управления шаговым двигателем
step_pin = 32  # Номер пина для шагового сигнала
#dir_pin = 35  # Номер пина для сигнала направления

# Установка режима пинов в OUTPUT
GPIO.setup(step_pin, GPIO.OUT)
#GPIO.setup(dir_pin, GPIO.OUT)
current_time = time.time()
# Управление шаговым двигателем
def control_stepper_motor(steps, delay):
    # Направление движения (True - вперед, False - назад)
    direction = True
    kol_oborotov = 0
    kol_shagov = 0        
    # Установка направления движения
    #GPIO.output(dir_pin, direction)
    # Генерация шагов двигателя
    for _ in range(steps):
        # Генерация шагового сигнала
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(delay)
        kol_shagov+=1
        kol_oborotov = kol_shagov//1600
        degrees = ((kol_shagov/1600)*360)
        print(angle_change(degrees, degrees=((kol_shagov/1600)*360))
        print("kol_shagov = ", kol_shagov)
        print("kol_oborotov = ", kol_oborotov)
        print("degrees = ", degrees%360)
    	# Остановка двигателя
    GPIO.output(step_pin, GPIO.LOW)
# Пример использования
control_stepper_motor(1600, 0.000)  # Выполнить 200 шагов с задержкой 0.01 секунды
final_time =  time.time()
# Освободить ресурсы и завершить программу
GPIO.cleanup()
print(current_time, final_time)
print(current_time - final_time)
