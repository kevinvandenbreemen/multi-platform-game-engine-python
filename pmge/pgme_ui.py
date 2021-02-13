from kivy.app import App
from kivy.uix.widget import Widget

import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label

class PMGEWindow(Widget):
    pass

class PMGEApp(App):
    def build(self):
        return PMGEWindow()

if __name__ == '__main__':
    PMGEApp().run()