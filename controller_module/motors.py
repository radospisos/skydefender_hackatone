import Jetson.GPIO as GPIO
import time

class Motors: #Создаём класс моторы
    def __init__(self, stepPin, dirPin): # Для каждого мотора пин шаговый (ШИМ) и пин направления
        GPIO.setmode(GPIO.BOARD)
        self.stepPin = stepPin # пин на котором задаётся движение мотора
        self.dirPin = dirPin #вот этот пин под вопросом
        # при создании экземпляра
        self.current_steps = 0
        self.steps_to_tilt = 0
        self.Xcurrent_angle = 90
        self.Ycurrent_angle = 0
        self.mooved_angle = 0
        self.begin_time = 0
        self.final_time = 0
        self.angular_velocity = 0
        self.time_to_rotate = 0

    def move(self, angle_to_tilt, direction):
        self.steps_to_tilt = angle_to_tilt / 0.225
        if self.Xcurrent_angle == 180 and direction == 1:
            print('X = 180 and dir 1! Cant moove right.')
            self.Xcurrent_angle = 180
        elif self.Xcurrent_angle == 0 and direction == 0:
            print('X = 0 and dir 0! Cant moove left.')
            self.Xcurrent_angle = 0
        elif self.Ycurrent_angle == 90 and direction == 0:
            print('Y = 90 and dir 0! Cant moove up.')
            self.Ycurrent_angle = 90
        elif self.Ycurrent_angle == 0 and direction == 1:
            print('Y = 0 and dir 1! Cant moove down.')
            self.Ycurrent_angle = 0
        else:
            if direction == 1:
                direction = GPIO.HIGH
            else:
                direction = GPIO.LOW
            GPIO.output(self.dirPin, direction)
            self.begin_time = time.time()
            for _ in range(self.steps_to_tilt):# 0,225 это соотношение делителя на драйвере двигателя и 360гр
                GPIO.output(self.stepPin, GPIO.HIGH)# получаем количество шагов на которые надо прокрутить
                GPIO.output(self.stepPin, GPIO.LOW)
                self.current_steps += 1
                self.mooved_angle = self.current_steps*0.225
                if self.stepPin == 32:
                    if direction == 1:
                        self.Xcurrent_angle = self.Xcurrent_angle + self.mooved_angle
                    else:
                        self.Xcurrent_angle = self.Xcurrent_angle - self.mooved_angle
                else:
                    if direction == 1:
                        self.Ycurrent_angle = self.Ycurrent_angle - self.mooved_angle
                    else:
                        self.Ycurrent_angle = self.Ycurrent_angle + self.mooved_angle
            self.final_time = time.time()
    def get_XCurrentAngle(self):
        return self.Xcurrent_angle
    def get_YCurrentAngle(self):
        return self.Ycurrent_angle
    def getAngularVelocity(self):
        return self.mooved_angle/self.time_to_rotate
