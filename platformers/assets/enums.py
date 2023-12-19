from enum import Enum


class Colours(Enum):
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)


class Language(Enum):
    ENGLISH = "English"
    HINDI = "hindi"
    BANGLA = "bangla"


class LevelState(Enum):
    START = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4
    EXIT = 5


class PlatformerState(Enum):
    MAIN_MENU = 1
    PLAYING_LEVEL = 2
    QUESTION = 3
    QUIT = 4
    WON = 5


class QuestionState(Enum):
    CORRECT = 1
    INCORRECT = 2


class CollisionType(Enum):
    BLOB = 1
    LAVA = 2
    EXIT = 3
    NONFATAL = 4
    COIN = 5


class PlayerEvent(Enum):
    JUMP = 1
    NOT_JUMPED = 2
    LEFT = 3
    RIGHT = 4
    NONE = 5
