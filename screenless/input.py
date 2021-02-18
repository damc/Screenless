INPUT_CONTROL = 1
INPUT_BACKSPACE = 2
INPUT_LEFT = 3
INPUT_RIGHT = 4
INPUT_UP = 5
INPUT_DOWN = 6


class Input:
    def __init__(self, on_input=(lambda x: None)):
        self.on_input = on_input

    def run(self):
        pass

    def exit(self):
        pass

