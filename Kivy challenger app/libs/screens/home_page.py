from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivy.properties import  NumericProperty
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.swiper import MDSwiper
from kivymd.toast import toast
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen


from libs.screenmanager import screenmanager
from libs.components.appbar01 import AppBar01
from libs.components.challenge_list import Challenge_list
# from libs.components.personal_list import Personal_list
from libs.components.acceptcard import Acceptcard
from libs.components.recommend import Recommend
from libs.components.popular import Popular
from libs.components.dailycard import Dailycard
from libs.database.DB import DB
from libs.nas_server import nas_api






class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class HomePage(MDScreen):
    username = StringProperty("NAME")
    userlevel = StringProperty("LEVEL")
    avatar = StringProperty("")
    # typedata = StringProperty("")
    GetMissionID = NumericProperty(0)
    GetMissionTypeID = NumericProperty(0)
    GetMissionTopicID = NumericProperty(0)
    VideoOrPhotoURL = StringProperty("")
    Title = StringProperty("")



    def on_enter(self):
        app = MDApp.get_running_app()
        self.list_recommends()
        self.list_populars()
        self.list_personal_list()
        self.list_daily_mission_list()
        UserAvatorresults = DB().GetUserAvatar(int(app.UserID))
        Nicknameresults = DB().GetUserNickName(int(app.UserID))
        Levelresults = DB().GetUserLevel(int(app.UserID))
        
        #跟DB要avatar path
        # avatarresults = '/docker/PIC/Avatar/avator_000000000009.jpg'


        #如果有值應該會User_Count=1，沒有值應該等於0，不應該出現"0" or "1" 若出現則應該跳出Error訊息以及顯示異常訊息並發送消息給開發者已供除錯
        # User_Count=len(Nicknameresults)

        #若有找到就做以下事情
        if len(Nicknameresults) != 0 and len(Levelresults) != 0:
            # for result in results:
                # List_Count=result
                # for DoubResult in List_Count:
                    #輸出User名稱
            self.username = Nicknameresults[0][0]
            self.userlevel = Levelresults[0][0]
            ######---------Avator not yet connect nas
            try:
                self.avatar = nas_api.Nas_geturl().show_pic(UserAvatorresults[0][0])
            except:
                self.avatar = 'avator_000000000005.jpg'
            print("\nUsername :", self.username)
            print("avatar :", nas_api.Nas_geturl().show_pic(UserAvatorresults[0][0]))
            print("userTOKEN :", self.userlevel,'\n')
            app.Username = self.username
        # print(Nicknameresults)
        print(
            '\n Global vars...\n',
            'UserID:',app.UserID,'\n',
            'Username' ,app.Username,'\n',
            'GetMissionTopicID' ,app.GetMissionTopicID,'\n',
            'GetMissionTypeID' ,app.GetMissionTypeID,'\n',
            'pre_mission_name' ,app.pre_mission_name,'\n',
            'GetMissionNameID' ,app.GetMissionNameID,'\n',
            'camera_pic' ,app.camera_pic,'\n',
            'GetMissionAuthor' ,app.GetMissionAuthor,'\n',
        )

    # --------------Recommend ------------------

    def list_recommends(self):
        app = MDApp.get_running_app()
        HomePageMissionListresults = DB().GetHomePageMissionList(int(app.UserID))
        if HomePageMissionListresults != '':
            try:
                # mission_name = ['mission_name_001','mission_name_002','mission_name_003','mission_name_004','mission_name_005']
                # image_id = ['image_box_001','image_box_002','image_box_003','image_box_004','image_box_005']
                self.ids.add_recommend.clear_widgets()
                for i in range(5):
                    
                    self.ids.add_recommend.add_widget(Recommend(
                        image_source = nas_api.Nas_geturl().show_pic( HomePageMissionListresults[i][2]),
                        text_source = HomePageMissionListresults[i][1],
                        GetMissionNameID = HomePageMissionListresults[i][0]

                    ))
                    print(
                        i,"]list_commends",'\n',
                        'image_source:',nas_api.Nas_geturl().show_pic( HomePageMissionListresults[i][2]),'\n',
                        "text_source:",HomePageMissionListresults[i][1],'\n',
                        'GetMissionNameID:',HomePageMissionListresults[i][0],'\n'
                    )
                    # a = mission_name[i]
                    # b = HomePageMissionListresults[i][1]
                    # f001 = "self.ids.%s.text='%s'" %(a,b)
                    # exec(f001)

                    # c = image_id[i]
                    # d = HomePageMissionListresults[i][2]
                    # f002 = "self.ids.%s.source= nas_api.Nas_geturl().show_pic('%s')" %(c,d)
                    # exec(f002)

            except:
                pass


    # --------------Popular ------------------

    def list_populars(self):
        app = MDApp.get_running_app()
        HomePageMissionListresults = DB().GetHomePageMissionList(int(app.UserID))
        if HomePageMissionListresults != '':
            try:
                # mission_name = ['mission_name_001','mission_name_002','mission_name_003','mission_name_004','mission_name_005']
                # image_id = ['image_box_001','image_box_002','image_box_003','image_box_004','image_box_005']
                self.ids.add_popular.clear_widgets()
                for i in range(5):
                    
                    self.ids.add_popular.add_widget(Popular(
                        image_source = nas_api.Nas_geturl().show_pic( HomePageMissionListresults[i][2]),
                        text_source = HomePageMissionListresults[i][1],
                        GetMissionNameID = HomePageMissionListresults[i][0]
                    ))
                    print(
                        i,"]list_populars",'\n',
                        'image_source:',nas_api.Nas_geturl().show_pic( HomePageMissionListresults[i][2]),'\n',
                        "text_source:",HomePageMissionListresults[i][1],'\n',
                        'GetMissionNameID:',HomePageMissionListresults[i][0],'\n'
                    )
                    # a = mission_name[i]
                    # b = HomePageMissionListresults[i][1]
                    # f001 = "self.ids.%s.text='%s'" %(a,b)
                    # exec(f001)

                    # c = image_id[i]
                    # d = HomePageMissionListresults[i][2]
                    # f002 = "self.ids.%s.source= nas_api.Nas_geturl().show_pic('%s')" %(c,d)
                    # exec(f002)

            except:
                pass


    def list_personal_list(self):
        app = MDApp.get_running_app()
        UserAcceptMissionListresults = DB().GetUserAcceptMissionList(int(app.UserID))
        self.ids.acceptcard_box.clear_widgets()
        for i in range(len(UserAcceptMissionListresults)):
            try:
                self.ids.acceptcard_box.add_widget(
                    Acceptcard(
                        post = nas_api.Nas_geturl().show_pic(UserAcceptMissionListresults[i][4]),
                        GetMissionName = UserAcceptMissionListresults[i][3],
                        GetMissionFinish = UserAcceptMissionListresults[i][5],
                        GetMissionTopicID = UserAcceptMissionListresults[i][0],
                        GetMissionTypeID = UserAcceptMissionListresults[i][1],
                        GetMissionNameID = UserAcceptMissionListresults[i][2]
                    )
                )
                print(
                    i,"]list_personal_list",'\n',
                    'post:',nas_api.Nas_geturl().show_pic(UserAcceptMissionListresults[i][4]),'\n',
                    "GetMissionName:",UserAcceptMissionListresults[i][3],'\n',
                    'GetMissionFinish:',UserAcceptMissionListresults[i][5],'\n',
                    'GetMissionTopicID:',UserAcceptMissionListresults[i][0],'\n',
                    'GetMissionTypeID:',UserAcceptMissionListresults[i][1],'\n',
                    'GetMissionNameID:',UserAcceptMissionListresults[i][2],
                )                
            except:
                pass 

    def list_daily_mission_list(self):
        app = MDApp.get_running_app()
        GetUserDailyChallengeresults = DB().GetUserDailyChallenge(int(app.UserID))
        self.ids.daily_acceptcard_box.clear_widgets()
        for i in range(len(GetUserDailyChallengeresults)):
            try:
                self.ids.daily_acceptcard_box.add_widget(
                    Dailycard(
                        DailyMissionTitle = GetUserDailyChallengeresults[i][0],
                        DailyFulfillConditions = GetUserDailyChallengeresults[i][1],
                        DailyChallengeList = GetUserDailyChallengeresults[i][2]
                    )
                )
                print(
                    i,"]list_daily_mission_list",'\n',
                    'DailyMissionTitle:' , GetUserDailyChallengeresults[i][0],'\n',
                    'DailyFulfillConditions:' , GetUserDailyChallengeresults[i][1],'\n',
                    'DailyChallengeList:' , GetUserDailyChallengeresults[i][2],'\n'
                )                
            except:
                pass   










    # Clock.schedule_once(on_enter)
    # Clock.schedule_once(on_tab_switch)
    # Clock.schedule_once(callback_for_menu_items)
    # Clock.schedule_once(show_example_grid_bottom_sheet)
        







