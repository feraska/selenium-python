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
@pytest.fixture(scope="session")
def setup_driver():
         options = Options()
         options.add_argument("--headless")  # Run tests without UI
         options.add_argument("--no-sandbox")
         options.add_argument("--disable-dev-shm-usage")

         selenium_grid_url =  url # Change based on your container setup
         driver = webdriver.Remote(command_executor=selenium_grid_url)
         #driver = webdriver.Remote(command_executor=selenium_grid_url, options=options)
        #driver  = webdriver.Chrome()
     # Create the folder if it doesn't exist
         os.makedirs("cardItem_screenshots", exist_ok=True)
         driver.get("https://nextjs-typescript.onrender.com")
         driver.add_cookie(cookie)
         driver.refresh()  # Refresh to apply the cookie
         yield driver  # Return the WebDriver instance to the tests

    # Teardown: Quit the driver after all tests
         driver.quit()
def onMouseOver(driver:webdriver.Chrome,fileName:str)->bool:
    screenshot_path = f"cardItem_screenshots/{fileName}.png"
    try:
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/")
        slider = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"slider")))
        
        li = WebDriverWait(slider, 20).until(EC.presence_of_element_located((By.TAG_NAME,"li")))
        actions = ActionChains(driver)
        img = li.find_element(By.TAG_NAME,"img")
        
        actions.move_to_element(img).perform()
        video = WebDriverWait(li, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"video")))
        time.sleep(3)
        driver.save_screenshot(screenshot_path)
        return True
    except Exception as e:
        driver.save_screenshot(screenshot_path)
        return False


def play(driver:webdriver.Chrome,fileName:str)->bool:
    screenshot_path = f"cardItem_screenshots/{fileName}.png"
    try:
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/")
        slider = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"slider")))
        
        li = WebDriverWait(slider, 20).until(EC.presence_of_element_located((By.TAG_NAME,"li")))
        actions = ActionChains(driver)
        img = li.find_element(By.TAG_NAME,"img")
        
        actions.move_to_element(img).perform()
        video = WebDriverWait(li, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"video")))

        buttons = li.find_element(By.CLASS_NAME,"buttons")
        first_child = buttons.find_element(By.XPATH,'./*')
        actions.click(first_child).perform()
        time.sleep(3)
        driver.save_screenshot(screenshot_path)
        return WebDriverWait(driver, 10).until(EC.url_contains('https://netflix-deploy-feraskas-projects.vercel.app/watch/'))
    except Exception as e:
        driver.save_screenshot(screenshot_path)
        return False
def addRemove(driver:webdriver.Chrome,fileName:str)->bool:
    screenshot_path = f"cardItem_screenshots/{fileName}.png"
    try:
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/")
        slider = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"slider")))
        li = WebDriverWait(slider, 20).until(EC.presence_of_element_located((By.TAG_NAME,"li")))
        actions = ActionChains(driver)
        img = li.find_element(By.TAG_NAME,"img")
        
        actions.move_to_element(img).perform()
        video = WebDriverWait(li, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"video")))

        buttons = li.find_element(By.CLASS_NAME,"buttons")
        sec_child = buttons.find_elements(By.XPATH,'./*')[1]
        second_child = sec_child.find_element(By.CSS_SELECTOR,"div > svg")
        actions.click(second_child).perform()
        time.sleep(3)
        driver.save_screenshot(screenshot_path)
        return True
    except Exception as e:
        driver.save_screenshot(screenshot_path)
        return False
def likeDislike(driver:webdriver.Chrome,fileName:str)->bool:
    screenshot_path = f"cardItem_screenshots/{fileName}.png"
    try:
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/")
        slider = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"slider")))
        
        li = WebDriverWait(slider, 20).until(EC.presence_of_element_located((By.TAG_NAME,"li")))
        actions = ActionChains(driver)
        img = li.find_element(By.TAG_NAME,"img")
        
        actions.move_to_element(img).perform()
        video = WebDriverWait(li, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"video")))

        buttons = li.find_element(By.CLASS_NAME,"buttons")
        sec_child = buttons.find_elements(By.XPATH,'./*')[2]
        second_child = sec_child.find_element(By.CSS_SELECTOR,"div > svg")
        actions.click(second_child).perform()
        time.sleep(3)
        driver.save_screenshot(screenshot_path)
        return True
    except Exception as e:
        driver.save_screenshot(screenshot_path)
        return False
def modal(driver:webdriver.Chrome,fileName:str)->bool:
    screenshot_path = f"cardItem_screenshots/{fileName}.png"
    try:
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/")
        slider = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"slider")))
        li = WebDriverWait(slider, 20).until(EC.presence_of_element_located((By.TAG_NAME,"li")))
        actions = ActionChains(driver)
        img = li.find_element(By.TAG_NAME,"img")
        actions.move_to_element(img).perform()
        video = WebDriverWait(li, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"video")))

        info = li.find_element(By.CSS_SELECTOR,".clicks > .tooltip > svg")
        actions.click(info).perform()
        
        time.sleep(3)
        driver.save_screenshot(screenshot_path)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"window")))
        return True
    except Exception as e:
        driver.save_screenshot(screenshot_path)
        return False
def test_mouseOver(setup_driver):
    assert onMouseOver(setup_driver,"test1") == True
def test_play(setup_driver):
    assert play(setup_driver,"test2") == True
def test_addRemove(setup_driver):
    assert addRemove(setup_driver,"test3") == True
def test_likeDislike(setup_driver):
    assert likeDislike(setup_driver,"test4") == True
def test_modal(setup_driver):
    assert modal(setup_driver,"test5") == True