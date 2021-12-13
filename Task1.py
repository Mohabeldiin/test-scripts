from selenium import webdriver
from selenium.webdriver.common.keys import Keys #The Keys are referring to keyboard keys. It's used to ID the different Keys on the keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
PATH = "C:\Selenuim file\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net") # when u wanna to go to this website
print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
  main = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID, "main"))
  )
  #print(main.text)
  articals = main.find_element_by_tag_name("article")
  for articale in articals:
    header =articale.find_element_by_class_name("entery-summary")
    print(header.tex)
      
finally:
  driver.quit()

#print(driver.page_source)

#time.sleep(2)
#driver.quit() # it will close the chrome but if we wanna to close the specific tab use [driver.close()]

