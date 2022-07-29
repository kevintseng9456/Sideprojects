#--------------------------------------------------輸入影片模式(retinaface + arcface)
from retinaface import RetinaFace
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import time

#影像辨識-------------------------------------------------------
cap = cv2.VideoCapture('test.mp4')

while(True):
    _, img = cap.read()
    try:

    #圖像辨識-------------------------------------------------------

    #透過RetinaFace辨識人像，默認閾值設置為 0.9。如果要以低解析度檢測人臉，則可以降低它。
        faces  = RetinaFace.detect_faces(img,threshold = 0.9)

        #圖像參數
        faces.keys()
        
        #取出參數
        for key in faces.keys():

            #第X張人像總參數
            identity = faces[key]

            #人像矩形邊界參數
            facial_area = identity["facial_area"]

            #特徵標記
            landmarks = identity["landmarks"]

            #將numpy.float數值轉換為int，因為cv2.circle參數center格式需要int
            le = tuple(map(int,landmarks["left_eye"]))
            re = tuple(map(int,landmarks["right_eye"]))
            n  = tuple(map(int,landmarks["nose"]))
            lm = tuple(map(int,landmarks["mouth_left"]))
            rm = tuple(map(int,landmarks["mouth_right"]))
            
            #框出人像
            cv2.rectangle(img, (facial_area[2],facial_area[3]),(facial_area[0],facial_area[1]),(255,255,255),1)
            #標記左眼位置
            cv2.circle(img, le, 1, (0, 0, 255), -1)
            #標記右眼位置
            cv2.circle(img, re, 1, (0, 0, 255), -1)
            #標記鼻子位置
            cv2.circle(img, n, 1, (0, 0, 255), -1)
            #標記左嘴角位置
            cv2.circle(img, lm, 1, (0, 0, 255), -1)
            #標記右嘴角位置
            cv2.circle(img, rm, 1, (0, 0, 255), -1)   

        # #設定顯示圖片大小
        # plt.figure(figsize = (5,5))
        # #使圖片顯示完整
        # plt.imshow(img[:,:,::-1])
        # #顯示圖片
        # plt.show()

        #透過arcface辨識，img為辨識目標位置，db_path為影像資料庫位置
        df = DeepFace.find(img, db_path = "pic\\Ester", model_name = 'ArcFace',detector_backend = 'retinaface',enforce_detection=False)
        print(df.head())

        #驗證圖片
        result = DeepFace.verify(img, "pic\\Ester\\ester2000.jpg", model_name = 'ArcFace',detector_backend = 'retinaface',enforce_detection=False)
        print(result)
        
        try:
            #抓取辨識名字
            name = df.loc[0].values[0].split('/')[-2].split('\\')[-1]
            #抓取當前時間
            Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # cv2.putText(img, name, name_org, fontFace, fontScale, fontcolor, thickness, lineType)
            # cv2.putText(img, Time, time_org, fontFace, fontScale, fontcolor, thickness, lineType)
            print(f"我辨識這位是 {name}。")
        except:
            pass
    except:
        print("!! 辨識失敗 !!")
            
    # 當按下Esc結束迴圈
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
    cv2.imshow("video",img)
cap.release()
cv2.destroyAllWindows()