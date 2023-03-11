from utils.AudioManager import AudioManager


def main():
    audio_manager = AudioManager()
    frames = audio_manager.record(5)
    audio_manager.play(frames)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
