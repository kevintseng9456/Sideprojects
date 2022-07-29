#-----------------------------------收集照片用
import os
import time
import uuid
import cv2

#必須先有pic資料夾以及who資料夾(who改成人員名稱)
IMAGES_PATH = os.path.join('pic','who')
#30，為拍照張數
number_images = 30
#開鏡頭
cap = cv2.VideoCapture(0)
#抓取照片，並存入資料夾底下./pic/who
for imgnum in range(number_images):
    print('Collecting image {}'.format(imgnum))
    ret, frame = cap.read()
    imgname = os.path.join(IMAGES_PATH,f'{str(uuid.uuid1())}.jpg')
    cv2.imwrite(imgname, frame)
    cv2.imshow('frame', frame)
    time.sleep(0.5)

    # 當按下Esc結束迴圈
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
#關閉相機
cap.release()
cv2.destroyAllWindows()