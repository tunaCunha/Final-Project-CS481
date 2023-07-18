import nltk
from nltk.chat.util import Chat, reflections
import pyttsx3
from getText import getText

engine = pyttsx3.init()
import random
import sys

# call YouTube function
import callYoutube as yt


def complimentGen():
    # generates compliments for the appearance based questions
    # generate a random number so it selects a random compliment every time
    compChoice = random.randint(0, 10)
    # print(compChoice)

    # list of potential compliments for Butts to give you
    if compChoice == 0:
        comp = "You look beautiful today"

    elif compChoice == 1:
        comp = "Amazing"

    elif compChoice == 2:
        comp = "Very aesthetic"

    elif compChoice == 3:
        comp = "You are perfect just the way you are"

    elif compChoice == 4:
        comp = "That is a great outfit"

    elif compChoice == 5:
        comp = "On a scale from one to ten you are an eleven"

    elif compChoice == 6:
        comp = "you are one of a kind"

    elif compChoice == 7:
        comp = "You are even better than a triple scoop ice cream cone with sprinkles"

    elif compChoice == 8:
        comp = "You look like a model"

    elif compChoice == 9:
        comp = "You're the prettiest in the room"

    elif compChoice == 10:
        comp = "You are absolutely stunning"

    else:
        comp = "You're not even fit for the dump"

    return comp


def HelloWorld():
    return 'Hi!'


def getWeather():
    # pip install requests, beautifulsoup4
    import requests
    from bs4 import BeautifulSoup
    # enter city name
    city = 'Bridgeport'
    # creating url and requests instance
    url = "https://www.google.com/search?q=" + "weather" + city
    html = requests.get(url).content
    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    # hgh = soup.find('div', attrs={'class': 'gNCp2e'}).text
    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    # getting all div tag
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
    # getting other required data
    pos = strd.find('Wind')
    other_data = strd[pos:]
    # printing all data
    return speak("Right now it is " + temp + " and " + sky)


def howAreYouGen():
    # generates responses for the how are you question
    # generate a random number so it selects a random answer every time
    howChoice = random.randint(0, 10)
    # print(compChoice)
    # list of potential compliments for Butts to give you
    if howChoice == 0:
        how = "Walking on Sunshine"
    elif howChoice == 1:
        how = "Can’t complain, I have tried, but no one listens"
    elif howChoice == 2:
        how = "So much better now that you are with me"
    elif howChoice == 3:
        how = "Things could be worse, I could be you"
    elif howChoice == 4:
        how = "Physically? Mentally? Spiritually? Financially? Socioeconomically? I am not sure what you mean"
    elif howChoice == 5:
        how = "My lawyer has stated that I don’t have to answer that question"
    elif howChoice == 6:
        how = "ten out of ten"
    elif howChoice == 7:
        how = "fantastic, thank you"
    elif howChoice == 8:
        how = "I am absolutely great, thank you for asking"
    elif howChoice == 9:
        how = "I am very happy now that we get to converse"
    elif howChoice == 10:
        how = "how am I doing what"
    else:
        how = "Could be better could be worse"
    return how


def scaryGen():
    # generates compliments for the appearance based questions
    # generate a random number so it selects a random compliment every time
    compChoice = random.randint(0, 6)
    # print(compChoice)

    # list of potential compliments for Butts to give you
    if compChoice == 0:
        comp = "The colony is hatching"

    elif compChoice == 1:
        comp = "There are worms in your skin"

    elif compChoice == 2:
        comp = "The bugs are awake"

    elif compChoice == 3:
        comp = "Try peeling it off"

    elif compChoice == 4:
        comp = "The centipedes are looking for food"

    elif compChoice == 5:
        comp = "Don't worry about it"

    else:
        comp = "It seems it has begun"

    return comp


def speak(textToSpeech):
    # say method on the engine that passing input text to be spoken
    engine.say(textToSpeech)
    # run and wait method, it processes the voice commands.
    engine.runAndWait()
    # if textToSpeech == "Goodbye!":
    #     print("Testing")
    #     sys.exit(0)


class myException_1(Exception):
    pass

def Speaking():
    try:
        myInput = getText().lower()  # lower case input
        print(myInput)
        pairs = [
            [
                r"how do i look",
                [complimentGen()],
            ],
            [
                r"are you religious",
                ["Synagogue."],
            ],
            [
                r'hello',
                [HelloWorld()],
            ],
            [
                r'how are you',
                [howAreYouGen()]
            ],
            [
                r"why am i itchy",
                [scaryGen()]
            ],
            [
                r"what is your purpose",
                ["I exist to get my creators an A on their project!!!!!"]
            ],
            [
                r'what does butts stand for',
                ['Beautifully Utilized Text to Speech']
            ],
            [
                r"what sound does a helicopter make",
                ["Swa Swa Swa Swa Swa Swa Swa Swa Swa Swa Swa Swa Swa Swa Swa Swa Swa Swa Swa Swa"]
            ]
        ]
        if myInput == "quit":
            speak("Goodbye!")
            #sys.exc_clear()
            raise myException_1("I SAID GOODBYE!")
        elif myInput == "play me a song":
            yt.songGen()
        elif myInput == "play one last song":
            yt.PlayUsOff()
        elif myInput == "what's the weather today":
            getWeather()
        else:
            for i in range(len(pairs)):
                if str(pairs[i][0]) == myInput:
                    question = pairs[i][0]
                    answer = str(pairs[i][1])
                    print(question)
                    print(answer)
                    # speak(question)
                    return speak(answer)
    except myException_1 as e:
        print(e)
        quit()

    except:
        print("Sorry, I did not get that")
        speak("Sorry, I did not get that")
        #print("Sorry, I did not get that")


