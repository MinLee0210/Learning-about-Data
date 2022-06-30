import matplotlib.pyplot as plt
from numpy import *

x = linspace(0, 3, 6)
y = power(x, 2)

plt.plot(x, y, 'b')
plt.plot(x*2, 'g^', x*3, 'rs', x**x, 'y-')
# plt.axis([0, 6, 0, 12]) --extend the axis Ox then Oy
plt.axis([0, 6, 0, 30])
plt.xlabel('x')
plt.ylabel('y')
# plt.title('Data visualization: y=x**2')

plt.show()