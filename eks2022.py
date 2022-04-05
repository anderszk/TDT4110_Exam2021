import numpy as np

a,b,n = 0, np.pi/2, 2

def f(x):
    return np.log(np.sin(x)+1)

h = (b-a)/n
print(h)

sum = h*f(np.pi/8)

sum = sum + f(np.pi*3/8)


print(round(sum,3))