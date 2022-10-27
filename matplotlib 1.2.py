from numpy import *
from matplotlib.pyplot import *

t = arange(0, 1, 0.01)
y_1 = 10 * exp(t)
f = cos(20*t)
plot(t, y_1, color='black')
plot(t, f, color='red')
title('graph')
xlabel('x(t)')
ylabel('y(t)')
show()
