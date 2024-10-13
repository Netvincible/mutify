#!/usr/bin/env python3
from kivy.uix.screenmanager import RiseInTransition
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.modalview import ModalView
from kivy.animation import Animation
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.uix.popup  import Popup
from kivy.uix.image import Image
from kivy.uix.label import Label
from datetime import datetime
from kivy.clock import Clock
from kivy.app import App
import time
import subprocess
import sys
import os

LabelBase.register(name="Elianto",fn_regular='Elianto-Regular.ttf')

class startup(Animation, RiseInTransition,RelativeLayout):
    def __init__(self, **args):
        super(startup).__init__(**args)
        intrologo=Image(source="netvincible.png", size_hint=(.1,.1), pos_hint={'center_x':0,'center_y':0}, opacity=0)
        jump_in=Animation(pos_hint={'center_x':.5,'center_y':.5},)
        jump_in.start(intrologo)
        jump_in.bind(on_complete=self.nextwindow)
    
    def nextwindow(self,event):
        transi=RiseInTransition(design())
        self.add_screen(transi)

class design(RelativeLayout):
    def __init__(self, **kwargs):
        super(design,self).__init__()
        Window.size=(1366,768)

        with self.canvas.before:
            self.canvas.opacity=1
            Rectangle(pos=(133,20), size=(1100,768), source='background.png')

        self.heading=self.add_widget(Label(text="MUTIFY",font_name="Elianto",
            font_size=50,
            size_hint=(0.3,0.3),
            color='#00FFFF',
            pos_hint= { 'center_x':0.5 ,'center_y':0.9}))

        global view
        view = ModalView(size_hint=(None, None), size=(450, 400))

        con=Popup(title="About Us",title_font='Elianto',title_size=20,content=Label(text="Hi!, This is Mutify, an app developed by Netvincible,\nwhich will mute spotify when Ads are being played \nand unmute automatically when Ads are over. \nThis App also features media controls, and displays \ntrack title. Melody Saver Right?. There's a lot of hardwork \nand patience behind making of this App by a 11th grade newbie.\n also a future IITian. \nTHANK ME LATER!!! "
        , pos_hint={'center_x':0.5, 'center_y':0.7}))
        view.add_widget(con)
        
        close=Button(text="OK", 
        size_hint=(0.25,0.1),pos=(10,10),
        pos_hint={'x':None, 'y':None })
        
        view.add_widget(close)
        close.bind(on_press=view.dismiss)

        # view.add_widget(Image(source='netvincible.png',
        # size_hint=(0.3,0.3), pos_hint={'x':.5, 'y':0.1}))
        global ads_muted
        
        global ad_num
        with open('/home/netvincible/Documents/Python/Mutify/log.txt', 'r') as file:
            content = file.read()
        words = content.split()

        var= "var"
        ad_num=""

        for i in range(len(words)):
            if words[i] == var and i<len(words) - 1:
                ad_num= words[i+1]
                break

        ads_muted=Label(text=f"Ads Muted={ad_num}",size_hint=(.2,.2),pos_hint={'center_x':.25,'center_y': .75},color='#FFA500')
        self.add_widget(ads_muted)
        
        self.ibutton= infobutton(size_hint=(0.15,0.15),
            pos_hint={'center_x':0.8,'center_y':0.9 })
        self.add_widget(self.ibutton)
        
        self.ext1=self.add_widget(Label(text="~Powered by Netvincible",
            right=1,
            pos_hint= {'center_x':0.8, 'center_y':0.8} ,
            size_hint=(0.15,0.15),
            font_size= 20,
            color='#FFA500'))

        global ext3
        ext3=Label(text='click above for song name \n',
            font_size="30",
            pos_hint={"center_x":0.5, "center_y":0.33},
            size_hint=(0.25,0.2),
            color="#FFA500")

        self.add_widget(ext3)

        ext2=titlebutton(pos_hint={'center_x': .5, 'center_y':.575},size_hint=(.3,.4))
        self.add_widget(ext2)

        self.forward=forwbutton(size_hint=(0.2,0.2), pos_hint={'center_x':.76, 'center_y':.58})
        self.add_widget(self.forward)
        
        global pause
        pause=pausebutton(size_hint=(.15,.15),pos_hint={'center_x':0.5, 'center_y':.25})
        self.add_widget(pause)

        self.rewind=rewindbutton(size_hint= (.2,.2), pos_hint={'center_x':0.24, 'center_y':.58})
        self.add_widget(self.rewind)

        global ON
        ON = start_stop(size_hint=(0.18, 0.18),pos_hint={'center_x':0.25, 'center_y':0.25})
        self.add_widget(ON)

        self.close= Button(text="Close",font_size=20, size_hint=(0.75,0.15) ,pos_hint={'center_x':0.5,'center_y':0.075}, background_color= '#FF0000')
        self.close.bind(on_press=self.closecode)
        self.add_widget(self.close)


    def closecode(self, event):
        os.system('kill $(pgrep source_linux.sh)')
        sys.exit(0)

