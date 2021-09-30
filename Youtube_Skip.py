import pyautogui as pt

black_X="D:\simple-AI\img\Web capture_17-9-2021_134651_www.youtube.com.jpeg"
blackX="D:\simple-AI\img\Web capture_16-9-2021_211448_www.youtube.com.jpeg"
white_X="D:\simple-AI\img\Web capture_17-9-2021_14747_www.youtube.com.jpeg"
whiteX="D:\simple-AI\img\Web capture_16-9-2021_222357_www.youtube.com.jpeg"
white_2="D:\simple-AI\img\Web capture_17-9-2021_142729_.jpeg"
ads_Skip="D:\simple-AI\img\Web capture_16-9-2021_203249_www.youtube.com.jpeg"
ads_Skip_2="D:\simple-AI\img\Web capture_17-9-2021_14330_www.youtube.com.jpeg"
Youtube_Auto_ON_OFF="D:\simple-AI\img\Web capture_17-9-2021_1405_www.youtube.com.jpeg"
Auto_ON_OFF_2="D:\simple-AI\img\Screenshot 2021-09-17 173648.png"

def Auto_Close_ADS():

    if pt.locateCenterOnScreen(black_X,confidence=.8,grayscale=True): 
        pt.sleep(2)       
        position_1 = pt.locateCenterOnScreen(blackX,confidence=.8,grayscale=True)
        pt.click(position_1)

    elif pt.locateCenterOnScreen(white_X,confidence=.8): 
        pt.sleep(2)       
        position_1 = pt.locateCenterOnScreen(whiteX,confidence=.8,grayscale=True)
        pt.click(position_1)

    elif pt.locateCenterOnScreen(white_2,confidence=.8,grayscale=True): 
        pt.sleep(2)       
        position_1 = pt.locateCenterOnScreen(whiteX,confidence=.8,grayscale=True)
        pt.click(position_1)

    elif pt.locateCenterOnScreen(ads_Skip, confidence=.8,grayscale=True):
        pt.sleep(2)
        position_Skip=pt.locateCenterOnScreen(ads_Skip, confidence=.8,grayscale=True)
        pt.click(position_Skip)

    elif pt.locateCenterOnScreen(ads_Skip_2, confidence=.8):
        pt.sleep(1)
        position_Skip=pt.locateCenterOnScreen(ads_Skip_2, confidence=.8,grayscale=True)
        pt.click(position_Skip)        


'''while True:
    if pt.locateCenterOnScreen(Youtube_Auto_ON_OFF, confidence=.8):
        Auto_Close_ADS() 
        print("Done Sir !")       
    else:
        print("No Data !") '''

while True:
    Auto_Close_ADS()
    
