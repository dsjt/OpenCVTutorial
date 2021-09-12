# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 二値化
# 頻出の処理であるため、注意深く行う。

# 単純なしきい値処理
# 値を決め打ちで二値化するもの。反転処理とかはせずにオプションを指定して柔軟に二値化できる。
#
img = cv.imread('data/oden.png', 0)
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ['Original Image', 'Binary', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()


# 適応的しきい値処理
# 画像の小領域ごとにしきい値を計算する。
img = cv.imread('data/oden.png', 0)
img = cv.medianBlur(img, 5)

ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                           cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv.THRESH_BINARY, 11, 2)

titles = ['Original Image', 'Global Threshollding (v=127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
# 図らずも、輪郭を取るような処理になった。


# 大津の二値化
# 輝度ヒストグラムが双方性分布を持つと過程し、その中間にしきい値を設定する。
img = cv.imread('data/oden.png', 0)
ret1, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)

blur = cv.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)

images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image', 'Histgram', 'Global Thresholding(v=127)',
          'Original Noisy Image', 'Histgram', "Otsu's Thresholding",
          'Gaussian filtered Image', 'Histgram', "Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3, 3, i*3+1)
    plt.imshow(images[i*3], 'gray')
    plt.subplot(3, 3, i*3+2)
    plt.hist(images[i*3].ravel(), 256)
    plt.title(titles[i*3+1])
    plt.xticks([])
    plt.yticks([])
    plt.subplot(3,3,i*3+3)
    plt.imshow(images[i*3+2], 'gray')
    plt.title(titles[i*3+2])
    plt.xticks([])
    plt.yticks([])
plt.show()


# 大津の二値化の仕組みは、二峰性分布の各クラスの分散の最小化である。
# 式中のP(i) は、輝度がiである画素の個数
# 各分布における分散を求め、それの重み付き和を取り、これを最小化することを目指す。


import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('data/oden.png', 0)
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
plt.subplot(1, 2, 1), plt.imshow(img, 'gray')
plt.xticks([]), plt.yticks([]), plt.title('Original')
plt.subplot(1, 2, 2), plt.imshow(thresh1, 'gray')
plt.xticks([]), plt.yticks([]), plt.title('Binary')
plt.savefig('data/oden_binary.png')



import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('data/oden.png', 0)
ret, thresh1 = cv.threshold(img, 0, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)
plt.subplot(2, 2, 1), plt.imshow(img, 'gray')
plt.xticks([]), plt.yticks([]), plt.title('Original')
plt.subplot(2, 2, 2), plt.imshow(thresh1, 'gray')
plt.xticks([]), plt.yticks([]), plt.title('Otsu')
plt.subplot(2, 1, 2), plt.hist(img.ravel(), bins=32)
plt.savefig('data/oden_otsu.png')

import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('data/oden.png', 0)
thresh1 = th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                     cv.THRESH_BINARY, 11, 2)
plt.subplot(1, 2, 1), plt.imshow(img, 'gray')
plt.xticks([]), plt.yticks([]), plt.title('Original')
plt.subplot(1, 2, 2), plt.imshow(thresh1, 'gray')
plt.xticks([]), plt.yticks([]), plt.title('Adaptive')
plt.savefig('data/oden_adaptive.png')
