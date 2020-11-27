from __future__ import annotations
from abc import ABC, abstractmethod
from collections import namedtuple


class ChessPieceFactory:
    @staticmethod
    def create_piece(name: str, i: int, j: int) -> ChessPiece:
        if name == 'queen':
            return Queen(i, j)
        if name == 'rook':
            return Rook(i, j)
        if name == 'bishop':
            return Bishop(i, j)
        if name == 'knight':
            return Knight(i, j)
        if name == 'king':
            return King(i, j)


class ChessPiece(ABC):
    def __init__(self, i, j):
        self._i = i
        self._j = j
    
    @abstractmethod
    def collision(self, other: ChessPiece) -> bool:
        pass


class Queen(ChessPiece):
    def collision(self, other: Queen) -> bool:
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
    def collision(self, other: Rook) -> bool:
        if self._i == other._i and self._j == other._j:
            return False
        if self._i == other._i:
            return True
        if self._j == other._j:
            return True
        return False


class Bishop(ChessPiece):
    def collision(self, other: Bishop) -> bool:
        if self._i == other._i and self._j == other._j:
            return False
        if abs(self._i - other._i) == abs(self._j - other._j):
            return True
        return False


class Knight(ChessPiece):
    def collision(self, other: Knight) -> bool:
        if self._i == other._i and self._j == other._j:
            return False
        if abs(self._i - other._i) == 2 and abs(self._j - other._j) == 1:
            return True
        if abs(self._i - other._i) == 1 and abs(self._j - other._j) == 2:
            return True
        return False


class King(ChessPiece):
    def collision(self, other: King) -> bool:
        if self._i == other._i and self._j == other._j:
            return False
        if abs(self._i - other._i) in (0, 1) and abs(self._j - other._j) in (0, 1):
            return True
        return False
