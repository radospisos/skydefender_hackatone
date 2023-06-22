import cv2

class Tracker:
    def __init__(self):
        self.tracker = cv2.legacy.TrackerMedianFlow_create()

    def init(self, frame, bbox):
        #if frame.empty():
        #    pass
        self.tracker.init(frame, bbox)

    def update(self, frame):
        #if frame.empty():
        #    pass
        ok, bbox = self.tracker.update(frame)
        if not ok:
            pass
        return ok, bbox
