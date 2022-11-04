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

src_base = cv.imread('img.png')
hsv_base = cv.cvtColor(src_base, cv.COLOR_BGR2HSV)
h_bins = 50
s_bins = 60
histSize = [h_bins, s_bins]

h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges  # concat lists
channels = [0, 1]

hist_base = cv.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
base_base = cv.compareHist(hist_base, hist_base, cv.HISTCMP_CORREL)


vidcap = cv.VideoCapture('video.mp4')
success, image = vidcap.read()
count = 0
while success:
    hsv_frame = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    hist_frame = cv.calcHist([hsv_frame], channels, None, histSize, ranges, accumulate=False)
    cv.normalize(hist_frame, hist_frame, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
    comp1 = cv.compareHist(hist_base, hist_frame, cv.HISTCMP_CORREL)
    comp2 = cv.compareHist(hist_base, hist_frame, cv.HISTCMP_INTERSECT)
    print("comp1:  ", comp1, " comp2 : ", comp2, "  cont",count)
    success, image = vidcap.read()
    if count == 873:
        a = image
    count += 1

cv.imshow('result', a)
cv.imshow('original', src_base)
cv.waitKey()

