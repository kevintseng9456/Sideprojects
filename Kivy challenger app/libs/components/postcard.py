from kivymd.uix.card import MDCard
from kivymd.uix.card import MDCardSwipe
# from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivy.properties import  NumericProperty
# from kivymd.uix.swiper import MDSwiperItem
from kivymd.app import MDApp

from libs.database.DB import DB

class PostCard(MDCard):
    profile_pic = StringProperty("./avator/avator_000000000008.jpg")
    avatar = StringProperty("./avator/avator_000000000005.jpg")
    username = StringProperty("username")
    usernameID = NumericProperty(0)
    post = StringProperty("./avator/avator_000000000009.jpg")
    caption = StringProperty("caption")
    likes = StringProperty("like")
    posted_ago = StringProperty()
    comments = StringProperty("comment")
    MissionSeed = NumericProperty(0)

    def on_enter(self):
        # print("enter")
        # Clock.schedule_interval(my_callback,2)
        return super().on_enter()

    def Upload_AssessmentPoint(self, good_or_bad):
        app = MDApp.get_running_app()
        DB().UploadAssessmentPoint(
            UserID = int(app.UserID),
            GetMissionAuthor = int(self.usernameID),
            GetMissionID = int(app.GetMissionNameID),
            GetMissionTypeID = int(app.GetMissionTypeID),
            GetMissionTopicID = int(app.GetMissionTopicID),
            JudgePoint = good_or_bad,
            GetMissionSeed = self.MissionSeed
        )
        print(
            '\nUpload_AssessmentPoint\n',
            'UserID:', int(app.UserID),'\n',
            'GetMissionAuthor:', self.usernameID,'\n',
            'GetMissionID:', int(app.GetMissionNameID),'\n',
            'GetMissionTypeID:', int(app.GetMissionTypeID),'\n',
            'GetMissionTopicID:', int(app.GetMissionTopicID),'\n',
            'JudgePoint:', good_or_bad,'\n',
            'GetMissionSeed:', self.MissionSeed,'\n',
        )
