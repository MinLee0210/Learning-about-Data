# EXPLORING PLOT TYPES
import matplotlib.pyplot as plt
import numpy as np

# Scatter plot: used to visualize the relationship betweens 
#              variables measured in the same dataset.

# x = np.random.normal(0, 1, 5)
# y = np.random.normal(0, 1, 5)

# plt.scatter(x, y, c = ['b', 'g', 'k', 'r', 'c'])
# plt.show()

# Bar plot: uses to present grouped data with rectangular bars, 
#         which can either vertical or horizontal.

# x = np.arange(5)
# y = 3.14 + 2.71 * np.random.rand(5)

# plt.subplots(2)
# plt.subplot(211)
# plt.bar(x, y, align='center', alpha=0.4, color='y')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('bar plot in vertical')
# plt.subplot(212)
# plt.barh(x, y, align='center', alpha=0.4, color='c')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('bar plot in horizontal')

# plt.show()

# Contour plots: used to present the relationship between three numeric variables
#                 in two dimensions. Two variables are drawn along the x and y axes,
#                 the third variable z, is used for contour levels that are plotted as
#                 differenct colors

# x = np.linspace(-1, 1, 255)
# y = np.linspace(-2, 2, 300)
# z = np.sin(y[:, np.newaxis]) * np.cos(x)

# # plt.contour(x, y, z, 255, linewidth=2)
# plt.contourf(x, y, z, 255)
# # The contourf is used when we want to draw a contour lines and filled contours
# plt.show()

# Histogram plot: used to represent the distribuation of numerical data graphically.

# mu, sigma = 100, 25
# fig, (ax0, ax1) = plt.subplots(ncols=2)

# x = mu + sigma * np.random.rand(1000)
# ax0.hist(x, 20, density=1, histtype='stepfilled', 
#         facecolor='g', alpha=0.75)
# ax0.set_title('Stepfilled histogram')

# ax1.hist(x, bins=[100, 150, 165, 170, 195], density=1, 
#          histtype='bar', rwidth=0.8)
# ax1.set_title('Uniquel bins histogram')
# # Automatically adjust subplot parameters to give specified padding
# plt.tight_layout()
# plt.show()

