from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://facebook.com/')

print(f"Page title: {browser.title}")


browser.quit()