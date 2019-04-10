import numpy as np
import matplotlib.pyplot as plt
from ascot_utils import common_style
ptot_ascot = 530
st = (1-(530/600))*100.
ol = 94.21/ptot_ascot*100.
pabs = 100.-st-ol
common_style()
ascot_data = [st, pabs, 0, ol]
nubeam_data = [10, 67, 8, 15]
labels = 'S.T.', 'P. Abs.', 'C.X.', 'O.L.'
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# Plot
f=plt.figure(); ax1=f.add_subplot(111)
ax1.pie(ascot_data, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
f=plt.figure(); ax2=f.add_subplot(111)
ax2.pie(nubeam_data, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal'); ax2.axis('equal')

plt.show()
