import scipy
import scipy.io.wavfile
import pylab
import matplotlib

# Computes the Short-Time Fourier Transform (STFT) of a signal, with a given
# window length, and shift between adjacent windows
def stft(x, window_len=4096, window_shift=2048):
    w = scipy.hamming(window_len)
    X = scipy.array([scipy.fft(w*x[i:i+window_len])
        for i in range(0, len(x)-window_len, window_shift)])
    return scipy.absolute(X[:,0:window_len/2])

# Plot a transformed signal X, i.e., if X = stft(x), then 
# plot_transform(X) plots the spectrogram of x
def plot_transform(X):
    pylab.ion()
    pylab.figure()
    pylab.imshow(scipy.log(X.T), origin='lower', aspect='auto', interpolation='nearest', norm=matplotlib.colors.Normalize())
    pylab.xlabel('Window index')
    pylab.ylabel('Transform coefficient')
    pylab.ioff()

# Plot a list of peaks in the form [(s1, f1), (s2, f2), ...]
def plot_peaks(peak_list):
    pylab.ion()
    pylab.figure()
    s_list, f_list = zip(*peak_list) 
    pylab.plot(s_list, f_list, 'bo')
    pylab.xlabel('Window index')
    pylab.ylabel('Transform coefficient')
    pylab.ioff()


if __name__ == '__main__':
    rate, data = scipy.io.wavfile.read('example.wav')
# Strip out the stereo channel if present
    if (len(data.shape) > 1):
        data = data[:,0]

# Get just the first 10 seconds as our audio signal
    x = data[0:10*rate]

    X = stft(x)
    plot_transform(X)

# Save the figure we just plotted as a .png
    pylab.savefig('spectrogram.png')

# Plot some dummy peaks
    plot_peaks([(100, 50), (200, 87), (345, 20)])
    pylab.savefig('peaks.png')

# Wait for the user to continue (exiting the script closes all figures)
    raw_input('Press [Enter] to finish')
