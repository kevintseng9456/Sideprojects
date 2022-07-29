from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivy.properties import  NumericProperty




class Dailycard(MDCard):
    DailyMissionTitle = StringProperty("")
    DailyFulfillConditions = StringProperty("")
    DailyChallengeList = StringProperty("N")

    def on_enter(self):
        self.upload_or_ok_icon()
    
    def upload_or_ok_icon(self):
        if self.DailyChallengeList == 'Y':
            self.ids.upload_or_ok_icon.source = './image/OK_icon.png'


