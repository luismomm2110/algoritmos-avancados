from __future__ import annotations
from abc import ABC, abstractmethod
from collections import defaultdict
from typing import List


class Estrategia(ABC):
    @abstractmethod
    def do(self, data: List):
        pass


class Resolver(Estrategia):
    def do(self, data: List):
        pass


class Cache(Estrategia):
    def do(self, cache: defaultdict, data: str) -> List:
        return cache.get(str)
