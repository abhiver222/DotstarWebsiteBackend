'''
to run this, you'll need Google's Tesseract OCR project: https://code.google.com/p/tesseract-ocr/wiki/ReadMe#Installation
'''
import pytesseract,cStringIO,urllib,pymysql
from config import *
from PIL import Image,ImageOps

def build_res(row,solved):
    print('netid {0}, euler {1}, solved {2}'.format(row[0],row[1],str(solved)))

conn = pymysql.connect(host=DB_HOST,port=DB_PORT,user=DB_USER,passwd=DB_PASSWORD, db=DB_NAME)
cur = conn.cursor()
cur.execute('SELECT Netid,Euler FROM UserDetails')
conn.commit()
for row in cur:
    if row[1]==None:
        print('netid {0} has no account'.format(row[0]))
        continue
    try:
        original = Image.open(cStringIO.StringIO(urllib.urlopen('https://projecteuler.net/profile/{0}.png'.format(row[1])).read()))
    except IOError:
        print('netid {0}\'s account ({1}) doesn\'t exist'.format(row[0],row[1]))
        continue

    cropped = original.crop((0,43,100,12+43)) #yes, could move left to get rid of 'solved', but this decreases OCR accuracy
    solved = pytesseract.image_to_string(cropped)
    sp = solved.split(' ')
    number = 0
    if len(sp) == 1:
        build_res(row,0)
    elif sp[1] == 'e':
        build_res(row,6)
    elif sp[1].lower() == 'i':
        build_res(row,1)
    elif sp[1].lower() == '3n':
        build_res(row,30)
    else:
        build_res(row,sp[1])



cur.close()
conn.close()
