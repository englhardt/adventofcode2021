import numpy as np
from scipy.ndimage import convolve

raw = open('input.txt').read().splitlines()
enhc = [i for i, c in enumerate(raw[0]) if c == '#']
img = np.array([[c == '#' for c in l] for l in raw[2:]]).astype(int)
img = np.pad(img, ((100, 100), (100, 100)))
kernel = np.array([[1, 2, 4], [8, 16, 32], [64, 128, 256]])
for i in range(50):
    img = convolve(img, kernel, mode="constant", cval=i % 2)
    img = np.isin(img, enhc).astype(int)
    if i == 1:
        print(img.sum())
print(img.sum())
