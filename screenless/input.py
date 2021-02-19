INPUT_CONTROL = 1
INPUT_BACKSPACE = 2
INPUT_LEFT = 3
INPUT_RIGHT = 4
INPUT_UP = 5
INPUT_DOWN = 6
INPUT_EXIT = 7


class Input:
    def input(self):
        pass

    def __call__(self):
        return self.input()
