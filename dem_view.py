import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os
import numpy as np
import cv2
from imutils import paths
import rasterio
from rasterio.plot import show, reshape_as_raster, reshape_as_image
import csv
from PIL import Image
import time
from matplotlib import cm

img_1 = cv2.imread('demSample.png', cv2.IMREAD_GRAYSCALE)
img1 = np.array(img_1)
img_2 = cv2.imread('dtmSample.png', cv2.IMREAD_GRAYSCALE)
img2 = np.array(img_2)
img1_raw = np.array(img_1)
img2_raw = np.array(img_2)
img1 = img1_raw[750:1100,750:1100 ]
img2 = img2_raw[750:1100,750:1100 ]
print(img1.shape)
print(img2.shape)
img1 =np.where(img1>=250, 0, img1)
img2 =np.where(img2>=250, 0, img2)

X1 = np.arange(0, img1.shape[1])
Y1 = np.arange(0, img1.shape[0])
x1, y1 = np.meshgrid(X1, Y1)
X2 = np.arange(0, img2.shape[1])
Y2 = np.arange(0, img2.shape[0])
x2, y2 = np.meshgrid(X2, Y2)


#plt.imshow(img)
fig, (ax1, ax2) = plt.subplots(1,2, subplot_kw={"projection": "3d"})
ax1.plot_surface(x1, y1, img1, cmap=cm.Blues)
ax2.plot_surface(x2, y2, img2, cmap=cm.Reds)
ax1.contour(x1, y1, img1+5, 20)
ax2.contour(x2, y2, img2+5, 20 )
#ax.plot_surface(img)

#ax1.set_xlim(600, 1200)
#ax1.set_ylim(600, 1200)
#ax2.set_xlim(600, 1200)
#ax2.set_ylim(600, 1200)
plt.tight_layout()
plt.show()
