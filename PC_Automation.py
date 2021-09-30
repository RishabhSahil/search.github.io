from time import sleep
from AI_Robot_Tools import AI_Speech_Recognition
from pyautogui import click
import pyautogui 
import keyboard
from keyboard import press,write,press_and_release
import os
import webbrowser as web
import winshell
import Search_Web as spk
from Speak_AI import Speak
import pyautogui as pt
from keyboard import press,press_and_release
import wikipedia as aiwiki
from ai_replay import *
import AI_WebSearch 

okwait=robot_ok()
workdone_replay=work_done_replay()
AI_To_Search=['Search','search','Robot search','search Robot ']

def AI_Open(Text):
    press_and_release('win + s')
    sleep(1)
    write(Text)
    sleep(1)
    press_and_release('enter')
    #click(x=110, y=214)

def AI_Close():
    press_and_release('ctrl + w')

def AI_restore():
    press_and_release('win + up arrow')    

def AI_Minimize():
    press_and_release('win + m')    

def AI_PC_Login():
    press_and_release('win + l')  

def AI_PC_Singin():
    sleep(2)
    press_and_release('space') 
    sleep(3)
    press_and_release('enter')      
#while True:
    #query=input(">>>> ")
    #AI_Open(query) 

def AI_Voice_Typeing(Text):
    sleep(2)
    pyautogui.typewrite(Text,0.2)
    sleep(2)       

def AI_Save():
    press_and_release('ctrl + s') 

def AI_Enter():
    press_and_release('enter')

def AI_Shift():
    press_and_release('shift')

def AI_delete():
    press_and_release('del')     

def AI_home():
    press_and_release('home')

def AI_end():
    press_and_release('end')

def AI_Zoom_In():
    press_and_release('ctrl +')

def AI_Zoom_Out():
    press_and_release('ctrl -') 

def AI_Back():
    press_and_release('backspace')

def AI_Space():
    press_and_release('space')

def AI_Mute():
    press_and_release('f5')          

def open_new_tab():
    press_and_release('ctrl + t')

def reopen_tab():
    press_and_release('ctrl + shift + t')    

def battery_saver():
    press_and_release('win + a')
    sleep(6)
    click(x=1117, y=699)

def new_folder():
    press_and_release('ctrl + shift + n')

def import_folder():
    press_and_release('ctrl + o')  

def downkey():
    press_and_release('Down Arrow')

def upkey():
    press_and_release("Up Arrow")

def leftkey():
    press_and_release('Left Arrow')

def rightkey():
    press_and_release('Right Arrow') 

def allselect():
    press_and_release('ctrl + a')

def aicopy():
    press_and_release('ctrl + c')

def aipest():
    press_and_release('ctrl + v')

def aiundo():
    press_and_release('ctrl + z')

def aicut():
    press_and_release('ctrl + x')

def copyhistory():
    press_and_release('win + v')    

def airun():
    press_and_release('win + r')

def AI_Restart_():
    press_and_release('win')
    sleep(4)
    click(x=16, y=700)
    sleep(2)
    click(x=34, y=653)


def AI_Shutdown_():
    press_and_release('win')
    sleep(4)
    click(x=16, y=700)
    sleep(2)
    click(x=45, y=621)    

def AI_Whatsapp_Status():
    press_and_release('win + s')
    sleep(3)
    write("WhatsApp Desktop")
    sleep(0)
    press_and_release('enter')
    sleep(20)
    click(x=272, y=61)
    sleep(3)
    click(x=71, y=212)

def AI_Whatsapp(Text,mass):
    press_and_release('win + s')
    sleep(3)
    write("WhatsApp Desktop")
    sleep(3)
    press_and_release('enter')
    sleep(20)  
    press_and_release('ctrl + f')
    sleep(1)
    write(Text)  
    sleep(3)
    press_and_release('enter')
    sleep(4)
    write(mass)
    sleep(2)
    press_and_release('enter')

def AI_Screenshot():
    img=pyautogui.screenshot()
    path="D:\\Screenshot\\"
    name=AI_Speech_Recognition.AI_SpeechRecognition(1,4,7,'en-in')
    img.save(f"{path}{name}.png")

def Valume_up():
    press("valumeup")
    press("valumeup")
    press("valumeup")
    press("valumeup")
    press("valumeup")
    press("valumeup")
    press("valumeup")
    press("valumeup")
    press("valumeup")
    press("valumeup")

def Valume_down():
    press("valumedown")  
    press("valumedown") 
    press("valumedown") 
    press("valumedown") 
    press("valumedown") 
    press("valumedown") 
    press("valumedown") 
    press("valumedown") 
    
def AI_Wifi_Automation():
    sleep(2)
    click(x=1145, y=750, duration=2)
    sleep(4)   
    click(x=1114, y=187, duration=2) 
    sleep(2)  
    click(x=1286, y=271, duration=2)
    sleep(2)
    click(x=1145, y=750, duration=2)

def AI_Click():
    sleep(3)
    press_and_release("space")

def clr_recy():
    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)

def AI_Youtube_Download():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip 
    from time import sleep

    sleep(2)

    click(x=942,y=59)

    hotkey('ctrl','c')

    value = pyperclip.paste()

    Link = str(value) # Important 

    def Download(link):
        
        url = YouTube(link)

        video = url.streams.first()

        video.download("D:\\Video Download\\")

    Download(Link)
    from AI_Robot_Tools import AI_Speak
    AI_Speak.Speak("Done Sir , I Have Downloaded The Video .")
    AI_Speak.Speak("You Can Go And Check It Out.")

    os.startfile("D:\\Video Download\\")

