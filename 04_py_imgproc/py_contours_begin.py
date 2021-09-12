# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 輪郭の取得に関するチュートリアル。
# 輪郭の取得の仕組みについては触れていない。

im = cv.imread('data/oden.png')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
image, contours, hierarchy = cv.findContours(thresh,
                                             cv.RETR_TREE,
                                             cv.CHAIN_APPROX_SIMPLE)

# cv.imshow('thresh', thresh)
# cv.imshow('image', image)
# cv.waitKey(0)
# cv.destroyAllWindows()

# ax = plt.subplot(1, 1, 1, aspect=1)
# for cont in contours:
#     print(cont.shape)
#     print(cont)
#     plt.plot([c[0][0] for c in cont], [c[0][1] for c in cont])
# ax.invert_yaxis()
# plt.show()


im = cv.drawContours(im, contours, -1, (0, 255, 0), 3)
cv.imshow('image', im)
cv.waitKey(0)
cv.destroyAllWindows()
