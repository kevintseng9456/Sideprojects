from kivymd.app import MDApp
from kivy.uix.camera import Camera
from kivymd.uix.screen import MDScreen
from datetime import datetime

from libs.screenmanager import screenmanager
from libs.screens.challenge_data_page import Content
 
class Camera_page(MDScreen):
    # Take the current frame of the video as the photo graph       
    def on_enter(self):
        self.ids.camera.play = True
    def onCameraClick(self):
        app = MDApp.get_running_app()
        self.ids.camera.play = False
        app.root.current = 'Upload_form_page'
        print("ZXC123")
        now = datetime.now()
        s = datetime.strftime(now, '%Y%m%d%H%M%S')
        app.camer_pic = str(app.UserID) + s
        path = "./" + app.camer_pic
        self.ids.camera.export_to_png(path)

        Content().import_pic(path)

