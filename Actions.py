import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia 
from nltk.tokenize import word_tokenize
import pywhatkit
import requests
from newsapi.newsapi_client import NewsApiClient
import clipboard
import pyjokes
import time as tt
import string
import random
import SecureConnection
import NormalConnection
from pprint import pprint
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

news_api_key='a431c88a88654454a7500dbcb0cbb7ac'


def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def takeCommandMic(engine):
    
	while True:
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Listening...")
			r.pause_threshold = 1
			audio = r.listen(source)

		try:
			query = r.recognize_google(audio, language='en-GB')
			print(query)
			return query
		except Exception as e:
			print(e)
			speak(engine, "Could you please repeat what you just said for me?")


def speak(engine, audio):
	engine.say(audio)
	engine.runAndWait()


def time(engine):
	Time = datetime.datetime.utcnow().strftime("%I:%M:%S") #format time ---> hour = I, minutes = M, seconds = S
	speak(engine, "the current time is:")
	print(Time)
	speak(engine, Time)

def date(engine):
	year = int(datetime.datetime.now().year)
	month = int(datetime.datetime.now().month)
	date = int(datetime.datetime.now().day)
	speak(engine, "the current date is: ")
	speak(engine, date)
	speak(engine, month)
	speak(engine, year)

def greeting(engine):
	hour = datetime.datetime.now().hour
	if hour >= 6 and hour <12:
		speak(engine, "good morning love!")
	elif hour >= 12 and hour <18:
		speak(engine, "good afternoon my darling!")
	elif hour >= 18 and hour <24:
		speak(engine, "good evening sweetheart!")
	else:
		speak(engine, "good night my dear!")


def wishme(engine):
	speak(engine, "Welcome back love!")
	greeting(engine)
	speak(engine, "Veetek at your service, please tell me how can I help you?")


def weather(engine):
	speak(engine, "Say the city name")
	city = takeCommandMic(engine).lower()
	url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=b57e90af4835ac43eafaa77441c166df'
	
	speak(engine, "Hold for a moment, Fetching weather for you")
	try:
		res = requests.get(url)
		data = res.json()
		weather = data['weather'][0]['main']
		temp = data['main']['temp']
		desp = data['weather'][0]['description']
		try:
			res = SecureConnection.addWeather(city, weather, temp, desp)
			print(res)
		except:
			raise Exception	
	
		temp = round((temp - 32) * 5/9)
		print(weather)
		print(temp)
		print(desp)
		speak(engine, f'the weather in {city} city')
		speak(engine, 'Temperature : {} degree celcius'.format(temp))
		speak(engine, 'weather is {}'.format(desp))
	except:
		speak(engine, "Failed to fetch weather")
		raise Exception


def sendEmail(engine):

	your_email = "ysheorantestemail@gmail.com"
	your_password = "ysheoran27@testemail"
	your_name = "Natasha Shep"

	try:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(your_email, your_password)
		
		names, emails = get_contacts('contacts.txt')  # read contacts
		message_template = read_template('message.txt')  # message template

		speak(engine, "what is the subject of the email?")
		subject = takeCommandMic(engine).lower()
		
		speak(engine, 'what should I say?')
		content = takeCommandMic(engine).lower()
		
		for name, email in zip(names, emails):
			# create a message
			msg = MIMEMultipart()       

			# add in the actual person name to the message template
			message = message_template.substitute(PERSON_NAME = name.title(), CONTENT = content, YOUR_NAME = your_name)

			# setup the parameters of the message
			msg['From'] = your_email
			msg['To'] = email
			msg['Subject'] = subject

			# add in the message body
			msg.attach(MIMEText(message, 'plain'))
			print(msg)
			# send the message via the server set up earlier.
			print(server.send_message(msg))
			del msg
			try:
				res = SecureConnection.addEmail(your_email, email , subject, content)
				print(res)
			except:
				raise Exception
		server.close()
	except Exception as e:
		print(e)
		speak("unable to send the email")
	

