from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.properties import StringProperty


from libs.components.challenge_name_card import Challenge_name_card
from libs.screenmanager import screenmanager
from libs.database.DB import DB
from libs.nas_server import nas_api


class Challenge_name_page(MDScreen):
    namemissionsource =StringProperty("")
    def on_enter(self, *args):
        app = MDApp.get_running_app()
        GetMissionNameresults = DB().GetMissionName(int(app.GetMissionTypeID))
        if GetMissionNameresults != '':
            '''Creates a list of cards.'''
            self.ids.name_mission_grid.clear_widgets()
            for i in range(len(GetMissionNameresults)):
                self.ids.name_mission_grid.add_widget(
                    Challenge_name_card(
                        namemissionsource = nas_api.Nas_geturl().show_pic(GetMissionNameresults[i][4]),
                        GetMissionNameID = GetMissionNameresults[i][2],
                        pre_mission_name = GetMissionNameresults[i][3]
                    )
                )
                print(
                    i,']Challenge_name_page\n',
                    'namemissionsource:',nas_api.Nas_geturl().show_pic(GetMissionNameresults[i][4]),'\n',
                    'Username' ,app.Username,'\n',
                    'pre_mission_name' ,GetMissionNameresults[i][3],'\n',
                    'GetMissionNameID' ,GetMissionNameresults[i][2],'\n',
                )
        return super().on_enter(*args)

    def callback(self):
        app = MDApp.get_running_app()
        app.root.current = 'home'
        print("------home------") 