from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def get_login_info():

    info = []
    f = open('login.txt')

    for line in f.readlines():
        info.append(line.strip('\n'))

    f.close()

    return info


url = 'https://music.youtube.com/'
options = uc.ChromeOptions()
driver = uc.Chrome(options=options, use_subprocess=True)
driver.get(url)


def log_in():
    USERNAME = get_login_info()[2]
    PASSWORD = get_login_info()[3]

    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sign-in-link.ytmusic-nav-bar')))
    driver.find_element(by=By.CSS_SELECTOR, value='.sign-in-link.ytmusic-nav-bar').click()

    username_field = '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, username_field)))
    driver.find_element(by=By.XPATH, value=username_field).send_keys(USERNAME)
    driver.find_element(by=By.CSS_SELECTOR, value='.VfPpkd-LgbsSe-OWXEXe-k8QpJ:not(:disabled)').click()

    password_field = '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, password_field)))
    driver.find_element(by=By.XPATH, value=password_field).send_keys(PASSWORD)
    time.sleep(1)
    driver.find_element(by=By.CSS_SELECTOR, value='.VfPpkd-LgbsSe-OWXEXe-k8QpJ:not(:disabled)').click()


def play_song(song: str):
    search_button = 'tp-yt-paper-icon-button.ytmusic-search-box, input.ytmusic-search-box, input.ytmusic-search-box::placeholder'
    WebDriverWait(driver, timeout=7).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_button)))
    driver.find_element(by=By.CSS_SELECTOR, value=search_button).click()
    driver.find_element(by=By.CSS_SELECTOR, value='input.ytmusic-search-box').send_keys(song)
    driver.find_element(by=By.CSS_SELECTOR, value='input.ytmusic-search-box').send_keys(Keys.ENTER)
    time.sleep(3)

    option_lst = '//*[@id="contents"]/ytmusic-responsive-list-item-renderer[1]/div[2]/div[1]/yt-formatted-string/a'
    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.XPATH, option_lst)))
    driver.find_element(by=By.XPATH, value=option_lst).click()

    song_choice = '/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[1]/a'
    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.XPATH, song_choice)))
    driver.find_element(by=By.XPATH, value=song_choice).click()


def play():
    play_button = '/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[3]'
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, play_button)))
    driver.find_element(by=By.XPATH, value=play_button).click()


def pause():
    pause_button = '/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[3]'
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, pause_button)))
    driver.find_element(by=By.XPATH, value=pause_button).click()


def repeat(word):
    if word == 'song':
        repeat_on = '/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[3]/div/tp-yt-paper-icon-button[2]'
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, repeat_on)))
        driver.find_element(by=By.XPATH, value=repeat_on).click()
        time.sleep(0.5)
        driver.find_element(by=By.XPATH, value=repeat_on).click()
    if word == 'off':
        rep_off = '/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[3]/div/tp-yt-paper-icon-button[2]'
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, rep_off)))
        driver.find_element(by=By.XPATH, value=rep_off).click()
