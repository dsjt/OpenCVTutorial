# -*- coding: utf-8 -*-
# 楕円近似、直線近似の例は、具体例を作成する。
# 失敗例も作成する。
# （２つのオブジェクトが重なって存在するとき、一つのまとまりとしてみてしまう）
# 輪郭の近似も非常によく、サンプルを作成したいところ。
# 線の単純化アルゴリズムは、サンプルと仕組みに関する記述のリンクを張る（DP）

import numpy as np
import cv2 as cv

img_color = cv.imread('data/oden.png')
img = cv.imread('data/oden.png', 0)
ret, thresh = cv.threshold(img, 127, 255, 0)
imgEdge, contours, hierarchy = cv.findContours(thresh, 1, 2)


# モーメントの計算は輪郭から行う。
cnt = contours[0]
for cont in contours:
    if len(cnt) < len(cont):
        cnt = cont
M = cv.moments(cnt)
print(M)


print("重心: {0}".format((M['m10']/M['m00'], M['m01']/M['m00'])))
print("面積: {0}".format(M['m00']))
print("周囲長: {0}".format(cv.arcLength(cnt, True)))

# 輪郭の近似
# Douglas-Peucker algorithmとのこと
# 追って理解する
# https://www.trail-note.net/tech/thinout/ など
im = img_color.copy()
for p in [0.001, 0.1, 0.01, 0.0001]:
    epsilon = p * cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, epsilon, True)

    print(approx.shape)
    im = cv.drawContours(im, approx, -1, (0, 255, 0), 3)
    cv.imshow('image', im)
    cv.waitKey(0)
    cv.destroyAllWindows()
    break


# 凸包
im = img_color.copy()
hull = cv.convexHull(cnt)
k = cv.isContourConvex(hull)
print(k)
cv.drawContours(im, hull, -1, (0, 255, 0), 3)
cv.imshow('convex hull', im)
cv.waitKey(0)
cv.destroyAllWindows()


# 外接矩形
im = img_color.copy()
x, y, w, h = cv.boundingRect(cnt)
im = cv.rectangle(im, (x, y), (x+w, y+h), (0, 255, 0), 2) # 画像上に矩形を重ねる

rect = cv.minAreaRect(cnt)
print(f"rect: {rect}")
box = cv.boxPoints(rect)
print(f"box: {box}")
box = np.int0(box)
im = cv.drawContours(im, [box], 0, (0, 0, 255), 2)
cv.imshow('boundingRect', im)
cv.waitKey(0)
cv.destroyAllWindows()


# 最小外接円
im = img_color.copy()
(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
im = cv.circle(im,center,radius,(0,255,0),2)
ellipse = cv.fitEllipse(cnt)
im = cv.ellipse(im, ellipse, (255, 0, 0), 2)
im = cv.drawContours(im, cnt, -1, (0, 255, 0), 3)

cv.imshow('minEnclosingCircle', im)
cv.waitKey(0)
cv.destroyAllWindows()


# 直線
im = img_color.copy()
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
cv.imshow('minEnclosingCircle', im)
cv.waitKey(0)
cv.destroyAllWindows()
