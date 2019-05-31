import cv2
import matplotlib.pyplot as plt 
import numpy as np 
from scipy import signal
img = cv2.imread('monalisa.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray,cmap='gray')
plt.show()
mean = 0
var = 100
sigma = var**0.5
row,col = 276,182 
gauss = np.random.normal(mean,sigma,(row,col))
gauss = gauss.reshape(row,col)
gray_noisy = gray +6* gauss
plt.imshow(gray_noisy,cmap='gray')
plt.show()
## Mean filter
Hm = np.array([[1,1,1],[1,1,1],[1,1,1]])/float(9)
Gm =signal.convolve2d(gray_noisy,Hm,mode='same')
#################
Gm =signal.convolve2d(Gm,Hm,mode='same')
Gm =signal.convolve2d(Gm,Hm,mode='same')
##################
plt.imshow(Gm,cmap='gray')
plt.show()
#####################
Gm =signal.convolve2d(Gm,Hm,mode='same')
##################
plt.imshow(Gm,cmap='gray')
plt.show()
#####################
Gm =signal.convolve2d(Gm,Hm,mode='same')
Gm =signal.convolve2d(Gm,Hm,mode='same')
##################
plt.imshow(Gm,cmap='gray')
plt.show()
#####################
Gm =signal.convolve2d(Gm,Hm,mode='same')
Gm =signal.convolve2d(Gm,Hm,mode='same')
##################
plt.imshow(Gm,cmap='gray')
plt.show()
#####################
Gm =signal.convolve2d(Gm,Hm,mode='same')
Gm =signal.convolve2d(Gm,Hm,mode='same')
##################
plt.imshow(Gm,cmap='gray')
plt.show()
#####################
Gm =signal.convolve2d(Gm,Hm,mode='same')
Gm =signal.convolve2d(Gm,Hm,mode='same')
Gm =signal.convolve2d(Gm,Hm,mode='same')

##################
plt.imshow(Gm,cmap='gray')
plt.show()
#####################
#####################

