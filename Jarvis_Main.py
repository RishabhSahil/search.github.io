

import pyttsx3
from Speak_AI import Speak
from PC_Automation import AI_Whatsapp
from AI_WebSearch import Temp
from AI_Robot_Tools import AI_Tools
import Search_Web as spk
import webbrowser as web
import windows_search as wds
import pyautogui as pt
import speech_recognition as sr 
import os
from keyboard import press,press_and_release
from time import sleep
from datetime import datetime
from ai_replay import *
from Jarvis_Talking import AI_English_ChatBot

querycommand=your_command()
okwait=robot_ok()
writreply=Robot_really()
readyreply_=ready_replay()
shutdown_12=AI_shut_down_replay()
restart_12=AI_restart_replay()
bye_replay_robot=last_talk()
workdone_replay=work_done_replay()
write_replayrobo=write_replay()
close_robo=['close','close jarvis','jarvis close','close app','app close','jarvis app close','this file close','jarvis file close','close jarvis','folder close','close this windows',"close this tab","close tab","tab close","exit tab","tab exit","exit file","file exit","folder exit","exit folder","close this windows","windows close"]
read_reply=["read","jarvis read","read jarvis","read text","read this word"]
okwait=robot_ok()
workdone_replay=work_done_replay()
sorry_rply=RobtoSorry_replay()
saverobo=["save","sabe"]
enterrobo=["enter","inter","jarvis inter","inter jarvis"]
shiftrobo=["shift","sift","jarvis sift","sift jarvis"]
deleterobo=["delete","dilite","jarvis dilite","dilite jarvis","jarvis delite","delite jarvis","dilete jarvis","dilete","jarvis dilete"]
backrobo=["back"]
homerobo=["home","up","page up","pageup","up page","uppage"]
endrobo=["end","down","done","done jarvis","jarvis done","down page","page down","done page","page done"]
zooninrobo=["zoom in","in","zoomin"]
zoomoutrobo=["zoom out","out","zoomout"]
spacerobo=["space","pause","push","pus","start","stop"]
frobo=["full screen","fullscreen","small screen","smoll screen"]
mrobo=["mute","unmute","stop sound","play sound","sound off","off sound","off","on","on sound","sound on"]
downkey_rep=["don key","down key","donkey","donekey","done","down","down key","don key","done key","dan key"]
upkey_rep=["upkey","up kay","up key"]
rightkey_rep=["right key","rite key","rightkey","ritekey"]
leftkey_rep=["left key","leftkey"]
all_rep=["all select","all","select all","jarvis select","jarvis select all","all select jarvis"]
cut_rep=["cut","cut jarvis","jarvis cut","cut text","text cut","cut this","this cut","jarvis cut","jarvis this cut","cut text","text cut","jarvis text cut","jarvis cut text"]
copy_rep=["copy","copy text","text copy","copy jarvis","jarvis copy","copy this","this copy","jarvis copy","jarvis this copy","copy text","text copy","jarvis text copy","jarvis copy text"]
pest_rep=["pest","pest jarvis","jarvis pest","pest this","this pest","jarvis pest","jarvis this pest","pest text","text pest","jarvis text pest","jarvis pest text"]
copyhistory_rep=["copy history"]
run_res=["run","run jarvis","jarvis run"]
shutdown_ai_reply=["shutdown","shut down","pc shut down","pc shutdown","pc shutdown jarvis","jarvis pc shutdown","pc shut down jarvis","jarvis pc shut down","shut done","shut done","jarvis shutdown","jarvis shut down","shut down jarvis","shutdown jarvis"]
restart_ai_replay=["restart","restart jarvis","jarvis restart","pc restart","restart pc","jarvis pc restart","pc restart jarvis"]
type_reply=["type","type jarvis","jarvis type","write","write jarvis","jarvis write","name type","type name","jarvis name type","jarvis type name"]
screen_replay=["screenshot","jarvis screenshot","screenshot jarvis","screen shot","jarvis screen shot","screen shot jarvis"]
click_replay=["click","click jarvis","jarvis click","photo"]
valumeup_=["valume up","jarvis valume up","valume up jarvis","sound up","sound up jarvis","jarvis sound up"]
valumedown_=["valume down","jarvis valume down","valume down jarvis","sound down","sound down jarvis","jarvis sound down","sound in jarvis","valume in jarvis","valume in","jarvis valume in","sound in","jarvis sound in"]
AI_To_Windows_Search=['Windows Search','window search','search Robot','Robot search','windows search','Robot Windows Search','Robot window search','window search Robot']
open_windows_app=['open','Robot open','open Robot']
jarvis_stop=['stop','break','sleep','you sleep','you can sleep know','Robot sleep','Robot stop','bye','have a good day','bye have a good day']
closeapp=['close','close tab','close this tab','tab close','close this windo','close this windows','close file','close this file']

