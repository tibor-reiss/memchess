from __future__ import annotations
from abc import ABC, abstractmethod
from collections import namedtuple


class ChessPieceFactory:
    @staticmethod
    def create_piece(name, i, j):
        if name == 'queen':
            return Queen(i, j)
        if name == 'rook':
            return Rook(i, j)


class ChessPiece(ABC):
    def __init__(self, i, j):
        self._i = i
        self._j = j
    
    @abstractmethod
    def collision(self):
        pass


class Queen(ChessPiece):
    def collision(self, other: Queen):
        if self._i == other._i and self._j == other._j:
            return False
        if self._i == other._i:
            return True
        if self._j == other._j:
            return True
        if abs(self._i - other._i) == abs(self._j - other._j):
            return True
        return False


class Rook(ChessPiece):
    def collision(self, other: Rook):
        if self._i == other._i and self._j == other._j:
            return False
        if self._i == other._i:
            return True
        if self._j == other._j:
            return True
        return False
