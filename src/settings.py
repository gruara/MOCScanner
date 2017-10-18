SETTINGS_PRIORITY = 1

#PYFORMS_MODE = 'TERMINAL'

PYFORMS_STYLESHEET = 'style.css'
PYFORMS_STYLESHEET_LINUX = 'style.css'

DEVICE_STRING   =  'Canon MG4200 series Network'
DEVICE_BYTES    = b'Canon MG4200 series Network'

# Can only get pytwain working with bmp at the moment!
SCAN_PATH = 'C:\\Users\\Andrew\\MOCScanner\\src\\Scan'

FILE_TYPE_JPEG  = '.jpg'
FILE_TYPE_BMP   = '.bmp'

FILE_TYPE = FILE_TYPE_JPEG

#
#  TWAIN Settings
#        see http://www.data-tech.com/help/imnettwain/Twain%20Capabilities.html
#
PIXEL_TYPE_BW   = 0
PIXEL_TYPE_GREY = 1
PIXEL_TYPE_RGB  = 2
PIXEL_TYPE_PAL  = 3

PIXEL_TYPE = PIXEL_TYPE_BW

UNIT_INCHES     = 0
UNIT_CM         = 1
UNIT_PICAS      = 2
UNIT_POINTS     = 3
UNIT_TWIPS      = 4
UNIT_PIXELS     = 5
UNIT_MM         = 6

UNITS = UNIT_INCHES

SCAN_AREA = (0.9,0.6,3.8,1.6) # X,Y,wIDTH,DEPTH