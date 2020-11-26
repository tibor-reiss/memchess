from typing import List, Optional

from src.rules import ChessPieceFactory
from src.db import update_db


FACT = ChessPieceFactory()


def run_task(
        board_size: int,
        number_of_pieces: int,
        name: str,
        id: str,
        instance_path: str,
        start_i: int = 1,
        start_j: int = 0,
        pieces: Optional[List] = None,
        main_task: bool = False
):
    total = 0
    if pieces is None:
        pieces = []
    for i in range(start_i, board_size + 1):
        if i < start_i:
            continue
        for j in range(1, board_size + 1):
            if i == start_i and j <= start_j:
                continue            
            place_piece(pieces, name, i, j)
            if not check_pieces(pieces):
                remove_last_piece(pieces)
                continue
            if len(pieces) == board_size:
                total += 1
                remove_last_piece(pieces)
                continue
            if i == board_size and j == board_size:
                remove_last_piece(pieces)
                continue
            total += run_task(
                board_size,
                number_of_pieces - 1,
                name,
                id,
                instance_path,
                start_i=i,
                start_j=j,
                pieces=pieces)
            remove_last_piece(pieces)
    if main_task:
        update_db(instance_path, id, str(total))
    return total


def place_piece(pieces, name, i, j):
    new_piece = FACT.create_piece(name, i, j)
    pieces.append(new_piece)


def remove_last_piece(pieces):
    pieces.pop()


def check_pieces(pieces):
    if len(pieces) <= 1:
        return True
    for p1 in pieces:
        for p2 in pieces:
            if p1.collision(p2):
                return False
    return True
