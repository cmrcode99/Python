import matplotlib.pyplot as plt
import numpy as np 
x=np.linspace(0,5,11)
y=x**2
d=plt.plot(x,y, 'g')
c=plt.show()
print(c)