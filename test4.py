from selenium import webdriver
import time

def log_fb():
    chrome_path= r"C:\Users\Allen Zhu\Desktop\chromedriver_win32\chromedriver.exe"
    br = webdriver.Chrome(chrome_path)
    br.get('https://www.facebook.com/')
    time.sleep(3)
    user = br.find_element_by_css_selector('#email')
    user.send_keys('woaibeiqi@outlook.com')
    password=br.find_element_by_css_selector('#pass')
    password.send_keys('Zhuyifei19930417')
    log=br.find_element_by_css_selector('#u_0_5')
    log.click()

log_fb()