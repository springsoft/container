#coding=utf-8
from selenium import webdriver
from time import sleep

driver = webdriver.Remote(
command_executor='http://132.232.147.75:5555/wd/hub',
desired_capabilities={'browserName': 'chrome'}
)

driver.get('http://www.baidu.com')
print("get baidu")
sleep(1)
driver.find_element_by_id("kw").send_keys("hello world")
print("click baidu")
sleep(2)
driver.find_element_by_id("su").click()
sleep(2)
print("picture baidu")
driver.get_screenshot_as_file("./baidu_img.png")

driver.quit()
print("end...")
