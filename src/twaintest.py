import twain
from tkinter import *
from tkinter import messagebox

#FIX needed to twain.py to change 'import Image' to below to allow non .bmp files
from  PIL import Image
import settings
import datetime


root = Tk()
root.title('scan.py')



def twa():
    print(twain.version())
 
 #   scanners = twain.SourceManager(root).source_list

 #   ds = scanners[0]
    try:
        dso = twain.SourceManager(root).open_source(settings.DEVICE_BYTES)
    except:
        print('Aaaaaaaaaaaaaahhh')


    print(dso.get_capability_current(twain.ICAP_MINIMUMWIDTH))
    print(dso.get_capability_current(twain.ICAP_MINIMUMHEIGHT))    
    print(dso.get_capability_current(twain.ICAP_PHYSICALWIDTH))
    print(dso.get_capability_current(twain.ICAP_PHYSICALHEIGHT))
    print(dso.get_capability_current(twain.ICAP_FRAMES))
    
    dso.set_capability(twain.ICAP_FRAMES,twain.TWTY_FRAME, settings.SCAN_AREA)
#    OR
#    dso.set_image_layout((0.9,0.6,3.8,1.6))


    dso.set_capability(twain.ICAP_UNITS,twain.TWTY_INT16,settings.UNITS)
    dso.set_capability(twain.ICAP_PIXELTYPE,twain.TWTY_INT16,settings.PIXEL_TYPE)
#    dso.set_image_layout(settings.SCAN_AREA)
    
    try:
        dso.acquire_file( before=GetName, show_ui=False )
    except:
        print('ooooooooooohhhhhhhh')
        dso.close()

    dso.close()
    print(dso.file_xfer_params)
    
    

    
def GetName(imagedets):
    print(imagedets)
    file = 'img'+ datetime.datetime.now().strftime('%Y%m%d%H%M')
    return settings.SCAN_PATH + '//' + file + settings.FILE_TYPE 

if __name__ == '__main__':
    twa()    