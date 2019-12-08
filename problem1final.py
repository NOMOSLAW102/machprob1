import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(0,99,num=100,endpoint=True)
y = np.zeros(len(n))

for i in n:
    i=int(i)
    x = i
    while x>=10:
        x=x-10
    z=((x*x)-7)
    z=int(z)
    y[i]=z
plt.stem(n,y, use_line_collection=True)
print ('We set the values of n as 0 to 99, with an increment of 1. As seen in the graph, the value of f creates a pattern, the first value of f starts off in -7, then goes to -6,-3, 2, 9, and so on, and ends in 74, eventually restarting again in -7. It does not have a constant increase, the increase starts off with 1, then 3, then 5, essentially increasing by 2 every step.') 
plt.xlabel('n')
plt.ylabel('f')
plt.title( 'f(n)' )
plt.show()