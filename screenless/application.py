from .io import KeyboardInput
from .io import OfflineSpeakerOutput


class Application:
    def __init__(
            self,
            commands,
            starting_command=None,
            input_=None,
            output=None
    ):
        self.commands = commands
        self.starting_command = starting_command
        self.input = input_ or KeyboardInput()
        self.output = output or OfflineSpeakerOutput()

    def run(self):
        self.starting_command()


class Command:
    def __init__(self, execute, names=None, exit_=None):
        self.execute = execute
        self.names = names
        self.exit = exit_

    def __call__(self, *args, **kwargs):
        self.execute()
