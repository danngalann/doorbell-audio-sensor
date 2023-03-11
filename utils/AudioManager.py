import math

import pyaudio
import wave

import numpy as np


class AudioManager:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024

    def record(self, duration):
        stream = self.p.open(format=self.FORMAT,
                             channels=self.CHANNELS,
                             rate=self.RATE,
                             input=True,
                             frames_per_buffer=self.CHUNK)

        frames = []
        for i in range(0, int(self.RATE / self.CHUNK * duration)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        stream.stop_stream()
        stream.close()

        return frames

    def play(self, frames):
        stream = self.p.open(format=self.FORMAT,
                             channels=self.CHANNELS,
                             rate=self.RATE,
                             output=True,
                             frames_per_buffer=self.CHUNK)

        for frame in frames:
            stream.write(frame)

        stream.stop_stream()
        stream.close()

    def get_frames_from_file(self, filename):
        wf = wave.open(filename, 'rb')
        stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()),
                             channels=wf.getnchannels(),
                             rate=wf.getframerate(),
                             output=True,
                             frames_per_buffer=self.CHUNK)

        frames = []
        data = wf.readframes(self.CHUNK)
        while data:
            frames.append(data)
            data = wf.readframes(self.CHUNK)

        stream.stop_stream()
        stream.close()

        return frames

    @staticmethod
    def get_frequencies(frames) -> np.ndarray:
        samples = np.frombuffer(b''.join(frames), dtype=np.int16)
        frequencies = np.fft.rfft(samples)
        frequencies = abs(frequencies)

        return frequencies

    @staticmethod
    def get_decibels(frames) -> float:
        samples = np.frombuffer(b''.join(frames), dtype=np.int16)
        rms = np.sqrt(np.mean(np.square(samples)))

        return abs(20 * math.log10(rms / 32767))

    def cleanup(self):
        self.p.terminate()
