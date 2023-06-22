from motors import Motors

xMoto = Motors(stepPin=32,dirPin=22 )
yMoto = Motors(stepPin=33,dirPin=24 )

pan = 90 # X - горизрнт
tilt = 45 # Y - вертикаль

objX = x+w/2 # Х координата центра баундинг бокса
objY = y+h/2 # У координата центра баундинг бокса
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
        pan = pan - errorPan / 43  # цифра из головы, пропорция между кол-вом пикселей и градусом поворота
    if abs(errorTilt) > 15:
        tilt = tilt - errorTilt / 43  # можно поставить больше делитель и будет чуть плавнее
    if pan > 180:  # Тут мы задаём максимальный угол на который может повернуться камера
        pan = 180
        print('Pan is out of range')
    if pan < 0:  # Тут мы задаём максимальный угол на который может повернуться камера
        pan = 0
        print('Pan is out of range')
    if tilt > 180:  # Тут мы задаём максимальный угол на который может повернуться камера
        tilt = 180
        print('Pan is out of range')
    if tilt < 0:  # Тут мы задаём максимальный угол на который может повернуться камера
        tilt = 0
        print('Pan is out of range')
    # Тут должен быть угол поворота двигателя:
    xMoto.moveClockwise(angle_to_tilt=pan)# Угол поворота по горизонтали = pan
    yMoto.moveClockwise(angle_to_tilt=tilt)# Угол поворота по вертикали = tilt
    break