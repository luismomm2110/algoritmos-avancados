from abc import ABC, abstractmethod


class Posicao(ABC):
    def __init__(self, x: int, y: int, podeVisitar: bool, char: str) -> None:
        self.x = x
        self.y = y
        self.podeVisitar = podeVisitar
        self.char = char

    @abstractmethod
    def mover(self, visitor: Visitor) -> None:
        pass

    def aceita_visita(self):
        return self.podeVisitar

    def visitar(self, r):
        pass

    def chegou_na_saida(self):
        pass

    def proximas_posicoes(self) -> list:
        return []


class Entrada(Posicao):
    def __init__(self, x: int, y: int, podeVisitar: bool, char: str) -> None:
        super().__init__(x, y, True, 'S')

        def mover(self, visitor: Visitor) -> None:
            pass

        def chegou_na_saida(self):
            return False


class Parede(Posicao):
    def __init__(self, x: int, y: int, podeVisitar: bool, char: str) -> None:
        super().__init__(x, y, False, '#')

        def mover(self, visitor: Visitor) -> None:
            pass

        def chegou_na_saida(self):
            return False


class Saida(Posicao):
    def __init__(self, x: int, y: int, podeVisitar: bool, char: str) -> None:
        super().__init__(x, y, True, 'S')

        def mover(self, visitor: Visitor) -> None:
            pass

        def chegou_na_saida(self):
            return True


class Queijo(Posicao):
    def __init__(self, x: int, y: int, podeVisitar: bool, char: str) -> None:
        super().__init__(x, y, True, 'C')

        def mover(self, visitor: Visitor) -> None:
            pass

        def chegou_na_saida(self):
            return False


class Caminho(Posicao):
    def __init__(self, x: int, y: int, podeVisitar: bool, char: str) -> None:
        super().__init__(x, y, True, '.')

        def mover(self, visitor: Visitor) -> None:
            pass

        def chegou_na_saida(self):
            return False
