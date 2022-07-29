from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivymd.app import MDApp

from libs.database.DB import DB
from libs.components.acceptcard import Acceptcard
from libs.nas_server import nas_api

class Personal_list(MDBoxLayout):
    print("INININ")
    def on_enter(self):

        app = MDApp.get_running_app()
        UserAcceptMissionListresults = DB().GetUserAcceptMissionList(int(app.UserID))
        print("UserAcce",len(UserAcceptMissionListresults))

        for i in range(len(UserAcceptMissionListresults)):

            self.ids.acceptcard_box.add_widget(
                Acceptcard(
                    post = nas_api.Nas_geturl().show_pic(UserAcceptMissionListresults[i][4]),
                    GetMissionName = UserAcceptMissionListresults[i][3],
                    GetMissionFinish = UserAcceptMissionListresults[i][5]
                )
            )  
            print(
                i,"]Personal_list",'\n',
                'post:',nas_api.Nas_geturl().show_pic( UserAcceptMissionListresults[i][4]),'\n',
                "GetMissionName:",UserAcceptMissionListresults[i][1],'\n',
                'GetMissionFinish:',UserAcceptMissionListresults[i][0],'\n'
            )             