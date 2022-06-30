
import matplotlib.pyplot as plt
from numpy import *

x = linspace(0, 3, 6)
y = power(x, 2)

# plt.figure('a')

# plt.subplot(221) -- stands for there is 2x2 subplots and this is the first subplot.
# plt.title('Visualization of y+y')
# plt.plot(y + y, 'r--')
# plt.grid()

# plt.subplot(222)
# plt.title('Visualization of y*3')
# plt.plot(y*3, 'ko')
# plt.grid()

# plt.subplot(223)
# plt.title('Visualization of y*y')
# plt.plot(y*y, 'b^')
# plt.grid()

# plt.subplot(224)
# plt.title('Visualization of a blank graph')
# plt.grid()

# We can create axes manually, instead of rectangular grid, using
# plt.axes([left, bottom, width, height]) (all input are in the fractional [0, 1])

plt.figure('b')
ax1 = plt.axes([0.05, 0.1, 0.4, 0.32])
ax2 = plt.axes([0.52, 0.1, 0.4, 0.32])
ax3 = plt.axes([0.05, 0.53, 0.87, 0.44])
plt.show()