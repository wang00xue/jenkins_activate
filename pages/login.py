
# 登录页元素
from pages.base_selenium import Base
from selenium.webdriver.common.by import By
from util.fangfa import *
class Login(Base):
    def __init__(self) -> None:
        super().__init__()
        self.user=self.driver.find_element(By.CSS_SELECTOR,'input[formcontrolname="username"]')
        self.pwd=self.driver.find_element(By.CSS_SELECTOR,'input[formcontrolname="password"]')
        self.log_on=self.driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
        # 用户名密码为空及用户名为空
        # self.jiaoyan_yonghu=(By.XPATH,'//*[contains(text(),"请输入用户名")]')
        # 用户名存在密码为空
        # self.jiaoyan_mimakong=(By.XPATH,'//*[contains(text(),"请输入密码")]')
        # 用户名密码都错误
        # self.jiaoyan_cuowu=(By.XPATH,'//*[contains(text(),"用户不存在！")]')
        # 用户名正确密码错误
        # self.jiaoyan_mima=(By.XPATH,'//*[contains(text(),"用户验证不通过！")]')
        # 用户名和密码都正确，登录成功
        self.jiaoyan_sc='http://170.254.228.174/#/home'
        # 获取错误提示
        self.jiaoyan_cw=(By.XPATH,'/html/body/app-root/div/div[2]/app-login-page/app-login-form/div/div/div/div/div[2]/div[2]/div[2]/div/form/div[4]')

        
         

        
        # self.title=self.driver.title


    # def login(self,user='Administrator',pwd='111111'):
    #     self.logger = get_logger()
    #     self.logger.info('申请查询页')
    #     self.user.send_keys(user)
    #     self.pwd.send_keys(pwd)
    #     jietu('登录页截图',self.driver)
    #     self.log_on.click()
    #     return self.driver












