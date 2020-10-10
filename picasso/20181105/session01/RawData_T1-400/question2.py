import matplotlib.pyplot as plt
import numpy as np

# 2c
data = np.loadtxt("session_1_5112018105323.txt", skiprows=14)

# 2d
uind = np.arange(300)

# 2e
ut = np.cumsum(data[uind,1])

# 2g
from matplotlib.patches import Rectangle, Circle
plt.figure()
currentAxis = plt.gca()

# Draw maze boundaries
currentAxis.add_patch(Rectangle((-12.5, -12.5), 25, 25, fill=None,lw=2))

# Draw pillars inside maze
currentAxis.add_patch(Rectangle((-7.5, 2.5), 5, 5, fill=None,ec='yellow'))
currentAxis.add_patch(Rectangle((-7.5, -7.5), 5, 5, fill=None, ec='blue'))
currentAxis.add_patch(Rectangle((2.5, 2.5), 5, 5, fill=None, ec='red'))
currentAxis.add_patch(Rectangle((2.5, -7.5), 5, 5, fill=None, ec='green'))

# Add marker to last point
currentAxis.add_patch(Circle((data[uind,2][-1],data[uind,3][-1]), radius=0.25, color='orange'))

# Add text labels to mark locations of posters
plt.text(-5, -8.75, '1')
plt.text(-8.25, 5, '2')
plt.text(7.5, -5, '3')
plt.text(5, 7.75, '4')
plt.text(5, 1.25, '5')
plt.text(-5, -2, '6')

# Plot position data
plt.plot(data[uind,2],data[uind,3])
plt.show()
