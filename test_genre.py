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
from selenium.webdriver.chrome.options import Options
@pytest.fixture(scope="function")
def setup_driver():
        
        #driver  = webdriver.Chrome()
        options = Options()
        options.add_argument("--headless")  # Run tests without UI
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        selenium_grid_url =  url # Change based on your container setup
        driver = webdriver.Remote(command_executor=selenium_grid_url,options=options)
     # Create the folder if it doesn't exist
        os.makedirs("genre_screenshots", exist_ok=True)
        driver.get("https://nextjs-typescript.onrender.com")
        driver.add_cookie(cookie)
        driver.refresh()  # Refresh to apply the cookie
        yield driver  # Return the WebDriver instance to the tests

    # Teardown: Quit the driver after all tests
        driver.quit()
def genre1(driver:webdriver.Chrome,fileName:str)->bool:
    screenshot_path = f"genre_screenshots/{fileName}.png"
    try:
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/movies")
        select_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME,"select")))
        select = Select(select_element)
        select.select_by_index(1)
        WebDriverWait(driver, 20).until(EC.url_to_be("https://netflix-deploy-feraskas-projects.vercel.app/movies?g=28"))
        driver.save_screenshot(screenshot_path)
        return True
    except Exception as e:
        driver.save_screenshot(screenshot_path)
        return False

def genre2(driver:webdriver.Chrome,fileName:str)->bool:
    screenshot_path = f"genre_screenshots/{fileName}.png"
    try:
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/movies")
        select_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME,"select")))
        select = Select(select_element)
        select.select_by_index(2)
        WebDriverWait(driver, 20).until(EC.url_to_be("https://netflix-deploy-feraskas-projects.vercel.app/movies?g=12"))
        driver.save_screenshot(screenshot_path)
        return True
    except Exception as e:
        driver.save_screenshot(screenshot_path)
        return False


def test_genre1(setup_driver):
    assert genre1(setup_driver,"test1") == True
def test_genre2(setup_driver):
    assert genre2(setup_driver,"test2") == True