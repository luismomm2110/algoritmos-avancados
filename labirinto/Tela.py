from collections import defaultdict
from Comando import InterromperPrograma, LeitorDeArquivo
from typing import AnyStr

from labirinto.Solver.Estrategia import Resolver


class Tela:
    def __init__(self) -> None:
        self.arquivo = ""
        self.comando = None

    def selecionar_arquivo(self) -> None:
        self.arquivo = input("Selecione o arquivo")


def main():
    tela = Tela()
    isRunning = True
    cache = defaultdict()

    while isRunning:
        comando = input('Digite o nome do arquivo ou aperte Q para sair')
        if comando.capitalize() == 'Q':
            tela.comando = InterromperPrograma()
            isRunning = tela.comando.execute()
        else:
            tela.comando = LeitorDeArquivo(
                Resolver(), tela.arquivo, cache=cache)
            tela.comando.execute()


if __name__ == "__main__":
    main()
