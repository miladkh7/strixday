# -*- coding: utf-8 -*-
# Use Python 3
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
import time
import datetime
from khayyam import JalaliDatetime
import requests
from StringIO import StringIO
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from io import BytesIO
import sys
reload(sys) 
sys.setdefaultencoding('UTF8')




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    comment = db.Column(db.String(400))

    def __init__(self, name, comment):
        self.name = name
        self.comment = comment
         
    def __repr__(self):
        return 'Name %r ' % self.name


@app.route('/')
def hello():
    return 'strix bot'

def handle(msg):
 content_type, chat_type, chat_id = telepot.glance(msg)
 if content_type == 'text':
    command = msg['text']
    print ('Got command: %s' % command)
    mss = command
    mss=mss.replace('/', ',')
    mss=mss.replace('.', ',')
    mss=mss.replace('-', ',')
    mss=mss.split(',')
    now =JalaliDatetime.now()
    zz=""
    zzz=''
    kk=0
    if len(mss)<3 :
         if command == 'Time':
             ss=str(datetime.datetime.now())
         elif command == '/help':
             sss= 'سلام واسه استفاده بايد تاريخ رو با يکي از فرمت هاي زير وارد کني' +'\n'+'1364/3/27'+'\n'+'1382-3-27'+'\n'+'1373.1.15'+'\n'+'1373,4,5'
             ss= str(sss)
         elif command == 'راهنما':
             sss= 'سلام واسه استفاده بايد تاريخ رو با يکي از فرمت هاي زير وارد کني' +'\n'+'1364/3/27'+'\n'+'1382-3-27'+'\n'+'1373.1.15'+'\n'+'1373,4,5'
             ss= str(sss)
         elif command == '/start':
            markupp = ReplyKeyboardMarkup(keyboard=[['راهنما']],resize_keyboard=True)
            bot.sendMessage(chat_id, "خیلی خوش اومدی لطفا یه تاریخ وارد کن", reply_markup=markupp)
         elif command == 'ممنون':
            ss=str("خواهش میکنم مهربون .. قابلی نداشت ")
         elif command == 'احمق':
             ss=str("خودتی")
         else :
           ss='اگه میشه تاریخ رو اینجوری وارد کن تا من بتونم بخونمش' + '\t' + '1372.11.5'
           kk=1
    else:
        
        
     databa=User.query.filter_by(name=str(chat_id))
     if databa.count()>0:
      tedadestefade=databa.count()
      com=databa[tedadestefade-1].comment
      sumofuse=db.session.query(User).count()
      markup = ReplyKeyboardMarkup(keyboard=[[command],['راهنما']],resize_keyboard=True)
      bot.sendMessage(chat_id, command, reply_markup=markup)
     old=JalaliDatetime(int(mss[0]),int(mss[1]),int(mss[2]))
     dif = [100,200,222,300,333,400,444,500,555,600,666,700,777,800,888,900,999,1000,1111,2000,2222,3000,3333,4000,4444,5000,5555,6000,6006,6116,6226,6336,6446,6556,6666,6776,6886,6996,7000,7007,7100,7117,7200,7227,7300,7337,7400,7447,7500,7557,7600,7667,7700,7777,7800,7887,7900,7997,8000,8100,8200,8228,8300,8338,8400,8448,8500,8558,8668,8778,8888,9000,9009,9999,10000,11111,12000,13000,14000,15000,16000,17000,18000,19000,20000,21000,22000,22222,23000,24000,25000,26000,27000]
     i=0
     d=(now-old).days
     if now.dayofyear()<old.dayofyear() :
       ruzt=old.dayofyear() -now.dayofyear()
     else :
       ruzt=old.dayofyear() + 365 - now.dayofyear()
  
     ss='سلام امروز ' +str(d)+ ' روزه هستی '
     ss=ss+"\n" + str(ruzt) + " روز مونده تا به دنیا بیای "
     zzz="      you are  " +str(d) +"  days old "
     cc=d
     for x in dif:
        dif1=datetime.timedelta(x)
        date=old+dif1
        jdate=JalaliDatetime(date)
        if (jdate>now and i<10):
             ss= ss + '\n' + str(jdate.strftime('%A %D %B %N')) +  ' میشی '+str(dif1.days) + " روزه "
             if (i<1):
               zz= zz + '\n'  +'You will be '+ str(dif1.days) + ' days old in the next ' + str(dif1.days - cc) +' days'

             i=i+1
     ss= ss +'\n' +'\n'+ str(tedadestefade) + " تعداد استفاده شما  "+'\n' + str(sumofuse) + " تعداد استفاده کل  "+'\n'+ 'مواظب خوبیات باش' +" @strixdaybot "
     zz= zz +'\n' +'\n' + '               Take care of your good behaviors' +'\n'+ '               and appreciate your days of life' +'\n'+'\n'+'\n'+'\n'+'\n' +'                             telegram: @strixdaybot '
     
     
    img = requests.get("http://behkaroma.ir/p.jpg")
    ff= requests.get("http://behkaroma.ir/p.ttf")
    font1 = ImageFont.truetype(StringIO(ff.content),30)
    font2 = ImageFont.truetype(StringIO(ff.content),40)
    font3 = ImageFont.truetype(StringIO(ff.content),50)

    image = Image.open(StringIO(img.content))
    draw = ImageDraw.Draw(image)
    draw.text((30, 150),zzz,(0,0,0),font=font3) 
    draw.text((20, 400),zz,(255,255,255),font=font1) 
    bio = BytesIO()
    bio.name = 'image.jpeg'
    image.save(bio, 'JPEG')
    bio.seek(0)
    if (kk==0):
     if len(zz)>10:
      bot.sendPhoto(chat_id, photo=bio)
    reg = User(str(chat_id),command)
    print(reg)
    db.session.add(reg)
    db.session.commit()
    bot.sendMessage(chat_id, text= ss )

bot = telepot.Bot('497132515:AAEv0n6J5iSbuu4LNFHmdojif6THnjYwKCI')
bot.message_loop(handle)
print ('I am listening ...')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    

while 1:
  time.sleep(10)
