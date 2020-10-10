import numpy as np
import matplotlib.pyplot as plt
from pyedfread import edf
from neo.io import BlackrockIO

# 2c
pos_data = np.loadtxt("session01/RawData_T1-400/session_1_5112018105323.txt", skiprows=14)

# 3b
samples, events, messages = edf.pread('181105.edf', trial_marker=b'Start Trial')

# 4c
reader = BlackrockIO('session01/181105_Block1.ns5')
bl = reader.read_block(lazy = True)

# 4e
broadband_data = np.array(bl.segments[0].analogsignals[1].load(time_slice=None, channel_indexes=[2]))

# 4f
sr = float(bl.segments[0].analogsignals[1].sampling_rate)

# 4g
reader = BlackrockIO('session01/181105_Block1.nev')
ev_rawtimes, _, ev_markers = reader.get_event_timestamps()

# 2d
uind = np.arange(300)

# 2e
ut = np.cumsum(pos_data[uind,1])

# 3f
esr = int(messages['RECCFG'][0][1])
samples['time'] = samples['time']/esr
events[['start','end']] = events[['start','end']]/esr
messages[['trialid_time','Cue_time','End_time']] = messages[['trialid_time','Cue_time','End_time']]/esr

# 3g
eind = np.arange(15000)
ex = samples['gx_left'][eind]
et = samples['time'][eind]
ex[ex>1920] = np.nan
ex[ex<0] = np.nan

# 4e
broadband_data = np.array(bl.segments[0].analogsignals[1].load(time_slice=None, channel_indexes=[2]))

# 4f
sr = float(bl.segments[0].analogsignals[1].sampling_rate)

plt.figure()

# Use markers plus some extra space as x limits
offset = 9

plt.subplot(3,1,2)
# eye position x as a function of time
plt.plot(et,ex)
plt.xlabel('Time (s)')
plt.ylabel('Eye Postion X')

yl = plt.ylim()
t2 = [messages['trialid_time'][1], messages['Cue_time'][1], messages['End_time'][1]]
plt.xlim(t2[0]-offset,t2[2]+offset) # adjust x limits
pt2 = np.kron(np.ones((2,1)),t2)
py2 = np.kron(np.ones((np.size(pt2,1),1)),yl).transpose()
plt.plot(pt2,py2)


plt.subplot(3,1,1)
# x-position in Unity as a function of time
plt.plot(ut,pos_data[uind,2])
plt.xlabel('Time (s)')
plt.ylabel('X-Pos')
mi = pos_data[uind,0].nonzero()
yl = plt.ylim()
t2 = ut[mi[0][1:]]
plt.xlim(t2[0]-offset,t2[2]+offset) # adjust x limits
pt2 = np.kron(np.ones((2,1)),t2)
py2 = np.kron(np.ones((np.size(pt2,1),1)),yl).transpose()
plt.plot(pt2,py2)

plt.subplot(3,1,3)
# broadband signal as a function of time
dataind = np.arange(0, 500000)
broadband_data=broadband_data[dataind]
plt.plot(dataind/sr, broadband_data)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (uV)')

yl = plt.ylim()
t2 = [ev_rawtimes[2], ev_rawtimes[4], ev_rawtimes[6]]
plt.xlim(t2[0]/sr-offset,t2[2]/sr+offset) # adjust x limits
pt2 = np.kron(np.ones((2,1)),t2)
py2 = np.kron(np.ones((np.size(pt2,1),1)),yl).transpose()
plt.plot(pt2/sr,py2)

plt.show()
