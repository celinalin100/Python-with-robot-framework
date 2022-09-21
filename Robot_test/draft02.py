from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


s=Service('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
chrome_web = webdriver.Chrome(service=s)
url = "https://furbo.com/tw"


def close_popup():
    chrome_web.get(url)
    chrome_web.implicitly_wait(5)
    chrome_web.maximize_window()
    # Explicitly wait:
    wait = WebDriverWait(chrome_web, 20)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pge_1ywRD0t10 > div.om-global-close-button.om-popup-close > span"))).click()
    #Wait Pop up banner -->close the banner
    print("Pop up window is closed successfully!")
    #Get into Furbb website

    chrome_web.close()
    
    pass
    



