from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
import cv2

class App(Tk):
    def __init__(self, scanning_modes):
        super().__init__()

        self.title('Application')
        self.geometry('1440x900')
        #self.resizable(False, False)
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.container.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Video stream panel.
        self.video = ttk.Label(self.container)
        self.video.grid(column=1, rowspan=30, columnspan=3, sticky="nw")
        self.video.grid_propagate(0)


        # Scanning mode menu panel.
        self.scanmode_label = ttk.Label(self.container, text="Режим сканування")
        self.scanmode_label.grid(row=0, column=4)
        self.scanning_modes = scanning_modes

        self.clicked = StringVar()
        options = ['Оберіть режим сканування'] + [self.scanning_modes[i][1] for i in self.scanning_modes]
        self.clicked.set(options[0])

        self.scanmode_choose = ttk.OptionMenu(self.container, self.clicked, *options, command=self.scanmode_options)
        self.scanmode_choose.grid(row=1, column=4, padx=10)
        self.sectorscan_label = ttk.Label(self.container, text="Введіть сектор сканування\n(2 кути за азімутом):")
        self.sectorscan_label1 = ttk.Label(self.container, text="Кут 1:")
        self.sectorscan_entry1 = ttk.Entry(self.container)
        self.sectorscan_label2 = ttk.Label(self.container, text="Кут 2:")
        self.sectorscan_entry2 = ttk.Entry(self.container)
        self.sectorfix_label = ttk.Label(self.container, text="Введіть кут за азімутом:")
        self.sectorfix_entry = ttk.Entry(self.container)
        self.scanmode_button = ttk.Button(self.container, text="Застосувати", command=self.apply_scan_mode)

    def apply_scan_mode(self):
        option = self.clicked.get()
        if option == self.scanning_modes['360scan'][1]:
            self.scanning_modes['360scan'][0]()
        elif option == self.scanning_modes['sector_scan'][1]:
            self.scanning_modes['sector_scan'][0]()
        elif option == self.scanning_modes['sector_fix'][1]:
            self.scanning_modes['sector_fix'][0]()

    def scanmode_options(self, selected_item):
        if selected_item == self.scanning_modes['360scan'][1]:
            self.sectorfix_entry.grid_remove()
            self.sectorfix_label.grid_remove()
            self.sectorscan_label.grid_remove()
            self.sectorscan_label1.grid_remove()
            self.sectorscan_label2.grid_remove()
            self.sectorscan_entry1.grid_remove()
            self.sectorscan_entry2.grid_remove()
            self.sectorscan_entry1.grid_remove()
            self.scanmode_button.grid(row=2, column=4,padx=10)
        elif selected_item == self.scanning_modes['sector_scan'][1]:
            self.sectorfix_entry.grid_remove()
            self.sectorfix_label.grid_remove()
            self.sectorscan_label.grid(row=2, column=4,padx=10)
            self.sectorscan_label1.grid(row=3, column=4,padx=10)
            self.sectorscan_label2.grid(row=5, column=4,padx=10)
            self.sectorscan_entry1.grid(row=4, column=4,padx=10)
            self.sectorscan_entry2.grid(row=6, column=4,padx=10)
            self.sectorscan_entry1.grid(row=7, column=4,padx=10)
            self.scanmode_button.grid(row=8, column=4,padx=10)
        elif selected_item == self.scanning_modes['sector_fix'][1]:
            self.sectorfix_entry.grid(row=2, column=4,padx=10)
            self.sectorfix_label.grid(row=3, column=4,padx=10)
            self.sectorscan_label.grid_remove()
            self.sectorscan_label1.grid_remove()
            self.sectorscan_label2.grid_remove()
            self.sectorscan_entry1.grid_remove()
            self.sectorscan_entry2.grid_remove()
            self.sectorscan_entry1.grid_remove()
            self.scanmode_button.grid(row=4, column=4,padx=10)

    def get_app_image(self, image):
        new_width = 1200  # Укажите требуемую ширину
        aspect_ratio = image.shape[1] / float(image.shape[0])
        new_height = int(new_width / aspect_ratio)
        image = cv2.resize(image, (new_width, new_height))

        opencv_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)
        return photo_image
