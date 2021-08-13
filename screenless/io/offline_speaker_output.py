from pyttsx3 import init
from threading import Thread

from ..output import Output


class OfflineSpeakerOutput(Output):
    INPUT_TO_TEXT = {
        ' ': 'space',
        "\n": 'enter',
        "\r": 'enter'
    }

    def output(self, output):
        if output in OfflineSpeakerOutput.INPUT_TO_TEXT:
            output = OfflineSpeakerOutput.INPUT_TO_TEXT[output]
        thread = Thread(target=self._play_text, args=(output,))
        thread.start()

    def _play_text(self, text):
        engine = init()
        engine.say(text)
        engine.runAndWait()
