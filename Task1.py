from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")

driver.get("https://techwithtim.net") 
print(driver.title)


search = driver.find_element(By.NAME,"s")
driver.get("https://techwithtim.net")
driver.set_page_load_timeout(10)
driver.maximize_window()
driver.implicitly_wait(10)
x = driver.execute_script("return document.readyState")
if x == "complete":
    assert True
else:
    assert False
print(driver.title)
search = driver.find_element(By.NAME, "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
  main = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID, "main"))
  )
  
  articals = main.find_elements(By.TAG_NAME,"article")
  for articale in articals:

    header = articale.find_element(By.CLASS_NAME ,"entery-summary")
    print(header.text)
      
finally:
  driver.quit()
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articals = main.find_elements(By.TAG_NAME, "article")
    for articale in articals:

        header = articale.find_element(By.CLASS_NAME, "entery-summary")
    print(header.text)

finally:
    driver.quit()
