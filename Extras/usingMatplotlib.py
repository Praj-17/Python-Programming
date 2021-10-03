# THIS MODULE IS USED TO PLOT GRAPHHS
import numpy as np
import matplotlib.pyplot as plt #syntax
#EXAMPLE 1 plotting sina nd cos curves
x = np.arange(0,3*np.pi, 0.1)
y_sin =np.sin(x)
y_cos =np.cos(x)

#Plot the points using matpoltlib
plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.xlabel('x axis label: radians')
plt.ylabel('y axis label: values')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()

#HORIZONTAL SUBPLOT
from pylab import *
x = np.arange(0,3*np.pi, 0.1)
print(x)
y_sin =np.sin(x)
y_cos =np.cos(x)
subplot(2,1,1)
plot(x,y_sin)
plt.xlabel('x axis label: radians')
plt.ylabel('y axis label: values')
title("sin wave")
legend(['Sine'])
subplot(2,1,2)
plot(x,y_cos)
plt.xlabel('x axis label: radians')
plt.ylabel('y axis label: values')
title("Cos wave")
legend(['Cosine'])
show()
print("------------")

#VERTICAL SUBLOT
x = np.arange(0,3*np.pi, 0.1)
print(x)
y_sin =np.sin(x)
y_cos =np.cos(x)
subplot(1,2,1)
plot(x,y_sin)
plt.xlabel('x axis label: radians')
plt.ylabel('y axis label: values')
title("sin wave")
legend(['Sine'])
subplot(1,2,2)
plot(x,y_cos)
plt.xlabel('x axis label: radians')
plt.ylabel('y axis label: values')
title("Cos wave")
legend(['Cosine'])
show()
print("------------")
# DISPLAY IMAGE
#IMREAD()
import matplotlib.image as mpimg
from PIL import Image
img = Image.open(r"C:\Users\pwayk\Pictures\Camera Roll\ii.png")
plt.imshow(img)

