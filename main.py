from utils.AudioManager import AudioManager


def main():
    audio_manager = AudioManager()
    audio_manager.play_from_file('audio/doorbell.wav')
    audio_manager.cleanup()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
