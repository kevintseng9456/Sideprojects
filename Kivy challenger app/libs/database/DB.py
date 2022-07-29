import pymssql as database




class DB():
    # try:
    #     db = database.connect(server='khomestore.synology.me', user='sa', password='MSsql08408449', charset='utf8', database='APPSolutions', port='1433')
    # # db = database.connect(server='25.34.234.209', user='sa', password='08408449', charset='utf8', database='APPSolutions')
    # except:
    # db = database.connect(server='169.254.249.61', user='sa', password='MSsql08408449', charset='utf8', database='APPSolutions', port='1433')
    db = database.connect(server='169.254.249.61', user='sa', password='MSsql08408449', charset='utf8', database='APPSolutions', port='1433')

    #接著利用連結conn做cursor()
    cursor = db.cursor()


        # return cursor
    def GetUserID(self, useremail, password):
        self.cursor.execute(f"exec GetUserID @Email=%s,@Password=%s",(useremail,password))
        results = self.cursor.fetchall()
        
        
        return results
    def GetUserAvatar(self,UserID ):
        self.cursor.execute(f"exec GetUserAvatar @GetUserID=%s",(UserID))
        #fetchall取得所有結果列，以陣列或物件方式回傳
        results = self.cursor.fetchall()
        
        
        return results        
    def GetUserNickName(self, UserID):
        self.cursor.execute(f"exec GetUserNickName @UserID=%s",(UserID))
        results = self.cursor.fetchall()
        
        
        return results
    def GetUserLevel(self, UserID):
        self.cursor.execute(f"exec GetUserLevel @UserID=%s",(UserID))
        results = self.cursor.fetchall()
        
        
        return results
    def GetHomePageMissionList(self, UserID):
        self.cursor.execute(f"exec GetHomePageMissionList @UserPreferences=%s",(UserID))
        results = self.cursor.fetchall()
        
        
        return results
        
        # UserID??
    def GetMissionPageData(self, GetMissionNameID):
        self.cursor.execute(f"exec GetMissionPageData @ReadMissionID=%s",(GetMissionNameID))
        results = self.cursor.fetchall()
        
        
        return results

    def UploadUserMissionData(self, UserID, GetMissionID, GetMissionTypeID, GetMissionTopicID, VideoOrPhotoURL, Title):
        self.cursor.execute(f"exec UploadUserMissionData @GetUserID=%s,@GetMissionID=%s,@GetMissionTypeID=%s,@GetMissionTopicID=%s,@VideoOrPhotoURL=%s,@Title=%s"
        ,(UserID, GetMissionID, GetMissionTypeID, GetMissionTopicID, VideoOrPhotoURL, Title))
        #fetchall取得所有結果列，以陣列或物件方式回傳
        results = self.cursor.fetchall()
        self.db.commit()
        
        
        return results
    def GetMissionName(self,GetMissionTypeID):
        self.cursor.execute(f"exec GetMissionName @RedMissionTypeID=%s",(GetMissionTypeID))
        #fetchall取得所有結果列，以陣列或物件方式回傳
        results = self.cursor.fetchall()
        
        
        return results


    def SignUp_Create_Check(self,name,nickname,email,password,birthday,city,phoneNumber,gender):
        #執行SQL SERVER 預存程序SignUp_Create_Check 新增使用者資料到資料庫
        self.cursor.execute(f"exec SignUp_Create_Check @UserName=%s,@UserNickName=%s,@UserEmail=%s,@UserPassword=%s,@UserBirthday=%s,@UserCity=%s,@UserPhoneNumber=%s,@UserGender=%s"
            ,(name,nickname,email,password,birthday,city,phoneNumber,gender))
        results = self.cursor.fetchall()
        #SignUp_Status=len(results)
        self.db.commit()
        
          
        return results

    def UploadUserAcceptMission(self, UserID, GetMissionID, GetMissionTypeID, GetMissionTopicID):
        #執行SQL SERVER UploadUserAcceptMission 將選取要執行的任務上傳至資料庫
        self.cursor.execute(f"exec UploadUserAcceptMission @GetUserID=%s,@GetMissionID=%s,@GetMissionTypeID=%s,@GetMissionTopicID=%s"
        ,(UserID, GetMissionID, GetMissionTypeID, GetMissionTopicID))
        #fetchall取得所有結果列，以陣列或物件方式回傳
        results = self.cursor.fetchall()
        self.db.commit()
        return results

    def GetUserAcceptMissionList(self, UserID):
        #執行SQL SERVER GetUserAcceptMissionList 負責將抓取使用者已選取要執行的每日任務
        self.cursor.execute(f"exec GetUserAcceptMissionList @GetUserID=%s",(UserID))
        #fetchall取得所有結果列，以陣列或物件方式回傳
        results = self.cursor.fetchall()
        return results

    def UploadAssessmentPoint(self, UserID, GetMissionAuthor, GetMissionID, GetMissionTypeID, GetMissionTopicID, JudgePoint, GetMissionSeed   ):
    #上傳使用者評核某任務的結果
        self.cursor.execute(f"exec UploadAssessmentPoint @GetUserID=%s,@GetMissionAuthor=%s,@GetMissionID=%s,@GetMissionTypeID=%s,@GetMissionTopicID=%s,@JudgePoint=%s,@GetMissionSeed=%s"
        ,(UserID,GetMissionAuthor,GetMissionID,GetMissionTypeID,GetMissionTopicID,JudgePoint,GetMissionSeed))
        #fetchall取得所有結果列，以陣列或物件方式回傳
        results = self.cursor.fetchall()
        #與資料庫變更成立語法
        self.db.commit()
        return results

    def UploadReguestsChallenge(self,UserID,ChallengeName,UploadPictureVideo_1,UploadPictureVideo_2,ChallengeMissionExplan,SpecialRequirement):
#上傳使用者想執行的挑戰
        self.cursor.execute(f"exec UploadReguestsChallenge @UserID=%s,@ChallengeName=%s,@UploadPictureVideo1=%s,@UploadPictureVideo2=%s,@ChallengeMissionExplan=%s,@SpecialRequirement=%s"
        ,(int(UserID),ChallengeName,UploadPictureVideo_1,UploadPictureVideo_2,ChallengeMissionExplan,SpecialRequirement))
        #fetchall取得所有結果列，以陣列或物件方式回傳
        results = self.cursor.fetchall()
        #print(results)
        #如果有值應該會User_Count=1，沒有值應該等於0，不應該出現"0" or "1" 若出現則應該跳出Error訊息以及顯示異常訊息並發送消息給開發者已供除錯
        self.db.commit()

    def GetUserDailyChallenge(self,UserID):
#抓取使用者每日挑戰list
        self.cursor.execute(f"exec GetUserDailyChallenge @GetUserID=%s",(UserID))
        #fetchall取得所有結果列，以陣列或物件方式回傳
        results = self.cursor.fetchall()
        return results
# ------------------------------------------------
    def GetMissionTopic(self):
        #執行SQL SERVER 預存程序GetMissionTopic")查找任務TopicList有哪些
        self.cursor.execute(f"exec GetMissionTopic")
        #fetchall取得所有結果列，以陣列或物件方式回傳
        results = self.cursor.fetchall()
        
        
        return results

    def GetMissionType(self,GetMissionTopicID):
        #執行SQL SERVER 預存程序GetMissionType 根據傳入的TopicID查找對應的TypeList
        self.cursor.execute(f"exec GetMissionType @GetMissionTopicID=%s",(GetMissionTopicID))
        #fetchall取得所有結果列，以陣列或物件方式回傳
        results = self.cursor.fetchall()
        
        
        return results




        
      