jarvis_intro='''Hay I am Robot. How Can I help You Sir ?'''

def AI_SpeechRecognition_English():

    try:

        r = sr.Recognizer()
        
        r.pause_threshold = 0.8
        print("Listening...")
        with sr.Microphone() as source:
            audio = r.listen(source,4,4)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio,language='eng-in')
            print(f"You Said : {query}")
        
        except:
            return AI_SpeechRecognition_English()

        query = str(query).lower()
        return query

    except:
        return AI_SpeechRecognition_English()   

def AI_SpeechRecognition_Hindi():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source,4,4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language='hi')
        print(f"You Said : {query}")
    
    except:
        return AI_SpeechRecognition_Hindi()

    query = str(query).lower()
    return query

def Task_Start():
    jarvis_intro='''Hay I am Jarvis. How Can I help You Sir ?'''
    Speak(AI_Tools.AI_Wish_Time_Date(f'Good Morning ! {jarvis_intro}',f'Good Afternoon ! {jarvis_intro}',f'Good Evening ! {jarvis_intro}',f'Good Night ! {jarvis_intro}'))
    while True:
        command=AI_SpeechRecognition_English()
        query=str(command)
        if 'open youtube' in query:
            web.open('https://www.youtube.com')
            Speak('Opening Youtube')
            os.startfile('startyoutubeauto.bat') 
        elif 'open google' in query:
            web.open('https://www.google.com')
            Speak('Opening Google')
            os.startfile('startgoogleauto.bat')
        elif 'search google' in query or 'google search' in query:
            Speak('What Should I Search on Google !')
            search=str(query)
            Speak(spk.Search_Google(search,2)) 
            Speak(f'Your query Google Search {search}')  
            os.startfile('startgoogleauto.bat')      
        elif 'search youtube' in query or 'youtube search' in query:
            Speak('What Should I Search on Youtube !')
            search=str(query)
            spk.Search_Youtube(search)
            Speak(f'Your query Youtube Search {search}') 
            os.startfile('startyoutubeauto.bat') 
        elif 'play video' in query or "video play" in query or "play music" in query or "play movie" in query:
            Speak('What Should I Play !')
            search=str(query)
            spk.Youtube_Search_PlayVideo(search)
            Speak(f'Enjoye Bro !')  
            os.startfile('startyoutubeauto.bat')          
        elif 'Wikipedia' in query:
            Speak(spk.AI_Wikipedia(query))
            os.startfile('startgoogleauto.bat')
        elif 'how to' in query:
            Speak(spk.how_to_query(query))
            Speak(f'Your query {query}')   
            os.startfile('startgoogleauto.bat')  
        elif 'windows search' in query or "window search" in query:
            wds.open_any_app(query)          
        elif query in AI_To_Windows_Search:
            Speak('What Should I Windows Search !')
            search=str(query)
            wds.open_any_app(search)
            Speak(f'Your query Windows Search {search}')  
        elif query in open_windows_app:
            Speak('What Should I Open !')
            search=str(query)
            wds.open_any_app(search)
            Speak(f'Opening {search}')  

        elif query in saverobo or "jarvis save" in query or "save jarvis" in query or "save file" in query or "file save" in command: 
            Speak(f"{querycommand} : {query}")
            from PC_Automation import AI_Save
            AI_Save()
            Speak(workdone_replay)

        elif query in enterrobo or "jarvis enter" in query or "enter jarvis" in query:
            from PC_Automation import AI_Enter
            Speak(okwait)
            AI_Enter()
            Speak(workdone_replay)

        elif query in shiftrobo or "jarvis shift" in query or "shift jarvis" in query:
            from PC_Automation import AI_Shift
            Speak(okwait)
            AI_Shift() 
            Speak(workdone_replay) 
        
        elif query in deleterobo or "jarvis delete" in query or "delete jarvis" in query:
            from PC_Automation import AI_delete
            Speak(okwait)
            AI_delete()
            Speak(workdone_replay)

        elif query in backrobo or "jarvis back" in query or "back jarvis" in query:
            from PC_Automation import AI_Back
            Speak(okwait)
            AI_Back()
            Speak(workdone_replay)

        elif query in homerobo or "up gape" in query:
            from PC_Automation import AI_home
            Speak(okwait)
            AI_home()
            Speak(workdone_replay)

        elif query in endrobo or "down jarvis" in query or "jarvis down" in query:      
            from PC_Automation import AI_end
            Speak(okwait)
            AI_end()
            Speak(workdone_replay)

        elif query in zoomoutrobo or "zoom out" in query or "zoom out jarvis" in query or "jarvis zoom out" in query:
            from PC_Automation import AI_Zoom_Out
            Speak(okwait)
            AI_Zoom_Out()
            Speak(workdone_replay)

        elif query in zooninrobo or "zoom in" in query:
            from PC_Automation import AI_Zoom_In
            Speak(okwait)
            AI_Zoom_In()
            Speak(workdone_replay)

        elif query in  spacerobo:
            from PC_Automation import AI_Space
            Speak(okwait)
            AI_Space() 
            Speak(workdone_replay)             

        elif query in mrobo:
            from PC_Automation import AI_Mute
            Speak(okwait)
            AI_Mute()   
            Speak(workdone_replay) 

        elif "on battery saver" in query or "battery saver" in query:
            from PC_Automation import battery_saver
            Speak(okwait)
            battery_saver() 
            Speak(workdone_replay)

        elif "on wifi" in query or "connect wifi" in query or "wifi connect" in query or "wifi on" in query:
            from PC_Automation import AI_Wifi_Automation
            Speak(okwait)  
            AI_Wifi_Automation()
            Speak(workdone_replay)  

        elif "create new folder" in query or "folder create" in query or "create folder" in query or "new folder" in query:  
            from PC_Automation import new_folder
            Speak(okwait)
            new_folder()
            Speak(workdone_replay)

        elif "import folder" in query or "open folder" in query or "folder open" in query or "folder import" in query:
            from PC_Automation import import_folder 
            Speak(okwait)
            import_folder()  
            Speak(workdone_replay)

        elif query in downkey_rep or "press down" in query or "press done" in query or "downkey" in query:     
            from PC_Automation import downkey
            Speak(okwait)
            downkey()
            Speak(workdone_replay)

        elif query in upkey_rep or "press up key" in query or "press up" in query or "upkey" in query:     
            from PC_Automation import upkey
            Speak(okwait)
            upkey()
            Speak(workdone_replay)

        elif query in leftkey_rep or "press left key" in query or "press left" in query or "leftkey" in query:
            from PC_Automation import leftkey
            Speak(okwait)
            leftkey()
            Speak(workdone_replay)

        elif query in rightkey_rep or "press right key" in query or "press right" in query or "rightkey" in query:
            from PC_Automation import rightkey
            Speak(okwait)
            rightkey()
            Speak(workdone_replay)

        elif query in all_rep:
            from PC_Automation import allselect
            Speak(okwait)
            allselect()
            Speak(workdone_replay)

        elif query in copy_rep:
            from PC_Automation import aicopy
            Speak(okwait)
            aicopy()
            Speak(workdone_replay)

        elif query in cut_rep:
            from PC_Automation import aicut
            Speak(okwait)
            aicut()
            Speak(workdone_replay)

        elif query in pest_rep:
            from PC_Automation import aipest
            Speak(okwait)
            aipest()
            Speak(workdone_replay)

        elif query in copyhistory_rep:
            from PC_Automation import copyhistory
            Speak(okwait)
            copyhistory()
            Speak(workdone_replay)

        elif query in run_res:
            from PC_Automation import airun 
            Speak(okwait)
            airun() 
            Speak(workdone_replay)  

        elif query in shutdown_ai_reply:
            from PC_Automation import AI_Shutdown_
            Speak(shutdown_12)
            Speak(bye_replay_robot)
            AI_Shutdown_()
            Speak(workdone_replay)

        elif query in restart_ai_replay:
            from PC_Automation import AI_Restart_
            Speak(restart_12) 
            Speak(bye_replay_robot)                           
            AI_Restart_()
            Speak(workdone_replay) 

        elif query in screen_replay or "take screenshot" in query or "take a screenshot" in query:    
            from PC_Automation import AI_Screenshot
            Speak(okwait)
            sleep(1)
            Speak(write_replayrobo)
            AI_Screenshot()
            sleep(2)
            Speak(workdone_replay)

        elif query in click_replay or "click photo" in query or "photo click" in query or "take a photo" in query or "take photo" in query:
            Speak(okwait)
            from PC_Automation import AI_Click
            AI_Click()       
            Speak(workdone_replay)

        elif query in valumeup_:
            Speak(okwait)
            from PC_Automation import Valume_up
            Valume_up()
            Speak(workdone_replay)

        elif query in valumedown_:
            Speak(okwait)
            from PC_Automation import Valume_down
            Valume_down()
            Speak(workdone_replay)

        elif query in close_robo:
            from PC_Automation import AI_Close
            Speak(okwait)
            sleep(2)
            AI_Close()
            Speak(workdone_replay)

        elif 'minimize' in query or 'hide file' in query or 'hide windows' in  query:
            from PC_Automation import AI_Minimize
            Speak(okwait)
            sleep(2)
            AI_Minimize()
            Speak(workdone_replay)

        elif 'maximise' in  query or 'show file' in  query or 'show windows' in  query:
            from PC_Automation import AI_restore
            Speak(okwait)
            sleep(2)
            AI_restore() 
            Speak(workdone_replay)      
        
        elif  query in read_reply:
            import AI_WebSearch as web22
            web22.read()

        elif 'show me notes' in  query or 'show notes' in  query or 'notes show' in  query:
            import AI_WebSearch as web420
            web420.note_show() 

        elif 'mening in' in  query or 'translate in' in  query:
            import AI_WebSearch as tran
            tran.AI_Mening( query)

        elif 'calculate' in  query:
            import AI_WebSearch as webcal
            webcal.calculate( query)  

        elif 'clear recycle bin' in query:
            from PC_Automation import clr_recy
            clr_recy()               
        
        elif 'remember' in query:
            from PC_Automation import AI_Remember
            AI_Remember()

        elif 'temperature' in query:
            Speak(Temp(query))    
        
        elif 'time' in  query:
            strTime = datetime.now().strftime('%H:%M:%S')
            Speak(f'Sir, the time is {strTime}')

        elif 'date' in query:
            date = datetime.date.today()
            Speak(f'Sir, the date is {date}')
        elif 'day' in query:
            day = datetime.now().strftime("%A")
            Speak(f'Sir, the day is {day}')    

        elif 'read' in  query:
            import AI_WebSearch as web22
            web22.read() 

        elif 'jokes' in  query or "jok" in  query:
            import AI_WebSearch as web23
            ab=web23.AI_jokes()   
            Speak(ab)   

        elif 'cpu' in  query:
            import AI_WebSearch as web3
            web3.ai_cpu()

        elif 'power' in  query:
            import AI_WebSearch as web00
            web00.AI_Battery()  

        elif 'note' in  query or 'notes' in  query:
            import AI_WebSearch as web123
            web123.AI_Notes_write( query)  

        elif query in jarvis_stop:
            Speak('Ok You Call me any time bye have a good day !')
            break      

        elif 'you can sleep know' in query or 'go and sleep' in query:
            Speak('Ok You Call me any time bye have a good day !')
            break

        elif query in closeapp:
            press_and_release('ctrl+w')

        elif "whatsapp status" in query:
            from PC_Automation import AI_Whatsapp_Status  
            Speak(okwait)
            AI_Whatsapp_Status()
            Speak(workdone_replay)

        elif "whatsapp" in query:
            from PC_Automation import AI_Whatsapp_Status  
            Speak('what to send in message')
            massage=str(query)
            AI_Whatsapp(Text=query,mass=massage)
            Speak(workdone_replay)

        elif query in type_reply or 'voice typeing' in query or 'type jarvis' in query or 'jarvis type' in query or "write jarvis" in query or "jarvis write" in query or 'right' in query or 'right jarvis' in query:
            Speak(okwait)
            sleep(1)
            Speak(writreply)
            query_write=str(query)
            from PC_Automation import AI_Voice_Typeing
            Speak(readyreply_)
            typing=AI_Voice_Typeing(query_write)
            Speak(typing)

        elif 'can you talk me' in query or 'you talk me' in query or 'talking me' in query or 'can you chat' in query or 'talking to me' in query or 'talk to me' in query:
            Speak('Yes ! but talk me english') 
            AI_English_ChatBot(query)   

def Main():
    while True:
        command=AI_SpeechRecognition_English()
        if 'wake up' in command:
            Task_Start()
        elif 'can you talk me' in command or 'you talk me' in command or 'talking me' in command or 'can you chat' in command or 'talking to me' in command or 'talk to me' in command:
            Speak('Yes ! but talk me english') 
            AI_English_ChatBot(command=command)     

Main()
