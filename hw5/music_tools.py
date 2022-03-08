import os
import sounddevice as sd
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import pandas as pd

def load_df() :
    """
    Loads the training and test dataframes
    containing the metadata of the sound files.  The fields are:
    filename: name of wave file in the wav_data/ folder
    frequency: frequency (in Hz) of note being played
    instrument_family: integer representing type of instrument played
    instrument_family_str: string representing type of instrument played
    pitch: midi number of note played (frequency = 440 * 2**((pitch-69)/12))
    sample_rate: rate at which sound was sampled in Hz (16000 Hz)
    Returns:
    df_train: training data
    df_test: test data
    """
    df = pd.read_csv('scale_data.csv')
    df_train,df_test = df[0:1000],df[1000:]
    return df_train,df_test

def pitch2freq(pitch) :
    """
    Converts pitch (midi number) to frequency (in Hz)
    """
    return 440*2**((pitch-69)/12)

def freq2pitch(freq) :
    """
    Converts (positive) frequency (in Hz) to pitch (midi number)
    """
    return int(round(np.log2(freq/440)*12+69))

def load_signal(filename) :
    """
    Given a filename, loads the corresponding wave file from wav_data and returns it as a numpy array.
    See documentation of soundfile.read for more info.
    Params:
    filename: name of wave file
    Returns:
    signal: 1d float64 numpy array of wave file 
    sampling_rate: rate in Hz that the sound was sampled at
    """
    name = os.path.join('wav_data',filename) if filename.endswith('.wav') else os.path.join('wav_data',filename+'.wav')
    signal,sampling_rate = sf.read(name)
    return signal,sampling_rate

def load_signals(df) :
    """
    Returns a 2d numpy array of all of the signal data in df.
    Params:
    df: dataframe with filename column
    Returns:
    2d numpy array where each row is a signal for the corresponding row in the df
    """
    L = []
    for file in df['filename'] :
        L.append(load_signal(file)[0])
    return np.stack(L,axis=0)
    
def play_signal(signal,sampling_rate) :
    """
    Plays a given signal.
    Params:
    signal: 1d float64 numpy array of signal
    sampling_rate: rate in Hz that the sound was sampled at
    """
    sd.play(0.25*signal,sampling_rate,blocking = True)

def play_file(filename) :
    """
    Plays a given signal given in a file.
    Params:
    filename: filename containing audio signal
    """
    play_signal(*load_signal(filename))
    
    
def main() :
    df = load_df()
    print(df.head())
    print(df.iloc[0])
    a = load_signals(df)
    print(a.shape)
    play_signal(*load_signal(df['filename'][0]))
    play_signal(a[0,:],df['sample_rate'][0])
    
if __name__ == "__main__" :
    main()
