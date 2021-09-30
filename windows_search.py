import pyautogui as pt
from keyboard import press,press_and_release

def open_any_app(Text):
    text1=str(Text)
    text2=text1.replace('open','')
    text3=text2.replace('jarvis','')
    text4=text3.replace('windows','')
    text5=text4.replace('search','')
    answer=text5.replace('window','')
    press_and_release('win+s')
    pt.sleep(5)
    pt.write(answer,0.3)
    pt.sleep(3)
    press('enter')
