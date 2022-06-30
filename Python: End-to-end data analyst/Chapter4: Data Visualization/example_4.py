# LEGEND AND ANNOTATIONS
import matplotlib.pyplot as plt
import numpy as np

# # LEGENDS
# # Legends are an important elements that used to identify plot elements
# # in a figure

# x = np.linspace(0, 1, 20)
# y1 = np.sin(x)
# y2 = np.cos(x)
# y3 = np.tan(x)

# # plt.plot(x, y1, 'c', label='y=sin(x)')
# # plt.plot(x, y2, 'y', label='y=cos(x)')
# # plt.plot(x, y3, 'r', label='y=tan(x)')
# # plt.legend(loc='upper left')

# # The loc arguments can be others than just 'upper
# p1 = plt.plot(x, y1, 'c', label='y=sin(x)')
# p2 = plt.plot(x, y2, 'y', label='y=cos(x)')
# p3 = plt.plot(x, y3, 'r', label='y=tan(x)')

# lsin = plt.legend(handles=p1, loc='lower right')
# lcos = plt.legend(handles=p2, loc='upper left')
# ltan = plt.legend(handles=p3, loc='upper right')
# # Note: with these line of code, just ltan appers in the figure, 
# #         to solve this, add lsin and lcos as a separate artists to the axes
# plt.gca().add_artist(lsin)
# plt.gca().add_artist(lcos)
# # Use tight_layout() as a way to automatically adjust subplot parameters to specified padding
# plt.tight_layout()
# plt.grid()
# plt.show()

# ANNOTATIONS

x = np.linspace(-2.4, 0.4, 20)
y = x*x + x*2 + 1

plt.plot(x, y, 'c', linewidth=2.0)
plt.text(-1.5, 1.8, 'y= x^2 + 2*x + 1', fontsize=14, style='italic')
plt.annotate('minima point', xy=(-1, 0), 
             xytext=(-1, 0.3), 
             horizontalalignment='center', 
             verticalalignment='top', 
             arrowprops=dict(arrowstyle='->', 
             connectionstyle='arc3'))

plt.show()