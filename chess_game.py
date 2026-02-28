import chess
import chess.engine

class ChessGame:
    def __init__(self):
        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci("path/to/your/engine")

    def play(self):
        while not self.board.is_game_over():
            print(self.board)
            if self.board.turn:
                self.player_move()
            else:
                self.engine_move()
        print("Game over. Result: " + str(self.board.result()))

    def player_move(self):
        move = input("Enter your move (in UCI format): ")
        try:
            self.board.push_uci(move)
        except ValueError:
            print("Invalid move. Please try again.")
            self.player_move()

    def engine_move(self):
        result = self.engine.play(self.board, chess.engine.Limit(time=1))
        self.board.push(result.move)

    def __del__(self):
        self.engine.quit()

if __name__ == '__main__':
    game = ChessGame()
    game.play()