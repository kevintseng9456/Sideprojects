from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty

class AppBar01(MDBoxLayout):
    username = StringProperty("NAME")
    userlevel = StringProperty("Level")

    #avator path
    avatar = StringProperty("")
    