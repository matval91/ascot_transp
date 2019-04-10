"""
tool to compare the ionization of transp and ascot
"""
import pytransp.classes.transp_deposition as td
import a4py.classes.particles as ascot_particles
import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
from utils.plot_utils import _plot_RZsurf, limit_labels, common_style
from mpl_toolkits.mplot3d import Axes3D
common_style()


tr_fname='/mnt/N41a/home/vallar/tr_client/TCV/58823/58823O03_birth.cdf2'
as_fname='/home/vallar/ASCOT/runs/TCV/58823/ascot_58823091.h5'
time=0.9

tr_obj = td.absorption(tr_fname)
as_obj = ascot_particles.TCV_iniend(as_fname)
npart=2000
rt=tr_obj.data_i['R'][0:npart]
zt=tr_obj.data_i['z'][0:npart]
phit = tr_obj.data_i['phi'][0:npart]
xt = np.multiply(rt, np.cos(phit))
yt = np.multiply(rt, np.sin(phit))

ra=as_obj.data_i['R'][0:npart]
za=as_obj.data_i['z'][0:npart]
phia = as_obj.data_i['phi'][0:npart]
xa = np.multiply(ra, np.cos(phia))
ya = np.multiply(ra, np.sin(phia))
if 1>2:
    f=plt.figure(figsize=(6,10)); ax=f.add_subplot(111)
    ax.scatter(rt, zt, s=20, marker='.', color='r', label='NUBEAM')
    ax.scatter(ra, za, s=20, marker='.', color='b', label='ASCOT')
    _plot_RZsurf(as_obj.Rsurf, as_obj.zsurf, as_obj.RZsurf, ax)
    ax.plot(as_obj.R_w, as_obj.z_w, lw=2.3, color='k')
    limit_labels(ax, r'R [m]', r'Z [m]')
    ax.axis('equal')
    ax.legend(loc='lower center', scatterpoints=1)
    f.tight_layout()

    f=plt.figure(); ax=f.add_subplot(111)
    ax.scatter(xt, yt, s=20, marker='.', color='r', label='NUBEAM')
    ax.scatter(xa, ya, s=20, marker='.', color='b', label='ASCOT')
    circle1 = plt.Circle((0, 0), as_obj.R0, color='k', fill=False, linestyle='--')      
    ax.add_artist(circle1)
    circle1 = plt.Circle((0, 0), min(as_obj.R_w), lw=2.3, color='k', fill=False, linestyle='-')      
    ax.add_artist(circle1)
    circle1 = plt.Circle((0, 0), max(as_obj.R_w), lw=2.3, color='k', fill=False, linestyle='-')      
    ax.add_artist(circle1)
    ax.legend(loc='lower right', scatterpoints=1); ax.axis('equal')
    limit_labels(ax, r'X [m]', r'Y [m]')
    f.tight_layout()
    
    f3d=plt.figure(figsize=(15,9))
    ax3d = f3d.add_subplot(111, projection='3d')
    phi_tt = np.arange(0.*np.pi,2.02*np.pi,0.02*np.pi)
    z_tok = as_obj.z_w
    x_tok = np.zeros((len(phi_tt),len(as_obj.R_w)),dtype=float)
    y_tok = np.zeros((len(phi_tt),len(as_obj.R_w)),dtype=float)
    for i,R in enumerate(as_obj.R_w):
        x_tok[:,i] = R*np.cos(phi_tt)
        y_tok[:,i] = R*np.sin(phi_tt)
    ax3d.plot_surface(x_tok,y_tok,z_tok,color='k',alpha=0.15)
    ax3d.scatter(xt,yt,zs=zt, color='r', marker='.', s=20, label=r'NUBEAM')
    ax3d.scatter(xa,ya,zs=za, color='b', marker='.', s=20, label=r'ASCOT')
    ax3d.legend(loc='upper left', scatterpoints=1)
    ax3d.xaxis.labelpad=30
    ax3d.yaxis.labelpad=30
    ax3d.zaxis.labelpad=30
    M=5
    yticks = ticker.MaxNLocator(M)
    xticks = ticker.MaxNLocator(M)
    # tick positions with set_minor_locator.
    ax3d.yaxis.set_major_locator(yticks)
    #ax.yaxis.set_minor_locator(yticks_m)
    ax3d.xaxis.set_major_locator(xticks)
    ax3d.set_xlabel(r'X [m]'); ax3d.set_ylabel(r'Y [m]'); ax3d.set_zlabel(r'Z [m]')
    
    f3d.tight_layout()

f=plt.figure(); ax=f.add_subplot(111)
ax.hist(tr_obj.data_i['R'], bins=20, normed=True, color='r', fill=False, histtype='step', label='NUBEAM', lw=2.3)
ax.hist(as_obj.data_i['R'], bins=20, normed=True, color='k', fill=False, histtype='step', label='ASCOT', lw=2.3)
limit_labels(ax, r'R [m]', r'Marker density')
ax.axvline(0.88, lw=2.3, color='k', linestyle='--')
ax.legend(loc='upper left')
f.tight_layout()

f=plt.figure(); ax=f.add_subplot(111)
ax.hist(tr_obj.data_i['z'], bins=20, normed=True, color='r', fill=False, histtype='step', label='NUBEAM', lw=2.3)
ax.hist(as_obj.data_i['z'], bins=20, normed=True, color='k', fill=False, histtype='step', label='ASCOT', lw=2.3)
limit_labels(ax, r'z [m]', r'Marker density')
ax.legend(loc='upper left')
f.tight_layout()

plt.show()
