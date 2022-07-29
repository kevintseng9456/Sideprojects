from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
# from kivy.core.window import Window
# from kivy.clock import Clock
# from functools import partial
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.popup import Popup
from datetime import datetime

from libs.screenmanager import screenmanager
from libs.database.DB import DB
from libs.nas_server import nas_api
# from libs.components.missionpage import SwipeToDeleteItem
from libs.components.postcard import PostCard
# from libs.components.upload_form import Dialog,Content


globaltext = ''

class Dialog:
    dialog = None
    app = MDApp.get_running_app()

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     Clock.schedule_once(self.dialog_close)
    #     Window.bind(on_keyboard=self.events)

    def show_confirmation_dialog(self):
        if not self.dialog:
            
            self.dialog = MDDialog(
                width_offset = 0,
                # title="Address:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text = "SAVE",
                        on_press = Content().save,
                        on_release =  self.dialog_close
                        # lambda _: self.dialog.dismiss()
                        # self.dialog_close
                        # text_color=self.app.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text = "UPLOAD", 
                        on_release = Content().upload,
                        on_press =  self.dialog_close
                        # text_color=self.app.theme_cls.primary_color
                    ),
                ],

            )
        print("Bchildren: ",self.children)
        self.dialog.open()


    def dialog_close(self, *args, **kwargs):
        app = MDApp.get_running_app()
        # self.ids.textinfo.text = self.default_text
        self.dialog.dismiss(force = True)
        # app.camera_pic = ''
        # lambda _: self.dialog.dismiss()



class Content(BoxLayout,Dialog):
    imagesource = StringProperty("./image/food_and_drink.png")
    titletext = StringProperty("輸入標題")
    contexttext = StringProperty("輸入內容")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Window.bind(on_keyboard=self.events)
        app = MDApp.get_running_app()
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )
        if app.camera_pic == '':
            pass
        else:
            self.imagesource = app.camera_pic
    def import_pic(self,pic_path):
        # pic = self.ids['VideoOrPhotoURL'](source = "./IMG_{}.png".format(pic_path))
        self.ids.VideoOrPhotoURL.source = "./IMG_{}.png".format(pic_path)
        # self.ids.VideoOrPhotoURL.reload()
        
    def call_app(self):
        app = MDApp.get_running_app()
        return app

    def callback(self):
        self.call_app().root.current = 'home'

    def camera_on(self):
        # app = MDApp.get_running_app()
        # self.call_app().root.current = 'Camera_page'
        camera().show_camera_popup()




    def call_dialog_close(self):
        self.dialog_close()

    def valuetowidget_text(self):
        return globaltext

    def valuetowidget_video(self):
        path = self.ids.VideoOrPhotoURL.source.split('/')[-1]
        path = '/docker/PIC/Useruploadimage/' + path
        print(path)
        self.ids.VideoOrPhotoURL.source = "./image/food_and_drink.png"
        return path
        
    def text_store(self,*args, **kwargs):
        # print(globaltext)
        global globaltext
        globaltext = self.ids.texttitle.text


# class upload_or_save(Content):

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)



                    #上傳失敗
    def upload(self, *args, **kwargs):
        app = MDApp.get_running_app()
        # DB().UploadUserMissionData(1,1,1,1,"docker/PIC/Useruploadimage/food_and_drink.png",self.valuetowidget_text())
        DB().UploadUserMissionData(
            int(app.UserID), 
            int(app.GetMissionNameID), 
            int(app.GetMissionTypeID), 
            int(app.GetMissionTopicID), 
            self.valuetowidget_video(), 
            self.valuetowidget_text()
        )

        DB().UploadUserAcceptMission(
            int(app.UserID), 
            int(app.GetMissionNameID), 
            int(app.GetMissionTypeID), 
            int(app.GetMissionTopicID)
        )

        print(
            'UPLOAD\n',
            'UserID:',int(app.UserID), '\n'
            'GetMissionNameID:',int(app.GetMissionNameID), '\n'
            'GetMissionTypeID:',int(app.GetMissionTypeID), '\n'
            'GetMissionTopicID:',int(app.GetMissionTopicID), '\n'
            'valuetowidget_video:',self.valuetowidget_video(), '\n'
            'valuetowidget_text:',self.valuetowidget_text(), '\n'
            'camera_pic',app.camera_pic,'\n'
        )        


        nas_api.Nas_geturl().upload_pic(app.camera_pic)
        print("UPLOAD DOWN")



    def save(self, *args, **kwargs):
        app = MDApp.get_running_app()
        DB().UploadUserMissionData(
            int(app.UserID), 
            int(app.GetMissionNameID), 
            int(app.GetMissionTypeID), 
            int(app.GetMissionTopicID), 
            self.valuetowidget_video(), 
            self.valuetowidget_text()
        )        

        DB().UploadUserAcceptMission(
            int(app.UserID), 
            int(app.GetMissionNameID), 
            int(app.GetMissionTypeID), 
            int(app.GetMissionTopicID)
        )
        print(
            'UPLOAD\n',
            'UserID:',int(app.UserID), '\n'
            'GetMissionNameID:',int(app.GetMissionNameID), '\n'
            'GetMissionTypeID:',int(app.GetMissionTypeID), '\n'
            'GetMissionTopicID:',int(app.GetMissionTopicID), '\n'
            'valuetowidget_video:',self.valuetowidget_video(), '\n'
            'valuetowidget_text:',self.valuetowidget_text(), '\n'
            'camera_pic',app.camera_pic,'\n'
        )  

        nas_api.Nas_geturl().upload_pic(app.camera_pic)
        print("SAVE DOWN")

    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    # def events(self, instance, keyboard, keycode, text, modifiers):
    #     '''Called when buttons are pressed on the mobile device.'''

    #     if keyboard in (1001, 27):
    #         if self.manager_open:
    #             self.file_manager.back()
    #     return True   