def sendwhatsmsg(engine):
	speak(engine, "Can you tell me the name of the person")
	name = takeCommandMic(engine).lower()
	print(name)
	speak(engine, "Please speak the phone number with starting with country code")
	number = takeCommandMic(engine).replace(" ", "")
	print(number)
	speak(engine, "What's the message")	
	message = takeCommandMic(engine)
	print(message)
	try:
		wb.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
		sleep(20)
		pyautogui.press('enter')
		speak(engine, "Message sent")
		try:
			res = SecureConnection.addMessage(name,number,message)
			print(res)
		except:
			raise Exception	
	except:
		speak(engine, "Failed to send message")


def youtubeplay(engine):
	speak(engine, "what should i search for on youtube?")
	topic = takeCommandMic(engine)
	try:
		url = pywhatkit.playonyt(topic) #open video first result in the search
		try:
			res = NormalConnection.addYoutubeHistory(url)
			print(res)
		except:
			pass	
	except:
		speak(engine, "Failed to play")


def openwebsite(engine):
	speak(engine, 'which website should I open?')
	search = takeCommandMic(engine)
	try:
		url = wb.open(search)
		print(url)
		try:
			res = NormalConnection.addWebHistory(search)
			print(res)
		except:
			raise Exception	
	except:
		speak(engine, "Failed to open the website")	


def searchgoogle(engine):
	speak(engine, 'what should i search for?')
	search = takeCommandMic(engine)
	try:
		url = wb.open('https://www.google.com/search?q='+search)
		print(url)
		try:
			res = NormalConnection.addSearchHistory(search, "")
		except:
			raise Exception	
	except:
		speak(engine, "Failed to search")

def news(engine):
	newsapi = NewsApiClient(api_key = news_api_key)
	speak(engine, 'what topic would you like to hear?')
	topic = takeCommandMic(engine)
	data = newsapi.get_top_headlines(q=topic,
									language='en',
									page_size=5)
	newsdata = data['articles']
	for x,y in enumerate(newsdata):
		#provide top 5 news
		print(f'{x}{y["description"]}')
		speak(engine, (f'{x}{y["description"]}'))
	
	speak(engine, "that's it for now I will update you later")

	try:
		res = NormalConnection.addNewsHistory(topic)
		print(res)
	except:
		raise Exception
	
def wikipedia(engine):
	speak(engine, 'What should I search on wikipedia...')
	topic = takeCommandMic(engine)
	result = wikipedia.summary(topic, sentences = 2)
	print(result)
	speak(engine, result)
	try:
		res = NormalConnection.addWikiHistory(topic, result)
		print(res)
	except:
		raise Exception	

def note(engine):
	
	speak(engine, 'What is going to be the title for the note')
	title = takeCommandMic(engine)
	
	speak(engine, 'What should I note down')
	content = takeCommandMic(engine)

	speak(engine, 'Shall I mark it as a todo?')
	todo = takeCommandMic(engine).lower()
	# Expecting ans in yes or no
	TODO = False
	if todo == 'yes':
		TODO = True
	try:
		res = SecureConnection.addNote(title, content, TODO)
		print(res)
	except:
		raise Exception	

def pendingnotes(engine):
	speak(engine, "Collecting your pending notes")
	try:
		result = SecureConnection.getNote(True)
		pprint(result)
		if not result == None:
			speak(engine, "Reading out your pending notes")
			for res in result:
				speak(engine, "title" + res['title'] + "and content is" + res['content'])
	except:
		speak(engine, "failed to fetch")
		raise Exception

def text2speech(engine):
	text = clipboard.paste()
	print(text)
	speak(engine, text)

def covid(engine):
	r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
	data = r.json()
	covid_data = f'Confirmed cases : {data["cases"]} \n Deaths  :{data["deaths"]} \n Recovered {data["recovered"]}'
	print(covid_data)
	speak(engine, covid_data)

def screenshot(engine):
	name_img = tt.time() #store the name of the image in a form of datetime
	name_img = f'C:\\Users\\ak\\Downloads\\JARVUS 2.0\\screenshot\\{name_img}.png'
	img = pyautogui.screenshot(name_img)
	img.show()  #open image
	speak(engine, "Screenshot captured at path " + f'C:\\Users\\ak\\Downloads\\JARVUS 2.0\\screenshot\\{name_img}.png' )

