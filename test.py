from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path=r'C:/Users/DELL/Downloads/chromedriver_win32_80/chromedriver.exe')
driver.get("https://www.piraiinfo.com")   # To load the webpage
time.sleep(0.5)  #delay
driver.get("https://piraiinfo.com/about-us/") #navigate to next pages
time.sleep(0.5)
driver.get("https://piraiinfo.com/data-services/")
time.sleep(1)
driver.get("https://piraiinfo.com/cloud-services/")
time.sleep(0.5)
driver.get("https://piraiinfo.com/devops-service/")
time.sleep(1)
driver.get("https://piraiinfo.com/contact-us/")
name = driver.find_element_by_xpath("//input[@placeholder='Name']")#to fill the contact us form using xpath locater
name.send_keys('M.Poojha')
email = driver.find_element_by_xpath("//input[@placeholder='Email']")
email.send_keys('poojhasweetie@gmail.com')
Phone = driver.find_element_by_xpath("//input[@placeholder='Phone Number']")
Phone.send_keys('8870447784')
Mess = driver.find_element_by_xpath("//textarea[@placeholder='Message']")
Mess.send_keys('Thankyou for shortlisting me')
submitbtn = driver.find_element_by_xpath("//input[@class=wpcf7-form-control wpcf7-submit send-btn sub_but']")#to submit the form using selenium script
submitbtn.click()

