from gtts import gTTS
from os import path, remove
from pyaudio import PyAudio, paContinue
from pydub import AudioSegment
from threading import Timer
from wave import open

from ..input import INPUT_EXIT, INPUT_BACKSPACE, INPUT_CONTROL
from ..input import INPUT_RIGHT, INPUT_LEFT, INPUT_DOWN, INPUT_UP
from ..output import Output


class GoogleSpeakerOutput(Output):
    AUDIO_DIRECTORY_PATH = "audio"

    INPUT_TO_TEXT = {
        ' ': 'space',
        "\n": 'enter',
        "\r": 'enter'
    }

    STREAM_INACTIVITY_CHECK = 3

    def output(self, output):
        if output in GoogleSpeakerOutput.INPUT_TO_TEXT:
            output = GoogleSpeakerOutput.INPUT_TO_TEXT[output]
        file_path = self._save(output)
        self._play(file_path)

    def _save(self, output):
        mp3_path = GoogleSpeakerOutput.AUDIO_DIRECTORY_PATH + "/" + output + ".mp3"
        wav_path = GoogleSpeakerOutput.AUDIO_DIRECTORY_PATH + "/" + output + ".wav"

        if path.exists(wav_path):
            return wav_path

        tts = gTTS(output)
        tts.save(mp3_path)

        sound = AudioSegment.from_mp3(mp3_path)
        sound.export(wav_path, format="wav")
        remove(mp3_path)

        return wav_path

    def _play(self, file_path):
        file = open(file_path, 'rb')
        py_audio = PyAudio()

        def callback(_in_data, frame_count, _time_info, _status):
            data = file.readframes(frame_count)
            return data, paContinue

        stream = py_audio.open(
            format=py_audio.get_format_from_width(file.getsampwidth()),
            channels=file.getnchannels(),
            rate=file.getframerate(),
            output=True,
            stream_callback=callback
        )

        stream.start_stream()

        def close_if_inactive():
            if stream.is_active():
                timer2 = Timer(3, close_if_inactive)
                timer2.start()

            stream.stop_stream()
            stream.close()
            py_audio.terminate()

        timer = Timer(3, close_if_inactive)
        timer.start()
