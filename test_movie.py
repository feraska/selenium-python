from selenium import webdriver
#from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest
import requests
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
cookie = {
    "name":"access_token",
    "value":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2NTA4MTFjODlmOGYwNWQxZmNhYWZlOSIsImlhdCI6MTczMzA2NzMzMH0.HBSHII8VHPj6I6WuT_CSUefVpPLn2hNpA5KlnffkTKw",
    "domain":"nextjs-typescript.onrender.com",
    "httpOnly": True,
    "secure": True,
    "sameSite": "None",
    
}
# def quit():
#     driver.quit()
def login (e,p):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    #driver = webdriver.Chrome()
    try:
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/login")
        
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"login")))
        driver.implicitly_wait(30)
        email = driver.find_element(By.NAME,"email")
        password = driver.find_element(By.NAME,"password")

        email.send_keys(e)
    
        password.send_keys(p)
    
        submit = driver.find_element(By.TAG_NAME,"button")
        
        submit.click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"playing")))
        return True
    except Exception as e:
        return False
    finally:
        driver.quit()
def logout():

    #driver = webdriver.Chrome()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    
    try:
        #driver.get("https://netflix-deploy-feraskas-projects.vercel.app")
        driver.get("https://nextjs-typescript.onrender.com")
        driver.add_cookie(cookie)
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app")
        #driver.implicitly_wait(30)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME,"header")))
        header = driver.find_element(By.TAG_NAME,"header")
        logout = header.find_element(By.CLASS_NAME,"logout")
        logout.click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"login")))
        return True
    except Exception as e:
        print(f"error{e}")
        return False
            
def onMouseOver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    try:
        driver.get("https://nextjs-typescript.onrender.com")
        driver.add_cookie(cookie)
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app")
        driver.implicitly_wait(30)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"slider")))
        slider = driver.find_element(By.CLASS_NAME,"slider")
        li = slider.find_element(By.TAG_NAME,"li")
        actions = ActionChains(driver)
        img = li.find_element(By.TAG_NAME,"img")
        actions.move_to_element(img).perform()
        video = li.find_element(By.CLASS_NAME,"video")

        # svg = buttons[0].find_elements(By.TAG_NAME,"svg")
        # svg[0].click()
        # print(svg)
        if video.is_displayed:
            return True
        return False
    except Exception as e:
        print(f"error{e}")
        return False
def play():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    try:
        driver.get("https://nextjs-typescript.onrender.com")
        driver.add_cookie(cookie)
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app")
        driver.implicitly_wait(30)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"slider")))
        slider = driver.find_element(By.CLASS_NAME,"slider")
        li = slider.find_element(By.TAG_NAME,"li")
        img = li.find_element(By.TAG_NAME,"img")
        actions = ActionChains(driver)
        actions.move_to_element(img).perform()
        buttons = li.find_element(By.CLASS_NAME,"buttons")
        first_child = buttons.find_element(By.XPATH,'./*')
        
        actions.click(first_child).perform()
        WebDriverWait(driver, 30).until(EC.url_to_be("https://netflix-deploy-feraskas-projects.vercel.app/watch/1241982"))
        return True
    except Exception as e:
        print(f"error{e}")
        return False
def addRemove():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    try:
        driver.get("https://nextjs-typescript.onrender.com")
        driver.add_cookie(cookie)
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app")
        driver.implicitly_wait(30)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"slider")))
        slider = driver.find_element(By.CLASS_NAME,"slider")
        li = slider.find_element(By.TAG_NAME,"li")
        img = li.find_element(By.TAG_NAME,"img")
        actions = ActionChains(driver)
        actions.move_to_element(img).perform()
        buttons = li.find_element(By.CLASS_NAME,"buttons")
        child = buttons.find_elements(By.XPATH,'./*')
        second_child = child[1].find_element(By.CSS_SELECTOR,"div > svg")
        actions.click(second_child).perform()
        #WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"loading")))
        return True
    except Exception as e:
        print(f"error{e}")
        return False
