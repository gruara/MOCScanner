import pyforms
from   pyforms          import BaseWidget
from   pyforms.Controls import ControlText
from   pyforms.Controls import ControlButton
from   pyforms.Controls import ControlImage
from   pyforms.Controls import ControlEmptyWidget
from pysettings import conf
import settings
conf+=settings

class ScannerUI(BaseWidget):

    def __init__(self):
        super(ScannerUI,self).__init__('MOC Scanner')

        #Definition of the forms fields
        self._button1 = ControlButton('Scan')
        self._button2 = ControlButton('Save Image')
        self._image = ControlImage('Scanned Image')
        self._image.value = 'C:\\Users\\Andrew\\MOCScanner\\src\\Test Image.jpg'
        
#         print('there')
#         self._image1 = Image()
#         print('everywhere')
#         try:
#             self._image1.value = 'C:\\Users\\Andrew\\MOCScanner\\src\\Test Image.png'
#         except:
#             print('gone tits up')
#         self._image1.repaint()
        
class Image(BaseWidget):

    def __init__(self):
        super(Image,self).__init__('Image')
        self._panel = ControlEmptyWidget()

        #Definition of the forms fields
        self._image = ControlImage('Scanned Image')
        self._button1 = ControlButton('Bloody Hell')
        print( 'here')

#Execute the application
if __name__ == "__main__":   pyforms.start_app( ScannerUI )
