# -*- coding: utf-8 -*-
"""Hw4_CV_MKh.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oTwfOTpQfXsWaeJ6xroMnJzsk9uSvu5v

# تمرین چهارم -
## OpenCv

## Loading Relevant Libraries and Packages
"""

## Importing necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
#from cv2 import cv2_imshow

"""### Loading the Image"""

img = cv2.imread("Dark.jpg")

"""### Linear Brightness"""

alpha = float(input("Enter your desirable alpha within range of [0.1 - 3.0]:"))
beta = int(input("Enter your desirable beta:"))

L_Bright = cv2.convertScaleAbs(img, alpha = alpha, beta = beta)
plt.imshow(L_Bright[:,:,::-1]); plt.title("Linear Correction")

"""### Gamma Correction"""

img.shape

Gamma = [2, 1, 1/2, 1/3, 1/4, 5]
Gamma_Corr = np.zeros((6, 900, 900, 3), np.uint8)
#### Each Gamma
try:
  for j in range(6):
    lookUpTable = np.empty((1,256), "uint8")
    for i in range(256):
      lookUpTable[0, i] = np.clip(pow(i/255.0, Gamma[j])*255.0, 0, 255)
    Gamma_Corr[j,:,:,:] = cv2.LUT(img, lookUpTable)
except:
  "Raise the error"
else:
  print("Successfull")

plt.figure(figsize = [18, 12])
plt.subplot(231); plt.imshow(Gamma_Corr[0,:,:,::-1]), plt.title("Gamma Correction with gamma 2")
plt.subplot(232); plt.imshow(Gamma_Corr[1,:,:,::-1]), plt.title("Gamma Correction with gamma 1")
plt.subplot(233); plt.imshow(Gamma_Corr[2,:,:,::-1]), plt.title("Gamma Correction with gamma 1/2")

plt.subplot(234); plt.imshow(Gamma_Corr[3,:,:,::-1]), plt.title("Gamma Correction with gamma 1/3")
plt.subplot(235); plt.imshow(Gamma_Corr[4,:,:,::-1]), plt.title("Gamma Correction with gamma 1/4")
plt.subplot(236); plt.imshow(Gamma_Corr[5,:,:,::-1]), plt.title("Gamma Correction with gamma 5")

"""# Seyedali Seyedhosseini
## The End
"""