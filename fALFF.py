import nilearn
from scipy import signal
import numpy as np

def create_falff(time_series):
    #Clean data using bandpass filtering Butterworth from Nilearn
    time_series_cleaned = nilearn.signal.clean(time_series.T, sessions=None, detrend=True,
                                               standardize=None, confounds=None,
                                               low_pass=0.25, high_pass=0.01, t_r=2.0,
                                               ensure_finite=True)

    #Compute power spectra
    freqs_cleaned, psd_cleaned = signal.welch(time_series_cleaned, fs=0.5, window='boxcar',
                                              nperseg=None, noverlap=None, nfft=168,
                                              detrend='constant', return_onesided=False,
                                              scaling='spectrum', axis=-1, average='mean')

    #Compute fALFF
    fALFF_container = []
    for row in psd_cleaned:
        low_freq = row[(freqs_cleaned>=0) & (freqs_cleaned<=0.08)]
        sum_low_freq = np.sum(low_freq)
        all_freq = row[(freqs_cleaned>=0) & (freqs_cleaned<=0.25)]
        sum_all_freq = np.sum(all_freq)
        fALFF=sum_low_freq/sum_all_freq

        fALFF_container.append(fALFF)


    return fALFF_container
