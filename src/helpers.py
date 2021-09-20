from models.error_entry import ErrorEntry
from models.img import ImageEntry
from models.token import Token
from models.celda import Celda
from jinja2 import Environment, select_autoescape
from jinja2.loaders import FileSystemLoader
from os import startfile
from PIL import Image, ImageDraw
from typing import List
from datetime import datetime


def parse_true_false_color(lst_pixels: List[Celda]):
    for pix in lst_pixels:
        if not pix.is_draw:
            pix.color = '#FFFFFF'
            pix.is_draw = True


def create_image(img_element: ImageEntry, opt: str):
    lst_pixels = img_element.celdas.copy()

    img = Image.new('RGB', (img_element.ancho, img_element.alto), 'white')
    draw = ImageDraw.Draw(img)

    span_x: int = img_element.ancho // img_element.columnas
    span_y: int = img_element.alto // img_element.filas

    parse_true_false_color(lst_pixels)
    if opt == 'NORMAL':
        for celda in lst_pixels:
            x_start: int = celda.pos_x * span_x
            y_start: int = celda.pos_y * span_y

            x_end: int = x_start + span_x
            y_end: int = y_start + span_y

            draw.rectangle((x_start, y_start, x_end, y_end),
                           fill=celda.color,
                           width=0)
    elif opt == 'MIRRORX':
        rotate_x(lst_pixels, img_element.columnas)
        for celda in lst_pixels:
            x_start: int = celda.pos_x * span_x
            y_start: int = celda.pos_y * span_y

            x_end: int = x_start + span_x
            y_end: int = y_start + span_y

            draw.rectangle((x_start, y_start, x_end, y_end),
                           fill=celda.color,
                           width=0)
    elif opt == 'MIRRORY':
        rotate_y(lst_pixels, img_element.filas)
        for celda in lst_pixels:
            x_start: int = celda.pos_x * span_x
            y_start: int = celda.pos_y * span_y

            x_end: int = x_start + span_x
            y_end: int = y_start + span_y

            draw.rectangle((x_start, y_start, x_end, y_end),
                           fill=celda.color,
                           width=0)
    elif opt == 'DOUBLEMIRROR':
        rotate_xy(lst_pixels, img_element.columnas, img_element.filas)
        for celda in lst_pixels:
            x_start: int = celda.pos_x * span_x
            y_start: int = celda.pos_y * span_y

            x_end: int = x_start + span_x
            y_end: int = y_start + span_y

            draw.rectangle((x_start, y_start, x_end, y_end),
                           fill=celda.color,
                           width=0)

    filename: str = datetime.now().strftime('%d-%m-%Y-%H-%M-%S')

    img.save('prueba-{}.png'.format(filename))
    startfile('prueba-{}.png'.format(filename))


def rotate_x(lst_pixels: List[Celda], cols: int):
    for pix in lst_pixels:
        pix.pos_x = cols - pix.pos_x


def rotate_y(lst_pixels: List[Celda], rows: int):
    for pix in lst_pixels:
        pix.pos_y = rows - pix.pos_y


def rotate_xy(lst_pixels: List[Celda], cols: int, rows: int):
    for pix in lst_pixels:
        pix.pos_x = cols - pix.pos_x
        pix.pos_y = rows - pix.pos_y


def process_file(tokens: List[Token], errs: List[ErrorEntry]):
    env = Environment(loader=FileSystemLoader('src/templates'),
                      autoescape=select_autoescape(['html']))
    template = env.get_template('table_report.jinja2.html')

    html_file = open('reports.html', 'w+', encoding='utf-8')
    html_file.write(template.render(tokens=tokens, errs=errs))
    html_file.close()
    startfile('reports.html')
