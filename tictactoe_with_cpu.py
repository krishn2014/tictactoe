#!/usr/bin/python

from tictactoe import MARKER, TieGameException, InvalidMoveException, TicTacToe

QUIT = ['q', 'Q']
END_GAME_MSG = "Enter 'q' to end game"

def make_move_cpu(tictactoe, marker, prev_player_move):
    """
    Checks for potential winning position in 3*3 tictactoe and makes moves accordingly
    """
    size = tictactoe.get_size()

    if tictactoe.is_empty(2 ,2):
        tictactoe.make_move('2 2', marker)
    else:
        pp_move = [int(x) for x in prev_player_move.split(' ')]
        r, c = (size-pp_move[0]+1, size-pp_move[1]+1)
        if tictactoe.get_marker(pp_move[0], pp_move[1]) == tictactoe.get_marker(pp_move[0], c) and tictactoe.is_empty(pp_move[0], 2):
            tictactoe.make_move("%s %s" % (pp_move[0], 2), marker)
        elif tictactoe.get_marker(pp_move[0], pp_move[1]) == tictactoe.get_marker(r, pp_move[1]) and tictactoe.is_empty(2, pp_move[1]):
            tictactoe.make_move("%s %s" % (2, pp_move[1]), marker)
        elif pp_move[0] == 2 and tictactoe.get_marker(pp_move[0], pp_move[1]) == tictactoe.get_marker(1, pp_move[1]) and tictactoe.is_empty(3, pp_move[1]):
            tictactoe.make_move("%s %s" % (3, pp_move[1]), marker)
        elif pp_move[0] == 2 and tictactoe.get_marker(pp_move[0], pp_move[1]) == tictactoe.get_marker(3, pp_move[1]) and tictactoe.is_empty(1, pp_move[1]):
            tictactoe.make_move("%s %s" % (1, pp_move[1]), marker)
        elif pp_move[1] == 2 and tictactoe.get_marker(pp_move[0], pp_move[1]) == tictactoe.get_marker(pp_move[0], 1) and tictactoe.is_empty(pp_move[0], 3):
            tictactoe.make_move("%s %s" % (pp_move[0], 3), marker)
        elif pp_move[1] == 2 and tictactoe.get_marker(pp_move[0], pp_move[1]) == tictactoe.get_marker(pp_move[0], 3) and tictactoe.is_empty(pp_move[0], 1):
            tictactoe.make_move("%s %s" % (pp_move[0], 1), marker)
        elif tictactoe.is_empty(r, c) and tictactoe.is_empty(r, c):
            tictactoe.make_move("%s %s" % (r,c), marker)
        else:
            cell = tictactoe.get_empty_cells()[0]
            tictactoe.make_move_cell(cell, marker)

def play_tictactoe():
    """
    Executes TicTacToe between two players
    """
    print "Size of Tic Tac Toe board: 3"
    size = 3

    marker = raw_input("Choose the marker u want to use from %s: " % MARKER)
    if marker not in MARKER:
        print "wrong marker chossen"
        return
    
    t = TicTacToe(size)
    print "Tic Tac Toe board"
    t.display()

    turn = MARKER.index(marker)
    player = 0
    inpt = ''

    while (inpt not in QUIT):
        try:
            if player != 0:
                make_move_cpu(t, MARKER[turn], inpt)
            else:
                inpt = raw_input("Player %s make your move: " % (player+1))
                t.make_move(inpt, MARKER[turn])
            t.display()
            if t.is_winner(MARKER[turn]):
                print "Player %s wins" % ((player+1) if player == 0 else 'CPU')
                print "Game End"
                return
            turn = turn ^ 1
            player = player ^ 1
        except TieGameException as e:
            print (e)
            return
        except InvalidMoveException as e:
            print (e)
        except Exception as e:
            print "Error: Exiting game"
            return


if __name__ == "__main__":
    play_tictactoe()
