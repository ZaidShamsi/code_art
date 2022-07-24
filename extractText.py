# Using selenium for data extraction
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# for suppressing the browser
from selenium.webdriver.firefox.options import Options

option = webdriver.FirefoxOptions()
option.add_argument('--headless')
s = Service(r"C:\Users\Alig\Desktop\webdrivers\geckodriver.exe")
#driver_object = webdriver.Firefox(service = s, options = option)
driver_object = webdriver.Firefox(service = s)
driver_object.implicitly_wait(10)

def extractText(URL):
    driver_object.get(URL)
    more_places_btn = driver_object.find_element(By.CSS_SELECTOR, "div[class = 'mSBLIb ndElDd'] a")
    more_places_btn.click()
    anchorTagList = driver_object.find_elements(By.CSS_SELECTOR, "div[class='VkpGBb']")
    address_list = []
    phone_list = []
    company_name_list = []
    index = 0
    for anchorTag in anchorTagList:
        anchorTag.click()
        if index == 0:
            print(index)
            company_name_1 = driver_object.find_element(By.CSS_SELECTOR, "div[class='SPZz6b'] h2 span").get_attribute('innerText')
            #company_name_1 = company_name_1.get_attribute('innerText')
            #print(company_name_1)
            company_name_list.append(company_name_1)
            try:
                address = driver_object.find_element(By.CSS_SELECTOR, "span[class='LrzXr']")
                address = address.get_attribute('innerText')
                #print(address)
                address_list.append(address)
                phone = driver_object.find_element(By.CSS_SELECTOR, "span[class='LrzXr zdqRlf kno-fv'] a span")
                phone = phone.get_attribute('innerText')
                #print(phone)
                phone_list.append(phone)
            except:
                address_list.append('Not Found')
                phone_list.append('Not Found')
        elif index > 0:
            print(index)
            company_name_2 = driver_object.find_element(By.CSS_SELECTOR, "div[class='SPZz6b'] h2 span").get_attribute('innerText')
            #company_name_2 = company_name_2.get_attribute('innerText')
            #print(company_name_2)
            #company_name_list.append(company_name_2)
            while company_name_2 == company_name_1:
                print('inside while loop')
                time.sleep(2)
                company_name_2 = driver_object.find_element(By.CSS_SELECTOR, "div[class='SPZz6b'] h2 span").get_attribute('innerText')
                #company_name_2 = company_name_2.get_attribute('innerText')
                #print(company_name_2)
            company_name_list.append(company_name_2)
            company_name_1 = company_name_2
            try:
                address = driver_object.find_element(By.CSS_SELECTOR, "span[class='LrzXr']")
                address = address.get_attribute('innerText')
                #print(address)
                address_list.append(address)
                phone = driver_object.find_element(By.CSS_SELECTOR, "span[class='LrzXr zdqRlf kno-fv'] a span")
                phone = phone.get_attribute('innerText')
                #print(phone)
                phone_list.append(phone)
            except:
                address_list.append('Not Found')
                phone_list.append('Not Found')
        index += 1
    return company_name_list, address_list, phone_list
