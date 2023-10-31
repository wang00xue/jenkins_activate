



# 实时制卡

from pages.base_selenium import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from business.file_processing import login
# import util.fangfa
from util.fangfa import *
from time import sleep
from selenium import webdriver
# 需要调用util方法直接定位到指定元素,传TXET
class shishizhika(Base):
    def __init__(self,tiaoma,driver=webdriver.Chrome) -> None:
        super(shishizhika,self).__init__(driver)
        self.logger = get_logger()
        self.logger.info('实时制卡')
        self.tiaoma=tiaoma
        # 首页一级菜单
        self.driver=driver
        # 申请条码
        self.loc_one=(By.CSS_SELECTOR,"input[formcontrolname='applicationNumber']")
        # WebDriverWait(self.driver,60,2).until(EC.presence_of_element_located(self.loc_one))
        sleep(2)
        self.shenqingtiaoma=self.driver.find_element(*self.loc_one)
        #  查询实时制卡信息 
        self.chaxunshishizhika=(By.XPATH,'//*[contains(text(),"查询实时制卡信息")]')
        # 确定按钮
        self.queding=(By.XPATH,'//*[contains(text(),"确定")]')
        # 取消按钮
        self.quxiao=(By.XPATH,'//*[contains(text(),"取消")]')
        # 申请查询列表
        self.wenzi=(By.XPATH,'//*[contains(text(),"%s")]'% tiaoma)
        #  重调 
        self.chongdiao=(By.XPATH,'//*[contains(text(),"重调")]')

        # 交易结果
        self.chulijieguo=(By.CLASS_NAME,'mat-column-runFlagDescription')
                                                

 

