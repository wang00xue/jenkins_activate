
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from time import sleep
import logging
import logging.handlers
import datetime
import os
# from util.fangfa import get_logger
def get_logger():

    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)
    path=os.getcwd()
    rf_handler = logging.handlers.TimedRotatingFileHandler(path+'\\logs\\all.log', when='midnight', interval=1, backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0),encoding='utf-8')
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    f_handler = logging.FileHandler(path+'\\logs\\error.log',encoding='utf-8')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger

class Base :
    def __init__(self) -> None:
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        self.logger = get_logger()


    def case(self):
        asss=self.driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys('123')
        ass=self.driver.find_element(By.CSS_SELECTOR,'input[value="百度一下"]').click()
        # js="var q=document.documentElement.scrollTop=10000"
        # self.driver.execute_script(js)
        sleep(2)
        element=self.driver.find_element(By.XPATH,'//*[contains(text(),"相关搜索")]')
        ss=self.driver.execute_script("arguments[0].scrollIntoView();",element)
        a=self.driver.find_element(By.XPATH,'//a[text()="更多"]').click()
        num=self.driver.window_handles 
        #获取当前页的所有句柄
        self.driver.switch_to.window(num[1]) 
        # #跳到新的标签页;因为当页，num[o]表示主页面driver.switch_to_window(num[o])#回到主页面的句树
        b=self.driver.find_element(By.XPATH,'//*[contains(text(),"驾")]').click()

    def case1(self):
        asss=self.driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys('123')
        self.logger.debug('输入')
        asa=self.driver.find_element(By.XPATH,'//input[@id="kw"]')
        aas=asa.get_property("outerHTML")
        print(aas)
        ass=self.driver.find_element(By.CSS_SELECTOR,'input[value="百度一下"]').click()
        sleep(2)
        element=self.driver.find_element(By.XPATH,'//*[contains(text(),"大家还在搜")]')
        ss=self.driver.execute_script("arguments[0].scrollIntoView();",element)    
        xiangxixinxi=self.driver.find_elements(By.XPATH,'//*[contains(text(),"123")]')
        xiangxixinxi[1].click()
        
        
aa=Base()
aa.case1()


# class BasePage():
#     """selenium基类"""
  
#     def __init__(self, driver=None):
#         self.log = Log().logger
#         self.report = cm.allure_json
#         self.broswer = CONF.web_broswer or 'firefox'
#         self.base_url = CONF.web_url
#         self.timeout = 6
#         if driver is None:
#             self.set_driver(driver)
#         else:
#             self.driver = driver
#             self.wait = WebDriverWait(self.driver, self.timeout)
#             self.action_chain = ActionChains(self.driver)
 
#     def set_driver(self, driver):
#         if 'chrome' == driver.lower().strip():
#             options = chrome_op()
#             options.add_argument("--ignore-certificate-errors")
#             self.driver = webdriver.Chrome(os.path.join(cm.DRIVER_PATH, 'chromedriver'),
#                                             chrome_options=options)
#         elif 'firefox' == driver.lower().strip():
#             binary_file = CONF.firefox_binary or '/usr/bin/firefox-esr'
#             executable_path = os.path.join(cm.DRIVER_PATH, 'geckodriver')
#             options = firefox_op()
#             options.binary = FirefoxBinary(binary_file)
#             service = Service(executable_path=executable_path)
#             my_profile = webdriver.FirefoxProfile()
#             my_profile.accept_untrusted_certs = True
#             self.driver = webdriver.Firefox(firefox_profile=my_profile, options=options,
#                                              service=service)
#         else:
#             raise Exception('暂不支持%s浏览器驱动' % driver)
#         self.wait = WebDriverWait(self.driver, self.timeout)
#         self.action_chain = ActionChains(self.driver)








class Test260161_ECS():
    def setup(self) -> None:
        self.ecs_manager_page = ecs_manager_page

    def teardown(self) -> None:
        if getattr(self, 'ecs_name', False):
            self.ecs_manager_page.search_ecs('名称', self.ecs_name)
            result = self.ecs_manager_page.check_ecs_table_iszero()
            if result == False:
                self.ecs_manager_page.clear_ecs('名称', self.ecs_name)
            bin_manager_page = BINManagerPage(driver=self.ecs_manager_page.driver)
            bin_manager_page.clear_bin(self.ecs_name)






















