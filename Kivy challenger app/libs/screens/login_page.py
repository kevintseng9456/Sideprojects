from kivymd.uix.screen import MDScreen
import pymssql as database
import re
from kivy.properties import  NumericProperty
from kivymd.app import MDApp

from libs.database.DB import DB
from libs.screenmanager import screenmanager
# import json

class LoginPage(MDScreen):

    def Loginbutton(self):
        app = MDApp.get_running_app()
        #必須先取得使用者ID
        useremail = self.ids.user_email.text
        password = self.ids.user_password.text

        #------------input email format filter--------------------
        mailRex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        self.ids.login_error_message.text = self.ids.login_error_message.text
        #-----------email format error----------------------------
        if re.match(mailRex,useremail) != None:
            self.ids.login_error_message.text = ""
        else:
            self.ids.login_error_message.text = "Check the Email or Password again"
        

        #------------input password format filter------------------
        passwordRex = r"(^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{10,}$)"
        #-----------password format error----------------------------
        if re.match(passwordRex,password) != None:
            self.ids.login_error_message.text = ""
        else:
            self.ids.login_error_message.text = "Check the Email or Password again"
        
        if  useremail != "" and password != "" and self.ids.login_error_message.text == "":    

            results = DB().GetUserID(useremail, password)

            #如果有值應該會User_Count=1，沒有值應該等於0，不應該出現"0" or "1" 若出現則應該跳出Error訊息以及顯示異常訊息並發送消息給開發者已供除錯
            User_Count=len(results)

            #若有找到就做以下事情
            if User_Count!= 0 and results[0][0] != None:
                # for result in results:
                    # List_Count=result
                    # for DoubResult in List_Count:
                        #輸出User名稱
                app.UserID = results[0][0]

                print("Global UserID :", app.UserID)
                print("------home------") 
                return True

            else :
                self.ids.login_error_message.text ="User not exist"