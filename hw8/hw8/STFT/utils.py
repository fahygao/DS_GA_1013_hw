nperseg = 512
window_size = 5


import urllib.request
import tarfile

import os
import glob

import numpy as np
from scipy.io import wavfile

from scipy import signal
from copy import deepcopy

def download_and_extract_data(url):
    ftpstream = urllib.request.urlopen(url)
    thetarfile = tarfile.open(fileobj=ftpstream, mode="r|gz")
    thetarfile.extractall()
    
    
def get_data(path_to_sound_data):
    
    def perform_stft_and_inverse(source, nperseg, fs):
        source_stft = signal.stft(source, fs = fs, nperseg=nperseg);
        _, source_istft =  signal.istft(source_stft[2], fs=fs, nperseg=nperseg);
        return np.real(source_istft)
    
    def get_sound_array(file_path_array, nperseg, fixed_max = None):
        sound_array = [None]*len(file_path_array);
        fs_array = [None]*len(file_path_array);
        max_array = [None]*len(file_path_array);
        for i, x in enumerate(file_path_array):
            fs, data = wavfile.read(x);
            sound_array[i] = perform_stft_and_inverse( data.astype(float), nperseg, fs);

            if fixed_max is None:
                max_array[i] = np.max(np.abs(sound_array[i]))
            else:
                max_array[i] = fixed_max;

            sound_array[i] = sound_array[i]/max_array[i]

            fs_array[i] = fs
        return sound_array, fs_array, max_array
    
    n_val = 5
    files_source = glob.glob(os.path.join(path_to_sound_data, '*.wav'))
    files_source = np.sort(files_source)
    list_val_images = files_source[-n_val:]
    list_train_images = list( set(files_source) - set(list_val_images));
    
    train_dataset, train_fs_array, train_max_array = get_sound_array(list_train_images, nperseg)
    val_dataset, val_fs_array, val_max_array = get_sound_array(list_val_images, nperseg)

    return train_dataset, train_fs_array, train_max_array, val_dataset, val_fs_array, val_max_array
