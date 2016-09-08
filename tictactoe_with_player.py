#!/usr/bin/python

from tictactoe import MARKER, TieGameException, InvalidMoveException, TicTacToe

QUIT = ['q', 'Q']
END_GAME_MSG = "Enter 'q' to end game"

def play_tictactoe():
    """
    Executes TicTacToe between two players
    """
    size = input("Enter size of Tic Tac Toe board: ")

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
            inpt = raw_input("Player %s make your move: " % (player+1))
            t.make_move(inpt, MARKER[turn])
            t.display()
            if t.is_winner(MARKER[turn]):
                print "Player %s wins" % (player+1)
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
