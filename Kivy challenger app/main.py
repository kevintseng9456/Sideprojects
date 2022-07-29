from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.clock import Clock
from synology_api import vpn

from libs.screenmanager import screenmanager
from libs.screens.home_page import HomePage 
from libs.screens.login_page import LoginPage
from libs.screens.signup_page import SignupPage
from libs.screens.challenge_data_page import Challenge_data_page
from libs.screens.challenge_name_page import Challenge_name_page
from libs.screens.Upload_form_page import Upload_form_page
# from libs.screens.camera_page import Camera_page




class ChallengerApp(MDApp):
    UserID = 1
    Username = ''
    GetMissionTopicID = 1
    GetMissionTypeID = 1
    pre_mission_name = ""
    GetMissionNameID = 1
    camera_pic = ''
    GetMissionAuthor = ''

    font_name = './font/Droid-Sans-Fallback.ttf'
    font_size = '12sp'
    card_radius = [12]
    card_left_right_padding = '16dp'
    card_and_card_padding = '8dp'


    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green" 
        # self.theme_cls.secondary_text_color = "Gray"
        # Window.size = [412, 892]
        Window.size = [412, 750]
        self.load_all_kv_files()
        
        return screenmanager()

    def load_all_kv_files(self):
        Builder.load_file('libs/screenmanager.kv')
        Builder.load_file('libs/screens/login_page.kv')
        Builder.load_file('libs/screens/signup_page.kv')
        Builder.load_file('libs/screens/home_page.kv')
        Builder.load_file('libs/screens/challenge_name_page.kv')
        Builder.load_file('libs/screens/challenge_data_page.kv')
        Builder.load_file('libs/screens/Upload_form_page.kv')
        # Builder.load_file('libs/screens/camera_page.kv')
        # Builder.load_file('libs/screens/camera_page.kv')

        Builder.load_file('libs/components/appbar01.kv')
        Builder.load_file('libs/components/appbar02.kv')
        Builder.load_file('libs/components/appbar03.kv')
        Builder.load_file('libs/components/missionpage.kv')
        Builder.load_file('libs/components/challenge_name_card.kv')
        Builder.load_file('libs/components/postcard.kv')
        Builder.load_file('libs/components/acceptcard.kv')
        Builder.load_file('libs/components/personal_list.kv')
        Builder.load_file('libs/components/challenge_list.kv')
        Builder.load_file('libs/components/recommend.kv')
        Builder.load_file('libs/components/dailycard.kv')
        # Builder.load_file('libs/components/upload_form.kv')
        
        # Builder.load_file('libs/components/story_creator.kv')
        # Builder.load_file('libs/components/bottom_nav.kv')
        # Builder.load_file('libs/components/circular_avatar_image.kv')
        # Builder.load_file('libs/components/post_card.kv')

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        # instance_tab.ids.label.text = tab_text   
        pass
if __name__ == "__main__":
    # # count = 0
    # def my_callback(dt):
    #     # global count
    #     # count += 1
    #     # if count == 10:
    #     #     print('Last call of my callback, bye bye !')
            
    #     #     return False
    #     # # event.cancel()
    #     # print('My callback is called')
    #     # print("####  Clock  ##### \n",Clock.get_events()," \n######## clock #########")
    #     print("####  Clock  ##### \n",Clock.get_fps()," \n######## clock #########")
    #     print("#### r Clock  ##### \n",Clock.get_rfps()," \n######## clock #########")
    #     print("#### t Clock  ##### \n",Clock.get_time()," \n######## clock #########")
    #     print("#### i Clock  ##### \n",Clock.idle()," \n######## clock #########")
    # event = Clock.schedule_interval(my_callback,2)
    ChallengerApp().run()