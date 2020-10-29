import numpy as np
from pprint import pprint

attribute = {1: 'Credit History', 2: 'Wealth', 3: 'Assets'}
def entropy(x):
    result = 0
    value, counts = np.unique (x, return_counts=True)
    freqs = counts.astype ('float') / len (x)
    for p in freqs:
        if p != 0.0:
            result -= p * np.log2 (p)
    return result

def Entropy_gain(y, x):
    result = entropy (y)
    value, counts = np.unique (x, return_counts=True)
    freqs = counts.astype ('float') / len (x)

    for p, v in zip (freqs, value):
        result -= p * entropy (y[x == v])
    return result

def divide(a):
    return {b: (a == b).nonzero ()[0] for b in np.unique (a)}

def split(x, y):
    if len (set (y)) == 1 or len (y) == 0:
        return y
    gain = np.array ([Entropy_gain (y, x_attr) for x_attr in x.T])
    selected_attr = np.argmax (gain)
    if np.all (gain < 1e-6):
        return y

    sets = divide (x[:, selected_attr])
    result = {}
    for k, v in sets.items ():
        y_subset = y.take (v, axis=0)
        x_subset = x.take (v, axis=0)
        result["%s = %d" % (attribute[selected_attr + 1], k)] = \
            split (x_subset, y_subset)

    return result

x1 = [0, 0, 1, 1, 2, 2]
x2 = [0, 1, 1, 0, 0, 1]
x3 = [1, 0, 0, 0, 1, 1]
y = np.array ([0, 0, 1, 0, 1, 1])

X = np.array ([x1, x2, x3]).T
pprint(split (X, y))