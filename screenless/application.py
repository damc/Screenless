from .event_dispatcher import EventDispatcher
from .io import KeyboardInput
from .io import SpeakerOutput


class Application:
    def __init__(
            self,
            commands,
            default_command=None,
            input_=None,
            output=None
    ):
        self.commands = commands
        self.default_command = default_command
        self.input = input_ or KeyboardInput()
        self.output = output or SpeakerOutput()

    def run(self):
        self.input.on_input = EventDispatcher(
            {'command': self._handle_commands}
        )
        self.output.run()
        self.default_command()
        self.input.run()

    def exit(self):
        self.input.exit()
        self.output.exit()

    def _handle_commands(self, input_):
        pass


class Command:
    def __init__(self, execute, names=None, exit_=None):
        self.execute = execute
        self.names = names
        self.exit = exit_

    def __call__(self, *args, **kwargs):
        self.execute()
