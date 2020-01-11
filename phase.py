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

fct = lambda w: -np.arctan(w/w0)

y = [fct(i) for i in create_log(6)]

ax = plt.gca()
plt.plot(create_log(6),y)
plt.xscale("log")

ax.set_xlabel("w (rad/s)")
ax.set_ylabel(r"$\phi$")

plt.show()
