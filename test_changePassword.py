from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import os
import time
from cons import cookie
from cons import cookieN
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
@pytest.fixture(scope="session")
def setup_driver():
        
        driver  = webdriver.Chrome()
     # Create the folder if it doesn't exist
        os.makedirs("changePassword_screenshots", exist_ok=True)
        driver.get("https://nextjs-typescript.onrender.com")
        driver.add_cookie(cookie)
        driver.refresh()  # Refresh to apply the cookie
        yield driver  # Return the WebDriver instance to the tests

    # Teardown: Quit the driver after all tests
        driver.quit()
def changePassword(driver:webdriver.Chrome,fileName:str,currentPasswordValue:str,newPasswordValue:str,rePasswordValue:str)->bool:
        screenshot_path = f"changePassword_screenshots/{fileName}.png"
        try:
            driver.get("https://netflix-deploy-feraskas-projects.vercel.app/password")
            password = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"password")))
            currentPassword = password.find_element(By.NAME,"currentPassword")
            newPassword = password.find_element(By.NAME,"newPassword")
            rePassword = password.find_element(By.NAME,"rePassword")
            submit = password.find_element(By.CSS_SELECTOR,"button[type=submit]")
            currentPassword.send_keys(currentPasswordValue)
            newPassword.send_keys(newPasswordValue)
            rePassword.send_keys(rePasswordValue)
            submit.click()

            WebDriverWait(driver, 10).until(EC.url_to_be("https://netflix-deploy-feraskas-projects.vercel.app/"))
            driver.save_screenshot(screenshot_path)
            return True
        except Exception as e:
            driver.save_screenshot(screenshot_path)
            return False

def cancelClick(driver:webdriver.Chrome,fileName:str)->bool:
        screenshot_path = f"changePassword_screenshots/{fileName}.png"
        try:
            driver.get("https://netflix-deploy-feraskas-projects.vercel.app/password")
            password = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"password")))
            
            cancel = password.find_element(By.CSS_SELECTOR,"button[type=button]")
            cancel.click()
            WebDriverWait(driver, 10).until(EC.url_to_be("https://netflix-deploy-feraskas-projects.vercel.app/"))
            driver.save_screenshot(screenshot_path)
            return True
        except Exception as e:
            driver.save_screenshot(screenshot_path)
            return False


def isAuth(driver:webdriver.Chrome,fileName:str)->bool:
        screenshot_path = f"changePassword_screenshots/{fileName}.png"
        driver.delete_cookie('access_token')
        try:
            driver.get("https://netflix-deploy-feraskas-projects.vercel.app/password")
            WebDriverWait(driver, 10).until(EC.url_to_be("https://netflix-deploy-feraskas-projects.vercel.app/login"))
            time.sleep(2)
            driver.save_screenshot(screenshot_path)
            return True
        except Exception as e:
            driver.save_screenshot(screenshot_path)
            return False
@pytest.mark.parametrize("f , currentPassword, newPassword,rePassword, expected",[
    
    ("test1","","","",False),
    ("test2","","1","1",False),
    ("test3","1","","2",False),
    ("test4","1","2","",False),
    ("test5","1","1","2",False),
    ("test6","1","2","2",False),
    ("test7","123","123","123",True),
],ids=[
    "All fields are not empty",
    "current password is empty and other not",
    "new password is empty and other not",
    "re-type password is empty and other not",
    "new password and retype password is not equal",
    "the currrent password and new password is  equal but the current password not correct",
    "the all is correct",
       ])
def test_changePassword(setup_driver,f,currentPassword,newPassword,rePassword,expected):
    
    assert changePassword(setup_driver,f,currentPassword,newPassword,rePassword) == expected
def test_cancelClick(setup_driver):
    
    assert cancelClick(setup_driver,"test8") == True
def test_isAuth(setup_driver):
    
    assert isAuth(setup_driver,"test9") == True