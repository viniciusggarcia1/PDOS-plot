import numpy as np
from matplotlib import pyplot as plt

def graph_s (E, ldos, legd, marker):
    #Es, ldos = np.loadtxt(file, unpack=True, usecols=(0,1))
    if marker == False:
        plt.plot(E, ldos, lw=2, zorder=1, label=legd)
    if marker == True:
        plt.plot(E, ldos, color='black', lw=2, zorder=1, label='Total')
    

    # Add legend
    plt.legend(loc='upper right')

    # Add labels and title
    plt.xlabel('$E$-$E_F$ (eV)', fontsize=18)
    plt.ylabel('DOS (States/eV)', fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.ylim(bottom=0)
    plt.autoscale(enable=True, axis='both', tight=True)
    #plt.xlim(-10, 1)
    plt.axvline(0, linestyle='dashed', color='gray')

'''   
def graph_p (file, legd):
    Ep, ldos, asd, asd, asd= np.loadtxt(file, unpack=True, usecols=(0,1,2,3,4))

    if sdfdf =dsfsd:
        plt.plot(Ep, ldos, color='blue', lw=2, zorder=1, label=legd)
    else:
        plt.plot(Ep, ldos, color='blue', lw=2, zorder=1, label=legd)
        plt.plot(Ep, asd, color='blue', lw=2, zorder=1, label=legd)
        plt.plot(Ep, asd, color='blue', lw=2, zorder=1, label=legd)
        plt.plot(Ep, asd, color='blue', lw=2, zorder=1, label=legd)
    

    # Add legend
    plt.legend(loc='upper right')

    # Add labels and title
    plt.xlabel('$E$-$E_F$ (eV)', fontsize=18)
    plt.ylabel('DOS (States/eV)', fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.ylim(bottom=0)
    plt.xlim(-10, 1)
    plt.axvline(0, linestyle='dashed', color='gray')

'''