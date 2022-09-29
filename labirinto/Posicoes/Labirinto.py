from typing import List
from Posicao import Caminho, Entrada, Posicao, Queijo, Saida, Parede


class Labirinto():
    def __init__(self, fonte: List) -> None:
        self.posicoes = self._criar_posicoes(fonte)

    def _criar_posicoes(self, fonte: List[str]) -> List[Posicao]:
        posicoes = []

        for x in range(len(fonte)):
            for y in range(len(fonte)):
                if fonte[x][y] == '.':
                    posicoes.append(Caminho())
                if fonte[x][y] == 'S':
                    posicoes.append(Entrada())
                if fonte[x][y] == 'C':
                    posicoes.append(Queijo())
                if fonte[x][y] == 'E':
                    posicoes.append(Saida())
                if fonte[x][y] == '#':
                    posicoes.append(Parede())
                else:
                    raise Exception('posicao invalida')
