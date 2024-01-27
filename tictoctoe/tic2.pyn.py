class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Representing the Tic-Tac-Toe board as a list

    def display_board(self):
        for i in range(0, 9, 3):
            print(self.board[i], '|', self.board[i + 1], '|', self.board[i + 2])
            if i < 6:
                print('---------')

    def available_moves(self):
        return [i for i, cell in enumerate(self.board) if cell == ' ']

    def make_move(self, position, player):
        self.board[position] = player

    def is_winner(self, player):
        # Check rows, columns, and diagonals for a winner
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        return any(all(self.board[i] == player for i in combo) for combo in winning_combinations)

    def is_board_full(self):
        return ' ' not in self.board


class AIPlayer:
    def __init__(self, marker):
        self.marker = marker

    def minimax(self, state, depth, maximizing_player, alpha, beta):
        if state.is_winner('X'):
            return -1  # Human wins
        elif state.is_winner('O'):
            return 1   # AI wins
        elif state.is_board_full():
            return 0   # It's a draw

        available_moves = state.available_moves()

        if maximizing_player:
            max_eval = float('-inf')
            for move in available_moves:
                state.make_move(move, 'O')
                eval = self.minimax(state, depth + 1, False, alpha, beta)
                state.make_move(move, ' ')
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Alpha-Beta Pruning
            return max_eval
        else:
            min_eval = float('inf')
            for move in available_moves:
                state.make_move(move, 'X')
                eval = self.minimax(state, depth + 1, True, alpha, beta)
                state.make_move(move, ' ')
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha-Beta Pruning
            return min_eval

    def get_best_move(self, game):
        best_score = float('-inf')
        best_move = None

        for move in game.available_moves():
            game.make_move(move, 'O')
            score = self.minimax(game, 0, False, float('-inf'), float('inf'))
            game.make_move(move, ' ')

            if score > best_score:
                best_score = score
                best_move = move

        return best_move


def main():
    game = TicTacToe()
    ai_player = AIPlayer('O')

    while True:
        # Player's turn
        player_move = int(input("Enter your move (1-9): ")) - 1

        if player_move not in game.available_moves():
            print("Invalid move. Try again.")
            continue

        game.make_move(player_move, 'X')
        game.display_board()

        if game.is_winner('X'):
            print("Congratulations! You win!")
            break
        elif game.is_board_full():
            print("It's a draw!")
            break

        # AI's turn
        print("AI's move:")
        ai_move = ai_player.get_best_move(game)
        game.make_move(ai_move, 'O')
        game.display_board()

        if game.is_winner('O'):
            print("AI wins! Better luck next time.")
            break
        elif game.is_board_full():
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()