# -*- coding: utf-8 -*-
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 平滑化

# 2D Convolution
# カーネルの要素は一様なので、この場合画像をぼやかすフィルタとなる。
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('data/oden.png')
img = img[:,:,::-1]
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

# 平均による平滑化
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('data/oden.png')
img = img[:,:,::-1]
blur = cv.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

# ガウシアンによる平滑化
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('data/oden.png')
img = img[:,:,::-1]
blur = cv.GaussianBlur(img, (5, 5), 0)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.show()

# 中央値フィルタによる平滑化
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('data/oden.png')
img = img[:,:,::-1]
median = cv.medianBlur(img, 5)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.show()


# バイラテラルフィルタ
# ガウシアンフィルタだが、周辺領域から似た画素値を持つものだけでフィルタリングを行う
# 結果としてエッジを保存することができる
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('data/oden.png')
img = img[:,:,::-1]
blur = cv.bilateralFilter(img, 9, 75, 75)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Bilateral')
plt.xticks([]), plt.yticks([])
plt.show()


# まとめ
img = cv.imread('data/oden.png')
img = img[:, :, ::-1]
blur = cv.blur(img,(5,5))
gaussian = cv.GaussianBlur(img, (5, 5), 0)
median = cv.medianBlur(img, 5)
bilateral = cv.bilateralFilter(img, 9, 75, 75)
plt.subplot(151), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(152), plt.imshow(blur), plt.title('Blur')
plt.xticks([]), plt.yticks([])
plt.subplot(153), plt.imshow(gaussian), plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.subplot(154), plt.imshow(median), plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.subplot(155), plt.imshow(bilateral), plt.title('Bilateral')
plt.xticks([]), plt.yticks([])
plt.savefig("data/oden_filtering.png")
