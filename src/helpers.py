from models.error_entry import ErrorEntry
from models.img import ImageEntry
from models.token import Token
from jinja2 import Environment, select_autoescape
from jinja2.loaders import FileSystemLoader
from os import startfile
from PIL import Image, ImageDraw
from typing import List


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

    img.save('prueba.png')
    startfile('prueba.png')


def process_file(tokens: List[Token], errs: List[ErrorEntry]):
    env = Environment(loader=FileSystemLoader('src/templates'),
                      autoescape=select_autoescape(['html']))
    template = env.get_template('table_report.jinja2.html')

    html_file = open('reports.html', 'w+', encoding='utf-8')
    html_file.write(template.render(tokens=tokens, errs=errs))
    html_file.close()
    startfile('reports.html')