def passwordgen(engine):
	s1 = string.ascii_lowercase
	s2 = string.ascii_lowercase
	s3 = string.digits
	s4 = string.punctuation

	passlen = 8
	s = []
	s.extend(list(s1))
	s.extend(list(s2))
	s.extend(list(s3))
	s.extend(list(s4))

	random.shuffle(s)
	newpass = ("".join(s[0:passlen]))
	print(newpass)
	speak(engine, newpass)

def jokes(engine):
	speak(engine, pyjokes.get_joke())

def fetch_news(engine):
	speak(engine, "Fetching your recent news searches")
	try:
		result = NormalConnection.getNewsHisotry()
		speak(engine, "here you go, your most recent seaches are ")
		for res in result:
			speak(engine, res['keyword'])
	except:
		speak(engine, "Failed to fetch!!!")

def fetch_web(engine):
	speak(engine, "Fetching your recently opened websites")
	try:
		result = NormalConnection.getWebHisotry()
		speak(engine, "here you go, your most recent websites accessed are")
		for res in result:
			speak(engine, res['keyword'])
	except:
		speak(engine, "Failed to fetch!!!")

def fetch_search(engine):
	speak(engine, "Fetching your recent web searches")
	try:
		result = NormalConnection.getSearchHisotry()
		speak(engine, "here you go, your most recent searches are ")
		for res in result:
			speak(engine, res['keyword'])
	except:
		speak(engine, "Failed to fetch!!!")


def fetch_wiki(engine):
	speak(engine, "Fetching your recent wikipedia searches")
	try:
		result = NormalConnection.getWikiHisotry()
		speak(engine, "here you go, your most recent searches are ")
		for res in result:
			speak(engine, res['keyword'])
	except:
		speak(engine, "Failed to fetch!!!")


def fetch_youtube(engine):
	speak(engine, "Fetching your youtube favourites")
	try:
		result = NormalConnection.getYoutubeFav()
		speak(engine, "here you go, your favourite youtube videos are printed on console")
		for res in result:
			print(res['keyword'])
			speak(engine, "the link" + str(res['keyword']) + "has been played " + str(res["count"]) + " times ")
	except:
		speak(engine, "Failed to fetch!!!")


def fetch_weather(engine):
	speak(engine, "Fetching your recent weather searches")
	try:
		result = SecureConnection.getWeather()
		speak(engine, "here you go, your most recent searches are ")
		for res in result:
			weather = res['weather']
			temp = res['temp']
			desp = res['desc']
			city = res["location"]
			temp = round((temp - 32) * 5/9)
			print(city)
			print(weather)
			print(temp)
			print(desp)
			speak(engine, f'the weather in {city} city')
			speak(engine, 'Temperature : {} degree celcius'.format(temp))
			speak(engine, 'weather is {}'.format(desp))
	except:
		speak(engine, "Failed to fetch!!!")


def fetch_emails(engine):
	speak(engine, "Fetching your recent sent emails")
	try:
		result = SecureConnection.getEmail()
		speak(engine, "here you go, your most recent emails are ")
		for res in result:
			speak(engine, "you have sent an email to " + res["reciever"] + "having subject as" + res["subject"])
	except:
		speak(engine, "Failed to fetch!!!")


def fetch_messages(engine):
	speak(engine, "Fetching your recent sent messages")
	try:
		result = SecureConnection.getMessage()
		speak(engine, "here you go, your most recent messages are ")
		for res in result:
			speak(engine, "you have sent " + res['content'] + "to" + res["number"])
	except:
		speak(engine, "Failed to fetch!!!")

def fetch_notes(engine):
	speak(engine, "Collecting your recent notes")
	try:
		result = SecureConnection.getAllNotes()
		pprint(result)
		if not result == None:
			speak(engine, "Reading out your recent notes")
			for res in result:
				print(res)
				speak(engine, "title" + res['title'] + "and description is" + res['content'])
	except:
		speak(engine, "failed to fetch")
		raise Exception


# if __name__ == "__main__":
# 	fetch_notes()