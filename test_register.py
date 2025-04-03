from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest

import os
import time
from cons import cookie
@pytest.fixture(scope="session")
def setup_driver():
        driver = webdriver.Chrome()
     # Create the folder if it doesn't exist
        os.makedirs("navbar_screenshots", exist_ok=True)
        yield driver  # Return the WebDriver instance to the tests

    # Teardown: Quit the driver after all tests
        driver.quit()


def register_success(driver:webdriver.Chrome,fileName:str,firstNameValue:str,lastNameValue:str,emailValue:str,passwordValue:str)->bool:
    screenshot_path = screenshot_path = f"register_screenshots/{fileName}.png"
    try:
        
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/register")
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"register")))
        
        firstName = driver.find_element(By.NAME,"firstName")
        lastName = driver.find_element(By.NAME,"lastName")
        email = driver.find_element(By.NAME,"email")
        password = driver.find_element(By.NAME,"password")
        driver.implicitly_wait(10)  
        firstName.send_keys(firstNameValue)
        lastName.send_keys(lastNameValue)
        email.send_keys(emailValue)
        password.send_keys(passwordValue)
        submit = driver.find_element(By.TAG_NAME,"button")
        submit.click()
        p_tags = driver.find_elements(By.TAG_NAME, "p")
        WebDriverWait(driver, 10).until(EC.visibility_of(p_tags[1]))
        return True
    except Exception as e:
        driver.save_screenshot(screenshot_path)
        return False

@pytest.mark.parametrize("f , firstName, lastName, email, password, expected",[
    
    ("test1","","","","",False),
    ("test2","","kasabri","feras.94.kasabri@gmail.com","123",False),
    ("test3","feras","","feras.94.kasabri@gmail.com","123",False),
    ("test4","feras","kasabri","","123",False),
    ("test5","feras","kasabri","feras.94.kasabri@gmail.com","",False),
    ("test6","feras","kasabri","feras.94.kasabri@gmail.com","123",False),
     ("test7","feras","kasabri","feras.94@hotmail.com","123",False),
],ids=[
    "all fields is empty",
    "If first name is empty and all this not empty message error",
    "If last name is empty and all of this not empty message error",
    "If email is empty and all of this not empty message error",
    "If password is empty and all of this not empty message error",
    "If the user exists",
    "If all the fields are correct",
       ])
def test_register(setup_driver,f,firstName,lastName,email,password,expected):
    
    assert register_success(setup_driver,f,firstName,lastName,email,password) == expected
def register_page(driver:webdriver.Chrome,fileName:str)->bool:
    screenshot_path =  f"register_screenshots/{fileName}.png"
    try:
        # Open website and set cookie
        driver.get("https://nextjs-typescript.onrender.com")
        driver.add_cookie(cookie)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME,"header")))
        driver.save_screenshot(screenshot_path)
        return driver.current_url == 'https://netflix-deploy-feraskas-projects.vercel.app/'
    except Exception as e:
        driver.save_screenshot(screenshot_path)
        return False
def test_page(setup_driver):
    assert register_page(setup_driver,"test8") == True