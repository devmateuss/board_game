from core.config import settings

from .game_board import GameBoard
from core.player.player_cautious import PlayerCautious
from core.player.player_demanding import PlayerDemanding
from core.player.player_impulsive import PlayerImpulsive
from core.player.player_random import PlayerRandom

strategies = {
    "impulsive": PlayerImpulsive,
    "demanding": PlayerDemanding,
    "cautious": PlayerCautious,
    "randomer": PlayerRandom,
}


def create_player(strategy: str, *args, **kwargs):
    try:
        return strategies[strategy](strategy=strategy, *args, **kwargs)

    except KeyError:
        available_strategies = ", ".join(strategies.keys())
        raise NotImplementedError(
            f"The player strategy '{strategy}' is not implemented."
            f"Please use the available strategies: {available_strategies}"
        )


def create_board():
    board = GameBoard()
    players = [
        create_player(strategy)
        for strategy in settings.ENV_STRATEGY
    ]
    board.players = players
    return board
