
#Imports
import pyttsx3
#********************************************
def voice(inputu):
    engine.say(inputu)
    engine.runAndWait()  
engine=pyttsx3.init()
voice('initializing edupudi')
voice('i am edupudi, , created by sibi')
#********************************************
from tkinter import *
import time as t
import subprocess as sp
import os
import datetime as dt
import psutil
import pydictionary as pd
import random
import socket
import webbrowser
import wikipedia
import speech_recognition as sr
from bs4 import BeautifulSoup as bs
import requests

#********************************************
#Functions
class RoundedButton(Canvas):
    def __init__(self, parent, width, height, cornerradius, padding, color, bg, command=None):
        Canvas.__init__(self, parent, borderwidth=0, 
            relief="raised", highlightthickness=0, bg=bg)
        self.command = command

        if cornerradius > 0.5*width:
            print("Error: cornerradius is greater than width.")
            return None

        if cornerradius > 0.5*height:
            print("Error: cornerradius is greater than height.")
            return None

        rad = 2*cornerradius
        def shape():
            self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=color, outline=color)
            self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=color, outline=color)
            self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=color, outline=color)
            self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=color, outline=color)
            self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=color, outline=color)


        id = shape()
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0)
        height = (y1-y0)
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()
def adt():
  global frontwin
  global win
  def sav(a):
    global frontwin
    global win
    fyl=open('TTD.txt','r')
    chk=fyl.read()
    fyl.close()
    if chk =='' or chk==' ':      
      fyl=open('TTD.txt','a')
      fyl.write(a.widget.get())
      fyl.close()
    else:
      fyl=open('TTD.txt','a')
      fyl.write('\n'+a.widget.get())
      fyl.close()
    win.destroy()
    voice('item added sir')
    start()
  win=Tk()
  a=Entry(win)
  a.pack()
  a.bind("<Return>",sav)

