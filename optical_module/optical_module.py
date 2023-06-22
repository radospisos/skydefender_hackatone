import cv2

class OpticalModule:
    def __init__(self, channel):
        self.channel = channel
        self.capture = cv2.VideoCapture(self.channel)
        self.test_devices()

    def __del__(self):
        self.capture.release()

    def test_devices(self):
        if self.capture is None or not self.capture.isOpened():
            raise Exception(str("Camera device is not available on channel " + str(self.channel)))
        else:
            print('Camera device is available on channel', str(self.channel))

    def frame(self):
        ret, frame = self.capture.read()
        if ret:
            return frame
