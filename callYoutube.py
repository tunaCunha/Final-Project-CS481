import time
import random

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import time as ts

import Speaking

def PlayUsOff():
    songEnd = "https://www.youtube.com/watch?v=uZW4vbIstoo"
    theEndSong = playASong(songEnd)
    return theEndSong


def songGen():
    # generates responses for the how are you question
    # generate a random number so it selects a random answer every time
    songChoice = random.randint(0, 10)
    # print(compChoice)
    # list of potential compliments for Butts to give you
    if songChoice == 0:
        song = "https://www.youtube.com/watch?v=H5v3kku4y6Q&ab_channel=HarryStylesVEVO"
    elif songChoice == 1:
        song = "https://www.youtube.com/watch?v=4mkqdzW2PUw"
    elif songChoice == 2:
        song = "https://www.youtube.com/watch?v=9jxvXP3cW44"
    elif songChoice == 3:
        song = "https://www.youtube.com/watch?v=6_b7RDuLwcI&ab_channel=Jaysean"
    elif songChoice == 4:
        song = "https://www.youtube.com/watch?v=PnjDqXlVDB0&ab_channel=TajTracks"
    elif songChoice == 5:
        song = "https://www.youtube.com/watch?v=3ZRsclDfVmU&ab_channel=Cakes%26Eclairs"
    elif songChoice == 6:
        song = "https://www.youtube.com/watch?v=z2XNKQugsHg&ab_channel=IconicSound"
    elif songChoice == 7:
        song = "https://www.youtube.com/watch?v=ypkWaDN87MI&ab_channel=TheCountryStar"
    elif songChoice == 8:
        song = "https://youtu.be/6WlI24rv__g"
    elif songChoice == 9:
        song = "https://www.youtube.com/watch?v=MeQbFMrXNX0&ab_channel=Nomnomthichthit"
    elif songChoice == 10:
        song = "https://www.youtube.com/watch?v=70-yIsMuHhA"
    else:
        song = "https://www.youtube.com/watch?v=nhhyvNNKTCI"
    playASong(song)


def playASong(url):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get(url)
    time.sleep(5)
    actions = ActionChains(driver)
    actions.context_click().send_keys(Keys.SPACE).perform() #play
    ts.sleep(5)
    return None
    #driver.close()
    Speaking.Speaking()
    theSong= playASong(url)
    return theSong

