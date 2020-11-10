from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.tab import MDTabsBase

KV = '''
BoxLayout:
    orientation:'vertical'
    
    MDToolbar:
        id: button
        title: 'Shopping list'
        right_action_items: [["dots-vertical", lambda x: app.menu.open()]]
            
    ScreenManager: 
        id:screen_manager
        MainScreen:
        SettingsScreen:
        AboutScreen:

<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"

    MDTextField:
        hint_text: "City"

    MDTextField:
        hint_text: "Street"
  
<MainScreen>:
    name: 'main' 
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
    MDFloatingActionButton:
        icon: "plus"
        pos_hint: {"center_x": .9, "center_y": .1}
        md_bg_color: [0.11372549019607843, 0.9137254901960784, 0.7137254901960784, 1.0]
        on_release: app.show_alert_dialog()


<SettingsScreen>:
    name: 'settings'
    MDIconButton:
        id: back_from_settings
        icon: "arrow-left"
        pos_hint: {"center_x": .075, "center_y": .95}
        on_release: app.back_to_main_menu()
    MDLabel:
        text: 'Settings'
        halign: 'center'
        
<AboutScreen>:
    name: 'about'
    MDIconButton:
        id: back_from_about
        icon: "arrow-left"
        pos_hint: {"center_x": .075, "center_y": .95}
        on_release: app.back_to_main_menu()
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
    pass

class Content(BoxLayout):
    pass

class MyApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.button,
            # caller=self.screen.ids.screen_manager.get_screen('main').ids.button,
            items=[{"text": 'Settings'}, {"text": 'About project'}],
            width_mult=4
        )
        self.menu.bind(on_release=self.callback)
        self.dialog = MDDialog(
            title="Address:",
            type="custom",
            content_cls=Content(),
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color
                ),
                MDFlatButton(
                    text="OK", text_color=self.theme_cls.primary_color
                ),
            ],
        )

    def show_alert_dialog(self):
        self.dialog.open()

    def back_to_main_menu(self):
        self.root.ids.screen_manager.current = 'main'

    def callback(self, instance_menu, instance_menu_item):
        if instance_menu_item.text == 'Settings':
            self.root.ids.screen_manager.current = 'settings'
        if instance_menu_item.text == 'About project':
            self.root.ids.screen_manager.current = 'about'
        instance_menu.dismiss()

    def build(self):
        return self.screen


MyApp().run()
