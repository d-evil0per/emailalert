import imaplib
import email
from gtts import gTTS
import os
import getpass
import datetime
import json





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


# #================================ Speak function =================================================

def speak(text):
    tts = gTTS(text, lang='en')
    tts.save("output.mp3")
    os.system("mpg321 output.mp3 --stereo 2>/dev/null;")

# #========================== Speak function ends =================================================

def read_email_from_gmail(username,currentDT,configdata):
    ORG_EMAIL   = configdata['mail']['ORG_EMAIL']
    FROM_EMAIL  = configdata['mail']['FROM_EMAIL'] + ORG_EMAIL
    FROM_PWD    = configdata['mail']['FROM_PWD']
    SMTP_SERVER = configdata['mail']['SMTP_SERVER']
    SMTP_PORT   = configdata['mail']['SMTP_PORT']
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    print("Attempting Login into your email account.")
    mail.login(FROM_EMAIL,FROM_PWD)
    print("Loggedin!!.")
    print("Checking inbox!!")
    mail.select('inbox')
    print("Checking UNSEEN mails!!")
    typ,data= mail.search(None, '(UNSEEN)')
    count = len(data[0].split())
    # print(count)
    from_email=[]
    i=0 
    if count>0:
        for eachid in data[0].split():
            print("id"+str(eachid))
            if str(eachid)!="" :
                i+=1
                uid=eachid
                print("Fetching Mail details!!")
                status,message = mail.fetch(uid, '(RFC822)' )
                for response_part in message:
                    if isinstance(response_part, tuple):
                        msg=email.message_from_bytes(response_part[1])
                        email_from = msg['from'].split(" ")
                        from_email.append(email_from[0])
                print("Marking Mail as SEEN!!")
                success = mail.store(uid, '+FLAGS', '\Seen') 
            
        if i>0:
            if i==1:
                text=username+", You have an Email From "+from_email[0]+",with a Subject Saying "+msg['subject']
            else :
                set_from=set(from_email)
                from_list=", ".join(set_from)
                text=username+", You have "+str(i)+" Emails From "+from_list
                print(text)
                speak(text)
    else:
        print("You Dont have any new emails!!")
        speak("You Dont have any new emails")

banner()
username = getpass.getuser()
username=username.replace("-","")
currentDT = datetime.datetime.now()
# configuration reading
print("Loading Configuration...")
with open('mailconfig.json') as json_file:
    configdata = json.load(json_file)
print("Configuration Loaded Successfully...")
read_email_from_gmail(username,currentDT,configdata)