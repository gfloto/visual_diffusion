import os, sys, torch
import numpy as np
import matplotlib.pyplot as plt

# linear sch.
T = 1000
t = np.arange(T)
beta = np.linspace(1e-4, 0.02, T)
alpha_lin = [np.prod(1 - beta[:i]) for i in range(T)]

# cosine
s = 0.008
alpha_cos = np.cos( (np.pi/2 * (t/T + s) / (1+s)) )**2

plt.plot(t, alpha_lin)
plt.plot(t, alpha_cos)
plt.show()

