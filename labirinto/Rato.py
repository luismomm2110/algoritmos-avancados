from Posicoes import Labirinto


class Rato:
    def __init__(self, labirinto: Labirinto) -> None:
        self.labirinto = labirinto
        self.position = self._achar_posicao_inicial()

    def _achar_posicao_inicial(self):
        return self.labirinto.posicao_inicial()

    def procurar_saida(self):
        return None
