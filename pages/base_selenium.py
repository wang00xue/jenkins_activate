# 基类
from selenium import webdriver
from util.fangfa import makedirs
from selenium.webdriver.common.by import By
class Base :
    def __init__(self,driver=None) :
        if driver == None :
            self.makedir=makedirs()
            self.driver=webdriver.Chrome()
            self.driver.get('http://170.254.228.174/#/login')
            self.driver.maximize_window()







