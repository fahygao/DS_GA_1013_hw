from music_tools import *
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

def main() :
    df_train,df_test = load_df()
    print(df_train.head())
    print("Number of training examples: %d"%len(df_train))
    print("Number of test examples: %d"%len(df_test))
    sigs_train,sigs_test = load_signals(df_train),load_signals(df_test)
    y_train,y_test = df_train['pitch'].values,df_test['pitch'].values
    all_pitches = sorted({p for p in y_train})
    print('Pitches:',pitches)
    print({s for s in df_train['instrument_family_str']})

    #model = LogisticRegression(multi_class='multinomial',solver='lbfgs')

if __name__ == "__main__" :
    main()
