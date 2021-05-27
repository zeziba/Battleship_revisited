from dataclasses import dataclass
from enum import Enum

import Player


class State(Enum):
    RUNNING: 0
    STOPPED: 1
    RESTART: 2


@dataclass()
class GameManager:
    state = State
    players = (Player.Player, Player.Player)

    def __repr__(self):
        return f"{self.state}"
