from optical_module.camera import Camera
from graphic_module import graphics
from graphic_module.gui import GUI
from controller_module.controller import Controller
from optical_module.detection.detector import Detector
from optical_module.tracking.tracker import Tracker
from optical_module.linear_regression import LinearRegression
from flags import Flags
from configs.config import *

class Orchestrator:
    def __init__(self, camera_channel=0):
        self.camera_channel = camera_channel
        self.camera = Camera(self.camera_channel)
        self.controller = Controller()
        self.detector = Detector()
        self.tracker = Tracker()
        self.linear_regression = LinearRegression()
        self.flags = Flags()

        self.initialize_scanning_modes()
        self.gui = GUI(self.scanning_modes)

        self.frame = None

    def stream(self):
        self.frame = self.camera.frame()

        if self.flags.get_flag('tracking'):
            ok, bbox = self.tracker.update(self.frame)
            if ok:
                self.frame = graphics.draw_rectangle(self.frame, bbox, (255, 255, 0))
            else:
                self.stop_tracker()
        else:
            detection_status, det_bbox = self.detector.detect(self.frame)
            if detection_status:
                self.flags.set_flag('detection', True)
                self.frame = graphics.draw_rectangle(self.frame, det_bbox, (0, 255, 0))
                self.linear_regression.add_point(det_bbox, self.frame.shape[1])
                if self.linear_regression.ready_to_approx():
                    self.initialize_tracker(det_bbox)
            else:
                self.flags.set_flag('detection', False)

        if self.linear_regression.ready_to_approx():
            pt1, pt2 = self.linear_regression.points()
            self.frame = graphics.draw_line(self.frame, pt1, pt2, (255, 0, 0))

        self.frame = graphics.update_scanning_info(self.frame, detection=self.flags.get_flag('detection'), tracking=self.flags.get_flag('tracking'), approx=self.linear_regression.ready_to_approx())
        user_image = self.gui.get_app_image(graphics.draw_default_markup(self.frame))
        self.gui.video.photo_image = user_image
        self.gui.video.configure(image=user_image)
        self.gui.video.after(1, self.stream)

    def initialize_tracker(self, bbox):
        self.tracker = Tracker()
        self.tracker.init(self.frame, bbox)
        self.flags.set_flag('tracking', True)

    def stop_tracker(self):
        self.flags.set_flag('detection', False)
        self.flags.set_flag('tracking', False)
        self.linear_regression.reset()

    def initialize_scanning_modes(self):
        scan_modes = get_config('scanning_modes.json')
        self.scanning_modes = {
            list(scan_modes.keys())[0]: [self.full_range_scan, scan_modes[list(scan_modes.keys())[0]]],
            list(scan_modes.keys())[1]: [self.full_range_scan, scan_modes[list(scan_modes.keys())[1]]],
            list(scan_modes.keys())[2]: [self.full_range_scan, scan_modes[list(scan_modes.keys())[2]]]
        }

    def full_range_scan(self):
        self.controller.full_range_scan()
        print('Scanning 360 degrees..')

    def sector_scan(self, lhs_angle, rhs_angle):
        self.controller.sector_scan(lhs_angle, rhs_angle)
        print('Scanning sector..')

    def sector_fix(self, angle):
        self.controller.sector_fix(angle)
        print('Fixed in a sector..')

    def mainloop(self):
        self.gui.mainloop()
