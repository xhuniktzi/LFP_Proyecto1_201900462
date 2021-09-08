from afd import automata
from analizador import analizador

from tkinter import Tk
from tkinter.filedialog import askopenfilename

if __name__ == '__main__':
    Tk().withdraw()
    filename = askopenfilename()
    file = open(filename, 'r+', encoding='utf-8').read()
    tokens, errores = automata(file)

    analizador(tokens)