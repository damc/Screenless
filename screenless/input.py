INPUT_CONTROL = ' control '
INPUT_BACKSPACE = ' backspace '
INPUT_LEFT = ' left '
INPUT_RIGHT = ' right '
INPUT_UP = ' up '
INPUT_DOWN = ' down '
INPUT_EXIT = ' exit '


class Input:
    def input(self):
        pass

    def __call__(self):
        return self.input()
