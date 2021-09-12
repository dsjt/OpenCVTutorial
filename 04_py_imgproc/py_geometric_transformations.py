# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread("data/oden.png")

# スケーリング
res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
height, width = img.shape[:2]
res = cv.resize(img, (2*width, 2*height), interpolation=cv.INTER_CUBIC)
cv.imshow("img", img)
cv.imshow("res", res)
cv.waitKey(0)
cv.destroyAllWindows()


# 並進
# 並進はaffine変換で表現できる。
# (x, y)方向への移動量が(tx, ty)のとき
# 変換行列M = [[1, 0, tx], [0, 1, ty]] を用いる。
rows, cols, channels = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('img', dst)
cv.waitKey(0)
cv.destroyAllWindows()

# 回転
# 回転についても変換行列で表現できる。
# 変換行列M = [[\cos\theta, -\sin\theta], [\sin\theta, \cos\theta]]
img = cv.imread('data/oden.png')
rows, cols, channels = img.shape
M = cv.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow('image', dst)
cv.waitKey(0)
cv.destroyAllWindows()


# アフィン変換
# 変換前後で並行性を保つ変換とのこと。
# 入力画像と出力画像の対応点の座標が3点ずつ必要
img = cv.imread('data/oden.png')
rows, cols, ch = img.shape
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv.getAffineTransform(pts1, pts2)
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('image', dst)
cv.waitKey(0)
cv.destroyAllWindows()

# 射影変換
# 変換の前後で直線性が保たれる
# 直線性というのは表現しづらいが、変換の画像を見るとわかる。
# 入力画像に引いた直線は、出力画像でも直線である。
img = cv.imread("data/oden.png")
rows, cols, ch = img.shape
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M, (300, 300))
cv.imshow('image', dst)
cv.waitKey(0)
cv.destroyAllWindows()
