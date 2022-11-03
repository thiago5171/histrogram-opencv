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
import cv2 as cv

vidcap = cv.VideoCapture('video.mp4')
success, image = vidcap.read()
count = 0
while success:
    success, image = vidcap.read()
    if count ==500 :
        a = image
    # print('Read a new frame: ', success, count)
    count += 1

cv.imshow('result', a)
cv.waitKey()

