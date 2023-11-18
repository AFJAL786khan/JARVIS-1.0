from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
import sys
sys.path.append('D:/MyData/Documents/CODING/Python/Jarvis')
from Body.Speak import Speak
from Body.Listen import Listen

warnings.simplefilter('ignore')

# Setting Up The Driver & Opening The Website :-

Link = "https://gpt4login.com/use-chatgpt-online-free/"
chrome_driver_path = 'D:\\MyData\\Documents\\CODING\\Python\\Jarvis\\Brain\\chromedriver.exe'
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(Link)

# File Operations :- Writing, Reading

def FileReader():
    File = open("D:\MyData\Documents\CODING\Python\Jarvis\DataBase\GPT_Chatlog\HIstoryChat.txt","r")
    Data = File.read()
    File.close()
    return Data

def FileWriter(Data):
    File = open("D:\MyData\Documents\CODING\Python\Jarvis\DataBase\GPT_Chatlog\HIstoryChat.txt","w")
    File.write(Data)
    File.close()

# Sending The Query To The Website :-

def ChatGPTBrain(Query):
    Query = str(Query)
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/div/textarea").send_keys(Query)
    # sleep(1)
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/button/span").click()
    Data = str(FileReader())

# Getting Replies :-

    while True:

        # sleep(0.5)

        try:
            AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
            Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).is_displayed()
            if str(Answer)=="True":
                break

        except:
            pass


    AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
    Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).text
    NewData = int(Data) + 2
    FileWriter(Data=str(NewData))
    return Answer

# Rest Of The Code

print("Starting The GPT4-Model.")
FileWriter(Data='3')

# while True:
def GPT_Brain(Query):
    try:
        print(f'Jarvis: {ChatGPTBrain(Query=Query)}')
        Speak(ChatGPTBrain(Query=Query))

    except:
        print('There Has been some Error.')


# while True:
#     query = Listen()
#     GPT_Brain(query)