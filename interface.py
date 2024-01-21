import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from PIL import ImageTk

from watermark import Watermark


class Interface:
    def __init__(self):
        self.watermark = None
        self.watermarked_image = None
        self.window = Tk()
        self.window.title("Watermark app")
        self.window.config(padx=20, pady=20)
        self.window.geometry("800x800")
        self.file_name = None
        self.save_path = None
        self.file_types = (("jpeg", ".jpeg"), ("png", ".png"), ("jpg", ".jpg"))

        self.main_label = Label(self.window, text="Path to image: ", font=("Arial", 16, "normal"))
        self.main_label.grid(row=0, column=0)
        self.watermark_label = Label(self.window, text="Watermark: ", font=("Arial", 16, "normal"))
        self.watermark_label.grid(row=1, column=0)

        self.entry = Entry(self.window, width=70, state=DISABLED)
        self.entry.grid(row=0, column=1)
        self.watermark_entry = Entry(self.window, width=30)
        self.watermark_entry.grid(row=1, column=1)

        self.search_button = Button(self.window, text="Open a photo", command=self.select_file)
        self.search_button.grid(row=0, column=2)

        self.upload_button = Button(self.window, text="Generate", command=self.watermark_button)
        self.upload_button.grid(row=1, column=2)

        self.save_button = Button(self.window, text="Save", command=self.save)
        self.save_button.grid(row=1, column=3)

        self.image = PhotoImage(file="Sem título.png")
        self.canvas = Canvas(width=700, height=700)
        self.background = self.canvas.create_image(350, 350, image=self.image)
        self.canvas.grid(row=2, column=0, columnspan=3)

        self.window.mainloop()

    def select_file(self):
        self.file_name = filedialog.askopenfilename(title="Open a image", initialdir='/User', filetypes=self.file_types)
        self.entry.config(state=tkinter.NORMAL)
        self.entry.delete(0, END)
        self.entry.insert(0, self.file_name)
        self.entry.config(state=tkinter.DISABLED)

    def watermark_button(self):
        if self.file_name is not None:
            self.watermark = Watermark(self.file_name, self.watermark_entry.get())
            self.watermarked_image = self.watermark.image_tk
            self.canvas.itemconfig(self.background, image=self.watermarked_image)

    def save(self):
        if self.watermarked_image is not None:
            self.save_path = filedialog.asksaveasfilename(title="Save the image", defaultextension=".png",
                                                          filetypes=[("png", ".png")])
            self.watermark.image.save(self.save_path, format='PNG')
