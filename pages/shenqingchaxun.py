
# 申请查询页

from pages.base_selenium import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from business.file_processing import login
import util.fangfa
from util.fangfa import *
from time import sleep
from selenium import webdriver
# 需要调用util方法直接定位到指定元素,传TXET
class shenqingchaxun(Base):
    def __init__(self,tiaoma,driver=webdriver.Chrome) -> None:
        super(shenqingchaxun,self).__init__(driver)
        self.logger = get_logger()
        self.logger.info('申请查询页')

        # 首页一级菜单
        self.driver=driver
        # 申请条码
        self.shenqingtiaoma_yuanshu=(By.CSS_SELECTOR,'input[formcontrolname="applicationNumber"]')
        self.shenqingtiaoma=self.driver.find_element(By.CSS_SELECTOR,'input[formcontrolname="applicationNumber"]')
        # 申请查询
        self.chaxunshenqing=self.driver.find_element(By.XPATH,'//*[contains(text(),"查询申请")]')
        # 申请查询列表
        self.wenzi=(By.XPATH,'//*[contains(text(),"%s")]'% tiaoma)
        # self.liebiao_sqtm=self.driver.find_element(By.XPATH,wenzi)
        # 申请件状态
        self.liebiao_zhuangtai=(By.XPATH,'/html/body/app-root/div/div[2]/app-list-page/div[2]/app-list-page-grid/div/div[2]/table/tbody/tr[1]/td[16]')

        self.tiaoma=tiaoma
        

    # def chaxun(self):
    #     self.shenqingtiaoma.send_keys(self.tiaoma)
    #     self.chaxunshenqing.click()
    #     # # 申请查询列表
    #     # wenzi='//*[contains(text(),%s)]'% tiaoma
    #     WebDriverWait(self.driver,60,2).until(EC.presence_of_element_located(self.liebiao_zhuangtai))
    #     # self.liebiao_sqtm=self.driver.find_element(By.XPATH,self.wenzi)
    #     # self.liebiao_sqtm.click()
    #     wenben=self.driver.find_element(*self.liebiao_zhuangtai).text
    #     self.logger.debug('申请件状态')
    #     while wenben=='装载':
    #         self.chaxunshenqing.click()
    #         wenben=self.driver.find_element(*self.liebiao_zhuangtai).text
    #         return wenben
    #     return wenben









