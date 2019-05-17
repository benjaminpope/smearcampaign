# publication quality plot

import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd
import matplotlib as mpl 
mpl.rcParams['font.size']=22               #10 
mpl.rcParams["font.family"] = "Times New Roman"

file = "HD_183124_smear_combined.clip.ts.fft"  # best one

data1 =  np.genfromtxt(file, names=True)
freq = data1['fre']
power = data1['power']

f, (ax1, ax2) = plt.subplots(1,2, gridspec_kw = {'width_ratios':[3,1]}, figsize=(16,9))

ax1.plot(freq, power, color='black')
#ax1.title(file)
ax1.set_xlabel('Frequency ($\mu$Hz)')
ax1.set_ylabel('Power density (ppm$^2/\mu$Hz)')
ax1.set_xlim(20,60)
ax1.set_ylim(0,200000)

peaks =  np.genfromtxt(file+'.peaks', comments='#')
ax1.scatter(peaks, 60000 + 0*peaks, marker='o')

radial = np.array([30.7, 34.8, 39.3, 43.6, 47.9])
radial = np.array([26.3, 30.7, 34.8, 39.3, 43.6, 47.9, 52])
for i in range(0, radial.size):
    ax1.plot([radial[i], radial[i]],[0, 1e6], color='black', linestyle='dotted')

period = 1e6/peaks

radial = np.array([30.7, 34.8, 39.3, 43.6, 47.9])


for DP in [300.1]:
#    ax2.figure(figsize=(8/1.5,12/1.5))
    ax2.plot(np.mod(period, DP), peaks, '-o')
    ax2.set_xlim(0,300)
    ax2.set_xlabel('Period mod ' + str(DP) +' (s)')
    ax2.set_ylabel('Frequency ($\mu$Hz)')
    for i in range(0, radial.size):
        ax2.plot([0, 350], [radial[i], radial[i]], color='black', linestyle='dotted')

plt.savefig('../paper/HD_183124.pdf',bbox_inches='tight')
