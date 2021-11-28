import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


#Read files
computedPitch = np.loadtxt('rl006.f0')
wavesurferPitch = np.loadtxt('rl006.f0ref')


#Time axis
time = np.zeros(len(computedPitch))
for i in range(len(computedPitch)):
    time[i] = i * 0.015


#Plotting the graph
plt.plot(time, computedPitch,'m', label = 'Computed Pitch')
plt.plot(time, wavesurferPitch,'c', label = 'Wavesurfer Pitch')

plt.xlabel('Time(s)')
plt.ylabel('Frequency(Hz)')
plt.title('Pitch comparison')
plt.legend(loc = 'upper right')
plt.show()  