import Jetson.GPIO as GPIO
import time
class Motors: #Создаём класс моторы
    def __init__(self, stepPin, dirPin): # Для каждого мотора пин шаговый (ШИМ) и пин направления
        GPIO.setmode(GPIO.BOARD)
        self.stepPin = stepPin # пин на котором задаётся движение мотора
        self.dirPin = dirPin #вот этот пин под вопросом
        # при создании экземпляра
        self.current_steps = 0
        self.abs_angle = 0
        self.current_angle = 0
        self.begin_time = 0
        self.final_time = 0
        self.angular_velocity = 0
        self.time_to_rotate = 0

        # для меня
        #print(stepPin, ' ', dirPin)

    def moveClockwise(self, angle_to_tilt):
        GPIO.output(self.dirPin, GPIO.HIGH)
        self.begin_time = time.time()
        if angle_to_tilt < 90:
            for _ in range(angle_to_tilt/0.225):# 0,225 это соотношение делителя на драйвере двигателя и 360гр
                GPIO.output(self.stepPin, GPIO.HIGH)# получаем количество шагов на которые надо прокрутить
                GPIO.output(self.stepPin, GPIO.LOW)
                self.current_steps += 1
                # для меня
                #print(self.stepPin, ' ', self.dirPin, ' ', angle_to_tilt)
            self.final_time = time.time()

    def moveCntrClockwise(self, angle_to_tilt):
        self.begin_time = time.time()
        GPIO.output(self.dirPin, GPIO.HIGH)
        for _ in range(angle_to_tilt/0.225):
            GPIO.output(self.stepPin, GPIO.HIGH)
            GPIO.output(self.stepPin, GPIO.LOW)
            # для меня
            #print(self.stepPin, ' ', self.dirPin, ' ', steps)
    def getAbsAngle(self, steps):
        self.abs_angle = steps / 1600
        return self.abs_angle
    def getCurrentAngle(self):
        self.current_angle = self.abs_angle%360
        return self.current_angle
    def getTimetoRotate(self):
        self.time_to_rotate = self.final_time - self.begin_time
        return self.time_to_rotate
    def getAngularVelocity(self):
        return self.abs_angle/self.time_to_rotate



