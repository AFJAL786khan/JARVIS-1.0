from Body.Listen import Listen
from Body.Speak import Speak
import smtplib

def Email():
    try:

        Speak("Sir Whom do you like to send this Email, Please Enter the Email Address of that person")
        receiver = input("Enter Receiptent's Email : ")

        Speak("Sir please enter the subject of the email")
        subject = Listen()

        Speak('What Message you would like to send Sir')
        content = Listen()

        message = f'Subject: {subject}\n\n{content}'

        sender_email = "afjalkhan17in@gmail.com"
        password = open("D:\MyData\Documents\CODING\Python\Jarvis\Data\Passwords\Email_SMTP", "r").read()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver, message)
        print('Message Has Been Sent Successfully')
        Speak('Message Has Been Sent Successfully')

        print(f'|----------------------------------------------|')
        print(f'| Sender Email : afjalkhan17in@gmail.com       |')
        print(f'| To : {receiver}                              |')
        print(f'| Subject : {subject}                          |')
        print(f'| Message : {content}                          |')
        print(f'|----------------------------------------------|')

        server.close()
        




    except Exception as e:
        Speak("Sorry, There being an error to send email")
        print(e)
        
# Email()


