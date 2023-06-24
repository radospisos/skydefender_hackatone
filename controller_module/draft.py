from motors import Motors
from optical_module.detection.detector import Detector
class MotoControll():
    def __init__(self, Detector):
        self.x_Moto = Motors(stepPin=32,dirPin=22)
        self.y_Moto = Motors(stepPin=33,dirPin=24 )
        pan_mid = 90 # X - горизрнт
        tilt_mid = 45 # Y - вертикаль
        ret, bbox = Detector().detect()

        if ret:
            x_bb, y_bb, width, height = bbox

            objX = x_bb+width/2 # Х координата центра баундинг бокса
            objY = y_bb+height/2 # У координата центра баундинг бокса
            errorPan = objX - width / 2 #по оси Х отклонение баундинг бокса от центра
            errorTilt = objY - height / 2 #по оси У отклонение баунданиг бокса от центра
            # if errorPan>0: # эта часть кода может быть либо слишком быстрой и не стабильной, либо медленной
            #   pan = pan-1
            # if errorPan<0:
            #   pan = pan+1
            # if errorTilt>0:
            #   tilt = tilt-1
            # if errorTilt<0:
            #   tilt = tilt+1
            while True:
                if abs(errorPan) > 15:
                    pan_mid = pan_mid - errorPan / 43  # цифра из головы, пропорция между кол-вом пикселей и градусом поворота
                if abs(errorTilt) > 15:
                    tilt_mid = tilt_mid - errorTilt / 43  # можно поставить больше делитель и будет чуть плавнее
                if pan_mid > 180:  # Тут мы задаём максимальный угол на который может повернуться камера
                    pan_mid = 180
                    print('Pan is out of range')
                if pan_mid < 0:  # Тут мы задаём максимальный угол на который может повернуться камера
                    pan_mid = 0
                    print('Pan is out of range')
                if tilt_mid > 180:  # Тут мы задаём максимальный угол на который может повернуться камера
                    tilt_mid = 180
                    print('Pan is out of range')
                if tilt_mid < 0:  # Тут мы задаём максимальный угол на который может повернуться камера
                    tilt_mid = 0
                    print('Pan is out of range')
                # Тут должен быть угол поворота двигателя:
                self.x_Moto.move(angle_to_tilt=pan_mid)# Угол поворота по горизонтали = pan
                self.y_Moto.move(angle_to_tilt=tilt_mid)# Угол поворота по вертикали = tilt
                break
