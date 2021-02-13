try:
    from kivy.app import App
except ImportError:
    import pip._internal as pip
    pip.main(['install', 'kivy'])
    from kivy.app import App

import kivy

from kivy.app import App
from kivy.uix.label import Label


class PMGEWindow(App):

    def build(self):
        return Label(text='Hello world')

if __name__ == '__main__':
    PMGEWindow().run()