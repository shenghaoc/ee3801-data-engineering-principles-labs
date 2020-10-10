import numpy as np
import matplotlib.pyplot as plt
from pyedfread import edf

# 3b
samples, events, messages = edf.pread('181105.edf', trial_marker=b'Start Trial')

# 3f
esr = int(messages['RECCFG'][0][1])
samples['time'] = samples['time']/esr
events[['start','end']] = events[['start','end']]/esr
messages[['trialid_time','Cue_time','End_time']] = messages[['trialid_time','Cue_time','End_time']]/esr

# 3g
eind = np.arange(15000)
ex = samples['gx_left'][eind]
ey = samples['gy_left'][eind]
et = samples['time'][eind]
ex[ex>1920] = np.nan
ex[ex<0] = np.nan
ey[ey>1080] = np.nan
ey[ey<0] = np.nan

# 3n NEED TO WRITE AND SUBMIT
plt.figure()
plt.subplot(2,1,1)
plt.plot(et,ex)
plt.xlabel('Time (s)')
plt.ylabel('Eye Postion X')

yl = plt.ylim()
xl = plt.xlim()
t2 = [messages['trialid_time'][1], messages['Cue_time'][1], messages['End_time'][1]]
pt2 = np.kron(np.ones((2,1)),t2)
py2 = np.kron(np.ones((np.size(pt2,1),1)),yl).transpose()
plt.plot(pt2,py2)

plt.subplot(2,1,2)
plt.xlim(xl)
plt.plot(et,ey)
plt.xlabel('Time (s)')
plt.ylabel('Eye Postion Y')

yl = plt.ylim()
py2 = np.kron(np.ones((np.size(pt2,1),1)),yl).transpose()
plt.plot(pt2,py2)
plt.show()