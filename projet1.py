import numpy as np
import matplotlib.pyplot as plt
t1=np.linspace(-0.01,0.01,100)
t2=np.linspace(-0.001,0.001,100)
t3=np.linspace(-0.0001,0.0001,100)
fe1=200
fe2=2000
fe3=20000
te1=np.arange(-0.01,0.01,1/fe1)
te2=np.arange(-0.001,0.001,1/fe2)
te3=np.arange(-0.0001,0.0001,1/fe3)
x1=2*np.cos(200*np.pi*t1)
x2=3*np.cos(2000*np.pi*t2)
x3=4*np.cos(20000*np.pi*t3)
x=2*np.cos(200*np.pi*t1)+3*np.cos(2000*np.pi*t2)+4*np.cos(20000*np.pi*t3)
xe=2*np.cos(200*np.pi*te1)+3*np.cos(2000*np.pi*te2)+4*np.cos(20000*np.pi*te3)
plt.plot(t3,x)
plt.show()
plt.plot(t3,x)
plt.stem(te3,xe)
plt.show()
plt.plot(t3,x)
plt.stem(te3,xe)
plt.step(te3,xe)
plt.show()
