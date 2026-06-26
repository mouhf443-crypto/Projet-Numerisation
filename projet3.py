import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(-2*np.pi,2*np.pi,100)
fe=-0.15915
te=np.arange(2*np.pi,-2*np.pi,1/fe)
x=np.exp(-t)
xe=np.exp(-te)
plt.plot(t,x)
plt.show()
plt.plot(t,x)
plt.stem(te,xe)
plt.show()
plt.plot(t,x)
plt.stem(te,xe)
plt.step(te,xe)
plt.show()
