import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib
import pyjokes
import json
from urllib.request import urlopen
import wolframalpha
import subprocess
import shutil
import tkinter
import random
import requests
import operator
import feedparser
import ctypes
from bs4 import BeautifulSoup
from urllib.request import urlopen
import win32com.client as wincl
import time
from countryinfo import CountryInfo

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def main_screen():

    global screen
    screen = Tk()
    screen.title(name_assistant)
    screen.geometry("100x250")
    screen.iconbitmap('app_icon.ico')


    name_label = Label(text = name_assistant,width = 300, bg = "black", fg="white", font = ("Calibri", 13))
    name_label.pack()


    microphone_photo = PhotoImage(file = "assistant_logo.png")
    microphone_button = Button(image=microphone_photo, command = Process_audio)
    microphone_button.pack(pady=10)

    settings_photo = PhotoImage(file = "settings.png")
    settings_button = Button(image=settings_photo, command = change_name_window)
    settings_button.pack(pady=10)
       
    info_button = Button(text ="Info", command = info)
    info_button.pack(pady=10)

    screen.mainloop()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning ")

    elif 12 <= hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")


assname = 'Dimwit'
user_id = ''


def assistantname():
    speak(" i am Dimwit your personal AI assistant here to make your life easier by providing u variety of functions, given in me by my creators")
    speak("How can i Help you today")


def get_info(country_name):
    url = "https://www.worldometers.info/coronavirus/country/" + country_name + "/"
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    cases = soup.find_all("div", class_="maincounter-number")
    total = cases[0].text
    total = total[1: len(total) - 2]
    recovered = cases[2].text
    recovered = recovered[1: len(recovered) - 1]
    deaths = cases[1].text
    deaths = deaths[1: len(deaths) - 1]
    ans = {'Total Cases': total, 'Recovered Cases': recovered, 'Total Deaths': deaths}
    return ans