def AI_Remember(text):
    remeber = open("D:\\Data Jarvis"+text+".text",'r')
    return remeber.read()   

def ChromeAuto(command200):

    command = command200

    if 'close this tab' in command:
        keyboard.press_and_release('ctrl + w')
        Speak(workdone_replay)

    elif 'new tab' in command:
        keyboard.press_and_release('ctrl + t')
        Speak(workdone_replay)

    elif 'new window' in command:
        keyboard.press_and_release('ctrl + n')
        Speak(workdone_replay)

    elif 'history' in command:
        keyboard.press_and_release('ctrl +h')
        Speak(workdone_replay)

    elif 'download' in command:
        press_and_release('ctrl + j')  
        Speak(workdone_replay) 

    elif 'reopen' in command or 'riopen' in command or 're open' in command:
        press_and_release('ctrl + shift + t')    
        Speak(workdone_replay)

    elif 'refresh' in command:
        press_and_release('ctrl + r')  
        Speak(workdone_replay) 

    elif 'add this page' in command:
        press_and_release('ctrl + d')  
        Speak(workdone_replay)

    elif 'read web' in command or 'riad' in command:
        press_and_release('ctrl + shift + u')
        Speak(workdone_replay)

    elif command in AI_To_Search:
        Speak('What Shoul I Search !')   
        search=command
        spk.AI_Search(search) 
        Speak(f'Your query Search {search}')     

    elif 'find' in command:
        press_and_release('ctrl + f')
        Speak(workdone_replay)

    elif 'go back' in command:
        press_and_release('alt + left arrow')
        Speak(workdone_replay)

    elif 'go forword' in command or 'go for word' in command:
        press_and_release('alt + right arrow') 
        Speak(workdone_replay)

    elif 'search' in command:
        Text_1=str(command)
        Text_2=Text_1.replace('search','')
        Text_3=Text_2.replace('jarvis search','')
        Text=Text_3.replace('jarvis search','')
        Speak(f'Searching {Text}')
        pt.sleep(2)
        press_and_release('ctrl+k')
        pt.write(Text,0.2)
        pt.sleep(1)
        press('enter')
        result_wiki = aiwiki.summary(Text,2)
        Speak(result_wiki)

    elif "open new tab" in command:
        from PC_Automation import open_new_tab
        Speak(okwait)
        open_new_tab()
        Speak(workdone_replay)

    elif "close tab open" in command or "open close tab" in command or "reopen close tab" in command or "close open" in command:
        from PC_Automation import reopen_tab
        Speak(okwait)
        reopen_tab()
        Speak(workdone_replay)    

    elif 'robo' in command or 'jar' in command:
        Speak(AI_WebSearch.AI_Jarvis_wikipedia(command))

    elif 'exit' in command or 'stop auto' in command or 'auto stop' in command:
        exit()                           

def YoutubeAuto(command):

    comm = command

    if 'restart' in comm or 'rest' in comm:
        keyboard.press('0')
        Speak(workdone_replay)

    elif 'mute' in comm or 'sound off' in comm or 'off sound' in comm:
        keyboard.press('m')
        Speak(workdone_replay)

    elif 'skip' in comm or 'skeep' in comm:
        keyboard.press('l')
        Speak(workdone_replay)

    elif 'back' in comm:
        keyboard.press('j')
        Speak(workdone_replay)

    elif 'full screen' in comm:
        keyboard.press('f')
        Speak(workdone_replay)

    elif 'film mode' in comm:
        keyboard.press('t')
        Speak(workdone_replay)

    elif 'push' in comm or 'poush' in comm or 'paush' in comm or 'poosh' in comm or 'pous' in comm or 'pus' in comm or 'resume' in comm or 'risum' in comm or 'start video' in comm or 'start' in comm or 'stop' in comm:
        keyboard.press('space bar') 

    elif 'like' in comm:
        click(x=566, y=701)  
        Speak(workdone_replay)   

    elif 'dis like' in comm or 'dislike' in comm or 'dise like' in comm or 'diselike' in comm:
        click(x=622, y=700)     
        Speak(workdone_replay) 

    elif 'next' in comm:
        press_and_release('shift + n')   
        Speak(workdone_replay) 

    elif 'mini' in comm:
        press_and_release('i')
        Speak(workdone_replay)

    elif 'refresh' in command:
        press_and_release('ctrl + r')    
        Speak(workdone_replay)

    elif 'search' in command:
        Text_1=str(command)
        Text_2=Text_1.replace('search','')
        Text_3=Text_2.replace('jarvis search','')
        Text=Text_3.replace('jarvis search','')
        Speak(f'Searching {Text}')
        pt.sleep(2)
        pt.press('/')
        pt.sleep(0.3)
        press_and_release('ctrl+a')
        pt.sleep(0.3)
        press('delete')
        pt.sleep(0.9)
        pt.write(Text,0.2)
        pt.sleep(1)
        press('enter')

    elif 'download' in  command:
        Speak(okwait)
        import PC_Automation as pcauto
        pcauto.AI_Youtube_Download()
        Speak(workdone_replay) 

    elif 'exit' in command or 'stop auto' in command or 'auto stop' in command:
        exit()       