from PIL import Image 
import os

path = ('gatto//')
dirs = os.listdir( path )

def grey():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imConv = im.convert('1') 
            imConv.save(f + 'result.jpg','JPEG', quality = 100)
            
grey()
