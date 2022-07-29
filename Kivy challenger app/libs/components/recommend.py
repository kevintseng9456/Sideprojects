from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.properties import  NumericProperty

class Recommend(MDCard):
    image_source = StringProperty("")
    text_source =  StringProperty("")
    GetMissionNameID = NumericProperty()