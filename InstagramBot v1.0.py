from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random


def scroll_option():
    followers_ul = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="_aano"]')))
    for i in range(1, 2):
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="_aano"]')))
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_ul)
        time.sleep(random.randint(0, 1))


def sub_process():
    global donor_sub, count

    print(f"Started at {time.strftime('%X')}")
    time_left = count + random.randint(120, 170)
    print("Time left to complete ≈", time_left, "min.")
    # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#react-root > section > main > div > div > div > section > div > button')))
    time.sleep(5)
    url_followers = f'https://www.instagram.com/{donor_sub}/followers/'
    browser.get(url_followers)
    repeats = 0

    while repeats < count:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="_aano"]')))
        if browser.find_elements(By.XPATH, "//button[@class='_acan _acap _acas']"):
            try:
                wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="_aano"]')))
                wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_acan _acap _acas"]'))).click()
                time.sleep(random.randint(50, 70))
                repeats += 1
            except:
                time.sleep(random.randint(510, 650))
                wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_a9-- _a9_1"]'))).click()
        else:
            print("No such SUB buttons")
            print("Scrolling")
            while True:
                scroll_option()
                time.sleep(random.randint(0, 1))
                if browser.find_elements(By.XPATH, "//button[@class='_acan _acap _acas']"):
                    break
    print('---Subscribe Process Complete---', repeats, '/', count)
    print(f"Finished at {time.strftime('%X')}")


def unsub_process():
    global account_name, count

    print(f"Started at {time.strftime('%X')}")
    time_left = count + random.randint(90, 120)
    print("Time left to complete ≈", time_left, "min.")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#react-root > section > main > div > div > div > section > div > button')))
    time.sleep(0.5)
    url_following = f'https://www.instagram.com/{account_name}/following/'
    browser.get(url_following)
    repeats = 0
    limit = 0

    while repeats < count:
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_acan _acap _acat"]'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_a9-- _a9-_"]'))).click()
            time.sleep(random.randint(50, 70))
            repeats += 1
            limit += 1
            if (limit % 11 == 0) and (limit > 0):
                time.sleep(random.randint(1, 3))
                browser.refresh()
                time.sleep(random.randint(10, 25))
            if (repeats % 50 == 0) and (repeats > 0):
                time.sleep(random.randint(1, 3))
                browser.refresh()
                time.sleep(random.randint(850, 1200))
        except:
            time.sleep(random.randint(510, 650))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_a9-- _a9_1"]'))).click()
    print('---Unsubscribe Process Complete---', repeats,'/', count)
    print(f"Finished at {time.strftime('%X')}")


def login_process():
    global login, password

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')))

    browser.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input').clear()
    login_input = browser.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')
    login_input.send_keys(login)

    browser.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(2) > div > label > input').clear()
    password_input = browser.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(2) > div > label > input')
    password_input.send_keys(password)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3) > button'))).click()


options = Options()
options.binary_location = "chrome.exe"  # write the path to the file
browser = Chrome("chromedriver.exe", chrome_options=options)  # write the path to the file
browser.maximize_window()
browser.get("https://www.instagram.com/")
wait = WebDriverWait(browser, 20)

login = 'your login'
password = 'your password'

# for unsub
account_name = 'your account name'

# for sub (need to be subscribed on it)
donor_sub = 'donor account name'

# Number of subscriptions or unsubscribes.
# a max of 200 in total per day, this is the Instagram limit.
count = 190

login_process()
## Choose one of the functions below. The unselected function must be commented out (#).
# unsub_process()
sub_process()