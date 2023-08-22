import numpy as np
from matplotlib import pyplot as plt

def graph_spdf (E, ldos, legd, marker, x):
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
    plt.xlim(x)
    plt.axvline(0, linestyle='dashed', color='gray')

def sum_spdf (spdf, qt_orb_p ,ldosS2, ltotx, ltoty, ltotz, qt_orb_d,
                                   dz2Dtot, dzxDtot, dzyDtot, dx2_y2Dtot, dxyDtot):
    ltot=0
    if 's' in spdf:
        ltot=ltot+ldosS2
        
    if 'px' in qt_orb_p:
        ltot=ltot+ltotx

    if 'py' in qt_orb_p:
        ltot=ltot+ltoty

    if 'pz' in qt_orb_p:
        ltot=ltot+ltotz
    
    if 'dz2' in (qt_orb_d):
        ltot=ltot+dz2Dtot

    if 'dzx' in (qt_orb_d):
        ltot=ltot+dzxDtot

    if 'dzy' in (qt_orb_d):
        ltot=ltot+dzyDtot

    if 'dx2-y2' in (qt_orb_d):
        ltot=ltot+dx2_y2Dtot

    if 'dxy' in (qt_orb_d):
        ltot=ltot+dxyDtot

    return ltot
