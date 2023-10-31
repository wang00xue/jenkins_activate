

from pages.base_selenium import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.fangfa import *
from time import sleep
from selenium import webdriver

class waibujiekou(Base):
    def __init__(self,tiaoma,driver=webdriver.Chrome) -> None:
        super(waibujiekou,self).__init__(driver)
        self.logger = get_logger()
        self.logger.info('外部接口后IN')
        self.tiaoma=tiaoma
        # 首页一级菜单
        self.driver=driver
        # 申请条码
        self.loc_one=(By.CSS_SELECTOR,"input[formcontrolname='applicationNumber']")
        # WebDriverWait(self.driver,60,2).until(EC.presence_of_element_located(self.loc_one))
        sleep(2)
        self.shenqingtiaoma=self.driver.find_element(*self.loc_one)
        #  搜索外部接口队列
        self.sousuozishen=self.driver.find_element(By.XPATH,'//*[contains(text()," 搜索外部接口队列")]')
        # 确定按钮
        self.queding=(By.XPATH,'//*[contains(text(),"确定")]')
        # 取消按钮
        self.quxiao=(By.XPATH,'//*[contains(text(),"取消")]')
        # 申请查询列表
        # self.wenzi=(By.XPATH,'//*[contains(text(),"%s")]'% tiaoma)
        self.tiaoguowaibujiekou=self.driver.find_element(By.XPATH,'//*[contains(text()," 跳过外部接口队列")]')
        # 申请查询列表
        self.wenzi=(By.XPATH,'//*[contains(text(),"%s")]'% tiaoma)

          









