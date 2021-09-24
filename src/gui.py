from tkinter import Button, Canvas, Frame, PhotoImage, Tk, Label
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
from typing import List
from afd import automata
from analizador import analizador
from helpers import create_image, process_file

from models.img import ImageEntry


class MainApplication:
    def __init__(self) -> None:
        self.lista_images: List[ImageEntry] = []

        self.root = Tk()
        self.frame = Frame()

        # self.root.geometry('600x600')
        self.root.geometry('300x300')
        self.frame.place(x=0, y=0)
        self.frame.config(width=300, height=300)

        self.btn_load_files = Button(self.frame,
                                     text="Cargar Archivo",
                                     command=self.load_file)
        self.btn_load_files.place(x=10, y=10)

        self.combo_images = Combobox(self.frame)
        self.combo_images.place(x=10, y=45)

        self.combo_transforms = Combobox(
            self.frame,
            values=['NORMAL', 'MIRRORX', 'MIRRORY', 'DOUBLEMIRROR'])
        self.combo_transforms.place(x=10, y=80)

        self.btn_process = Button(self.frame,
                                  text="Procesar",
                                  command=self.process_image)
        self.btn_process.place(x=10, y=115)

        # self.lbl_image = Canvas(self.frame, width=500, height=500)
        # self.lbl_image.place(x=10, y=150)

        self.root.mainloop()

    def load_file(self):
        filename = askopenfilename()
        filereader = open(filename, 'r+', encoding='utf-8')
        current_file = filereader.read()
        tokens, errs = automata(current_file)
        process_file(tokens, errs)
        if not len(errs) > 0:
            self.lista_images.clear()
            images = analizador(tokens)
            self.lista_images = images

            name_images: List[str] = []
            for img in images:
                name_images.append(img.titulo)

            self.combo_images['values'] = name_images

    def process_image(self):
        current_image = self.lista_images[self.combo_images.current()]
        current_opt = self.combo_transforms.get()
        if current_opt in ['NORMAL'
                           ] or current_opt in current_image.lista_filtros:
            create_image(current_image, current_opt)

        # photo = PhotoImage(file='../prueba.png')
        # self.lbl_image.create_image(0, 0, image=photo)


if __name__ == '__main__':
    MainApplication()