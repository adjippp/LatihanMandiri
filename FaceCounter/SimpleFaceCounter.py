import numpy as np 
import cv2 as cv

#disini saya menggunakan OpenCV yang mungkin belum cukup kompatibel dengan python 3.7 dan pylint yang saya gunakan
#sehingga harus menambahkan sesuatu dalam setting pylint agar menghindari error
#tekan ctrl+shift+p lalu ketik setting.json
#tambahkan "python.linting.pylintArgs": ["--extension-pkg-whitelist=cv2"],
#untuk install OpenCV dapat dilakukan pip install OpenCV

detektorWajah = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
detektorMata = cv.CascadeClassifier('haarcascade_eye.xml')

img= cv.imread('practice.jpg')
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

deteksi_wajah=detektorWajah.detectMultiScale(img_gray, 1.3,5)

font=cv.FONT_HERSHEY_SIMPLEX
jumlahWajah=0

for x,y,w,h in deteksi_wajah:
    jumlah+=1
    cv.putText(img,"Ketemu Gan!", (x,y-10),font,1,(0,0,255),2,cv.LINE_AA)
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = img_gray[y:y+h, x:x+w]
    roi_color = img[y:y+h,x:x+w]

deteksi_mata = detektorMata.detectMultiScale(roi_gray)
for ex,ey,ew,eh in deteksi_mata:
    cv.rectangle(roi_color,(ex+ey),(ex+ew,ey+eh),(0,255,0),2)
    cv.putText(img,"Jumlah Wajah: "+str(jumlah),(100,100),font,2,(0,100,255),2,cv.LINE_AA)
cv.namedWindow('Test Gambar',cv.WINDOW_NORMAL)
cv.imshow('Test Gambar',img)
cv.waitKey(0)
cv.destroyAllWindows()