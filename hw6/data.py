import numpy as np
import matplotlib.pyplot as plt

"""
Returns a tuple (small,med,large).  Each element of the tuple
is a 1-dimensional numpy array containing the samples
[f(0/N),...,f((N-1)/N)] where N is the length of the corresponding array.
"""
def load_data() :
    small = np.loadtxt('data2049.txt').view(complex)
    med = np.loadtxt('data4097.txt').view(complex)
    large = np.loadtxt('data8193.txt').view(complex)
    return small,med,large

def main() :
    s,m,l = load_data()

if __name__ == "__main__" :
    main()
