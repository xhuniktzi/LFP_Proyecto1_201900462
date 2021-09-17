from typing import List

from models.celda import Celda

class ImageEntry:
    def __init__(self) -> None:
        self.titulo: str = ''
        self.ancho: int = 0
        self.alto: int = 0
        self.filas: int = 0
        self.columnas: int = 0
        self.celdas: List[Celda] = []
        self.lista_filtros: list = []

