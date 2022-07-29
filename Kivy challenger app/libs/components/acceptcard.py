from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivy.properties import  NumericProperty


from libs.database.DB import DB
from libs.screens.challenge_data_page import*


class Acceptcard(MDCard,Dialog):
    # profile_pic = StringProperty("./avator/avator_000000000008.jpg")
    # avatar = StringProperty("./avator/avator_000000000005.jpg")
    # username = StringProperty("username")
    post = StringProperty("./avator/avator_000000000009.jpg")
    GetMissionFinish = StringProperty("N")
    GetMissionName = StringProperty("N/A")
    GetMissionTopicID = NumericProperty(0)
    GetMissionTypeID = NumericProperty(0)
    GetMissionNameID = NumericProperty(0)
    def on_enter (self):
        print(self.GetMissionFinish,'AAAA')
        self.upload_or_ok_icon()
    def upload_or_ok_icon(self):
        print(self.GetMissionFinish,'---')
        if self.GetMissionFinish == 'Y':
            self.ids.upload_or_ok_icon.source = './image/OK_icon.png'
    def call_challenge_data_page_dialog(self):
        app = MDApp.get_running_app()
        self.show_confirmation_dialog()
        app.GetMissionTopicID = self.GetMissionTopicID
        app.GetMissionTypeID = self.GetMissionTypeID
        app.GetMissionNameID = self.GetMissionNameID 
    # caption = StringProperty("caption")
    # likes = StringProperty("like")
    # posted_ago = StringProperty()
    # comments = StringProperty("comment")
    # def on_start(self):
    #     '''Creates a list of cards.'''
    #     for i in range(20):
    #         print("123")
    #         self.ids.md_list.add_widget(
    #             SwipeToDeleteItem(text=f"One-line item {i}")
    #         )
