from imap_tools import MailBox,AND
import imaplib
import getpass
import json
from gtts import gTTS
import playsound

def banner():
    os.system("clear")
    print("\n")
    print('███████╗███╗   ███╗ █████╗ ██╗██╗      █████╗ ██╗     ███████╗██████╗ ████████╗')
    print('██╔════╝████╗ ████║██╔══██╗██║██║     ██╔══██╗██║     ██╔════╝██╔══██╗╚══██╔══╝')
    print('█████╗  ██╔████╔██║███████║██║██║     ███████║██║     █████╗  ██████╔╝   ██║   ')
    print('██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     ██╔══██║██║     ██╔══╝  ██╔══██╗   ██║   ')
    print('███████╗██║ ╚═╝ ██║██║  ██║██║███████╗██║  ██║███████╗███████╗██║  ██║   ██║   ')
    print('╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ')
    print("\n")

def speak(text):
    tts = gTTS(text, lang='en') #gtts API to convert text to speech
    tts.save("output.mp3") #saving as the audio file
    playsound.playsound('output.mp3') #playing from audio file


def read_email_from_email(username,configdata):
    ORG_EMAIL   = configdata['mail']['ORG_EMAIL']
    FROM_EMAIL  = configdata['mail']['FROM_EMAIL'] + ORG_EMAIL
    FROM_PWD    = configdata['mail']['FROM_PWD']
    SMTP_SERVER = configdata['mail']['SMTP_SERVER']
    mail = MailBox(SMTP_SERVER).login(FROM_EMAIL, FROM_PWD)
    messages = mail.fetch(criteria=AND(seen=False),mark_seen=True,bulk=True)

    msg=list(messages)
    count=len(msg)
    if count>0:
        text=username+", You have an Email From "+msg[0].from_+",with a Subject Saying "+msg[0].subject
        print(text)
        speak(text)

    else:
        print("You Don't have any new emails!!")
        speak("You Don't have any new emails")



if __name__ == "__main__":
    banner()
    username = getpass.getuser()
    username=username.replace("-","")
    # configuration reading
    print("Loading Configuration...")
    with open(r'D:\Codes\Python\emailalert\mailconfig.json') as json_file:
        configdata = json.load(json_file)
    print("Configuration Loaded Successfully...")
    read_email_from_email(username,configdata)


