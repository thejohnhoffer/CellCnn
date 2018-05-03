import matplotlib.pyplot as plt
import _logicle as clogicle
import numpy as np

def _logicle(y, T, m, r, w):
    y = np.array(y, dtype='double')
    if w is None:
        if r == 0:
            w = 1 # don't like this but it works... FIX!
        else:
            w = (m - log10(T / abs(r))) / 2.0

    clogicle.logicle_scale(T, w, m, 0, y)
    return y


data = 10 ** np.arange(10)
T = 100
m = 10
r=None
w=0.5
y = _logicle(data, T, m, r, w)

plt.plot(y)
