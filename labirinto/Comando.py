from __future__ import annotations
from abc import ABC, abstractmethod
from collections import defaultdict
from typing import AnyStr, Dict
from Solver.Estrategia import Cache, Estrategia


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class LeitorDeArquivo(Command):
    def __init__(self, estrategia: Estrategia, filepath: str, cache: defaultdict):
        self.arquivo = filepath
        self._estrategia = estrategia
        self._cache = cache

    def execute(self) -> None:
        data = self._hash_arquivo()
        if (self._cache.get(data, None)):
            self._estrategia = Cache()
            return self._estrategia.do(self._cache, data)
        else:
            self.estrategia.do(data)

        return data

    @property
    def estrategia(self) -> Estrategia:
        return self._estrategia

    @estrategia.setter
    def estrategia(self, estrategia: Estrategia) -> None:
        self._estrategia = estrategia

    def _hash_arquivo(self) -> AnyStr:
        with open(self.arquivo) as file:
            data = hash(file.read())

            return data


class InterromperPrograma(Command):
    def execute(self) -> None:
        return False
