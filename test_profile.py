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
@pytest.fixture(scope="function")
def setup_driver():
        options = Options()
        options.add_argument("--headless")  # Run tests without UI
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        selenium_grid_url =  url # Change based on your container setup
        driver = webdriver.Remote(command_executor=selenium_grid_url,options=options)
        #driver  = webdriver.Chrome()
     # Create the folder if it doesn't exist
        os.makedirs("profile_screenshots", exist_ok=True)
        driver.get("https://nextjs-typescript.onrender.com")
        driver.add_cookie(cookie)
        driver.refresh()  # Refresh to apply the cookie
        yield driver  # Return the WebDriver instance to the tests

    # Teardown: Quit the driver after all tests
        driver.quit()

def editProfile(driver:webdriver.Chrome,fileName:str)->bool:
        screenshot_path = f"profile_screenshots/{fileName}.png"
        try:
            driver.get("https://netflix-deploy-feraskas-projects.vercel.app/profile")
            profile = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"profile")))
            file = profile.find_element(By.ID,"file")
            file_path = os.path.abspath("cover.jpeg")
            file.send_keys(file_path)
            submit = profile.find_element(By.CSS_SELECTOR,"button[type=submit]")
            submit.click()
            #driver.refresh()
            WebDriverWait(driver, 10).until(EC.url_to_be("https://netflix-deploy-feraskas-projects.vercel.app/"))
            driver.save_screenshot(screenshot_path)
            return True
        except Exception as e:
            driver.save_screenshot(screenshot_path)
            return False

def cancelClick(driver:webdriver.Chrome,fileName:str)->bool:
        screenshot_path = f"profile_screenshots/{fileName}.png"
        try:
            driver.get("https://netflix-deploy-feraskas-projects.vercel.app/profile")
            profile = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"profile")))
            cancel = profile.find_element(By.CSS_SELECTOR,"button[type=button]")
            cancel.click()
            #driver.refresh()
            WebDriverWait(driver, 10).until(EC.url_to_be("https://netflix-deploy-feraskas-projects.vercel.app/"))
            time.sleep(2)
            driver.save_screenshot(screenshot_path)
            return True
        except Exception as e:
            driver.save_screenshot(screenshot_path)
            return False
def isAuth(driver:webdriver.Chrome,fileName:str)->bool:
        screenshot_path = f"profile_screenshots/{fileName}.png"
        driver.delete_cookie("access_token")
        try:
            driver.get("https://netflix-deploy-feraskas-projects.vercel.app/profile")
           
            #driver.refresh()
            WebDriverWait(driver, 10).until(EC.url_to_be("https://netflix-deploy-feraskas-projects.vercel.app/login"))
            time.sleep(2)
            driver.save_screenshot(screenshot_path)
            return True
        except Exception as e:
            driver.save_screenshot(screenshot_path)
            return False
def test_profile(setup_driver):
    
    assert editProfile(setup_driver,"test1") == True
def test_cancelClick(setup_driver):
    
    assert cancelClick(setup_driver,"test2") == True
def test_isAuth(setup_driver):
    
    assert isAuth(setup_driver,"test3") == True