from __future__ import print_function
from __future__ import division
import cv2 as cv


comp_method = int(input("Qual metodo de comparação deseja utilizar \n[0] - HISTCMP_CORREL \n[1] - HISTCMP_CHISQR:  "))

print(cv.HISTCMP_CHISQR)
print(cv.HISTCMP_CORREL)

if comp_method != 0 and comp_method != 1:
    print("Opção inválida")
    exit()

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
    comp = cv.compareHist(hist_base, hist_frame, comp_method)

    if -0.1 > comp < 0.3:
        start = cv.equalizeHist(hsv_base)
        video_frame = cv.equalizeHist(hsv_frame)
        exist_in_video = True
        print(" comp2 : ", comp, "  cont", count)
    if 0.89 < comp < 1.1:
        start = cv.equalizeHist(hsv_base)
        video_frame = cv.equalizeHist(hsv_frame)
        exist_in_video = True
        print(" comp2 : ", comp, "  cont", count)

    success, image = vidcap.read()
    count += 1


if exist_in_video:
    cv.imshow('result', video_frame)
    cv.imshow('original', start)
else:
    print("A imagem nao faz parte do video!")
cv.waitKey()

