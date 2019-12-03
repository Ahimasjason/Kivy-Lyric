#:import utils kivy.utils
import sys
import webbrowser
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
import kivy.utils as utils
from .songs import *

Builder.load_file('application/app_layout.kv')

class FullImage(Image):
    pass

class CatScreen(Screen):
    pass

    def changer(self ,*args):
        pass

    def not_implemented(self,*args):

        popup = Popup(title='Not Implemented',
                    content=Label(text='will implemented later ........'),

                    size_hint=(None, None), size=(400, 400)
        )
        popup.open()

    def about(self,*args):
        webbrowser.open('https://github.com/Ahimasjason/Kivy-Lyric')

    def exit_screen(self,*args):
        sys.exit()

class SongsSelectScreen(Screen):
    pass
    def changer(self,*args):
        self.manager.get_screen('lyrics').set_song(args[0])
        self.manager.transition.direction = 'left'
        self.manager.current = 'lyrics'

class LyricsScreen(Screen):

    lyric_sc = StringProperty('')
    song_title = StringProperty('')

    def set_song(self,*args):
        song = args[0]
        song_list = song.split('_')
        song_title = ' '.join(char.upper() for char in song_list )
        self.lyric_sc =eval(song)
        self.song_title = song_title
    def changer(self,*args):
        '''
        `meth`
            To go back from Lyric screen song select screen
        '''
        # self.ids['lyric_back_button'].background_color = 1.0, 0.0, 0.0, 1.0
        self.manager.current ='SelectSong'

class MainApp(App):
    def __init__(self,**kw):
        super(MainApp,self).__init__(**kw)
        self.sm = ScreenManager()
        self.sm.add_widget(CatScreen(name='Catagory'))
        self.sm.add_widget(LyricsScreen(name='lyrics'))
        self.sm.add_widget(SongsSelectScreen(name='SelectSong'))

    def build(self):
        return self.sm


# if __name__ == '__main__':
#     app = MainApp()
#     app.run()
