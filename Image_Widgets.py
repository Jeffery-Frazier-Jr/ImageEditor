import customtkinter as ctk
from tkinter import filedialog, Canvas
from settings import *

class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, import_func):
        super().__init__(parent)
        self.grid(column = 0, columnspan = 2, row = 0, sticky = 'news')
        self.import_func = import_func

        ctk.CTkButton(self, text = 'open image', command = self.open_dialog).pack(expand = True)

    def open_dialog(self):
        path = filedialog.askopenfile().name
        self.import_func(path)

class ImageOutput(Canvas):
    def __init__(self, parent, resize_image):
        super().__init__(parent, bg = BACKGROUND_COLOR, bd = 0, highlightthickness = 0, relief = 'ridge')
        self.grid(row = 0, column = 1, sticky = 'news')
        self.bind('<Configure>', resize_image)

class CloseOutput(ctk.CTkButton):
    def __init__(self, parent, close_func):
        super().__init__(
            parent,
            command = close_func, 
            text = 'x', 
            text_color = WHITE, 
            fg_color= 'transparent', 
            width = 40, 
            height = 40, 
            corner_radius = 0, 
            hover_color = CLOSE_RED)
        self.place(relx  = .99, rely = .01, anchor = 'ne')