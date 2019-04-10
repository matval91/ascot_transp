"""
tool to compare the ionization of transp and ascot
"""
import transp_output
import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
from ascot_utils import _plot_RZsurf, limit_labels, common_style
from mpl_toolkits.mplot3d import Axes3D
common_style()


tr_fname1='/mnt/N41a/home/vallar/tr_client/TCV/58823/58823O02_fi_2.cdf'
time1=0.9
tr_fname2='/mnt/N41a/home/vallar/tr_client/TCV/58823/58823O02_fi_6.cdf'
time2=1.25

tr_obj1 = transp_output.fbm(tr_fname1)
tr_obj2 = transp_output.fbm(tr_fname2)

E1=tr_obj1.dict_dim['E']
xi1=tr_obj1.dict_dim['pitch']
tr_obj1._integrate_spacep()
tr_obj1._integrate_spaceE()
fE1 = tr_obj1.f_spacep_int
fxi1 = tr_obj1.f_spaceE_int

E2=tr_obj2.dict_dim['E']
xi2=tr_obj2.dict_dim['pitch']
tr_obj2._integrate_spacep()
tr_obj2._integrate_spaceE()
fE2 = tr_obj2.f_spacep_int
fxi2 = tr_obj2.f_spaceE_int
delta=fxi2-fxi1
if 1<2:
    f=plt.figure(); ax=f.add_subplot(111)
    ax.plot(E1*1e-3, fE1, 'k', lw=2.3,  label='No EC')
    ax.plot(E2*1e-3, fE2, 'k--', lw=2.3,  label='EC')
    ax.set_xlim([0,25])
    limit_labels(ax, r'E [keV]', r'f [1/keV]')
    ax.legend(loc='upper right')
    f.tight_layout()

    f=plt.figure(); ax=f.add_subplot(111)
    ax2 = ax.twinx()
    ax.plot(xi1, fxi1, 'k', lw=2.3,  label='No EC')
    ax.plot(xi2, fxi2, 'k--', lw=2.3,  label='EC')

    ax2.plot(xi2, delta*1e-17, 'r:', lw=2.3)
    ax2.set_ylabel(r'$\Delta/10^{17}$', color='r')
    ax2.plot(xi2, np.zeros(len(xi2)), 'r-')
    ax2.tick_params('y', colors='r')
    ax.set_xlim([-1., 1.])
    limit_labels(ax, r'$\xi=v_\parallel/v$', r'f')
    ax.legend(loc='center left')
    f.tight_layout()
#    f=plt.figure(); ax=f.add_subplot(111)
#    ax.scatter(xt, yt, s=20, marker='.', color='r', label='NUBEAM')
#    ax.scatter(xa, ya, s=20, marker='.', color='b', label='ASCOT')
#    circle1 = plt.Circle((0, 0), as_obj.R0, color='k', fill=False, linestyle='--')      
#    ax.add_artist(circle1)
#    circle1 = plt.Circle((0, 0), min(as_obj.R_w), lw=2.3, color='k', fill=False, linestyle='-')      
#    ax.add_artist(circle1)
#    circle1 = plt.Circle((0, 0), max(as_obj.R_w), lw=2.3, color='k', fill=False, linestyle='-')      
#    ax.add_artist(circle1)
#    ax.legend(loc='lower right', scatterpoints=1); ax.axis('equal')
#    limit_labels(ax, r'X [m]', r'Y [m]')
#    f.tight_layout()

plt.show()
