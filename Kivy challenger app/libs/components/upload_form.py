from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.clock import Clock

from libs.screenmanager import screenmanager
from libs.database.DB import DB
from libs.nas_server import nas_api

class Content(BoxLayout):
    def call_app():
        app = MDApp.get_running_app()
        return app


    def call_dialog_close(self):
        Dialog().dialog_close()

    def callback(self):
        
        self.call_app().root.current = 'home'
    def camera_on(self):
        # app = MDApp.get_running_app()
        self.call_app().root.current = 'Camera_page'
    def valuetowidget_text(self):
        text = self.ids.texttitle.text
        # self.ids.texttitle.text = '輸入標題...'
        print(text)
        return text
    def valuetowidget_video(self):
        path = self.ids.VideoOrPhotoURL.source.split('/')[-1]
        path = 'docker/PIC/Useruploadimage/' + path
        print(path)
        self.ids.VideoOrPhotoURL.source = "./image/food_and_drink.png"
        return path
    def text_store(self, text):
        self.ids.texttitle.text = text
        print(text)
        print(self.ids.texttitle.text)
        print(self.valuetowidget_text())
    # Clock.schedule_once(on_text,2)

    def upload(self):
        app = MDApp.get_running_app()       
        DB().UploadUserMissionData(
            int(app.UserID), 
            int(app.GetMissionNameID), 
            int(app.GetMissionTypeID), 
            int(app.GetMissionTopicID), 
            self.valuetowidget_video(), 
            self.valuetowidget_text()
        )

    def save(self):
        app = MDApp.get_running_app()        
        DB().UploadUserMissionData(
            int(app.UserID), 
            int(app.GetMissionNameID), 
            int(app.GetMissionTypeID), 
            int(app.GetMissionTopicID), 
            self.valuetowidget_video(), 
            self.valuetowidget_text()
        )

class Dialog():
    dialog = None
    app = MDApp.get_running_app()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.dialog_close)
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
                        on_press = Content().save()
                        # text_color=self.app.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text = "UPLOAD", 
                        on_press = Content().upload()
                        # text_color=self.app.theme_cls.primary_color
                    ),
                ],

            )
        self.dialog.open()

    def dialog_close(self):
        # self.ids.textinfo.text = self.default_text
        self.dialog.dismiss(force = True)