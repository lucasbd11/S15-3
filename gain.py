import matplotlib.pyplot as plt
import numpy as np


def create_log(max):
    list_x = []
    
    for i in range(0,max+1):
        for dec in range(0,9):
            list_x.append(10**i+dec*10**i)
    return list_x

w0 = 1119.8
h0 = 1/2

fct = lambda w: 20*np.log(h0)-10*np.log(1+(w**2)/w0)

y = [fct(i) for i in create_log(3)]

ax = plt.gca()
plt.plot(create_log(3),y)
plt.xscale("log")

ax.set_xlabel("w (rad/s)")
ax.set_ylabel("GdB")

plt.show()