def likeDislike():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    try:
        driver.get("https://nextjs-typescript.onrender.com")
        driver.add_cookie(cookie)
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app")
        driver.implicitly_wait(30)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"slider")))
        slider = driver.find_element(By.CLASS_NAME,"slider")
        li = slider.find_element(By.TAG_NAME,"li")
        img = li.find_element(By.TAG_NAME,"img")
        actions = ActionChains(driver)
        actions.move_to_element(img).perform()
        buttons = li.find_element(By.CLASS_NAME,"buttons")
        child = buttons.find_elements(By.XPATH,'./*')
        second_child = child[2].find_element(By.CSS_SELECTOR,"div > svg")
        actions.click(second_child).perform()
        #WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"loading")))
        return True
    except Exception as e:
        print(f"error{e}")
        return False
def modal():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    try:
        driver.get("https://nextjs-typescript.onrender.com")
        driver.add_cookie(cookie)
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app")
        driver.implicitly_wait(30)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"slider")))
        slider = driver.find_element(By.CLASS_NAME,"slider")
        li = slider.find_element(By.TAG_NAME,"li")
        img = li.find_element(By.TAG_NAME,"img")
        actions = ActionChains(driver)
        actions.move_to_element(img).perform()
        info = li.find_element(By.CSS_SELECTOR,".clicks > .tooltip > svg")
       
        actions.click(info).perform()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"window")))
        return True
    except Exception as e:
        print(f"error{e}")
        return False
def search():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    try:
        driver.get("https://nextjs-typescript.onrender.com")
        driver.add_cookie(cookie)
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app")
        driver.implicitly_wait(30)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME,"header")))
        header = driver.find_element(By.TAG_NAME,"header")
        search = header.find_element(By.CSS_SELECTOR,".search > svg")
        
        actions = ActionChains(driver)
        actions.click(search).perform()
        input = header.find_element(By.CSS_SELECTOR,".search > input")
        actions.send_keys_to_element(input,"f").perform()
        #WebDriverWait(driver, 30).until(EC.element_attribute_to_include("f"))
        return True
    except Exception as e:
        print(f"error{e}")
        return False
def register(e,p,f,l):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    #driver = webdriver.Chrome()
    try:
        driver.get("https://netflix-deploy-feraskas-projects.vercel.app/register")
        
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"register")))
        driver.implicitly_wait(30)
        email = driver.find_element(By.NAME,"email")
        password = driver.find_element(By.NAME,"password")
        firstName = driver.find_element(By.NAME,"firstName")
        lastName = driver.find_element(By.NAME,"lastName")
        email.send_keys(e)
        password.send_keys(p)
        firstName.send_keys(f)
        lastName.send_keys(l)
        submit = driver.find_element(By.TAG_NAME,"button")
        
        submit.click()
        p = driver.find_elements(By.TAG_NAME,"p")[1]
        WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element(p,"register successfully"))
        return True
    except Exception as e:
        return False
    #finally:
        #driver.quit()
# Open a webpage
@pytest.mark.parametrize("a, b, expected",[
    ("feras.94.kasabri@gmail.com", "123" , True),
    ("","",False),
    ("f.gmail.com","123",False),
    ("feras.94.kasabri@gmail.com","12",False),
    ("f.gmail.com","123",False)
],ids=["success","empty","email f","password f","email & password failure"])
def test_login(a,b,expected):
    assert login(a,b) == expected
    #driver.quit()
def test_logout():
    assert logout() == True

def test_onMouseOver():
    assert onMouseOver() == True
def test_play():
    assert play() == True
def test_addRemove():
    assert addRemove() == True
def test_likeDislike():
    assert likeDislike() == True
def test_modal():
    assert modal() == True
def test_search():
    assert search() == True 
@pytest.mark.parametrize("e, p, f, l, expected",
    [
        ("feras.94.kasabri@gmail.com","123","sanad","kasabri",False),
        ("sanad@gmail.com","123","sanad","kasabri",False),

    ],
    ids=["user is found","success"]
    )   
def test_register(e,p,f,l,expected):
    assert register(e,p,f,l) == expected