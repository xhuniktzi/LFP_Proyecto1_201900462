from re import I
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import List
from afd import automata
from analizador import analizador
from models.error_entry import ErrorEntry
from models.img import ImageEntry
from models.token import Token
from jinja2 import Environment, select_autoescape
from jinja2.loaders import FileSystemLoader
from os import startfile
from PIL import Image, ImageDraw


def process_file(tokens: List[Token], errs: List[ErrorEntry]):
    env = Environment(loader=FileSystemLoader('src/templates'),
                      autoescape=select_autoescape(['html']))
    template = env.get_template('table_report.jinja2.html')

    html_file = open('reports.html', 'w+', encoding='utf-8')
    html_file.write(template.render(tokens=tokens, errs=errs))
    html_file.close()


def create_image(img_element: ImageEntry):
    img = Image.new('RGB', (img_element.ancho, img_element.alto), 'white')
    draw = ImageDraw.Draw(img)

    x_space: int = img_element.ancho // img_element.columnas
    y_space: int = img_element.alto // img_element.filas

    for celda in img_element.celdas:
        x_start: int = celda.pos_x * x_space
        y_start: int = celda.pos_y * y_space

        x_end: int = x_start + x_space
        y_end: int = y_start + y_space

        draw.rectangle((x_start, y_start, x_end, y_end),
                       fill=celda.color if celda.is_draw else '#FFFFFF',
                       width=0)
        # for i in range(img_element.ancho):
        #     for j in range(img_element.alto):
        #         pixels[celda.pos_x + i,
        #                celda.pos_y + j] = ImageColor.getrgb(celda.color)

    img.save('prueba.png')


if __name__ == '__main__':
    Tk().withdraw()
    while True:
        print('''
---- ---- ---- Menu ---- ---- ----
1. Analizar Archivo
2. Ver Reportes
3. Crear Imagen
4. Mostrar Imagen
4. Salir
        ''')
        value = input('Ingresa una opción: ')
        if value == '1':
            filename = askopenfilename()
            filereader = open(filename, 'r+', encoding='utf-8')
            current_file = filereader.read()
            tokens, errs = automata(current_file)
            process_file(tokens, errs)
        elif value == '2':
            startfile('reports.html')
        elif value == '3':
            filename = askopenfilename()
            filereader = open(filename, 'r+', encoding='utf-8')
            current_file = filereader.read()
            tokens, errs = automata(current_file)
            images = analizador(tokens)
            create_image(images[0])
            # for img in images:
            #     create_image(img)
        elif value == '4':
            pass
        elif value == '5':
            break