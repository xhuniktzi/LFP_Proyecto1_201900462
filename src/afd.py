import re
from typing import List, Tuple
from models.error_entry import ErrorEntry
from models.token import Token


# recibe un string, retorna lista de tokens y errores
def automata(input: str) -> Tuple[Tuple[Token], Tuple[ErrorEntry]]:
    # definición de regex
    S = re.compile(r'[,;=\[\]\{\}]')
    W = re.compile(r'[A-Z]')
    D = re.compile(r'\d')
    C = re.compile(r'[0-9A-F]')

    input += '\n'  # Agregar char al final
    tokens: List[Token] = []  # Lista tokens
    errores: List[ErrorEntry] = []  # Lista errores
    estado: int = 0  # Estado inicial
    lexema: str = ''  # lexema actual
    index: int = 0  # indice

    row: int = 1  # fila
    col: int = 0  # columna
    while index < len(input):
        char = input[index]

        # Estado inicial
        if estado == 0:
            #Lista de transiciones
            if S.search(char):
                estado = 1
                index += 1
                col += 1
                lexema += char

            elif W.search(char):
                estado = 2
                index += 1
                col += 1
                lexema += char

            elif D.search(char):
                estado = 3
                index += 1
                col += 1
                lexema += char

            elif char == '"':
                estado = 4
                index += 1
                col += 1
                lexema += char

            elif char == '@':
                estado = 5
                index += 1
                col += 1
                lexema += char

            elif char == "#":
                estado = 6
                index += 1
                col += 1
                lexema += char

            # Caracteres ignorados
            elif re.search(r'[\n]', char):
                row += 1
                col = 0
                index += 1

            elif re.search(r'[ \t]', char):
                col += 1
                index += 1

            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 1:
            estado = 0
            tokens.append(Token('simbolo', lexema, row, col))
            lexema = ''

        elif estado == 2:
            if W.search(char):
                index += 1
                col += 1
                lexema += char

            else:
                if lexema in [
                        'TITULO', 'ANCHO', 'ALTO', 'FILAS', 'COLUMNAS',
                        'CELDAS', 'TRUE', 'FALSE', 'FILTROS', 'MIRRORX',
                        'MIRRORY', 'DOUBLEMIRROR'
                ]:
                    tokens.append(Token('reservada', lexema, row, col))

                else:
                    errores.append(ErrorEntry(row, col, lexema))
                    index += 1
                    col += 1

                estado = 0
                lexema = ''

        elif estado == 3:
            if D.search(char):
                index += 1
                col += 1
                lexema += char

            else:
                estado = 0
                tokens.append(Token('numero', lexema, row, col))
                lexema = ''

        elif estado == 4:
            if re.search(r'[ \w]', char):
                estado = 7
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 5:
            if char == '@':
                estado = 9
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 6:
            if C.search(char):
                estado = 12
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 7:
            if re.search(r'[ \w]', char):
                index += 1
                col += 1
                lexema += char
            elif char == '"':
                estado = 8
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 8:
            estado = 0
            tokens.append(Token('string', lexema, row, col))
            lexema = ''

        elif estado == 9:
            if char == '@':
                estado = 10
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 10:
            if char == '@':
                estado = 11
                index += 1
                col += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 11:
            estado = 0
            tokens.append(Token('separador', lexema, row, col))
            lexema = ''

        elif estado == 12:
            if C.search(char):
                estado = 13
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 13:
            if C.search(char):
                estado = 14
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 14:
            if C.search(char):
                estado = 15
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 15:
            if C.search(char):
                estado = 16
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 16:
            if C.search(char):
                estado = 17
                index += 1
                lexema += char
            else:
                errores.append(ErrorEntry(row, col, char))
                index += 1
                col += 1

        elif estado == 17:
            estado = 0
            tokens.append(Token('color', lexema, row, col))
            lexema = ''

    return tuple(tokens), tuple(errores)
