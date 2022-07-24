from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

s = Service(r"C:\Users\Alig\Desktop\webdrivers\geckodriver.exe")


webdriver_object = webdriver.Firefox(service = s)

URL = 

webdriver_object.get(URL)
