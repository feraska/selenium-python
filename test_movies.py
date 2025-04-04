from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import os
import time
from cons import cookie,url
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
         #driver = webdriver.Remote(command_executor=selenium_grid_url, options=options)
        #driver  = webdriver.Chrome()
     # Create the folder if it doesn't exist
         os.makedirs("movies_screenshots", exist_ok=True)
         driver.get("https://nextjs-typescript.onrender.com")
         driver.add_cookie(cookie)
         driver.refresh()  # Refresh to apply the cookie
         yield driver  # Return the WebDriver instance to the tests

    # Teardown: Quit the driver after all tests
         driver.quit()
def tologin(driver:webdriver.Chrome,fileName:str)->bool:
      screenshot_path = f"movies_screensohts/{fileName}.png"
      try:
            driver.delete_cookie("access_token")
            driver.get("https://netflix-deploy-feraskas-projects.vercel.app/movies")
            WebDriverWait(driver, 10).until(EC.url_to_be("https://netflix-deploy-feraskas-projects.vercel.app/login"))  # Wait for URL change
            driver.save_screenshot(screenshot_path)
            return True
      except Exception as e:
            driver.save_screenshot(screenshot_path)
            return False

def test_page(setup_driver):
    assert tologin(setup_driver,"test1") == True
