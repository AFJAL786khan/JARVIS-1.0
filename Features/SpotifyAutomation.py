from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome('D:\MyData\Documents\CODING\Python\Jarvis\Data\Spotify\chromedriver.exe')

# driver.get(url)