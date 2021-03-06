#!/usr/bin/env python
import numpy as np
from matplotlib.ticker import LinearLocator, FormatStrFormatter  
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D  
from matplotlib import cm
     
xData = np.arange(0,10,1)
yData1 = xData.__pow__(2.0)
yData2 = np.arange(15,61,5)
plt.figure(num=1, figsize=(8,6))
plt.title('Plot 1', size=14)
plt.xlabel('x-axis', size=14)
plt.ylabel('y-axis', size=14)
plt.plot(xData, yData1, color='b', linestyle='--', marker='o', label='y1 data')
plt.plot(xData, yData2, color='r', linestyle='-', label='y2 data')
plt.legend(loc='upper left')
plt.savefig('images/plot1.png', format='png')
#-----------
mu =0.0
sigma =2.0
samples = np.random.normal(loc=mu, scale=sigma, size=1000)
plt.figure(num=1, figsize=(8,6))
plt.title('Plot 2', size=14)
plt.xlabel('value', size=14)
plt.ylabel('counts', size=14)
plt.hist(samples, bins=40, range=(-10,10))
plt.text(-9,100, r'$\mu$ = 0.0, $\sigma$ = 2.0', size=16)
plt.savefig('images/plot2.png', format='png')
#----------
data =[33,25,20,12,10]
plt.figure(num=1, figsize=(6,6))
plt.axes(aspect=1)
plt.title('Plot 3', size=14)
plt.pie(data, labels=('Group 1','Group 2','Group 3','Group 4','Group 5'))
plt.savefig('images/plot3.png', format='png')
#------------------------------
fig = plt.figure()  
ax = fig.gca(projection='3d')  
X = np.arange(-5, 5, 0.25)  
Y = np.arange(-5, 5, 0.25)  
X, Y = np.meshgrid(X, Y)  
R = np.sqrt(X**2 + Y**2)  
Z = np.sin(R)  
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,  
        linewidth=0, antialiased=False)  
ax.set_zlim(-1.01, 1.01)  
 
ax.zaxis.set_major_locator(LinearLocator(10))  
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  
 
fig.colorbar(surf, shrink=0.5, aspect=5)  
 
plt.show() 