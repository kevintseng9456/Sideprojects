#------------------------------即時辨識打卡系統(openccv + arcface)
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import time

#opencv人臉辨識檔案
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#開啟相機
cap = cv2.VideoCapture(0)

#定義顯示文字參數
text = ''
name_org = (40, 80)
time_org = (40, 90)
fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 1
fontcolor = (0, 255, 0) # BGR
thickness = 2 
lineType = 4
bottomLeftOrigin = 1

#開始辨識
while True:
    #讀取影像
    _, img_raw = cap.read()
    #轉成灰階模式
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #此方法的任務是檢測不同大小的對象，並返回矩形的列表
    #詳細解釋可參考 https://blog.csdn.net/leaf_zizi/article/details/107637433
    faces = face_cascade.detectMultiScale(img_raw, 1.1, 8)
    # print("faces-->",faces)

    for i in range(len(faces)):
        try:
            #臉部位置
            face_x, face_y, face_w, face_h = faces[i]
            
            #抓出人臉
            img = img_raw[int(face_y):int(face_y+face_h), int(face_x):int(face_x+face_w)]

            #標記人臉範圍，名字位置，時間位置
            # for (x, y, w, h) in faces:
            cv2.rectangle(img_raw, (face_x, face_y), (face_x+face_w, face_y+face_h), (0, 255, 0), 2)
            name_org = (face_x, face_y-30)
            time_org = (face_x, face_y)
                
            #透過arcface辨識，img為辨識目標位置，db_path為影像資料庫位置
            df = DeepFace.find(img, db_path = "pic", model_name = 'ArcFace',enforce_detection=False)
            print(df.head())

            #驗證圖片
            # result = DeepFace.verify(img, "pic", model_name = 'ArcFace',enforce_detection=False)
            # print(result)
            
            try:
                #抓取辨識名字
                name = df.loc[0].values[0].split('/')[-2].split('\\')[-1]
                #抓取當前時間
                Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                #顯示名字、時間到畫面上
                cv2.putText(img_raw, name, name_org, fontFace, fontScale, fontcolor, thickness, lineType)
                cv2.putText(img_raw, Time, time_org, fontFace, fontScale, fontcolor, thickness, lineType)

                #打卡紀錄
                punch_path = 'output.txt'
                with open(punch_path, 'a') as f:
                    f.write(f"{name} at {Time} punch cad.\n")

                print(f"我辨識這位是 {name}。")
            except:
                pass
        except:
            pass
    #正常視窗大小
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    #秀出圖片                                           
    cv2.imshow('img', img_raw)                     

    # 當按下Esc結束迴圈
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
#關閉相機
cap.release()
cv2.destroyAllWindows()

