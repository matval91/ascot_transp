"""
tool to compare the 1d quantities of transp and ascot
"""
import transp_output
import a4py.classes.distributions as ascot_distributions
import a4py.classes.prof as ascot_prof
import matplotlib.pyplot as plt
import numpy as np
from utils.plot_utils import limit_labels, common_style
common_style()


tr_fname='/home/vallar/TCV/58823/58823V77.CDF' #this one is without cx
as_fname='/home/vallar/ASCOT/runs/TCV/58823/ascot_58823091.h5'
as_fname='/home/vallar/ASCOT/runs/TCV/58823/09/ascot.h5'

time=0.9

#as_fname='/home/vallar/ASCOT/runs/TCV/58823/ascot_58823251.h5'
#time=1.25

prof_ascot = ascot_prof.h5_profiles(as_fname, 51)
tr_obj = transp_output.output_1d(tr_fname)
as_obj = ascot_distributions.TCV_1d(as_fname)
# #Converting ascot poloidal rho to toroidal rho
# psi_poloidal = as_obj.infile['/boozer/psi'][:]
# psi_poloidal = np.flipud(psi_poloidal)
# q = np.abs(as_obj.infile['/boozer/qprof'][:])
# q=np.flipud(q)
# psi_t = np.zeros(len(q))
# rho_t = np.copy(psi_t)
# for i in range(len(psi_poloidal)):
#     psi_t[i] = np.trapz(q[0:i], psi_poloidal[0:i])
# psi_t = psi_t/np.max(psi_t)
# rho_t = np.sqrt(psi_t)    


ind_transp = np.argmin(tr_obj.t-time<0.)
#Converting transp toroidal rho to poloidal rho
rho_toroidal = tr_obj.file.variables['X'][ind_transp,:]
psi_toroidal = rho_toroidal**2
q = tr_obj.file.variables['Q'][ind_transp,:]

psi_p = np.zeros(len(q))
rho_p = np.copy(psi_p)
for i in range(len(psi_toroidal)):
    psi_p[i] = np.trapz(1./q[0:i], psi_toroidal[0:i])
psi_p = psi_p/np.max(psi_p)
rho_p = np.sqrt(psi_p)    

xtr=rho_p

f=plt.figure(); ax=f.add_subplot(111)
ax.plot(xtr, tr_obj.file.variables['NE'][ind_transp,:]*1e6, lw=2.3, color='r', label='NUBEAM')
ax.plot(prof_ascot.rho, prof_ascot.ne, lw=2.3, color='b', label='ASCOT')
limit_labels(ax, r'$\rho$', r'ne')
ax.legend(loc='upper right')
f.tight_layout()

f=plt.figure(); ax=f.add_subplot(111)
ax.plot(xtr, tr_obj.file.variables['TE'][ind_transp,:], lw=2.3, color='r', label='NUBEAM')
ax.plot(prof_ascot.rho, prof_ascot.te, lw=2.3, color='b', label='ASCOT')
#as_obj.plot_pe(ax=ax)
#ax.plot(xas, as_obj.pe, lw=2.3, color='k', label='ASCOT')
limit_labels(ax, r'$\rho$', r'te')
ax.legend(loc='upper right')
f.tight_layout()

f=plt.figure(); ax=f.add_subplot(111)
ax.plot(xtr, tr_obj.file.variables['NI'][ind_transp,:]*1e6, lw=2.3, color='r', label='NUBEAM')
ax.plot(prof_ascot.rho, np.sum(prof_ascot.ni[:,:], axis=0), lw=2.3, color='b', label='ASCOT')
#as_obj.plot_pe(ax=ax)
#ax.plot(xas, as_obj.pe, lw=2.3, color='k', label='ASCOT')
limit_labels(ax, r'$\rho$', r'ni')
ax.legend(loc='upper right')
f.tight_layout()

f=plt.figure(); ax=f.add_subplot(111)
ax.plot(xtr, tr_obj.file.variables['TI'][ind_transp,:], lw=2.3, color='r', label='NUBEAM')
ax.plot(prof_ascot.rho, prof_ascot.ti, lw=2.3, color='b', label='ASCOT')
#as_obj.plot_pe(ax=ax)
#ax.plot(xas, as_obj.pe, lw=2.3, color='k', label='ASCOT')
limit_labels(ax, r'$\rho$', r'ti')
ax.legend(loc='upper right')
f.tight_layout()

if 1<2:
    f=plt.figure(); ax=f.add_subplot(111)
    ax.plot(xtr, tr_obj.nb_FKP_vars['pe'][ind_transp,:]*1e-3, lw=2.3, color='r', label='NUBEAM')
    # nlines, lines, labels = as_obj._plot_pe()
    #plot_article(nlines, lines, labels, r'$\rho$', 'P_e (kW/$m^3$)', ax=ax)
    as_obj.plot_pe(ax=ax)
    ll=ax.lines[1]
    ll.set_label(r'ASCOT'); ll.set_ls('-')
#ax.plot(xas, as_obj.pe, lw=2.3, color='k', label='ASCOT')
    limit_labels(ax, r'$\rho$', r'P$_e$ [kW/m$^3$]')
    ax.legend(loc='upper right', fontsize='medium')
    f.tight_layout()

    f=plt.figure(); ax=f.add_subplot(111)
    ax.plot(xtr, tr_obj.nb_FKP_vars['pi'][ind_transp,:]*1e-3, lw=2.3, color='r', label='NUBEAM')
    as_obj.plot_pi_total(ax=ax)
    ll=ax.lines[1]
    ll.set_label(r'ASCOT'); ll.set_ls('-')
    #ax.plot(xas, as_obj.pe, lw=2.3, color='k', label='ASCOT')
    limit_labels(ax, r'$\rho$', r'P$_i$ [kW/m$^3$]')
    ax.legend(loc='upper right', fontsize='medium')
    f.tight_layout()

    f=plt.figure(); ax=f.add_subplot(111)
    ax.plot(xtr, (tr_obj.nb_FKP_vars['pi'][ind_transp,:]+tr_obj.nb_FKP_vars['pe'][ind_transp,:])*1e-3, lw=2.3, color='r', label='NUBEAM')
    as_obj.plot_totalpower(ax=ax)
    ll=ax.lines[1]
    ll.set_label(r'ASCOT'); ll.set_ls('-')
    #ax.plot(xas, as_obj.pe, lw=2.3, color='k', label='ASCOT')
    limit_labels(ax, r'$\rho$', r'P$_{TOT}$ [kW/m$^3$]')
    ax.legend(loc='upper right', fontsize='medium')
    f.tight_layout()

    f=plt.figure(); ax=f.add_subplot(111)
    ax.plot(xtr, tr_obj.nb_FKP_vars['nbcd'][ind_transp,:]*1e-3, lw=2.3, color='r', label='NUBEAM')
    as_obj.plot_current(ax=ax)
    ll=ax.lines[1]
    ll.set_label(r'ASCOT'); ll.set_ls('-')
    #ax.plot(xas, as_obj.pe, lw=2.3, color='k', label='ASCOT')
    limit_labels(ax, r'$\rho$', r'j [kA/m$^2$]')
    ax.legend(loc='upper right', fontsize='medium')
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
