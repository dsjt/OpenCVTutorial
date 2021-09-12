# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Canny法
# 手厚い。
# Sovelフィルタによる微分値と、その点において値が極大であるかどうかの判定、
# さらに２つの閾値でエッジかどうかを振り分けた上で、振り分けられない部分は
# エッジとの連結性によって判別する。

img = cv.imread('data/oden.png', 0)
edges = np.zeros_like(img)
cv.Canny(img, 100, 150, edges, 3, True)
# help(cv.Canny)

plt.subplot(121), plt.imshow(img,cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
