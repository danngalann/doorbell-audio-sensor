from utils.AudioManager import AudioManager
import numpy as np


def main():
    audio_manager = AudioManager()

    while True:
        # Record one second of audio
        frames = audio_manager.record(0.3)

        # Get the frequencies from the audio
        frequencies = audio_manager.get_frequencies(frames)

        # Get the decibel value from the audio
        decibels = audio_manager.get_decibels(frames)

        # Calculate the averages of the frequencies
        average_frequency = np.mean(frequencies)

        if decibels > 60:
            print(f"Average frequency: {average_frequency}")
            print(f"Noise: {decibels}db")

            if 19000 < average_frequency < 38000:
                print("Doorbell rung!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
