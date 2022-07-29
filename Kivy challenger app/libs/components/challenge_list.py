from kivymd.uix.gridlayout import MDGridLayout
from kivy.properties import StringProperty,ListProperty
from kivymd.app import MDApp
from kivymd.uix.bottomsheet import MDGridBottomSheet


from libs.database.DB import DB
from libs.components.acceptcard import Acceptcard


class Challenge_list(MDGridLayout):
    default_source = ListProperty(['',"./image/food_and_drink.png","./image/school_life.png"])

    def callback_for_menu_items(self, *args):
        app = MDApp.get_running_app()
        app.GetMissionTypeID = args[0]
        print("GetMissionTypeID : ",app.GetMissionTypeID)
        app.root.current = 'Challenge_name_page'
        print("------Challenge_name_page------") 


    def show_example_grid_bottom_sheet(self,topic_number):
        app = MDApp.get_running_app()
        app.GetMissionTopicID = topic_number
        print('GetMissionTopicID : ',app.GetMissionTopicID)

        bottom_sheet_menu = MDGridBottomSheet()

        # GetMissionTopicresults =  DB().GetMissionType(int(app.GetMissionTopicID))

        if topic_number == 2:
            data = {
                # '愛情': ["nature-people", 1],
                '歌曲': ["music-clef-treble", 2],
                '美食': ["food-fork-drink", 3],
            }
        else:
            data = {
                '愛情': ["nature-people", 1] ,
                # '歌曲': ["music-clef-treble", 2],
                # '美食': ["food-fork-drink", 3] ,
            }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[1][1]: self.callback_for_menu_items(y),
                icon_src=item[1][0],
            )
        bottom_sheet_menu.open()  