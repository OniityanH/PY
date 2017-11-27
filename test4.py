from selenium import webdriver
import time

def log_fb():
    chrome_path= r"C:\Users\Allen Zhu\Desktop\chromedriver_win32\chromedriver.exe"
    br = webdriver.Chrome(chrome_path)
    br.get('https://www.facebook.com/')
    time.sleep(3)
    user = br.find_element_by_css_selector('#email')
    user.send_keys('-')
    password=br.find_element_by_css_selector('#pass')
    password.send_keys('-')
    log=br.find_element_by_css_selector('#loginbutton')
    log.click()

log_fb()