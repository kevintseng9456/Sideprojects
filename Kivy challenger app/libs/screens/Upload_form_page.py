# from kivymd.uix.relativelayout import RelativeLayout
from kivymd.uix.screen import MDScreen
# from kivy.uix.widget import Widget
from kivymd.app import MDApp
import os
from kivy.clock import Clock

from libs.screenmanager import screenmanager
from libs.database.DB import DB
from libs.nas_server import nas_api

class Upload_form_page(MDScreen):
    
    # def on_enter(self, *args):
    #     app = MDApp.get_running_app()
    #     self.GetMissionID = 1
    #     self.GetMissionTypeID =  app.GetMissionTypeID
    #     self.GetMissionTopicID = 1
    #     self.VideoOrPhotoURL = 1
    #     self.Title = 1
    def callback(self):
        app = MDApp.get_running_app()
        app.root.current = 'home'
        print("------home------") 
    # def camera_on(self):
    #     app = MDApp.get_running_app()
    #     app.root.current = 'Camera_page'
    # def valuetowidget_text(self):
    #     text = self.ids.texttitle.text
    #     # self.ids.texttitle.text = '輸入標題...'
    #     print(text)
    #     return text
    # def valuetowidget_video(self):
    #     path = self.ids.VideoOrPhotoURL.source.split('/')[-1]
    #     path = 'docker/PIC/Useruploadimage/' + path
    #     print(path)
    #     self.ids.VideoOrPhotoURL.source = "./image/food_and_drink.png"
    #     return path
    # def text_store(self, text):
    #     self.ids.texttitle.text = text
    #     print(text)
    #     print(self.ids.texttitle.text)
    #     print(self.valuetowidget_text())
    # # Clock.schedule_once(on_text,2)


    def UploadReguestsChallenge(self,UserID,ChallengeName,UploadPictureVideo_1,UploadPictureVideo_2,ChallengeMissionExplan,SpecialRequirement):
        #上傳使用者想執行的挑戰
        UploadPictureVideo_1 = "無路徑"
        UploadPictureVideo_2 = "無路徑"
        DB().UploadReguestsChallenge(
            int(UserID),
            ChallengeName,
            UploadPictureVideo_1,
            UploadPictureVideo_2,
            ChallengeMissionExplan,
            SpecialRequirement
        )
        print(
            '\nUploadReguestsChallenge\n',
            'UserID:',int(UserID),'\n',
            'ChallengeName:',ChallengeName,'\n',
            'UploadPictureVideo_1:',UploadPictureVideo_1,'\n',
            'UploadPictureVideo_2:',UploadPictureVideo_2,'\n',
            'ChallengeMissionExplan:',ChallengeMissionExplan,'\n',
            'SpecialRequirement:',SpecialRequirement,'\n'
        )





# class Upload_button(RelativeLayout):

#     def upload(self):
#         app = MDApp.get_running_app()       
#         DB().UploadUserMissionData(
#             app.UserID, 
#             app.GetMissionNameID, 
#             app.GetMissionTypeID, 
#             app.GetMissionTopicID, 
#             Upload_form_page().valuetowidget_video(), 
#             Upload_form_page().valuetowidget_text()
#         )

# class Save_button(RelativeLayout):

#     def upload(self):
#         app = MDApp.get_running_app()        
#         DB().UploadUserMissionData(
#             app.UserID, 
#             app.GetMissionNameID, 
#             app.GetMissionTypeID, 
#             app.GetMissionTopicID, 
#             Upload_form_page().valuetowidget_video(), 
#             Upload_form_page().valuetowidget_text()
#         )
    