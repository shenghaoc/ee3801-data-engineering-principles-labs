# 4j NEED TO WRITE AND SUBMIT
import numpy as np
import matplotlib.pyplot as plt
from neo.io import BlackrockIO

# 4c
reader = BlackrockIO('181105_Block1.ns5')
bl = reader.read_block(lazy = True)

# 4e
data = np.array(bl.segments[0].analogsignals[1].load(time_slice=None, channel_indexes=[2]))

# 4f
sr = float(bl.segments[0].analogsignals[1].sampling_rate)

# 4g
reader = BlackrockIO('181105_Block1.nev')
ev_rawtimes, _, ev_markers = reader.get_event_timestamps()

plt.figure()
dataind = np.arange(0, 500000)
data=data[dataind]
plt.plot(dataind/sr, data)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (uV)')

yl = plt.ylim()
t2 = [ev_rawtimes[2], ev_rawtimes[4], ev_rawtimes[6]]
pt2 = np.kron(np.ones((2,1)),t2)
py2 = np.kron(np.ones((np.size(pt2,1),1)),yl).transpose()
plt.plot(pt2/sr,py2)
plt.show()
