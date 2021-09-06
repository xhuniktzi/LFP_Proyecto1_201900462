import re
from tkinter import Tk
from tkinter.filedialog import askopenfilename


class ErrorEntry:
    def __init__(self, linea: int, col: int, char: str) -> None:
        self.linea: int = linea
        self.col: int = col
        self.char: str = char


class Token:
    def __init__(self, token: str, lexema: str, fila: int, col: int) -> None:
        self.token: str = token
        self.lexema: str = lexema
        self.fila: int = fila
        self.col: int = col


# recibe un string, retorna lista de tokens y errores
def automata(input: str) -> tuple:
    # definición de regex
    S = re.compile(r'[,;=\[\]\{\}]')
    W = re.compile(r'[A-Z]')
    D = re.compile(r'\d')
    C = re.compile(r'[0-9A-F]')

    input += '\n'  # Agregar char al final
    tokens: list = []  # Lista tokens
    errores: list = []  # Lista errores
    estado: int = 0  # Estado inicial
    lexema: str = ''  # lexema actual
    index: int = 0  # indice
    while index < len(input):
        char = input[index]

        # Estado inicial
        if estado == 0:
            #Lista de transiciones
            if S.search(char):
                estado = 1
                index += 1
                lexema += char

            elif W.search(char):
                estado = 2
                index += 1
                lexema += char

            elif D.search(char):
                estado = 3
                index += 1
                lexema += char

            elif char == '"':
                estado = 4
                index += 1
                lexema += char

            elif char == '@':
                estado = 5
                index += 1
                lexema += char

            elif char == "#":
                estado = 6
                index += 1
                lexema += char

            # Caracteres ignorados
            elif re.search(r'[\n]', char):
                index += 1
            elif re.search(r'[ \t]', char):
                index += 1
            else:
                index += 1
                errores.append(char)

        elif estado == 1:
            estado = 0
            tokens.append(lexema)
            lexema = ''

        elif estado == 2:
            if W.search(char):
                index += 1
                lexema += char

            else:
                estado = 0
                tokens.append(lexema)
                lexema = ''

        elif estado == 3:
            if D.search(char):
                index += 1
                lexema += char

            else:
                estado = 0
                tokens.append(lexema)
                lexema = ''

        elif estado == 4:
            if re.search(r'[ \w]', char):
                estado = 7
                index += 1
                lexema += char
            else:
                index += 1
                errores.append(char)

        elif estado == 5:
            if char == '@':
                estado = 9
                index += 1
                lexema += char
            else:
                index += 1
                errores.append(char)

        elif estado == 6:
            if C.search(char):
                estado = 12
                index += 1
                lexema += char
            else:
                index += 1
                errores.append(char)

        elif estado == 7:
            if re.search(r'[ \w]', char):
                index += 1
                lexema += char
            elif char == '"':
                estado = 8
                index += 1
                lexema += char
            else:
                index += 1
                errores.append(char)

        elif estado == 8:
            estado = 0
            tokens.append(lexema)
            lexema = ''

        elif estado == 9:
            if char == '@':
                estado = 10
                index += 1
                lexema += char
            else:
                index += 1
                errores.append(char)

        elif estado == 10:
            if char == '@':
                estado = 11
                index += 1
                lexema += char
            else:
                index += 1
                errores.append(char)

        elif estado == 11:
            estado = 0
            tokens.append(lexema)
            lexema = ''

        elif estado == 12:
            if C.search(char):
                estado = 13
                index += 1
                lexema += char
            else:
                index += 1
                errores.append(char)

        elif estado == 13:
            if C.search(char):
                estado = 14
                index += 1
                lexema += char
            else:
                index += 1
                errores.append(char)

        elif estado == 14:
            if C.search(char):
                estado = 15
                index += 1
                lexema += char
            else:
                index += 1
                errores.append(char)

        elif estado == 15:
            if C.search(char):
                estado = 16
                index += 1
                lexema += char
            else:
                index += 1
                errores.append(char)

        elif estado == 16:
            if C.search(char):
                estado = 17
                index += 1
                lexema += char
            else:
                index += 1
                errores.append(char)

        elif estado == 17:
            estado = 0
            tokens.append(lexema)
            lexema = ''

    return tokens, errores


if __name__ == '__main__':
    Tk().withdraw()
    filename = askopenfilename()
    text = open(filename, 'r+', encoding='utf-8').read()
    tokens, errores = automata(text)
    print('Lista de tokens: {}'.format(tokens))
    print('Lista de errores: {}'.format(errores))