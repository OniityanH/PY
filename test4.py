from selenium import webdriver
import time

def log_fb():
    br = webdriver.Firefox()
    br.get('https://www.facebook.com/')
    time.sleep(40)
    user = br.find_element_by_css_selector('#email')
    user.send_keys('woaibeiqi@outlook.com')
    password=br.find_element_by_css_selector('#pass')
    password.send_keys('-')
    log=br.find_element_by_css_selector('#u_0_5')
    log.click()
    print("over")

log_fb()