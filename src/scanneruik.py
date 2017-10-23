
import kivy
kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.logger import Logger
from kivy.properties import ObjectProperty, StringProperty

import twain
from tkinter import *
from tkinter import messagebox
import settings
import datetime
import os
import base64

root = Tk()
root.title('scan.py')

file = ''

class MOCScanner(GridLayout):
    logapp = 'Scan: '
    Logger.info(logapp + 'Now I is here')
    background = StringProperty()
    bg = 1
    
# For some reason when setting an initial image here the image does not 
# chane in the do_action even thoughit looks like background is being set
# correctly
#    background ='Test Image.png'

    def do_action(self):
        Logger.info(self.logapp + 'Who\'s there?')
        if self.bg == 1:
            self.background = 'Test Image2.png'
            self.bg = 2
        else:
            self.background = 'Test Image.png'
            self.bg = 1
            
    def do_scan(self):
        global file 
        Logger.info(self.logapp + 'My favourite - Scanning')
        try:
            dso = twain.SourceManager(root).open_source(settings.DEVICE_BYTES)
        except:
            Logger.info(self.logapp + 'Can\'t open scanner')
            
        dso.set_capability(twain.ICAP_FRAMES,twain.TWTY_FRAME, settings.SCAN_AREA)
        dso.set_capability(twain.ICAP_UNITS,twain.TWTY_INT16,settings.UNITS)
        dso.set_capability(twain.ICAP_PIXELTYPE,twain.TWTY_INT16,settings.PIXEL_TYPE)
        dso.set_image_layout(settings.SCAN_AREA)
        try:
            dso.acquire_file( before=GetName, show_ui=False )
        except:
            Logger.info(self.logapp + 'Something\'s gone wrong')
            dso.close()
    
        dso.close()

        self.background = file
        Logger.info(self.logapp + 'Scanned to '  + file) 
        
    def do_download(self):
        pass

    def do_upload(self):
        global file 
        head, tail = os.path.split(file)
        print(file)
        print(head)
        print(tail)
        image = open(file, 'rb') #open binary file in read mode
        image_read = image.read()
        image_64_encode = base64.encodestring(image_read)
        
        
        restore = 'restore\\awgest.jpg'
        image_result = open(restore, 'wb') # create a writable image and write the decoding result
        image_result.write(base64.decodestring(image_64_encode))
        print(image_64_encode)
        
        
    
class ScannerApp(App):
    def build(self):
        Logger.info('Bloody hell I is here')
        return MOCScanner()
    
def GetName(imagedets):
        global file
        file = (settings.SCAN_PATH +
                '\\' +
                'img'+ 
                datetime.datetime.now().strftime('%Y%m%d%H%M') +
                '.' +
                settings.FILE_TYPE)
        return file

if __name__ == '__main__':
    ScannerApp().run()