def velapannu(query):
    global frontwin
    global voichn
    global win
    if 'open' in query.lower():
        if socket.gethostbyname(socket.gethostname())!="127.0.0.1":
            query=query.lower()
            query=query.split(' ')
            if query.count('open')>1:
                for i in range(query.count('open')-1):
                    query.remove('open')
            if query[-1]=='open':
                url=str(query[-2]+'.com')
            else:
                url=str(query[query.index('open')+1]+'.com')
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            voice('opening , '+ url)
            webbrowser.get(chrome_path).open(url)
            start()

        else:
          voice('sorry sir system is not connected to internet')
          start()
    elif 'wikipedia' in  query.lower():
        if socket.gethostbyname(socket.gethostname())!="127.0.0.1":
            try:
                query=query.replace("wikipedia","")
                prt=wikipedia.summary(query,sentences=2)
                voice('according to wikipedia , '+prt)
                win=Tk()
                initi=0
                countu=0
                for i in range(0,len(prt),30):
                    if i==(len(prt)//30)*30:
                        Label(win,text=prt[initi:]).grid(row=countu,column=0)
                    else:
                        Label(win,text=prt[initi:i]).grid(row=countu,column=0)
                    initi=i
                    countu+=1
                start()
            except:
                voice('sorry no data available')
                start()
        else:
              voice('sorry sir system is not connected to internet')
              start()
    elif 'meaning' in query.lower():
        if socket.gethostbyname(socket.gethostname())!="127.0.0.1":
            query=query.lower()
            if len(query.split(' '))==2:
                query=query.replace("meaning","")
                prt=pd.PyDictionary.meaning(query)
                prt=prt['Noun']
                if len(prt)>3:
                    prt=prt[:4]
            else:
                query=query.split(' ')
                prt=''
                for i in range(0,len(query)):
                    if query[i]=='meaning' and query[i+1]=='of' and (i+2)<=len(query):
                        prt=query[i+2]
                prt=pd.PyDictionary.meaning(prt)
                prt=prt['Noun']
                if len(prt)>3:
                    prt=prt[:4]
            voice(prt)
            win=Tk()
            initi=0
            countu=0
            wrd=''
            for i in prt:
                wrd+=i+'/'
            for i in range(0,len(wrd),30):
                if i==(len(wrd)//30)*30:
                    Label(win,text=wrd[initi:]).grid(row=countu,column=0)
                else:
                    Label(win,text=wrd[initi:i]).grid(row=countu,column=0)
                initi=i
                countu+=1
            start()
        else:
              voice('sorry sir system is not connected to internet')
              start()
    elif 'say' in query.lower():
        query=query.lower()
        query=query.replace('say','')
        voice(query)
        start()
    #elif 'weather' in query.lower():
     #   if socket.gethostbyname(socket.gethostname())!="127.0.0.1":
      #      weather()
       #     start()
        #else:
         #   voice('sorry sir system is not connected to internet')
          #  start()
    elif 'start' in query.lower():
        for i in range (len(query.split(' '))):
            if query.split(' ')[i].lower()=='start':
                starting=i+1
        try :
            os.system('start '+str(query.split(' ')[starting]))
        except:
            voice('no file found')
        start()
    elif query.lower() in ['bye','goodbye','see you']:
        voice('bye bye')
        close()
    elif 'flip a coin' in query.lower():
        voice('its '+['heads','tails'][random.randint(0,1)])
        start()
    elif 'activate' in query.lower()and 'protocol' in query.lower():
        query=query.lower()
        query=query.replace('activate ','')
        query=query.replace(' protocol','')
        if query=='intro':
            voice('I am edupudi , your personal assistant.')
            voice('i was made by sibi muukil using python.')
            voice('i can help you to simplify your tasks.')
            voice('here is the list of things i can do.')
            voice('i can open applications present in quick actions.')
            voice('i can maintain a todo list . i can open websites for you.')
            voice('i can search in wikipedia  . i can even give you meaning of words.')
            voice('but sorry ennala thamil pesa mudiyathu')
            voice('so lets get started')
            start()
        elif query=='voicechange':
            engine.setProperty('voice',(['']+engine.getProperty('voices'))[voichn].id)
            voichn=voichn*(-1)
            voice('voice changed sir')
            start()
        else:
            voice("no protocol available")
            start()
            
    else:
        voice('sorry sir, ,i dont get you')
        start()

def inpu():
  global frontwin
  def order(inp):
      inp=inp.widget.get()
      velapannu(inp)
  inp=Entry(frontwin)
  Label(frontwin,text='Command Box',relief='ridge').grid(row=9,column=0)
  inp.grid(row=10,column=0,ipadx=15)
  inp.bind("<Return>",order)  

def micset():
    if socket.gethostbyname(socket.gethostname())!="127.0.0.1":
        r=sr.Recognizer()
        with sr.Microphone() as source:
          voice('listening')
          audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language='en-in')
            print(f"recognizing: {query}\n")
            velapannu(query)
        except:
            voice('sorry sir, speech not recognized')
    else:
        voice('sorry sir, no network')
        start()
def micbutton():
    global frontwin
    RoundedButton(frontwin,25,25,12.4,2,'red2','gray95',command=micset).grid(row=11,column=0)
    Label(frontwin,text='MIC').grid(row=12,column=0)
def det():
  global frontwin
  global win
  try:
    def sav(a):
      global frontwin
      global win
      fyl=open('TTD.txt','r')
      wrt=fyl.readlines()
      fyl.close()
      wrt=wrt[:int(a.widget.get())-1]+wrt[int(a.widget.get()):]
      fyl=open('TTD.txt','w+')
      for i in wrt:
        fyl.write(i)
      fyl.close()
      win.destroy()
      voice('item deleted sir')
      start()
    win=Tk()
    a=Entry(win)
    a.pack()
    a.bind("<Return>",sav)
  except:
    print('')


def time():
  global tim
  string = t.strftime('%I:%M:%S %p') 
  tim.config(text = string) 
  tim.after(1000, time)
  
def batter():
  global batt
  battery=psutil.sensors_battery()
  percent=str(battery.percent)
  batt.config(text=percent+'%')
  batt.after(1000,batter)
  
def plugge():
  global plug
  battery=psutil.sensors_battery()
  plugged=battery.power_plugged
  if plugged==False: plugged="Not Plugged"
  else: plugged='Plugged'
  plug.config(text=plugged)
  plug.after(1000,plugge)
  
def date():
  global dat
  string = dt.datetime.now().strftime('%x')
  dat.config(text = string) 
  dat.after(1000, date)
  
def net_():
  global net
  I=socket.gethostbyname(socket.gethostname())
  k=''
  if I=="127.0.0.1":
      k='No Network'
  else :
      k='In Network'
  net.config(text = k)
  net.after(1000, net_)
def day_():
  global day
  string = dt.datetime.now().strftime('%A') 
  day.config(text = string) 
  day.after(1000, day_)
  
def calc():
    voice('opening calculator')
    sp.Popen('C:\\Windows\\System32\\calc.exe')
    start()
  
def paint():
    voice('opening paint')
    sp.Popen('C:\\Windows\\System32\\mspaint.exe')
    start()
  
def cmd():
    voice('opening command prompt')
    sp.Popen('C:\\Windows\\System32\\cmd.exe')
    start()

def pyth():
    voice('opening python')
    sp.Popen('C:\\Users\\SIBI MUGHIL\\AppData\\Local\\Programs\\Python\\Python36\\pythonw.exe')
    start()
    
def ggl():
    voice('opening chrome')
    sp.Popen('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
    start()
  
def np():
    voice('opening notepad')
    sp.Popen('C:\\Windows\\System32\\notepad.exe')
    start()
  
def ex():
    voice('opening excel')
    os.system("start EXCEL.EXE")
    start()
    
def dx():
    voice('opening word')
    os.system("start WINWORD.EXE")
    start()
    
def wp():
    voice('opening whatsapp')
    try:
        sp.Popen("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_0.4.930.0_x64__cv1g1gvanyjgm\\app\\WhatsApp.exe")
    except:
        voice('whatsapp not found')
    start()

def close():
    global frontwin
    frontwin.destroy()
    
def ppt():
    voice('opening powerpoint')
    os.system("start POWERPNT.EXE")
    start()

def quick():
  global frontwin
  Label(frontwin,text='Quick Actions:',relief='ridge').grid(row=0,column=1,ipadx=3,ipady=5)
  Button(frontwin,text='Calculator',command=calc,relief="ridge").grid(row=1,column=1,ipadx=12,ipady=4)
  Button(frontwin,text='Paint',command=paint,relief="ridge").grid(row=2,column=1,ipadx=25,ipady=4)
  Button(frontwin,text='Command',command=cmd,relief="ridge").grid(row=3,column=1,ipadx=10,ipady=4)
  Button(frontwin,text='Google',command=ggl,relief="ridge").grid(row=4,column=1,ipadx=19,ipady=4)
  Button(frontwin,text='Notepad',command=np,relief="ridge").grid(row=5,column=1,ipadx=15,ipady=4)
  Button(frontwin,text='Word',command=dx,relief="ridge").grid(row=6,column=1,ipadx=24,ipady=4)
  Button(frontwin,text='Excel',command=ex,relief="ridge").grid(row=7,column=1,ipadx=25,ipady=4)
  Button(frontwin,text='PowerPoint',command=ppt,relief="ridge").grid(row=8,column=1,ipadx=8,ipady=4)
  Button(frontwin,text='WhatsApp',command=wp,relief="ridge").grid(row=9,column=1,ipadx=11,ipady=4)
  Button(frontwin,text='Python',command=pyth,relief="ridge").grid(row=10,column=1,ipadx=19,ipady=4)
  Button(frontwin,text='Status',command=info,relief="ridge").grid(row=11,column=1,ipadx=22,ipady=4)
  Button(frontwin,text='Close',command=close,relief="ridge").grid(row=12,column=1,ipadx=24,ipady=4)

def info():
    battery=psutil.sensors_battery()
    plugged=battery.power_plugged
    batty=str(battery.percent)
    if plugged==False: plugged="Not Plugged"
    else: plugged='Plugged'
    string = dt.datetime.now().strftime('%x')
    I=socket.gethostbyname(socket.gethostname())
    k=''
    if I=="127.0.0.1":
        k='is Not in any Network'
    else :
        k='is In a Network'
    st = dt.datetime.now().strftime('%A')
    voice('system status')
    voice('current time '+t.strftime('%I:%M:%S %p'))
    voice(string)
    voice('today is '+st)
    #if I!='127.0.0.1':
        #weather()
    voice('battery status is'+batty+' percent and '+plugged)
    voice('system '+k)
def sttd():
    os.system("start TTD.txt")
    
def reminder():
    global frontwin
    Button(frontwin,text='Reminder:',relief='ridge',command='').grid(row=6,column=0)
    Button(frontwin,text='Today',relief='ridge',command='').grid(row=7,column=0)
    f1=Frame(frontwin)
    f1.grid(row=8,column=0)
    Button(f1,text='Add',relief='ridge',command='').grid(row=0,column=0)
    Button(f1,text='Delete',relief='ridge',command='').grid(row=0,column=1)
    
def start():
  global tim
  global batt
  global plug
  global dat
  global day
  global net
  global frontwin
  frontwin.destroy()
  frontwin=Tk()
  frontwin.title('EDUPUDI')
  quick()
  inpu()
  reminder()
  micbutton()
  TTD=open('TTD.txt','r')
  ttd=TTD.readlines()
  TTD.close()
      
  Button(frontwin,text='Things To Do:',command=sttd,relief="ridge").grid(row=0,column=3,ipady=4)
  
  cnt=1
  while cnt<=len(ttd) and cnt<12:
    Label(frontwin,text=str(cnt)+'.'+ttd[cnt-1]).grid(row=cnt,column=3)
    cnt+=1
  while cnt<=len(ttd) and cnt<22:
    Label(frontwin,text=str(cnt)+'.'+ttd[cnt-1]).grid(row=cnt-11,column=4)
    cnt+=1
    
  Button(frontwin,text='Add',command=adt,relief="ridge").grid(row=12,column=3,ipadx=50,ipady=4)
  Button(frontwin,text='Delete',command=det,relief="ridge").grid(row=12,column=4,ipadx=50,ipady=4)
  
  tim = Label(frontwin)
  tim.grid(row=0,column=0)
  time()
  
  batt=Label(frontwin)
  batt.grid(row=3,column=0)
  batter()
  
  plug=Label(frontwin)
  plug.grid(row=4,column=0)
  plugge()
  
  dat = Label(frontwin)
  dat.grid(row=1,column=0)
  date()
  
  day = Label(frontwin)
  day.grid(row=2,column=0)
  day_()

  net = Label(frontwin)
  net.grid(row=5,column=0)
  net_()
  frontwin.mainloop()
#********************************************

voice(['welcome Sibi','hi Sibi','good to see you Sibi','hello sibi'][random.randint(0,3)]+' sir')

#********************************************


#variables
tim=''
batt=''
plug=''
dat=''
day=''
net=''
win=''
voichn=-1

#********************************************

if input('Press enter to continue:')!='$':
    info()
#********************************************
    
frontwin=Tk()
frontwin.title('EDUPUDI')
start()
#********************************************

input()
