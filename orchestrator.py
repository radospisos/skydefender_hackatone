from optical_module.optical_module import OpticalModule
from display_module.graphics import Graphics
from display_module.gui import App
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
import cv2

class Orchestrator:
    def __init__(self, camera_channel=0):
        self.camera_channel = camera_channel
        self.optical_module = OpticalModule(self.camera_channel)
        self.display_module = Graphics()
        self.frame = None
        self.frames_counter = 0
        self.scanning_modes = {
            '360scan': [self.full_range_scan, "Сканування на 360 градусів"],
            'sector_scan': [self.sector_scan, "Сканування в секторі"],
            'sector_fix': [self.sector_fix, "Фіксація за кутом"]
        }
        self.app = App(self.scanning_modes)

    #def test_devices(self):
        #optical_module.camera.test_access(self.camera_channel)

    def full_range_scan(self):
        print('Scanning 360 degrees..')

    def sector_scan(self):
        print('Scanning sector..')

    def sector_fix(self):
        print('Fixed in a sector..')

    def stream(self):
        global label_widget
        self.frames_counter += 1
        self.frame = self.optical_module.frame()

        user_image = self.app.get_app_image(self.display_module.draw_default_markup(self.frame))
        self.app.video.photo_image = user_image
        self.app.video.configure(image=user_image)
        self.app.video.after(1, self.stream)

    def mainloop(self):
        self.app.mainloop()


o = Orchestrator()

o.stream()
o.mainloop()
