from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import os
import time
from cons import cookie,url
from cons import cookieN
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
@pytest.fixture(scope="session")
def setup_driver():
        options = Options()
        options.add_argument("--headless")  # Run tests without UI
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        selenium_grid_url =  url # Change based on your container setup
        driver = webdriver.Remote(command_executor=selenium_grid_url,options=options)
        #driver  = webdriver.Chrome()
     # Create the folder if it doesn't exist
        os.makedirs("sendMsg_screenshots", exist_ok=True)
        driver.get("https://nextjs-typescript.onrender.com")
        driver.add_cookie(cookie)
        driver.refresh()  # Refresh to apply the cookie
        yield driver  # Return the WebDriver instance to the tests

    # Teardown: Quit the driver after all tests
        driver.quit()
def sendMsg(driver:webdriver.Chrome,fileName:str,msg:str)->bool:
        screenshot_path = f"sendMsg_screenshots/{fileName}.png"
        try:
            driver.get("https://netflix-deploy-feraskas-projects.vercel.app/sendMsg")
            sendMsg = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"sendMsg")))
            input = sendMsg.find_element(By.TAG_NAME,"input")
            input.send_keys(msg)
            button = sendMsg.find_element(By.TAG_NAME,"button")
            button.click()
            p_tags = driver.find_elements(By.TAG_NAME, "p")
            WebDriverWait(driver, 10).until(EC.visibility_of(p_tags[1]))
            driver.save_screenshot(screenshot_path)
            return True
        except Exception as e:
            driver.save_screenshot(screenshot_path)
            return False
    
def isAuth(driver:webdriver.Chrome,fileName:str)->bool:
        screenshot_path = f"sendMsg_screenshots/{fileName}.png"
        driver.delete_cookie('access_token')
        try:
            driver.get("https://netflix-deploy-feraskas-projects.vercel.app/sendMsg")
            WebDriverWait(driver, 10).until(EC.url_to_be("https://netflix-deploy-feraskas-projects.vercel.app/login"))
            time.sleep(2)
            driver.save_screenshot(screenshot_path)
            return True
        except Exception as e:
            driver.save_screenshot(screenshot_path)
            return False
def isAdmin(driver:webdriver.Chrome,fileName:str)->bool:
        screenshot_path = f"sendMsg_screenshots/{fileName}.png"
        driver.add_cookie(cookieN)
        try:
            driver.get("https://netflix-deploy-feraskas-projects.vercel.app/sendMsg")
            WebDriverWait(driver, 10).until(EC.url_to_be("https://netflix-deploy-feraskas-projects.vercel.app/login"))
            time.sleep(2)
            driver.save_screenshot(screenshot_path)
            return True
        except Exception as e:
            driver.save_screenshot(screenshot_path)
            return False
@pytest.mark.parametrize("f , msg, expected",[
    
    ("test1","",False),
    ("test2","yael",True),
],ids=[
    "msg is empty",
    "msg is not empty",
       ])
def test_sendMsg(setup_driver,f,msg,expected):
    
    assert sendMsg(setup_driver,f,msg) == expected
def test_isAuth(setup_driver):
    
    assert isAuth(setup_driver,"test3") == True
def test_isAdmin(setup_driver):
    
    assert isAdmin(setup_driver,"test4") == False
