# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 収縮(Erosion)
img = cv.imread('data/oden.png', 0)
kernel = np.ones((8, 8), np.uint8)
erosion = cv.erode(img, kernel, iterations=1)

cv.imshow('image', erosion)
cv.waitKey(0)
cv.destroyAllWindows()


# 膨張(Dilation)
dilation = cv.dilate(img, kernel, iterations=1)
cv.imshow('image', dilation)
cv.waitKey(0)
cv.destroyAllWindows()


# オープニング(Opening)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
cv.imshow('image', opening)
cv.waitKey(0)
cv.destroyAllWindows()


# クロージング(Closing)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
cv.imshow('image', opening)
cv.waitKey(0)
cv.destroyAllWindows()


# モルフォロジー勾配
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
cv.imshow('image', gradient)
cv.waitKey(0)
cv.destroyAllWindows()


# トップハット変換
# オープニング処理で消える白ノイズを抽出する
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
cv.imshow('image', tophat)
cv.waitKey(0)
cv.destroyAllWindows()


# ブラックハット変換
# クロージング処理で消える黒穴ノイズを抽出する
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
cv.imshow('image', blackhat)
cv.waitKey(0)
cv.destroyAllWindows()


# カーネルの作成
print(cv.getStructuringElement(cv.MORPH_RECT, (5, 5)))
print(cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5)))
print(cv.getStructuringElement(cv.MORPH_CROSS, (5, 5)))
# 十字形カーネルを使う意味→４近傍？
