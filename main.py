import cv2
import numpy as np
import matplotlib.pyplot as plt

xx, yy = np.meshgrid(np.linspace(0, 5, 256), np.linspace(0, 5, 256))
fun = np.sinc(((xx - 2.5) + yy)*2.5)
plt.imshow(fun, cmap=plt.cm.gray)
