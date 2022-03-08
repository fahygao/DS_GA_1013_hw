import numpy as np
import matplotlib.pyplot as plt
import scipy.io

"""
Implements the Haar wavelet function (psi) at scale 2**s, position p.
Arguments:
s: the scale of the wavelet is 2**s
p: the position of the wavelet
n: the length of the returned vector is 2**n
Returns:
A numpy array of length 2**n containing the Haar wavelet with
scale 2**s at position p.
"""
def wavelet(s,p,n) :
    return None #Your code here
    
"""
Implements the Haar scaling function (phi) at scale 2**s, position p.
Arguments:
s: the scale of the scaling function is 2**s
p: the position of the scaling function
n: the length of the returned vector is 2**n
Returns:
A numpy array of length 2**n containing the Haar scaling function with
scale 2**s at position p.
"""
def scaling(s,p,n) :
    return None #Your code here

"""
Orthogonally projects the vector x onto the subspace V_k of vectors
that are constant on patches of length 2**k.
Arguments:
x: numpy array of data (of length 2**n for some n)
k: 0 <= k <= n
n: x has length 2**n
Returns:
A numpy array of length 2**n containing the orthogonal projection of x onto V_k.
"""
def projectV(x,k,n) :
    return None #Your code here

"""
Orthogonally projects the vector x onto the subspace W_k of Haar wavelets of scale 2**k.
Arguments:
x: numpy array of data (of length 2**n for some n)
k: 1 <= k <= n
n: x has length 2**n
Returns:
A numpy array of length 2**n containing the orthogonal projection of x onto W_k.
"""
def projectW(x,k,n) :
    return None #Your code here

"""
Computes the wavelet coefficients of x at scale 2**s.
Arguments:
x: numpy array of data (of length 2**n for some n)
s: 1 <= s <= n
n: x has length 2**n
Returns:
A numpy array of length 2**(n-s) containing the wavelet coefficents 
at scale 2**s in positions p=0,1,...
"""
def wavelet_coeffs(x,s,n) :
    return None #Your code here

def projectWavelet(w,s,n) :
    ws = []
    for p in range(len(w)):
        ws.append(wavelet(s,p,n))
    return np.dot(np.array(ws).T,w)
    

def plot_psiphi(s,n) :
    fig,axes = plt.subplots(2**(n-s),2)
    for p in range(len(axes)) :
        wax,sax = axes[p,0],axes[p,1]
        wax.stem(range(2**n),wavelet(s,p,n))
        wax.margins(.1,.1)
        sax.stem(range(2**n),scaling(s,p,n))
        sax.margins(.1,.1)
        wax.set_ylabel('p=%d'%p)
    axes[0,0].set_title('$\psi_{2^s,p}$')
    axes[0,1].set_title('$\phi_{2^s,p}$')
    fig.suptitle('$n=2^%d$, $s=%d$'%(n,s))
    plt.savefig('psiphiplot_%d_%d.pdf'%(s,n),bbox_inches='tight')
    plt.close()

def plot_downsampling(x,m,n) :
    fig,axes = plt.subplots(m-1,2)
    for k in range(1,m) :
        vax = axes[k-1,0]
        wax = axes[k-1,1]
        vax.plot(projectV(x.copy(),k,n))
        vax.margins(.1,.1)
        vax.set_ylabel('k=%d'%k)
        wax.plot(projectW(x.copy(),k,n))
        wax.margins(.1,.1)
    axes[0,0].set_title('$V_k$')
    axes[0,1].set_title('$W_k$')
    fig.suptitle('ECG Data Projected onto $V_k,W_k$')
    plt.savefig('ecg_project.pdf',bbox_inches='tight')
    plt.close()

def plot_wavelet(x,m,n) :
    fig,axes = plt.subplots(m-1,2)
    for k in range(1,m) :
        ax = axes[k-1,0]
        wax = axes[k-1,1]
        w = wavelet_coeffs(x.copy(),k,n)
        ax.stem(w)
        ax.margins(.1,.1)
        ax.set_ylabel('k=%d'%k)
        wax.plot(projectWavelet(w,k,n))
        wax.margins(.1,.1)
    axes[0,0].set_title('Wavelet Coeffs')
    axes[0,1].set_title('$W_k$')
    fig.suptitle('Wavelet Coeffs and Projection')
    plt.savefig('ecg_wavelet.pdf',bbox_inches='tight')
    plt.close()
    
def main() :
    plot_psiphi(1,3)
    plot_psiphi(2,3)
    n = 10
    ecg = scipy.io.loadmat('ecg.mat')['ecg'][0:2**n,0]
    plt.plot(ecg)
    plt.title('ECG Plot')
    plt.savefig('ecg.pdf',bbox_inches='tight')
    plt.close()
    m = 5
    plot_downsampling(ecg,m,n)
    plot_wavelet(ecg,m,n)
    
    
if __name__ == "__main__" :
    main()
