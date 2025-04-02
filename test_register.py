from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import allure
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
    try:
        with allure.step("Open Netflix register Page"):
            driver.get("https://netflix-deploy-feraskas-projects.vercel.app/register")
        with allure.step("Wait for register form"):
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"register")))
        with allure.step("Enter inputs"):
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
        with allure.step("Click register Button"):
            submit.click()
         
        # Wait for URL change
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME,"p"),"register successfully"))
        # **Find the success message dynamically**
        p_tags = driver.find_elements(By.TAG_NAME, "p")
        success_msg = next((p.text for p in p_tags if "register successfully" in p.text), None)
        screenshot_path = f"register_screenshots/{fileName}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="Login Screenshot", attachment_type=allure.attachment_type.PNG)
        return success_msg == "register successfully"
    except Exception as e:
        screenshot_path = screenshot_path = f"register_screenshots/{fileName}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="Login Screenshot Error", attachment_type=allure.attachment_type.PNG)
        return False
@allure.feature("Register Functionality")
@allure.story("Valid and Invalid Register Attempts")
@pytest.mark.parametrize("f , firstName, lastName, email, password, expected",[
    
    ("test1","","","","",False),
    ("test2","","kasabri","feras.94.kasabri@gmail.com","123",False),
    ("test3","feras","","feras.94.kasabri@gmail.com","123",False),
    ("test4","feras","kasabri","","123",False),
    ("test5","feras","kasabri","feras.94.kasabri@gmail.com","",False),
    ("test6","feras","kasabri","feras.94.kasabri@gmail.com","123",False),
     ("test7","feras","kasabri","feras@gmail.com","123",False),
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
    try:
        # Open website and set cookie
        driver.get("https://nextjs-typescript.onrender.com")
        driver.add_cookie(cookie)
        with allure.step("Wait for register form"):
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME,"header")))
        screenshot_path =  f"register_screenshots/{fileName}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="register Screenshot", attachment_type=allure.attachment_type.PNG)
        return driver.current_url == 'https://netflix-deploy-feraskas-projects.vercel.app/'
    except Exception as e:
        screenshot_path =  f"register_screenshots/{fileName}.png"
        print(driver.current_url)
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="register Screenshot Error", attachment_type=allure.attachment_type.PNG)
        return False
def test_page(setup_driver):
    assert register_page(setup_driver,"test8") == True