import pyaudio


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
        print("Recording...")

        frames = []
        for i in range(0, int(self.RATE / self.CHUNK * duration)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("Done recording.")
        stream.stop_stream()
        stream.close()

        return frames

    def play(self, frames):
        stream = self.p.open(format=self.FORMAT,
                             channels=self.CHANNELS,
                             rate=self.RATE,
                             output=True,
                             frames_per_buffer=self.CHUNK)
        print("Playing back...")

        for frame in frames:
            stream.write(frame)

        print("Done playing.")
        stream.stop_stream()
        stream.close()

    def cleanup(self):
        self.p.terminate()
