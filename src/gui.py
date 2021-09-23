from tkinter.filedialog import askopenfilename
from helpers import define_geometry, process_file
from tkinter import Button, Tk
from tkinter.ttk import Combobox, Label
from afd import automata
from analizador import analizador

window = Tk()
Label(window, text="Mostrar Imagenes").place(x=10, y=100)

combo_img_transform = Combobox(window, state='readonly').place(x=210, y=150)


def report_images():
    filename = askopenfilename()
    filereader = open(filename, 'r+', encoding='utf-8')
    current_file = filereader.read()
    tokens, errs = automata(current_file)
    process_file(tokens, errs)


def load_images():
    filename = askopenfilename()
    filereader = open(filename, 'r+', encoding='utf-8')
    current_file = filereader.read()
    tokens, errs = automata(current_file)
    images = analizador(tokens)
    combo_img = Combobox(window, state='readonly', values=images).place(x=210, y=100)

    combo_img_transform = Combobox(window, state='readonly').place(x=210,
                                                                   y=150)

# def view_images():
#     contador: int = 0
#     for img in lst_images:
#         contador += 1
#         print('{}. {}'.format(contador, img.titulo))
#     select_img = input('Ingresa un numero: ')
#     current_img = lst_images[int(select_img) - 1]

#     contador_2 = 0
#     print('0. NORMAL')
#     for opt in current_img.lista_filtros:
#         contador_2 += 1
#         print('{}. {}'.format(contador_2, opt))
#     select_opt = input('Ingrese una opción: ')

#     if select_opt != '0':
#         current_opt = current_img.lista_filtros[int(select_opt) - 1]
#     else:
#         current_opt = 'NORMAL'

#     create_image(current_img, current_opt)



window.geometry(define_geometry(window, 500, 500))
Label(window, text="Analizar Archivo y ver reportes").place(x=10, y=10)
btn_load = Button(window, text="Abrir", command=report_images).place(x=210,
                                                                     y=10)
Label(window, text="Cargar Imagenes").place(x=10, y=60)
btn_load_img = Button(window, text="Abrir", command=load_images).place(x=210,
                                                                       y=60)
btn_view_img = Button(window, text="Mostrar").place(x=210, y=200)
window.mainloop()
