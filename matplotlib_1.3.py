from numpy import *
from matplotlib.pyplot import *
#done you have to upload it to classroom
t = arange(0, 1, 0.03)
x = cos(10*t) * exp(-t)
y = sin(10*t) * exp(-t)
plot(x, y, color='black')
title('graph')
xlabel('x(t)')
ylabel('y(t)')
show()
