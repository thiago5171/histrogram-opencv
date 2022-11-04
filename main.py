# import cv2
#
# image = cv2.imread('poke.jpg', cv.IMREAD_GRAYSCALE)
# hist = cv2.calcHist([image], [0], None, [256], [0, 255])
# plt.hist(image.ravel(), 256,  [0, 256])
# plt.show()
# # cv2.imshow('mask', realMask)
# cv2.imshow('original', image)
# # cv2.imshow('result', hsv)
# cv2.waitKey()
from __future__ import print_function
from __future__ import division
import cv2 as cv

src_base = cv.imread('img1.png')
hsv_base = cv.cvtColor(src_base, cv.COLOR_BGR2GRAY)


hist_base = cv.calcHist([hsv_base], [0], None, [256], [0, 256])
cv.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)


vidcap = cv.VideoCapture('video.mp4')
success, image = vidcap.read()
count = 0
while success:
    hsv_frame = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    hist_frame = cv.calcHist([hsv_frame],  [0], None, [256], [0, 256])
    cv.normalize(hist_frame, hist_frame, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
    comp1 = cv.compareHist(hist_base, hist_frame, cv.HISTCMP_CORREL)
    comp2 = cv.compareHist(hist_base, hist_frame, cv.HISTCMP_CHISQR)
    print("comp1:  ", comp1, " comp2 : ", comp2, "  cont", count)
    success, image = vidcap.read()
    if comp2 == 0.0 or comp1 == 1.0:
        start = cv.equalizeHist(hsv_base)
        video_frame = cv.equalizeHist(hsv_base)
    count += 1

cv.imshow('result', video_frame)
cv.imshow('original', start)
cv.waitKey()

