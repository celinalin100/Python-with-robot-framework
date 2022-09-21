from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By




# option= webdriver.ChromeOptions()
# option.add_experimental_option("detach",True)
s=Service('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url='https://www.pinkoi.com/'
driver.get(url)

driver.implicitly_wait(5)
driver.maximize_window()

def login():
 
    logInButton = driver.find_element(By.CSS_SELECTOR,"#gheader > div > div > div.header-right > div > a.login.tab > span")
    logInButton.click()

    driver.implicitly_wait(5)

    google_log_in = driver.find_element(By.CSS_SELECTOR,"body > div.m-modal-desktop-wrap.m-modal-wrapper.m-login-desktop-modal-wrap.m-login-desktop-modal-wrap > div.m-modal-desktop.m-modal__body > div > div > div.n-login-entry > div.entry__content > div.n-login-wrapper > div.entry__sns-btn-group > div > div.sns-btn.sns-btn--google")
    google_log_in.click()

    driver.implicitly_wait(5)

    userid = driver.find_element(By.CSS_SELECTOR,"#identifierId")
    userid.send_keys("your_email")
    #the email without mobile phone number.

    continue_button_id = driver.find_element(By.CSS_SELECTOR,"#identifierNext > div > button > span")
    continue_button_id.click()
    driver.implicitly_wait(5)

    pwd = driver.find_element(By.CSS_SELECTOR,"#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
    pwd.send_keys("your_password")
    
    continue_button_pwd = driver.find_element(By.CSS_SELECTOR,"#passwordNext > div > button > span")
    continue_button_pwd.click()
    
    print("log_in pass!!!")

    driver.close()
    pass


