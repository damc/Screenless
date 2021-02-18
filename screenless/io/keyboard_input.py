from ..input import Input, INPUT_BACKSPACE, INPUT_CONTROL
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
        UP: INPUT_UP
    }

    def __init__(self, on_input=(lambda x: x)):
        super(KeyboardInput, self).__init__(on_input)
        self.exited = False

    def run(self):
        while not self.exited:
            key = readkey()
            if key == CTRL_B:
                exit(0)
            if key in KeyboardInput.KEY_TO_INPUT:
                self.on_input(KeyboardInput.KEY_TO_INPUT[key])
            else:
                self.on_input(key)

    def exit(self):
        self.exited = True
