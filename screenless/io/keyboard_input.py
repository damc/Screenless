from ..input import Input, INPUT_BACKSPACE, INPUT_CONTROL, INPUT_EXIT
from ..input import INPUT_DOWN, INPUT_LEFT, INPUT_RIGHT, INPUT_UP

from readchar import readkey
from readchar.key import BACKSPACE, CTRL_D, CTRL_B, DOWN, LEFT, RIGHT, UP


class KeyboardInput(Input):
    KEY_TO_INPUT = {
        BACKSPACE: INPUT_BACKSPACE,
        CTRL_D: INPUT_CONTROL,
        DOWN: INPUT_DOWN,
        LEFT: INPUT_LEFT,
        RIGHT: INPUT_RIGHT,
        UP: INPUT_UP,
        CTRL_B: INPUT_EXIT
    }

    def input(self):
        key = readkey()
        if key in KeyboardInput.KEY_TO_INPUT:
            return KeyboardInput.KEY_TO_INPUT[key]
        return key
