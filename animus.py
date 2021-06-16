#Dependencies
#pip install speechrecognition
#pip install playsound
#pip install gTTS
#pip install pyaudio
#pip install Pillow
#pip install tk

#Import packages
import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import sys
import random
from gtts import gTTS
from time import ctime
import tkinter
from PIL import Image,ImageTk
import winsound

#Record audio function
r = sr.Recognizer()
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            Animus_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            Animus_speak('Sorry I did not get that') 
        except sr.RequestError:
            Animus_speak('Sorry, my speech service is down')
        return voice_data

#Animus speak function
def Animus_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en', slow = False)
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

#Functions for button clicks
#Function for click Animus commands button
def click_Animus_commands():
    Animus_speak('I will get you started by explaining how my interface functions.')
    Animus_speak('I have been programmed with six commands that you can give me by either clicking the Animus button and saying a command, or by clicking one of the commands manually.')
    Animus_speak('Pretty simple right?')
    Animus_speak('Here is a quick overview of my commands.')
    Animus_speak('I can tell you my name and where I am from.')
    Animus_speak('I can tell you the date and time at your current location.')
    Animus_speak('I can do a voice search for you on Google for anything you are interested in.')
    Animus_speak('I can do a voice search for you on Google Maps for a specific location.')
    Animus_speak('I can do a voice search for you on YouTube and find you an awesome video to watch.')
    Animus_speak('And I can exit anytime that you want to turn me off.')
    Animus_speak('You can click the Animus button now to get started and say one of my commands, or just click one of my other commands when I am needed.')

#Function for click name button    
def click_name():
    Animus_speak('My name is Animus, and I am from the planet Cybertron!')
    Animus_speak('What else can I help you with?')

#Function for click time button    
def click_time():
    Animus_speak('The date and time are.')
    Animus_speak(time.ctime())
    Animus_speak('What else can I help you with?')

#Function for click search button   
def click_search():
    search = record_audio('What would you like to search for? You can say anything, and I will find it for you on the web!')
    url = 'https://google.com/search?q=' + search
    webbrowser.get().open(url)
    Animus_speak('Here is what I found for' + search)
    Animus_speak('What else can I help you with?')

#Function for click find location button
def click_find_location():
    location = record_audio('What is the location? Just say the location and I will pin point it for you on the map!')
    url = 'https://google.nl/maps/place/' + location + '/&amp;'
    webbrowser.get().open(url)
    Animus_speak(' Here is the location' + location)
    Animus_speak('What else can I help you with?')

#Function for click watch video button    
def click_watch_video():
    listnen_to = record_audio('What do you want to watch on youtube? Just say the name of an artist or subject, and I will find you the right video!')
    url = 'https://www.youtube.com/results?search_query=' + listnen_to
    webbrowser.get().open(url)
    Animus_speak(' Here is the' + listnen_to + ' video that you requested')
    Animus_speak('What else can I help you with?')
    
#Function for click exit button    
def click_exit():
    Animus_speak('I am always glad to help humans! Just run me again if you need any assistance!')
    sys.exit() 

#Function for click Animus button
def click_Animus():
    command = record_audio('How can I help you? Just say one of my commands, or what you want to search for.')
    print('Command: ' + command)
    if 'Animus' in command:
        Animus_speak('What can I help you with? Click the Animus button to say a command now, or just click one of my commands when I am needed.')
    if 'name' in command:
        click_name()
    if 'time' in command:
        click_time()
    if 'search' in command:
        click_search()
    if 'location' in command:
        click_find_location()
    if 'video' in command:
        click_watch_video()
    if 'exit' in command:
        click_exit()

#Animus greeting when progam is launched
Animus_speak('Launching Animus Digital Interface, please wait!')

#Launch the GUI
root= tkinter.Tk()
root.title("Animus Digital Assistant")
root.geometry('1920x1080')
load = Image.open('wallpaper.jpg')
render = ImageTk.PhotoImage(load)

#Render imaged to GUI
img = tkinter.Label(root,image = render)
img.place(x = 0, y = 0)

#Add Animus Commands Text to the GUI
img1 = ImageTk.PhotoImage(file = 'Animus-Commands.jpg')
b1 = tkinter.Button(root, image = img1, bg = 'black', command = click_Animus_commands)
b1.place(x = 100, y = 125)

#Add Animus command button to the GUI
img2 = ImageTk.PhotoImage(file = 'Animus-Voice.jpg')
b2 = tkinter.Button(root, image = img2, bg = 'black', command = click_Animus)
b2.place(x = 1230, y = 500)

#Add What Is Your Name command button to the GUI
img3 = ImageTk.PhotoImage(file = 'What-Is-Your-Name.jpg')
b3 = tkinter.Button(root, image = img3, bg = 'black', command = click_name)
b3.place(x = 100, y = 250)

#Add What Time is It command button to the GUI
img4 = ImageTk.PhotoImage(file = 'What-Time-Is-It.jpg')
b4 = tkinter.Button(root, image = img4, bg = 'black', command = click_time)
b4.place(x = 100, y =380)

#Add Search command button to the GUI
img5 = ImageTk.PhotoImage(file = 'Search.jpg')
b5 = tkinter.Button(root, image = img5, bg = 'black', command = click_search)
b5.place(x = 100, y = 510)

#Add Find Location command button to the GUI
img6 = ImageTk.PhotoImage(file = 'Find-Location.jpg')
b6 = tkinter.Button(root, image = img6, bg = 'black', command = click_find_location)
b6.place(x = 100, y = 640)

#Add Watch Video command button to the GUI
img7 = ImageTk.PhotoImage(file = 'Watch-Video.jpg')
b7 = tkinter.Button(root, image = img7, bg = 'black', command = click_watch_video)
b7.place(x = 100, y = 775)

#Add Exit command button to the GUI
img8 = ImageTk.PhotoImage(file = 'Exit.jpg')
b8 = tkinter.Button(root, image = img8, bg = 'black', command = click_exit)
b8.place(x = 100, y = 900)

#Run the main loop
root.mainloop()


    
