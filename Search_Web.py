from  webbrowser import open as ai_open
import pywhatkit
import wikipedia as aiwiki
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import requests
import pyautogui as pt
from keyboard import press,press_and_release
import random
from AI_Robot_Tools import AI_Tools
from Speak_AI import Speak

def Search_Youtube(Text):
    web = 'https://www.youtube.com/results?search_query='+Text
    ai_open(web)

def Search_Google(Text,line):
    web = 'https://www.google.com/search?q='+Text
    ai_open(web)
    result_wiki = aiwiki.summary(Text,line)
    return result_wiki

def Youtube_Search(Text):
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

def Google_TO_Search(Text,line):
    pt.sleep(2)
    press_and_release('ctrl+k')
    pt.write(Text,0.2)
    pt.sleep(1)
    press('enter')
    result_wiki = aiwiki.summary(Text,line)
    return result_wiki

def Youtube_Search_PlayVideo(Text):
    command_420=str(Text)
    command_42000=command_420.replace('play video','')  
    command_42025=command_42000.replace('video play','')
    command_420000000=command_42025.replace('play video on youtube','')                
    command_420520=command_420000000.replace('Robot play video','')  
    command_444444=command_420520.replace('Robot video play','')
    command_123=command_444444.replace('Robot play video on youtube','')
    web = 'https://www.youtube.com/results?search_query='+command_123
    ai_open(web)
    pywhatkit.playonyt(web) 

def Google_Search(Text,line):
    pywhatkit.search(Text)
    result_search = aiwiki.summary(Text,line)
    return result_search

def AI_Wikipedia(Text,line):
    pywhatkit.search(Text)
    result_wiki = aiwiki.summary(Text,line)
    return result_wiki  

def ip_Adder():
    ipAdd=requests.get('https://api.ipify.org').text
    pywhatkit.search('https://api.ipify.org')
    return ipAdd

def how_to_query(Text):
    max_result = 1
    how_to_func = search_wikihow(Text,max_result)
    assert len(how_to_func) == 1
    how_to_func[0].print()
    pywhatkit.search(Text)
    return how_to_func[0].summary
    
def ALL_Search_And_Data(command):
    ab = str(command)
    aa=ab.replace("Robot","")
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
        result = soup.find(class_='zCubwf').get_text()
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
                    result2 = soup.find(class_='BNeawe vvjwJb AP7Wnd').get_text()
                    return result2 
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
                                query = str(user_query)
                                text = query.replace("Robot","")
                                result_wiki = aiwiki.summary(text,2)   
                                return result_wiki
                            except:
                                aa="Sorry I'm learning now so can't tell .","Not in my data right now so I can't tell but will tell very soon.","I'm learning from you right now so I can't tell right now ."
                                ab=random.choice(aa)
                                return ab    

def response(input_message):
    ab = str(input_message)
    aa=ab.replace("mening","")
    hjhfhg=aa.replace("translate","")
    fgghjkhgbd=hjhfhg.replace("to mening ","")
    gyhjh=fgghjkhgbd.replace("mening in","")
    gyuhghiyguyhj=gyhjh.replace("mening to", "")
    gthghjlkyffhh=gyuhghiyguyhj.replace("translate to", "")
    user_query=gthghjlkyffhh.replace("translate in", "")
    try:
        if 'hindi' in user_query:
            hinditrans=AI_Tools.AI_Translate(Text=user_query,language='hi')
            return hinditrans.text
        elif 'english' in user_query:
            englishtrans=AI_Tools.AI_Translate(Text=user_query)
            return englishtrans.text    
    except:
        print(">>>")

def AI_Search(Text):

    if pt.locateCenterOnScreen("D:\simple-AI\img\Web capture_17-9-2021_1405_www.youtube.com.jpeg", confidence=.8):
        pt.sleep(2)
        query_1=str(Text)
        query_2=query_1.replace('search','')
        Youtube_Search(query_2)
    else:
        query_1=str(Text)
        query_2=query_1.replace('search','')
        Speak(Google_TO_Search(query_2,2))  
