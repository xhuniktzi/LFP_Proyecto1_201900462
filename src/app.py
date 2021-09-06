from config import window, menu_bar
from helpers import define_geometry

if __name__ == '__main__':
    geometry = define_geometry(window, 900, 500)
    window.config(menu=menu_bar)
    window.geometry(geometry)
    window.title('Proyecto 1 - LFP')
    menu_bar.add_command(label='Cargar Archivo...',
                         command=lambda: print('Cargar Archivo'))
    menu_bar.add_command(label='Analizar Archivo...',
                         command=lambda: print('Analizar Archivo'))
    menu_bar.add_command(label='Ver reportes...',
                         command=lambda: print('Ver reportes'))
    menu_bar.add_command(label='Seleccionar Imagen...',
                         command=lambda: print('Seleccionar Imagen'))
    menu_bar.add_command(label='Ver Imagen...',
                         command=lambda: print('Ver Imagen'))
    window.mainloop()