class MyLabel(Label):
    pass

class titlebutton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(titlebutton,self).__init__(**kwargs)
        self.source='logo.png'

    def on_press(self):
        Clock.schedule_interval(self.song_title, 1)
    
    def song_title(self,dt):
            song_name= os.popen('playerctl --player=spotify metadata | grep -i title')
            song_name=song_name.read()
            song_name=str(song_name)
            song_name=song_name.replace('spotify xesam:title               ' , 'Title: ')
            ext3.text=song_name

class infobutton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(infobutton,self).__init__(**kwargs)
        self.source='info_icon.png'

    def on_press(self):
        view.open()
    
class forwbutton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(forwbutton,self).__init__(**kwargs)
        self.source='forw.png'

    def on_press(self):
        os.system('playerctl --player=spotify next')

class pausebutton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(pausebutton,self).__init__(**kwargs)
        self.source='pause.png'

    def on_press(self):
        if self.source== 'pause.png':
            os.system('playerctl --player=spotify pause')
            self.source= 'play.png'
        
        elif self.source== 'play.png':
            os.system('playerctl --player=spotify play')
            self.source='pause.png'
        
        else:
            pass

class rewindbutton(ButtonBehavior,Image):
    def __init__(self, **kwargs):
        super(rewindbutton,self).__init__(**kwargs)
        self.source='back.png'

    def on_press(self):
        os.system('playerctl --player=spotify previous')

class start_stop(ButtonBehavior,Image):
    def __init__(self, **kwargs):
        super(start_stop, self).__init__(**kwargs)
        self.source='start_icon.png'
    
    def on_press(self):

        if self.source=='start_icon.png':
            global shellscript
            shellscript = subprocess.Popen(['sh' ,"/home/netvincible/Documents/Python/Mutify/source_linux.sh"] ,stdout=subprocess.PIPE)
            self.source='stop_icon.png'
            ON.size_hint=(0.18,0.18)
            ON.pos_hint={'center_x':.75, 'center_y':.25}
            global interval
            interval=Clock.schedule_interval(self.ad_count, 2)
        
        elif self.source=='stop_icon.png':
            os.system('kill $(pgrep source_linux.sh)')
            self.source='start_icon.png'
            ON.size_hint=(0.18,0.18)
            ON.pos_hint={'center_x':0.25, 'center_y':0.25}
            
            now=datetime.now()
            current_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            alpha_str= str(" var ") + str(final_ad_num) + str(" ")

            file = open("/home/netvincible/Documents/Python/Mutify/log.txt", 'w')
            file.write(f"{ alpha_str, current_time}")
            file.close()

            Clock.unschedule(interval)

        else:
            pass
        
    def ad_count(self,dt):
        # time.sleep(2)
        output_line = shellscript.stdout.readline().decode().strip()
        if not output_line or shellscript.poll() is not None:
            breakpoint

        try:
            # Convert output to an integer
            global result
            result = int(output_line)
            
        except ValueError:
            # Handle non-integer output lines here (if needed)
            pass
        
        global final_ad_num
        final_ad_num= int(result) + int(ad_num)
        ads_muted.text=f"Ads Muted: {int(final_ad_num)}"
    


class Mutify(App):
    def build(self):
        return design()

if __name__=="__main__":
    Mutify().run()
