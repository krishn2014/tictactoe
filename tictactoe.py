"""
This module contains defination for the class TicTacToe to represent TicTacToe game.
"""

import re

MARKER = ['o', 'x']

class InvalidMoveException(Exception):
    pass

class InvalidMarkerException(Exception):
    pass

class TieGameException(Exception):
    pass

class TicTacToe:

    def __init__(self, size=3):
        """
        Initialize TicTacToe game with initial board size to 3.

        Args:
            size: number of columns in tictactoe
        """
        self.size = size
        self.remaining_moves = size * size
        self.board = []
        for i in range(self.size):
            self.board.append(['-' for i in range(self.size)])

    def _is_winning_combination(self, combination, marker):
        """
        Declares if given combination is winning combination

        Args:
            combination: list of values in a combination
            marker: marker to check for
        Returns:
            True: if element==marker for all element in combination
            False: if above does not hold        
        """
        for i in combination:
            if i != marker:
                return False
        return True

    def display(self):
        """
        Displays tictactoe board to the user.
        """
        print '\n  ',
        for i in range(3):
            if i == 0:
                print "%s " % (i+1),
            else:
                print " %s " % (i+1),
        print '\n'     
        for i in range(self.size):
            print "%s " % (i+1),
            for j in range(self.size):
                if j != 0:
                    print '|',
                print self.board[i][j], 
            print '\n',

    def validate_move(self, move):
        """ 
        Validates a given move.

        Args:
            move: space separated string containing row and column number example: '2 3'
        Returns:
            List containing row and column number if its a valid move
        Raises:
            InvalidMoveException if invalid move is provided
        """    
        inpt = re.match('^\s*([0-9]+)\s+([0-9]+)\s*$', move)
        if inpt is None:
            raise InvalidMoveException("invalid move. please provide move in format 'row column'")

        r, c = int(inpt.group(1))-1 , int(inpt.group(2))-1

        if r >= self.size or c >= self.size or r < 0 or c < 0:
            raise InvalidMoveException("invalid move. please provide vlaue in range 1 to %s" % self.size)
        if self.board[r][c] != '-':
            raise InvalidMoveException("invalid move. given field is already marked. plese provide different field")
        return [r, c]

    def make_move(self, move, marker):
        """
        Make a move on the board.

        Args:
            move: move to make
            marker: marker to put in position given by move
        Returns:
            True if move is made successfull
        Raises:
            InvalidMoveException for unsuccessfull move
            InvalidMarkerException for invalid marker
        """
        if marker not in MARKER:
            raise InvalidMarkerException('please provide marker in %s' % MARKER)
        r, c = self.validate_move(move)
        self.board[r][c] = marker
        self.remaining_moves -= 1

    def is_winner(self, marker):
        """
        Declares if the player using marker passed is winner or not. 
        
        Args:
            marker: player's marker
        Returns:
            True: player is the winner
            False: if game is not over
        Raises:
            TieGameException if its a tie
        """
        pcombinations = []
        diag1 = []
        diag2 = []

        for i in list(range(self.size)):
            pcombinations.append(self.board[i])
            pcombinations.append([r[i] for r in self.board])
            for j in list(range(self.size)):
                if i == j:
                    diag1.append(self.board[i][j])
                if i == (self.size - j - 1):
                    diag2.append(self.board[i][j])

        pcombinations.append(diag1)
        pcombinations.append(diag2)
        for comb in pcombinations:
            if self._is_winning_combination(comb, marker):
                return True

        if  self.remaining_moves == 0:
            raise TieGameException('Game Tied')

        return False
