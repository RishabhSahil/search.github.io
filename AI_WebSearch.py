from  webbrowser import open as ai_open
from AI_Robot_Tools import AI_Speak
from AI_Robot_Tools.AI_Tools import AI_Translate
import pyautogui
import pywhatkit
import wikipedia as aiwiki
from pywikihow import search_wikihow
import requests
from bs4 import BeautifulSoup
import pyperclip
import datetime
import subprocess
import wolframalpha
import pyjokes
import psutil
import os
import random
import ai_replay as rpl
from Speak_AI import Speak

sorryai=rpl.RobtoSorry_replay()

try:
    app = wolframalpha.Client("KRJ4JH-GAL9UEAV7X")
except Exception:
    Speak('Some Feature Are Not Work')

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def Youtube_Search(Text):
    web = 'https://www.youtube.com/results?search_query='+Text
    ai_open(web)

def Youtube_Search_PlayVideo(Text):
    command_420=str(Text)
    command_4=command_420.replace('play video','')  
    command_4=command_420.replace('video play','')
    command_4=command_420.replace('play video on youtube','')                
    command_4=command_420.replace('jarvis play video','')  
    command_4=command_420.replace('jarvis video play','')
    command_4=command_420.replace('jarvis play video on youtube','')
    web = 'https://www.youtube.com/results?search_query='+command_4
    ai_open(web)
    pywhatkit.playonyt(web) 

def Google_Search(Text,line):
    pywhatkit.search(Text)
    result_search = aiwiki.summary(Text,line)
    return result_search

def AI_Wikipedia(Text,line):
    result_wiki = aiwiki.summary(Text,line)
    return result_wiki   

def how_to_query(Text):
    max_result = 1
    how_to_func = search_wikihow(Text,max_result)
    assert len(how_to_func) == 1
    how_to_func[0].print()
    return how_to_func[0].summary

def ip_Adder(return_Text):
    try:
        ipAdd=requests.get('https://api.ipify.org').text
        return ipAdd
    except:
        return return_Text

def Temp(Text):
    command2=str(Text)
    command=command2.replace('temperature in','')
    command=command2.replace('temperature','')
    command=command2.replace('jarvis temperature in','')
    command=command2.replace('temperature in','')
    command=command2.replace('in','')
    command=command2.replace('jarvis','')
    try:
        res = app.query(command)
        result22 = next(res.results).text
        Speak(result22)
    except:
        Speak(sorryai)
    
    if 'yes' in next:
        Speak("Tell Me The Name Of THE Place ")
        name = command
        res2=app.query(command)
        temperature = next(res2.results).text
        Speak(f"The Temperature in {name} is {temperature} celcius")
    else:
        Speak("no problem sir")

def read():
    pyautogui.hotkey("ctrl",'c')
    tobespoken=pyperclip.paste()
    Speak(tobespoken)

def AI_jokes():
    get = pyjokes.get_joke()
    return get
    
def ai_cpu():
    cpu = str(psutil.cpu_percent())
    print(cpu)
    Speak(f"You have used {cpu} of cpu.")        

def note_show():
    codePath = "D:\\Data Jarvis\\Jarvis_Data.txt"
    os.system(codePath)

def AI_Notes_write(command):
    note = command
    remember = open("D:\\Data Jarvis\\Jarvis_Data.txt", "w")
    remember.write(note)
    remember.close()
    Speak("I have noted that" + note)

def AI_Battery():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    Speak(f'sir our system have {percentage} percent battery')
    if percentage>=75:
        Speak('we have enougj power to continue our work')
    elif percentage>=40 and percentage>=75:
        Speak('we should connect our system to charging point to charge oue battery')
    elif percentage>=15 and percentage>=30:
        Speak('we dont,t have enough power to work, please connect to chargging')
    elif percentage>=15:
        Speak('we have very low power, please, please connect to charging the system will shutdown very soon.')

def AI_Mening(text):
    query=str(text)
    query = query.replace("jarvis","")
    query = query.replace("google search","")
    query = query.replace("google","")
    query = query.replace("translate in","meaning in")
    query = query.replace("of","in")
    query = query.replace("or","in")
    query = query.replace("on","in")
    try:
        if 'hindi' in query:
            hindiresult=AI_Translate(query,'en').text
            Speak(hindiresult)
        elif 'english' in query:
            englishresult=AI_Translate(query,'hi').text 
            Speak(englishresult)   
    except:
        aa = random.choice(sorryai)
        Speak(aa)

def calculate(command):
    try:
        res = app.query(command)
        return next(res.results).text
    except:
        return sorryai

def AI_Jarvis_wikipedia(command):
    ab = str(command)
    aa=ab.replace("jarvis","")
    hjhfhg=aa.replace("robot","")
    gyhjh=hjhfhg.replace("google search","")
    gthghjlkyffhh=gyhjh.replace("wiki", "")
    user_query=gthghjlkyffhh.replace("wikipedia", "")
    try:
        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
        }
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.find(class_='yp1CPe wDYxhc').get_text()
        return result
    except:
        try:
            result = soup.find(class_='Z0LcW XcVN5d').get_text()
            return result
        except:
            try:
                result = soup.find(class_='hgKElc').get_text()
                return result
            except:
                try:
                    result2 = soup.find(class_='tw-target-rmn tw-ta-container F0azHf tw-nfl').get_text()
                    return result2
                except:
                    try:
                        result2 = soup.find(class_='thODed').get_text()
                        return result2
                    except:
                        try:
                            res = app.query(command)
                            return next(res.results).text
                        except:
                            try:
                                query = str(user_query)
                                text = query.replace("jarvis","")
                                result_wiki = aiwiki.summary(text,2)   
                                return result_wiki
                            except:
                                Speak(random.choice(sorryai))


def Temp(message):
    ab = str(message)
    aa=ab.replace("jarvis","")
    hjhfhg=aa.replace("robot","")
    fgghjkhgbd=hjhfhg.replace("google ","")
    gyhjh=fgghjkhgbd.replace("google search","")
    gyuhghiyguyhj=gyhjh.replace("search", "")
    gthghjlkyffhh=gyuhghiyguyhj.replace("wiki", "")
    user_query=gthghjlkyffhh.replace("wikipedia", "")
    try:
        URL = "https://www.google.co.in/search?q=" + user_query
        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
        }
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.find(class_='vk_bk TylWce').get_text()
        result_replay = f"{result} °C"
        return result_replay
    except:
        aa="Sorry I'm learning now so can't tell .","Not in my data right now so I can't tell but will tell very soon.","I'm learning from you right now so I can't tell right now ."
        ab=random.choice(aa)
        return ab
