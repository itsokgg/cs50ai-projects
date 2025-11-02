from tictactoe import terminal, winner, actions, result
import pytest

X = "X"
O = "O"
EMPTY = None
def test_actions():
    assert actions([[X,X,O], [EMPTY,X, O], [O, O, EMPTY]]) == {(1,0), (2, 2)}
    assert actions([[X,EMPTY,O], [X,X, O], [O, EMPTY, EMPTY]]) == {(0, 1), (2, 1), (2, 2)}
    assert actions([[X, X, X], [EMPTY, EMPTY, O], [EMPTY, O, O]]) == "Game Over!"

def test_winner():
    # horizontal
    assert winner([[X, X, X], [EMPTY, EMPTY, O], [EMPTY, O, O]]) == X
    assert winner([[EMPTY, EMPTY, O], [X, X, X], [EMPTY, O, O]]) == X
    assert winner([[EMPTY, EMPTY, O], [EMPTY, O, O], [X, X, X]]) == X
    
    # vertical
    assert winner([[X, X, O], [X, EMPTY, O], [X, O, EMPTY]]) == X
    assert winner([[O, X, O], [X, X, O], [X, X, EMPTY]]) == X
    assert winner([[X, X, O], [EMPTY, EMPTY, O], [X, O, O]]) == O

    # diagonal
    assert winner([[X, X, O], 
                    [X, X, O], 
                    [EMPTY, O, X]]) == X
    assert winner([[X, EMPTY, O], 
                    [O, O, X], 
                    [O, X, X]]) == O
    
    # no win
    assert winner([[EMPTY, X, O], 
                    [O, EMPTY, X], 
                    [EMPTY, X, O]]) == None

def test_terminal():
    # win
    assert terminal([[X, X, X], [EMPTY, EMPTY, O], [EMPTY, O, O]]) == True
    
    # tie
    assert terminal([[X, X, O], 
                    [O, O, X], 
                    [X, X, O]]) == True
    
    # not terminal
    assert terminal([[EMPTY, X, O], 
                          [O, EMPTY, X], 
                          [EMPTY, X, O]]) == False
    assert terminal([[X,EMPTY,O], 
                    [X,X, O], 
                    [O, EMPTY, EMPTY]]) == False
    
    
def test_result():
    with pytest.raises(Exception):
        result([
                [X,EMPTY,O], 
                [X,X, O], 
                [O, EMPTY, EMPTY]], 
                (3, 0))