from utils.AudioManager import AudioManager


def main():
    audio_manager = AudioManager()
    frames = audio_manager.get_frames_from_file('audio/doorbell.wav')
    audio_manager.cleanup()

    print(audio_manager.get_frequencies(frames))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
