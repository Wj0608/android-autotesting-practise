__author__ = 'DELL'

#coding=utf-8
from appium import webdriver
import time



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'genymotion_vbox86tp_5.1_141215_182600'
desired_caps['appPackage'] = 'org.dae.exchange'
desired_caps['appActivity'] = 'org.dae.exchange.main.ui.activity.LoadingActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)  # TODO: check the app is open
# while driver.find_element_by_android_uiautomator("text(\"Not now\")") == None:
#     print("123")
#     time.sleep(1)
driver.find_element_by_android_uiautomator("text(\"Not now\")").click()
driver.find_element_by_android_uiautomator("text(\"My\")").click()
driver.find_element_by_android_uiautomator("text(\"Free registration\")").click()
driver.find_element_by_android_uiautomator("text(\"User nickname\")").send_keys("test1")
driver.find_element_by_android_uiautomator("text(\"Email\")").send_keys("test1@example.com")
driver.find_element_by_android_uiautomator("text(\"Send\")").click()
driver.find_element_by_android_uiautomator("text(\"Verification code\")").send_keys("123456")
driver.find_element_by_android_uiautomator("text(\"Next\")").click()
driver.find_element_by_xpath("//android.widget.EditText[contains(@index,'0')]").send_keys("123456")
driver.find_element_by_xpath("//android.widget.EditText[contains(@index,'2')]").send_keys("123456")
driver.find_element_by_android_uiautomator("text(\"Signup and login\")").click()
driver.find_element_by_android_uiautomator("text(\"Set up immediately\")").click()
driver.find_element_by_class_name("android.widget.EditText").send_keys("123456")
#  time.sleep(1)
driver.find_element_by_class_name("android.widget.EditText").send_keys("123456")
driver.find_element_by_android_uiautomator("text(\"Completed\")").click()
time.sleep(3)
driver.quit()