import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(-0.0000454545,0.0000454545,100)
fe=22000
te=np.arange(-0.0000454545,0.0000454545,1/fe)
x=np.cos(4*np.pi*10**3*t)*np.cos(4*np.pi*10**3*t)
xe=np.cos(4*np.pi*10**4*te)*np.cos(4*np.pi*10**3*te)
plt.plot(t,x)
plt.show()
plt.plot(t,x)
plt.stem(te,xe)
plt.show()
plt.plot(t,x)
plt.stem(te,xe)
plt.step(te,xe)
plt.show()
