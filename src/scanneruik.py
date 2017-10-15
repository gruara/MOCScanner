
import kivy
kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.logger import Logger
from kivy.properties import ObjectProperty, StringProperty


class MOCScanner(GridLayout):
    Logger.info('Now I is here')
    background = StringProperty()
    bg = 1
# For some reason when setting an initial image here the image does not 
# chane in the do_action even thoughit looks like background is being set
# correctly
#    background ='Test Image.png'

    def do_action(self):
        Logger.info('Who\'s there?')
        if self.bg == 1:
            self.background = 'Test Image2.png'
            self.bg = 2
        else:
            self.background = 'Test Image.png'
            self.bg = 1 
    
class ScannerApp(App):
    def build(self):
        Logger.info('Bloody hell I is here')

        return MOCScanner()

if __name__ == '__main__':
    ScannerApp().run()