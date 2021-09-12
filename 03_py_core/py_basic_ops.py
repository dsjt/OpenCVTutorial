# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('data/oden.png')

px = img[100, 100]
print(px)


blue = img[100, 100, 0]
print(blue)

img[100, 100] = [255, 255, 255]
print(img[100, 100])

print(img.item(10, 10, 2))
print(img.itemset((10, 10, 2), 100))
print(img.item(10, 10, 2))

print("----")

print(img.shape)
print(img.size)
print(img.dtype)

print("----")
ball = img[280:340, 210:270]
img[100:160, 210:270] = ball
# cv.imshow('image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()


print("----")
b, g, r = cv.split(img)
img = cv.merge((b, g, r))
b = img[:, :, 0]
img[:, :, 2] = 0
# cv.imshow('image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()


import matplotlib.pyplot as plt

RED = [255, 0, 0]

img1 = cv.imread('data/oden.png')
img1 = img1[:,:,::-1]

replicate = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=RED)

plt.subplot(231), plt.imshow(img1, 'gray'), plt.title("ORIGINAL")
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title("REPLICATE")
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title("REFLECT")
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title("REFLECT_101")
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title("WRAP")
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title("CONSTANT")
plt.show()
