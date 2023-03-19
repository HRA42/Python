from minimax import find_best_move
from tictactoe import TTTBoard
from board import Move, Board

board: Board = TTTBoard()


def get_player_move() -> Move:
    player_move: Move = Move(-1)
    while player_move not in board.legal_moves:
        play: int = int(input("Legales Feld eingeben (0-8):"))
        player_move = Move(play)
    return player_move


if __name__ == "__main__":
    # Spiel-Hauptschleife
    while True:
        human_move: Move = get_player_move()
        board = board.move(human_move)
        if board.is_win:
            print("Der Mensch gewinnt!")
            break
        elif board.is_draw:
            print("Unentschieden!")
            break
        computer_move: Move = find_best_move(board)
        print(f"Zug des Computers ist {computer_move}")
        board = board.move(computer_move)
        print(board)
        if board.is_win:
            print("Der Computer gewinnt!")
            break
        elif board.is_draw:
            print("Unentschieden!")
            break


