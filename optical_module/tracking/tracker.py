import cv2

class Tracker:
    def __init__(self):
        self.tracker = cv2.legacy.TrackerMedianFlow_create()

    def init(self, frame, bbox):
        try:
            self.tracker.init(frame, bbox)
        except:
            raise ValueError('invalid frame or bounding box')

    def update(self, frame):
        ok, bbox = self.tracker.update(frame)
        if not ok:
            pass
        return ok, bbox