class camera:
    popupWindow = None
    def show_camera_popup(self):
        show = Camera_content()
        # Camera_content().ids.camera.play = True
        self.popupWindow = Popup(title = "Camera",content = show, size_hint = (None,None),size = (412,892))
        self.popupWindow.open()
        # self.popupWindow.show.ids.camera.play = True
    # def camera_close(self, *args, **kwargs):
    #     self.popupWindow.dismiss(force = True)

class Camera_content(BoxLayout,camera):
    # def on_enter(self):
        # self.ids.camera.play = True
    def onCameraClick(self):
        app = MDApp.get_running_app()
        # self.ids.camera.play = False
        # app.root.current = 'Upload_form_page'
        now = datetime.now()
        s = datetime.strftime(now, '%Y%m%d%H%M%S')
        app.camera_pic = str(app.UserID) + s
        path = app.camera_pic
        # self.ids.camera.export_to_png(path)

        camera = self.ids['camera']
        path = "IMG_{}.png".format(path)
        camera.export_to_png(path)
        app.camera_pic = path
        # Content().import_pic(path)
        # self.ids.camera.play = False
        # self.camera_close()
        Upload_button().call_dialog()




class Upload_button(RelativeLayout,Dialog):
    def call_dialog(self):
        self.show_confirmation_dialog()

class Challenge_data_page(MDScreen):
    app = MDApp.get_running_app()

    def on_enter(self, *args):
        
        # print("Achildren: ",self.children)
        app = MDApp.get_running_app()
        # app.camera_pic = ''
        MissionPageDataresults = DB().GetMissionPageData(int(app.GetMissionNameID))
        try:
            self.ids.name_mission_box.clear_widgets()
            for i in range(len(MissionPageDataresults)):
                
                self.ids.name_mission_box.add_widget(
                    PostCard(
                        usernameID = MissionPageDataresults[i][0],
                        # username = DB().GetUserNickName(int(MissionPageDataresults[i][0]))[0][0],
                        caption = MissionPageDataresults[i][1],
                        post = nas_api.Nas_geturl().show_pic(MissionPageDataresults[i][2]),
                        MissionSeed = MissionPageDataresults[i][3]
                    )
                )
                print(
                    i,']Challenge_data_page\n',
                    'usernameID' ,MissionPageDataresults[i][0],'\n',
                    'caption' ,MissionPageDataresults[i][1],'\n',
                    'post' ,nas_api.Nas_geturl().show_pic(MissionPageDataresults[i][2]),'\n',
                    'MissionSeed' ,MissionPageDataresults[i][3],'\n',
                )
        except:
            pass
    def callback(self):
        app = MDApp.get_running_app()
        print(app.pre_mission_name)
        app.root.current = 'home'
        print("------home------") 

        # if MissionPageDataresults != '':
        #     '''Creates a list of cards.'''
        #     for i in range(len(MissionPageDataresults)):
        #         self.ids.increase_swiper.add_widget(
        #             SwipeToDeleteItem(
        #                 missionsource = nas_api.Nas_geturl().show_pic(MissionPageDataresults[i][2])
        #             )
        #         )




