# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# 画像ピラミッド
img = cv.imread("data/oden.png")
img = img[:,:,::-1]
higher_reso =img

lower_reso = cv.pyrDown(higher_reso)
lowerlower_reso = cv.pyrDown(lower_reso)

plt.subplot(2, 2, 1)
plt.imshow(higher_reso)
plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2)
plt.imshow(lower_reso)
plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3)
plt.imshow(lowerlower_reso)
plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4)
plt.imshow(cv.pyrDown(lowerlower_reso))
plt.xticks([]), plt.yticks([])
plt.show()
# この表示では画像サイズの変化が見て取れないため、よろしくないな



# ピラミッドをを使ったブレンディング
import cv2 as cv
import numpy as np

A = cv.imread("data/oden.png")
A = A[:256, :256]
B = cv.imread("data/music_koto_man.png")
B = B[:256, :256]

G = A.copy()
gpA = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)

G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)

lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpA[i])
    L = cv.subtract(gpA[i-1], GE)
    lpA.append(L)

lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpB[i])
    L = cv.subtract(gpB[i-1],GE)
    lpB.append(L)

LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack((A[:,:cols//2],B[:,cols//2:]))

# cv.imwrite('Pyramid_blending2.jpg',ls_)
# cv.imwrite('Direct_blending.jpg',real)
