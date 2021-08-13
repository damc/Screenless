from screenless.application import Application, Command
from screenless.input import Input, Output


def test_application():
    class TestInput(Input):
        def input(self, text):
            self.on_input(text)

    class TestOutput(Output):
        def __init__(self):
            self.outputted_text = ''

        def output(self, output):
            self.outputted_text += output

    class TestApplication(Application):
        def __init__(self):
            input = TestInput()

            super(TestApplication, self).__init__([],  outp)

            self.text = ''

        def output_inputted_text(self, input_):
            self.output(input_)