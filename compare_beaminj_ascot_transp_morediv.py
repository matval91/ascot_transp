"""
tool to compare the ionization of transp and ascot
"""
import transp_deposition
import ascot_particles
import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
from ascot_utils import _plot_RZsurf, limit_labels, common_style
from mpl_toolkits.mplot3d import Axes3D
common_style()


tr_fname='/mnt/N41a/home/vallar/tr_client/TCV/58823/58823O03_birth.cdf2'
as_fname22='/home/vallar/ASCOT/runs/TCV/run_58823_thesis/900_22mrad/bbnbi.h5'
as_fname08='/home/vallar/ASCOT/runs/TCV/run_58823_thesis/900_08mrad/bbnbi.h5'
as_fname36='/home/vallar/ASCOT/runs/TCV/run_58823_thesis/900_36mrad/bbnbi.h5'
as_fname17='/home/vallar/ASCOT/runs/TCV/run_58823_thesis/900/bbnbi.h5'
as_fname05='/home/vallar/ASCOT/runs/TCV/run_58823_thesis/900_05mrad/bbnbi.h5'
as_fname22d5='/home/vallar/ASCOT/runs/TCV/run_58823_thesis/900_22d5mrad/bbnbi.h5'

time=0.9

tr_obj = transp_deposition.absorption(tr_fname)
npart=20000
rt=tr_obj.data_i['R'][0:npart]
zt=tr_obj.data_i['z'][0:npart]
phit = tr_obj.data_i['phi'][0:npart]
xt = np.multiply(rt, np.cos(phit))
yt = np.multiply(rt, np.sin(phit))

as_obj22 = ascot_particles.TCV_iniend(as_fname22)
ra22=as_obj22.data_i['Rprt'][0:npart]
za22=as_obj22.data_i['zprt'][0:npart]
phia22 = as_obj22.data_i['phiprt'][0:npart]
xa22 = np.multiply(ra22, np.cos(phia22))
ya22 = np.multiply(ra22, np.sin(phia22))

as_obj08 = ascot_particles.TCV_iniend(as_fname08)
ra08=as_obj08.data_i['Rprt'][0:npart]
za08=as_obj08.data_i['zprt'][0:npart]
phia08 = as_obj08.data_i['phiprt'][0:npart]
xa08 = np.multiply(ra08, np.cos(phia08))
ya08 = np.multiply(ra08, np.sin(phia08))

as_obj36 = ascot_particles.TCV_iniend(as_fname36)
ra36=as_obj36.data_i['Rprt'][0:npart]
za36=as_obj36.data_i['zprt'][0:npart]
phia36 = as_obj36.data_i['phiprt'][0:npart]
xa36 = np.multiply(ra36, np.cos(phia36))
ya36 = np.multiply(ra36, np.sin(phia36))

as_obj36 = ascot_particles.TCV_iniend(as_fname36)
ra36=as_obj36.data_i['Rprt'][0:npart]
za36=as_obj36.data_i['zprt'][0:npart]
phia36 = as_obj36.data_i['phiprt'][0:npart]
xa36 = np.multiply(ra36, np.cos(phia36))
ya36 = np.multiply(ra36, np.sin(phia36))

as_obj22d5 = ascot_particles.TCV_iniend(as_fname22d5)
ra22d5=as_obj22d5.data_i['Rprt'][0:npart]
za22d5=as_obj22d5.data_i['zprt'][0:npart]
phia22d5 = as_obj22d5.data_i['phiprt'][0:npart]
xa22d5 = np.multiply(ra22d5, np.cos(phia22d5))
ya22d5 = np.multiply(ra22d5, np.sin(phia22d5))

as_obj05 = ascot_particles.TCV_iniend(as_fname05)
ra05=as_obj05.data_i['Rprt'][0:npart]
za05=as_obj05.data_i['zprt'][0:npart]
phia05 = as_obj05.data_i['phiprt'][0:npart]
xa05 = np.multiply(ra05, np.cos(phia05))
ya05 = np.multiply(ra05, np.sin(phia05))

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
ax.hist(tr_obj.data_i['R'], bins=20, normed=True, color='k', fill=False, histtype='step', label='NUBEAM', lw=2.3)
#ax.hist(ra22, bins=20, normed=True, color='r', fill=False, histtype='step', label='ASCOT 22 mrad', lw=2.3)
#ax.hist(ra08, bins=20, normed=True, color='b', fill=False, histtype='step', label='ASCOT 08 mrad', lw=1.8)
#ax.hist(ra36, bins=20, normed=True, color='g', fill=False, histtype='step', label='ASCOT 36 mrad', lw=1.8)
ax.hist(ra22d5, bins=20, normed=True, color='r', fill=False, histtype='step', label='ASCOT 22.5 mrad', lw=1.8)
ax.hist(ra05, bins=20, normed=True, color='g', fill=False, histtype='step', label='ASCOT 05 mrad', lw=1.8)
ax.set_xlim([0.6, 1.3])
limit_labels(ax, r'R [m]', r'Marker density')
ax.axvline(0.88, lw=2.3, color='k', linestyle='--')
ax.legend(loc='upper right', fontsize='medium')
f.tight_layout()

f=plt.figure(); ax=f.add_subplot(111)
ax.hist(tr_obj.data_i['z'], bins=20, normed=True, color='k', fill=False, histtype='step', label='NUBEAM', lw=2.3)
ax.hist(za22, bins=20, normed=True, color='r', fill=False, histtype='step', label='ASCOT 22 mrad', lw=2.3)
ax.hist(za08, bins=20, normed=True, color='b', fill=False, histtype='step', label='ASCOT 08 mrad', lw=1.8)
ax.hist(za36, bins=20, normed=True, color='g', fill=False, histtype='step', label='ASCOT 36 mrad', lw=1.8)
#ax.hist(za22d5, bins=20, normed=True, color='r', fill=False, histtype='step', label='ASCOT 22.5 mrad', lw=1.8)
#ax.hist(za05, bins=20, normed=True, color='g', fill=False, histtype='step', label='ASCOT 05 mrad', lw=1.8)

limit_labels(ax, r'z [m]', r'Marker density')
ax.legend(loc='upper right', fontsize='medium')
f.tight_layout()

plt.show()
