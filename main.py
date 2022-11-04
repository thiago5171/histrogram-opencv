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
exist_in_video = False
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
        video_frame = cv.equalizeHist(hsv_frame)
        exist_in_video = True
    count += 1


if exist_in_video:
    cv.imshow('result', video_frame)
    cv.imshow('original', start)
else:
    print("A imagem nao faz parte do video!")
cv.waitKey()

