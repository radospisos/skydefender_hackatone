# Python program to open the
# camera in Tkinter
# Import the libraries,
# tkinter, cv2, Image and ImageTk

from tkinter import *
import cv2
from PIL import Image, ImageTk
from tkinter import ttk

def emptyF():
    print('ok')

class App(Tk):
    def __init__(self, func):
        super().__init__()

        self.title('Application')
        #self.geometry('')
        self.label = ttk.Label(self)
        self.label.pack(padx=5, pady=20, side=LEFT)
        self.button = ttk.Button(self, text="test", command=emptyF)
        self.button['command'] = func
        self.button.pack(padx=5, pady=20)
        self.button2 = ttk.Button(self, text="test2")
        self.button2['command'] = func
        self.button2.pack(padx=5, pady=20)
        self.vid = cv2.VideoCapture(0)

    def open_camera(self):
        _, frame = self.vid.read()
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)
        self.label.photo_image = photo_image
        self.label.configure(image=photo_image)
        self.label.after(1, self.open_camera)


if __name__ == "__main__":
  app = App(app.open_camera())
  app.mainloop()
