from PIL import Image 
import os

path = ('elefante/')
dirs = os.listdir( path )

def rgray():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            img = im.resize((100, 100), Image.ANTIALIAS)
            imConv = img.convert('1') 
            imConv.save(f + 'result.jpg','JPEG', quality = 100)
            
rgray()
