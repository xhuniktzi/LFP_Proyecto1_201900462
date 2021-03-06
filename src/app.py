from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import List
from afd import automata
from analizador import analizador
from models.img import ImageEntry
from helpers import create_image, process_file

if __name__ == '__main__':
    lst_images: List[ImageEntry] = []
    Tk().withdraw()
    while True:
        print('''
---- ---- ---- Menu ---- ---- ----
1. Analizar Archivo y ver reportes
2. Cargar Imagenes
3. Mostrar Imagen
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
            filename = askopenfilename()
            filereader = open(filename, 'r+', encoding='utf-8')
            current_file = filereader.read()
            tokens, errs = automata(current_file)
            images = analizador(tokens)
            for img in images:
                lst_images.append(img)

        elif value == '3':
            contador: int = 0
            for img in lst_images:
                contador += 1
                print('{}. {}'.format(contador, img.titulo))
            select_img = input('Ingresa un numero: ')
            current_img = lst_images[int(select_img) - 1]

            contador_2 = 0
            print('0. NORMAL')
            for opt in current_img.lista_filtros:
                contador_2 += 1
                print('{}. {}'.format(contador_2, opt))
            select_opt = input('Ingrese una opción: ')

            if select_opt != '0':
                current_opt = current_img.lista_filtros[int(select_opt) - 1]
            else:
                current_opt = 'NORMAL'

            create_image(current_img, current_opt)
        elif value == '4':
            break