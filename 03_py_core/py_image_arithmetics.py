# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np


x = np.uint8([250])
y = np.uint8([10])
print(x, y, x.dtype)
print(cv.add(x, y))
print(x+y)

img1 = cv.imread('data/oden.png')[:385,:273,:]
img2 = cv.imread('data/music_koto_man.png')[:385,:273,:]
print(img1.shape)
print(img2.shape)
dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)
# cv.imshow('image', dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

img1 = cv.imread('data/music_koto_man.png')
img2 = cv.imread('data/oden.png')[:150, :200]

rows, cols, channels = img2.shape # 貼り付けるもの
roi = img1[0:rows, 0:cols]        # 貼り付け先

img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY) # 白黒画像
mask_inv = cv.bitwise_not(mask)

# print("--")
# print(roi.shape, mask_inv.shape)

# 背景は、mask_invの箇所を抜き出す
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv) # maskを適用するためにbitwise_andを利用
# オブジェクトは、maskの箇所を抜き出す
img2_fg = cv.bitwise_and(img2, img2, mask=mask)

dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv.imshow('image', img1)
cv.waitKey(0)
cv.destroyAllWindows()
