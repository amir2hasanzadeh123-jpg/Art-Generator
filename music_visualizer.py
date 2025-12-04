import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def visualize_audio(file="music.wav"):
    sr, data = wavfile.read(file)

    # تبدیل به مونو اگر استریو باشد
    if len(data.shape) == 2:
        data = np.mean(data, axis=1)

    # FFT
    fft_values = np.abs(np.fft.rfft(data))
    frequencies = np.fft.rfftfreq(len(data), 1 / sr)

    plt.figure(figsize=(12, 5))
    plt.plot(frequencies, fft_values)
    plt.title("Audio Frequency Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_audio()
