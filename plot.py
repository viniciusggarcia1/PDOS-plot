import numpy as np
from matplotlib import pyplot as plt
Ep, zdos1, xdos1, ydos1 = np.loadtxt('total_pxyz.dat', unpack=True, usecols=(0,1,2,3))
tot= np.loadtxt('hetero-pdos.pdos_tot', unpack=True, usecols=(2))
doss= np.loadtxt('total_s.dat', unpack=True, usecols=(1))
doss2= np.loadtxt('total_s2.dat', unpack=True, usecols=(1))


tot3=np.zeros(len(Ep))
for i in range(0, len(Ep)):
	tot3[i]=zdos1[i]+xdos1[i]+ydos1[i]+doss[i]


plt.plot(Ep, doss, color='orange', lw=1, zorder=1, label='s')
plt.plot(Ep, xdos1, color='red', lw=1, zorder=1, label='$p_x$')
plt.plot(Ep, ydos1, color='blue', lw=1, zorder=1, label='$p_y$')
plt.plot(Ep, zdos1, color='green', lw=1, zorder=1, label='$p_z$')
plt.plot(Ep, tot3, color='black', lw=1, zorder=1, label='Total')

# Add legend
plt.legend()

# Add labels and title
plt.xlabel('$E$-$E_F$ (eV)', fontsize=16)
plt.ylabel('DOS (States/eV)', fontsize=16)
plt.ylim(bottom=0)
plt.xlim(-6.5, 3)
plt.axvline(0, linestyle='dashed', color='gray')
#plt.title('')
plt.tight_layout()
#plt.show()
plt.savefig('graph.png', dpi=800)
