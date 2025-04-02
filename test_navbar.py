from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import os
import time
from cons import cookie
from cons import cookieN
@pytest.fixture(scope="session")
def setup_driver():
        
        driver  = webdriver.Chrome()
     # Create the folder if it doesn't exist
        os.makedirs("navbar_screenshots", exist_ok=True)
        driver.get("https://nextjs-typescript.onrender.com")
        driver.add_cookie(cookie)
        driver.refresh()  # Refresh to apply the cookie
        yield driver  # Return the WebDriver instance to the tests

    # Teardown: Quit the driver after all tests
        driver.quit()
def navbar_imgClick(driver:webdriver.Chrome,fileName:str)->bool:
    try:
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/")
        user = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"user")))
        img = user.find_element(By.TAG_NAME,'img')
        img.click()
        screenshot_path = f"navbar_screenshots/{fileName}.png"
        driver.save_screenshot(screenshot_path)
        settings = user.find_element(By.CLASS_NAME,'settings')
        return settings.is_displayed()
           
    except Exception as e:
        screenshot_path = screenshot_path = f"navbar_screenshots/{fileName}.png"
        driver.save_screenshot(screenshot_path)
        return False

def navbar_iconSearch(driver:webdriver.Chrome,fileName:str)->bool:
    try:
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/")
      
        search = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"search")))
        icon = search.find_element(By.TAG_NAME,'svg')
        icon.click()
        input = search.find_element(By.TAG_NAME,'input')
        input.send_keys("f")
        time.sleep(3)
        screenshot_path = f"navbar_screenshots/{fileName}.png"
        driver.save_screenshot(screenshot_path)
        WebDriverWait(driver,10).until(EC.url_to_be('https://netflix-deploy-feraskas-projects.vercel.app/search?q=f'))
       
        return True
           
    except Exception as e:
        screenshot_path = screenshot_path = f"navbar_screenshots/{fileName}.png"
        driver.save_screenshot(screenshot_path)
        return False

def navbar_iconNotification(driver:webdriver.Chrome,fileName:str)->bool:
    try:

        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/")
        notification = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"notification")))
        icon = notification.find_element(By.TAG_NAME,'svg')
        icon.click()     
        message = WebDriverWait(notification, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"messsage")))
        screenshot_path = f"navbar_screenshots/{fileName}.png"
        driver.save_screenshot(screenshot_path)
        return message.is_displayed()
           
    except Exception as e:
        screenshot_path = screenshot_path = f"navbar_screenshots/{fileName}.png"
        driver.save_screenshot(screenshot_path)
        return False

def navbar_iconLogout(driver:webdriver.Chrome,fileName:str)->bool:
    try:
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/")
        user = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"user")))
        img = user.find_element(By.TAG_NAME,'img')
        img.click()
        logout = user.find_element(By.CLASS_NAME,'logout')
        logout.click()
        screenshot_path = f"navbar_screenshots/{fileName}.png"
        driver.save_screenshot(screenshot_path)
        return driver.get_cookie('access_token') == None
           
    except Exception as e:
        screenshot_path = screenshot_path = f"navbar_screenshots/{fileName}.png"
        driver.save_screenshot(screenshot_path)
        return False
def navbar_changePassword(driver:webdriver.Chrome,fileName:str)->bool:
    try:
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/")
        user = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"user")))
        img = user.find_element(By.TAG_NAME,'img')
        img.click()
        settings = user.find_element(By.CLASS_NAME,'settings')
        a = settings.find_elements(By.TAG_NAME,'a')[0]
        a.click()
        screenshot_path = f"navbar_screenshots/{fileName}.png"
        WebDriverWait(driver, 20).until(EC.url_to_be("https://netflix-deploy-feraskas-projects.vercel.app/password"))
        driver.save_screenshot(screenshot_path)
        return True
    except Exception as e:
        screenshot_path = screenshot_path = f"navbar_screenshots/{fileName}.png"
        driver.save_screenshot(screenshot_path)
        return False
def navbar_editProfile(driver:webdriver.Chrome,fileName:str)->bool:
    try:
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/")
        user = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"user")))
        img = user.find_element(By.TAG_NAME,'img')
        img.click()
        settings = user.find_element(By.CLASS_NAME,'settings')
        a = settings.find_elements(By.TAG_NAME,'a')[1]
        a.click()
        screenshot_path = f"navbar_screenshots/{fileName}.png"
        WebDriverWait(driver, 20).until(EC.url_to_be("https://netflix-deploy-feraskas-projects.vercel.app/profile"))
        driver.save_screenshot(screenshot_path)
        return True
    except Exception as e:
        screenshot_path = screenshot_path = f"navbar_screenshots/{fileName}.png"
        driver.save_screenshot(screenshot_path)
        return False
def navbar_sendMsg(driver:webdriver.Chrome,fileName:str)->bool:
    try:
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/")
        user = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"user")))
        img = user.find_element(By.TAG_NAME,'img')
        img.click()
        settings = user.find_element(By.CLASS_NAME,'settings')
        a = settings.find_elements(By.TAG_NAME,'a')[2]
        a.click()
        screenshot_path = f"navbar_screenshots/{fileName}.png"
        WebDriverWait(driver, 20).until(EC.url_to_be("https://netflix-deploy-feraskas-projects.vercel.app/sendMsg"))
        driver.save_screenshot(screenshot_path)
        return True
    except Exception as e:
        screenshot_path = screenshot_path = f"navbar_screenshots/{fileName}.png"
        driver.save_screenshot(screenshot_path)
        return False
def navbar_isAuth(driver:webdriver.Chrome,fileName:str)->bool:
    try:
        driver.add_cookie(cookieN)
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/")
        user = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"user")))
        img = user.find_element(By.TAG_NAME,'img')
        img.click()
        settings = user.find_element(By.CLASS_NAME,'settings')
        a = settings.find_elements(By.TAG_NAME,'a')[2]
        a.click()
        screenshot_path = f"navbar_screenshots/{fileName}.png"
        driver.save_screenshot(screenshot_path)
        return False
    except Exception as e:
        screenshot_path = screenshot_path = f"navbar_screenshots/{fileName}.png"
        driver.save_screenshot(screenshot_path)
        return True
def test_imgClick(setup_driver):
    assert navbar_imgClick(setup_driver,"test1") == True
def test_iconSearch(setup_driver):
    assert navbar_iconSearch(setup_driver,"test2") == True
def test_iconNotification(setup_driver):
    assert navbar_iconNotification(setup_driver,"test3") == True
def test_iconLogout(setup_driver):
    assert navbar_iconLogout(setup_driver,"test4") == True
def test_changePassword(setup_driver):
    assert navbar_changePassword(setup_driver,"test5") == True
def test_editProfile(setup_driver):
    assert navbar_editProfile(setup_driver,"test6") == True
def test_sendMsg(setup_driver):
    assert navbar_sendMsg(setup_driver,"test7") == True
def test_isAuth(setup_driver):
    assert navbar_isAuth(setup_driver,"test8") == True