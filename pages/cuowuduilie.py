

# 错误队列
from pages.base_selenium import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from business.file_processing import login
from business.file_processing import *
import util.fangfa
from util.fangfa import *
from time import sleep
from selenium import webdriver
# 需要调用util方法直接定位到指定元素,传TXET
class cuowu(Base):
    def __init__(self,tiaoma,driver=webdriver.Chrome) -> None:
        super(cuowu,self).__init__(driver)
        self.logger = get_logger()
        self.logger.info('错误队列')
        # 首页一级菜单
        self.driver=driver
        # 申请条码
        self.loc_one=(By.CSS_SELECTOR, "input[formcontrolname='applicationNumber']")
        # WebDriverWait(self.driver,60,2).until(EC.presence_of_element_located(self.loc_one))
        # wait_dianji(driver,self.loc_one)
        sleep(2)
        self.shenqingtiaoma=self.driver.find_element(*self.loc_one)
        # 搜索校验失败队列按钮
        self.shousuojianyan=self.driver.find_element(By.XPATH, "//*[contains(text(),'搜索校验失败队列')]")
        


        # 列表框
        self.loc_two=(By.CLASS_NAME,'mat-checkbox-inner-container')
        liebiao=self.driver.find_elements(*self.loc_two)
        # 列表第一个
        self.liebiao1=liebiao[0]



        # 重新校验
        self.chongxinjiaoyan=self.driver.find_element(By.XPATH, "//*[contains(text(),'重新校验')]")

        self.tiaoma=tiaoma

    # 输入条码,点击查询,点击第一个元素,点击重新校验
    # def chongxinchaxun(self):
    #     WebDriverWait(self.driver,60,2).until(EC.presence_of_element_located(self.loc_one))
    #     self.shenqingtiaoma.send_keys(self.tiaoma)
    #     self.shousuojianyan.click()
    #     sleep(3)
    #     self.liebiao1.click()
    #     sleep(2)
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", self.chongxinjiaoyan)
    #     self.chongxinjiaoyan.click()
    #     jietu('点击重新查询',self.driver)
        











