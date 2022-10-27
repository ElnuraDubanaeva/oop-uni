from numpy import *
from matplotlib.pyplot import *

t = arange(0, 2, 0.01)
y = exp(t) * cos(20 * t)
plot(t, y, color='black')
title('graph')
xlabel('x(t)')
ylabel('y(t)')
show()
