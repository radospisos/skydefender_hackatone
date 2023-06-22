from optical_module.optical_module import OpticalModule
from display_module.graphics import Graphics
from display_module.gui import App
from controller_module.controller import Controller
from detection.detector import Detector
from tracking.tracker import Tracker
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
import cv2
import numpy as np

class Linearity:
    def __init__(self):
        self.reset()

    def add_point(self, bbox, frame_width):
        self.route_line_points['x'].append(int(bbox[0] + bbox[2]/2))
        self.route_line_points['y'].append(int(bbox[1] + bbox[3]/2))
        self.linearity_counter += 1
        if self.linearity_counter == self.POINTS_AMOUNT:
            coeffs = np.polyfit(np.array(self.route_line_points['x']), np.array(self.route_line_points['y']), 1)
            self.line['pt1'] = (0, int(coeffs[1]))
            self.line['pt2'] = (frame_width-1, int(coeffs[0]*(frame_width-1) + coeffs[1]))
            self.status = True

    def get_status(self):
        return self.status

    def points(self):
        if not self.status:
            return None
        return (self.line['pt1'], self.line['pt2'])

    def reset(self):
        self.POINTS_AMOUNT = 5
        self.route_line_points = {'x': [], 'y': []}
        self.linearity_counter = 0
        self.line = {'pt1': (), 'pt2': ()}
        self.status = False

class Orchestrator:
    def __init__(self, camera_channel=0):
        self.camera_channel = camera_channel
        self.optical_module = OpticalModule(self.camera_channel)
        self.display_module = Graphics()
        self.controller = Controller()
        self.detector = Detector()
        self.tracker = Tracker()
        self.frame = None
        self.frames_counter = 0
        self.scanning_modes = {
            '360scan': [self.full_range_scan, "Сканування на 360 градусів"],
            'sector_scan': [self.sector_scan, "Сканування в секторі"],
            'sector_fix': [self.sector_fix, "Фіксація за кутом"]
        }
        self.app = App(self.scanning_modes)
        self.tracking_flag = False
        self.detected_flag = False
        #self.LINEARITY_NUM = 5
        #self.route_line_points = {'x': [], 'y': []}
        #self.linearity_counter = 0
        #self.line = {'pt1': (), 'pt2': ()}
        self.linearity = Linearity()

        self.frame = None


    #def test_devices(self):
        #optical_module.camera.test_access(self.camera_channel)

    def full_range_scan(self):
        self.controller.full_range_scan()
        print('Scanning 360 degrees..')

    def sector_scan(self, lhs_angle, rhs_angle):
        self.controller.sector_scan(lhs_angle, rhs_angle)
        print('Scanning sector..')

    def sector_fix(self, angle):
        self.controller.sector_fix(angle)
        print('Fixed in a sector..')

    def stream(self):
        #self.frames_counter += 1
        self.frame = self.optical_module.frame()

        if self.tracking_flag:
            #print('tracking')
            ok, bbox = self.tracker.update(self.frame)
            #print('updated')
            if ok:
                self.frame = self.display_module.draw_rectangle(self.frame, bbox, (255, 255, 0))
            else:
                self.tracking_flag = False
                self.linearity.reset()
        else:
            detection_status, det_bbox = self.detector.detect(self.frame)
            if detection_status:
                #print('detected')
                self.frame = self.display_module.draw_rectangle(self.frame, det_bbox, (0, 255, 0))
                self.linearity.add_point(det_bbox, self.frame.shape[1])
                if self.linearity.get_status():
                    self.tracker = Tracker()
                    self.tracker.init(self.frame, det_bbox)
                    self.tracking_flag = True
                #self.tracker = Tracker()

        if self.linearity.get_status():
            pt1, pt2 = self.linearity.points()
            self.frame = cv2.line(self.frame, pt1, pt2, (255, 0, 0), 2)
        user_image = self.app.get_app_image(self.display_module.draw_default_markup(self.frame))
        self.app.video.photo_image = user_image
        self.app.video.configure(image=user_image)
        self.app.video.after(1, self.stream)

    def mainloop(self):
        self.app.mainloop()


o = Orchestrator()

o.stream()
o.mainloop()
