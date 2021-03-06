from core.config import settings

from core.board.factory import create_board
from core.board.game_statistics import show_statistics


def main():
    '''
    Uma vez executado deve rodar 300 simulações e exibir no console
    os dados de simulações referente as execulções.
    '''

    results = []
    for index in range(int(settings.ENV_NUMBER_SIMULATION)):
        board = create_board()
        while board.winner is None:
            for player in board.players:
                if player.gameover:
                    board.remove(player)
                winner = board.check_winner(player)
                if winner:
                    board.winner = winner
                    break
                board.play(player, board)
            board.played += 1
        results.append(board.finish())
    show_statistics(results)


if __name__ == "__main__":
    main()