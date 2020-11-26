import pytest

from src.rules import ChessPieceFactory
from src.calc import run_task


@pytest.fixture
def mock_update_db(mocker):
    mocker.patch('src.calc.update_db')


class Test_Queen:    
    def test_queen_same_row(self):
        q1 = ChessPieceFactory.create_piece('queen', 1, 1)
        q2 = ChessPieceFactory.create_piece('queen', 1, 10)
        assert q1.collision(q2)

    def test_queen_same_column(self):
        q1 = ChessPieceFactory.create_piece('queen', 2, 8)
        q2 = ChessPieceFactory.create_piece('queen', 5, 8)
        assert q1.collision(q2)

    def test_queen_diagonal(self):
        q1 = ChessPieceFactory.create_piece('queen', 1, 1)
        q2 = ChessPieceFactory.create_piece('queen', 2, 2)
        assert q1.collision(q2)

    def test_queen_no_collision(self):
        q1 = ChessPieceFactory.create_piece('queen', 1, 1)
        q2 = ChessPieceFactory.create_piece('queen', 2, 3)
        assert not q1.collision(q2)
    
    def test_queen_board_size_1(self, mock_update_db):
        assert 1 == run_task(1, 1, 'queen', 'a', 'b')
    
    def test_queen_board_size_1(self, mock_update_db):
        assert 0 == run_task(2, 2, 'queen', 'a', 'b')

    def test_queen_board_size_1(self, mock_update_db):
        assert 0 == run_task(3, 3, 'queen', 'a', 'b')

    def test_queen_board_size_1(self, mock_update_db):
        assert 2 == run_task(4, 4, 'queen', 'a', 'b')

    def test_queen_board_size_1(self, mock_update_db):
        assert 10 == run_task(5, 5, 'queen', 'a', 'b')

    def test_queen_board_size_1(self, mock_update_db):
        assert 4 == run_task(6, 6, 'queen', 'a', 'b')

    def test_queen_board_size_1(self, mock_update_db):
        assert 40 == run_task(7, 7, 'queen', 'a', 'b')

    def test_queen_board_size_1(self, mock_update_db):
        assert 92 == run_task(8, 8, 'queen', 'a', 'b')
