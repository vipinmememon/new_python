import pyttsx3 #this module used to text to speech
import pyjokes #this module used to genetrate random jokes
import speech_recognition as sr # this module udes to chsnge specch to text
import webbrowser #related to webbrowser work open etc
import datetime #related to datetime function
import time #related to time function eg:- sleep()
import os # related to operating system closed open deleted 
import psutil  #related to closed webbroser work
import subprocess  #realted to clodes webbroswer work
from PIL import Image #frm python imaging library import image
import pywhatkit as kit #pywhatkit related to  whatsapp function
import smtplib #related to email stmp lib
from email.mime.text import MIMEText #related to text msg
from email.mime.multipart import MIMEMultipart #related to subject , body ,msg of email
#speech to text function
def sptext():
    recognizer=sr.Recognizer() 
    with sr.Microphone() as source:
        print('Listening....')
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print('recognizing.........')
            data=recognizer.recognize_google(audio)
            print(data)
            return data

        except sr.UnknownValueError:
            print('Not understand')

#text to speech
def speechtext(data):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.say(data)
    engine.runAndWait()

 # Function to close a specific application (e.g., browser
def close_application(application_name):
    try:
        subprocess.run(f"taskkill /f /im {application_name}.exe", check=True, shell=True)
        print(f"{application_name} closed successfully.")
        return True
    except subprocess.CalledProcessError:
        print(f"Failed to close {application_name}.")
        return False

# function to show image
def show_img(filepath):
    try:
        img=Image.open(filepath)
        img.show()
    except Exception as e:
        print('an error ocuur')  
#function to send whatsapp messge
def send_whatsmg(number,message):
     try:
         kit.sendwhatmsg_instantly(number,message,wait_time=10) # schedule time ke liye kit.sendwhatmsg()
         print('message send successfully')
         speechtext('message send successfully to gaurav')
     except Exception as e: 
         print('an errror occur')
         speechtext('an error ocuur')

#define a function to send email
def send_email(receiver_email,subject,body):
    try:
        #sender email credential 
        sender_email='vipinmemon8123@gmail.com'
        sender_password='jbtk pwlz yudg axck'

        #set up the mime message
        msg=MIMEMultipart()
        msg['From']=sender_email
        msg['To']=receiver_email
        msg['Subject']=subject

        #email body
        msg.attach(MIMEText(body,'plain'))
        #connect to the smtp server and send email
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()#connection stalblish
        server.ehlo()#connection stalblish
        server.login(sender_email,sender_password)  
        server.send_message(msg)
        server.quit()
        print('email sent successfully')
        speechtext('email has been sent successfuly')
    except Exception as e:
        print(f'failed to send email {e}')
        speechtext('failed to send email')


if __name__=='__main__':
     if sptext().lower()=='hello 07':
       speechtext('hii')
       while True:  
         data1=sptext().lower()
         if 'your name' in data1:
             name='my name is zero seven '
             speechtext(name)
         elif 'how old are you' in data1: 
             age='i am 5 years old' 
             speechtext(age) 
         elif ' your gender' in data1:
             gender='sorry i am  vipin voice assistant'
             speechtext(gender)
         elif 'time' in data1:
             time1=datetime.datetime.now().strftime("%I%M%p")
             speechtext(time1)
         elif 'open youtube' in data1:
             speechtext('opening youtube')
            #  time.sleep(3)
             webbrowser.open("https://www.youtube.com/")
         elif 'closed youtube' in data1:
             if close_application('chrome'):
                 speechtext('youtube has been closed')
             else:
                 speechtext('youtube is not open')
                
         elif  'open instagram' in data1:
             speechtext('opening vipin instagram')
             webbrowser.open('https://www.instagram.com/')
         elif 'closed instagram' in data1:
             if close_application('chome'):
                 speechtext('instagram has been closed')
             else:
                 speechtext('instagram is  not open')   
         elif 'joke' in data1:
             joke=pyjokes.get_joke(language="en",category="neutral")
             speechtext(joke)
         elif 'play song' in data1:
             speechtext('play aaj ki raat from your folder ')
             add=r'C:\Users\vipin\OneDrive\Desktop\python\apython_notes'
             listsong=os.listdir(add)
             print(listsong)
             os.startfile(os.path.join(add,listsong[0]))
         elif 'exit' in data1:
             speechtext('thank you ') 
             break 
         elif 'show image'in data1:
             speechtext('showing image of ramanujan')
             show_img(r"C:\Users\vipin\OneDrive\Desktop\General&CN\ramanuj.jpg")
         elif 'send whatsapp message' in data1:
             speechtext('tell me message')
             msg=sptext().lower()
             send_whatsmg('+919661668783',msg)  
         elif 'send email' in data1: 
             speechtext('who should i send the email to?')
             recipient=sptext().lower()
             speechtext('what is the subject of email') 
             subject=sptext()
             speechtext('what is the body of message')
             body=sptext()
             send_email('saurabhk85440@gmail.com',subject,body)
         else:
             speechtext(f'now i dont  know  more about {data1} yet ')
       time.sleep(10)   #time interval delay after a work
     else:
          print('thanks') 
          speechtext('thanks')  
         
              


