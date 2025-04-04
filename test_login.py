from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import os
from cons import cookie,url
from selenium.webdriver.chrome.options import Options
@pytest.fixture(scope="function")
def setup_driver():
        #driver = webdriver.Chrome()
        options = Options()
        options.add_argument("--headless")  # Run tests without UI
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        selenium_grid_url =  url # Change based on your container setup
        driver = webdriver.Remote(command_executor=selenium_grid_url,options=options)
     # Create the folder if it doesn't exist
        os.makedirs("login_screenshots", exist_ok=True)
        yield driver  # Return the WebDriver instance to the tests

    # Teardown: Quit the driver after all tests
        driver.quit()
def login_success(driver:webdriver.Chrome,fileName:str,emailValue:str,passwordValue:str)->bool:
    screenshot_path = f"login_screenshots/{fileName}.png"
    try:
            
            driver.get("https://netflix-deploy-feraskas-projects.vercel.app/login")
        
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"login")))
        
            email = driver.find_element(By.NAME,"email")
            password = driver.find_element(By.NAME,"password")
            driver.implicitly_wait(10)  
            email.send_keys(emailValue)
            password.send_keys(passwordValue)
            submit = driver.find_element(By.TAG_NAME,"button")
        
            submit.click()
           
        
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME,"header")))

            driver.save_screenshot(screenshot_path)

            return driver.current_url == 'https://netflix-deploy-feraskas-projects.vercel.app/'
           
    except Exception as e:
        driver.save_screenshot(screenshot_path)
        return False
@pytest.mark.parametrize("f , email, password, expected",[
    
    ("test1","","",False),
    ("test2","","123",False),
    ("test3","","12",False),
    ("test4","f.gmail.com","",False),
    ("test5","feras.94.kasabri@gmail.com","",False),
    ("test6","f.gmail.com","12",False),
     ("test7","feras.94.kasabri@gmail.com","12",False),
    ("test8","f.gmail.com","123",False),
    ("test9","feras.94.kasabri@gmail.com", "123" , True),
],ids=[
    "all fields is empty",
    "email is empty and the password is correct",
    "email is empty and the password is incorrect",
    "email is incorrect and the password is empty",
    "email is correct and the password is empty",
    "email is incorrect and the password is incorrect",
    "email is correct and the password is incorrect",
    "email is incorrect and the password is correct",
    "email is correct and the password is correct",
       ])
def test_login(setup_driver,f,email,password,expected):
    
    assert login_success(setup_driver,f,email,password) == expected
def login_page(driver:webdriver.Chrome,fileName:str)->bool:
    screenshot_path =  f"login_screenshots/{fileName}.png"
    try:
            driver.get("https://netflix-deploy-feraskas-projects.vercel.app/login")
            WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))  # Wait for URL change
            driver.save_screenshot(screenshot_path)
            return driver.current_url == 'https://netflix-deploy-feraskas-projects.vercel.app/'
    except Exception as e:
        driver.save_screenshot(screenshot_path)
        return False
def test_page(setup_driver):
    assert login_page(setup_driver,"test10") == True