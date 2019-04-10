"""
tool to compare the distribution function of transp and ascot
"""
import transp_fbm
import a4py.classes.distributions_2d as ascot_distributions
import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
from utils.plot_utils import _plot_RZsurf, limit_labels, common_style
from mpl_toolkits.mplot3d import Axes3D
common_style()


tr_fname='/home/vallar/TCV/58823/58823V77_fi_1.cdf'
as_fname='/home/vallar/ASCOT/runs/TCV/58823/ascot_58823091.h5'
as_fname='/mnt/N41a/home/vallar/ASCOT/runs/TCV/58823/09/ascot.h5'
time=0.9

#tr_fname='/mnt/N41a/home/vallar/tr_client/TCV/58823/58823O02_fi_6.cdf'
#as_fname='/home/vallar/ASCOT/runs/TCV/58823/run/ascot.h5'
#time=1.25

tr_obj = transp_fbm.fbm(tr_fname)
as_obj = ascot_distributions.frzpe(as_fname)

Et=tr_obj.dict_dim['E']
xit=tr_obj.dict_dim['pitch']
tr_obj._integrate_spacep()
fEt = tr_obj.f_spacep_int

Ea=as_obj.dict_dim['E']/1.602e-19
xia=as_obj.dict_dim['pitch']
as_obj._integrate_spacep()
fEa = as_obj.f_spacep_int*1.602e-19

if 1<2:
    f=plt.figure(); ax=f.add_subplot(111)
    ax.plot(Et*1e-3, fEt, lw=2.3, color='r', label='NUBEAM')
    ax.plot(Ea*1e-3, fEa, lw=2.3, color='k', label='ASCOT')
    ax.set_xlim([0,25])
    limit_labels(ax, r'E [keV]', r'f [1/keV]')
    ax.legend(loc='upper right')
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
