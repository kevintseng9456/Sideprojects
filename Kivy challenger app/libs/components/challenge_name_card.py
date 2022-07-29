from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivy.properties import NumericProperty

class Challenge_name_card(MDCard):
    namemissionsource = StringProperty("")
    GetMissionNameID = NumericProperty(0)
    pre_mission_name = StringProperty("")
    