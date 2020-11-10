from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.tab import MDTabsBase

KV =  '''
BoxLayout:
    orientation:'vertical'
    MDScreen:
        ScreenManager: 
            id:screen_manager
            MainScreen:
            SettingsScreen:
            AboutScreen:
             

    MDToolbar:
        id: button
        title: 'Shopping list'
        right_action_items: [["dots-vertical", lambda x: app.menu.open()]]
    
    MDTabs:
        Tab:
            text: "History"
            MDLabel:
                text: 'History purchase'
                halign: 'center'

        Tab:
            text: "Active"
            MDLabel:
                text: 'Active items'
                halign: 'center'
<MainScreen>:
    name: 'main'
    MDLabel:
        text: 'Main'
        halign: 'center'

<SettingsScreen>:
    name: 'settings'
    MDLabel:
        text: 'Settings'
        halign: 'center'
        
<AboutScreen>:
    name: 'about'
    MDLabel:
        text: 'About'
        halign: 'center'
'''

class MainScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class AboutScreen(Screen):
    pass



class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class MyApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        menu_items = [{"text": 'Settings'},{"text": 'About project'}]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.button,
            items=menu_items,
            width_mult=4
        )
        self.menu.bind(on_release=self.callback)

    def callback(self,instance_menu, instance_menu_item):
        print(instance_menu, instance_menu_item.text)
        if instance_menu_item.text == 'Settings':
            self.root.ids.screen_manager.current = 'settings'
        if instance_menu_item.text == 'About project':
            self.root.ids.screen_manager.current = 'about'

    def build(self):
        return self.screen


MyApp().run()