def username():
    speak("May i ask your name")
    user_id = takeCommand()
    speak("Welcome {} its a pleasure to meet u".format(user_id))
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishme()
    username()
    assistantname()

    while True:

        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            speak("Here you go to Youtube\n")
            webbrowser.get(chrome_path).open("youtube.com")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            speak("Here you go to Google\n")
            webbrowser.get(chrome_path).open("google.com")

        elif 'open lms' in query:
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            speak("Here you go to lms Enjoy learning")
            webbrowser.get(chrome_path).open("lms.bennett.edu.in")

        elif 'open codezinger' in query:
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            speak("Here you go to Code Zinger Happy coding")
            webbrowser.get(chrome_path).open("labs.codezinger.com")

        elif 'open ms teams' in query:
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            speak("Here you go to ms team")
            webbrowser.get(chrome_path).open("teams.microsoft.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())

        elif 'open ms teams' in query:
            speak("Here you go to ms team")
            webbrowser.open("teams.microsoft.com")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, my lord")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            user_id = takeCommand()

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'introduce yourself' in query:
            speak(assistantname())

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            speak(user_id)
            speak("I hope u have a wonderfull time ahead")
            print("Thanks for giving me your time", user_id, "I hope u have a wonderfull time ahead")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Innovage.")

        elif "you'r relation with me44" in query:
            speak("If you talk then definitely your pal.")

        elif "why you came to world" in query:
            speak("Thanks to Innovage. Further, It's a secret")

        elif 'What is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Innovage")

        elif 'reason for your existence' in query:
            speak("I was created as launching project by Innovage ")

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop me from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write?")
            note = takeCommand()
            file = open('virtual assistant.txt', 'w')
            speak("My lord, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("virtual assistant.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "weather" in query:
            api_key = "0aa821de908b9c4642f6ad9105522605"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            print("Enter city name ")
            speak('Tell your city name')
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak("Temperature (in Kelvin) is")
                print(" Temperature (in kelvin) = ", str(current_temperature))
                speak(str(current_temperature))

                speak("Atmospheric pressure is")
                print("\n atmospheric pressure (in hPa) = ", str(current_pressure))
                speak(str(current_pressure))

                speak("Humidity is")
                print("\n humidity (in percentage) = ", str(current_humidity))
                speak(str(current_humidity))

                speak("The weather is")
                print("\n The weather is", str(weather_description))
                speak(str(weather_description))

            else:
                speak("City Not Found")
                print(" City Not Found ")

        elif "covid cases" in query:
            print("Select a country")
            speak("Select a Country")
            country_name = takeCommand()
            india = get_info(country_name)
            print("Covid Updates are")
            speak("Covid Updates are")
            for i, j in india.items():
                print(i + " : " + j)
                speak(i + " : " + j)

        elif "Capital of country" or "Capital" in query:
            try:
                speak("Name the country")
                print("Name the country")
                country = takeCommand()
                print(country)
                if country == 'england':
                    country = 'uk'
                capital = CountryInfo(country).capital()
                speak("Capital of")
                speak(country)
                speak("is")
                speak(capital)
                print("Capital of", country, "is", capital)

            except:
                speak("Country not recognised")
                print("Country not recognised")

        elif 'capital of state' in query:
            speak('Tell the name of State')
            state = takeCommand()
            if state == 'andhra pradesh':
                capital1 = 'Amaravati'
            elif state == 'arunachal pradesh':
                capital1 = 'Itanagar'
            elif state == 'assam':
                capital1 = 'Dispur'
            elif state == 'bihar':
                capital1 = 'Patna'
            elif state == 'chhattisgarh':
                capital1 = 'Raipur'
            elif state == 'goa':
                capital1 = 'Panaji'
            elif state == 'gujarat':
                capital1 = 'Gandhinagar'
            elif state == 'haryana':
                capital1 = 'Chandigarh'
            elif state == 'himachal pradesh':
                capital1 = 'Shimla'
            elif state == 'jharkhand':
                capital1 = 'Ranchi'
            elif state == 'karnataka':
                capital1 = 'Bengaluru'
            elif state == 'kerala':
                capital1 = 'Thiruvananthapuram'
            elif state == 'madhya pradesh':
                capital1 = 'Bhopal'
            elif state == 'maharashtra':
                capital1 = 'Mumbai'
            elif state == 'manipur':
                capital1 = 'Imphal'
            elif state == 'meghalaya':
                capital1 = 'Shillong'
            elif state == 'mizoram':
                capital1 = 'Aizawl'
            elif state == 'nagaland':
                capital1 = 'Kohima'
            elif state == 'odisha':
                capital1 = 'Bhubaneswar'
            elif state == 'punjab':
                capital1 = 'Chandigarh'
            elif state == 'rajasthan':
                capital1 = 'Jaipur'
            elif state == 'sikkim':
                capital1 = 'Gangtok'
            elif state == 'tamil nadu':
                capital1 = 'Chennai'
            elif state == 'telangana':
                capital1 = 'Hyderabad'
            elif state == 'tripura':
                capital1 = 'Agartala'
            elif state == 'Uttar Pradesh':
                capital1 = 'Lucknow'
            elif state == 'uttarakhand':
                capital1 = 'Dehradun'
            elif state == 'west bengal':
                capital1 = 'Kolkata'
            elif state == 'andaman and nicobar':
                capital1 = 'Port Blair'
            elif state == 'dadra and nagar haveli':
                capital1 = 'Daman'
            elif 'jammu and kashmir':
                capital1 = 'Srinagar (in Summer) and Jammu (in Winter)'
            elif state == 'Lakshadweep':
                capital1 = 'Kavaratti'
            elif state == 'Puducherry':
                capital1 = 'Pondicherry'
            elif state == 'Ladakh':
                capital1 = 'Leh'
            print("Capital of", state, "is", capital1)
            speak('Capital of')
            speak(state)
            speak('is')
            speak(capital1)
        elif 'How many states in India' in query:
            print("There are 28 states and 8 Union Territories in India")
            speak("There are 28 states and 8 Union Territories in India")
            
