from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.picker import MDDatePicker
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivymd.uix.list import OneLineListItem
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
import re
# from kivy.core.window import Window


from libs.screenmanager import screenmanager
from libs.database.DB import DB


class SignupPage(MDScreen):
    #picker
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open(animation=False)    
    
    def on_save(self, instance, value, date_range):
        self.ids.signup_Birthday.text = str(value)
        
    def on_cancel(self, instance, value):
        pass

    def gender(self,value):
        self.ids.signup_Gender.text = value
    def city(self,value):
        self.ids.signup_City.text = value         
    def Donebutton(self):
        
        SignUp_tablename="UserData"
        name = self.ids.signup_NAME.text
        email = self.ids.signup_EMAIL.text
        phoneNumber = self.ids.signup_PhoneNumber.text
        password = self.ids.signup_PASSWORD.text
        confirmpassword = self.ids.signup_CONFIRM_PASSWORD.text
        nickname = self.ids.signup_NickName.text
        gender = self.ids.signup_Gender.text
        birthday = self.ids.signup_Birthday.text
        city = self.ids.signup_City.text

        #------------input email format filter--------------------
        mailRex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        #-----------email format error----------------------------
        if re.match(mailRex,email) != None:
            self.ids.email_error_message.text = ""
            
        else:
            self.ids.email_error_message.text = "Email format error"
            return False
        

        #------------input password format filter------------------
        passwordRex = r"(^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{10,}$)"
        #-----------password format error----------------------------
        if re.match(passwordRex,password) != None:
            self.ids.password_error_message.text = ""
            DB().SignUp_Create_Check(name,nickname,email,password,birthday,city,phoneNumber,gender)
            # return True
            # confirmpassword = self.ids.signup_CONFIRM_PASSWORD.text
            # cursor.execute('''insert into {}(UserName,UserNickName,UserEmail,UserPassword,UserPerference,UserBirthday,UserCity,UserPhoneNumber,UserGender,UserChoiceMission)
            #                 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''.format(SignUp_tablename),(name,"fish",email,password,"","","","","",""))
            # #與資料庫變更成立語法
            # db.commit()
            # print("OK")
        else:
            self.ids.password_error_message.text = "Password format error"
            return False
        if  password != confirmpassword:
            self.ids.password_error_message.text = "Password format error"
            return False
        else:
            print("------login------") 
            return True
    def callback(self):
        app = MDApp.get_running_app()
        app.root.current = 'login'

# class Signup_pageApp(MDScreen):
#     def build(self):
#         # Mission=Builder.load_file(".\mission.kv")
#         # self.theme_cls.primary_palette = "Amber"
#         # return Mission
#         return SignupPage()

# if __name__ == '__main__':
#     Signup_pageApp().run()