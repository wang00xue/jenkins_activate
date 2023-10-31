

# 信审IN

from pages.base_selenium import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from business.file_processing import login
# import util.fangfa
from util.fangfa import *
from time import sleep
from selenium import webdriver

class xinshen_in(Base):
    def __init__(self,tiaoma,driver=webdriver.Chrome) -> None:
        super(xinshen_in,self).__init__(driver)
        self.logger = get_logger()
        self.logger.info('信审ins')
        self.tiaoma=tiaoma
        # 首页一级菜单
        self.driver=driver
        # 申请条码
        self.loc_one=(By.CSS_SELECTOR,"input[formcontrolname='applicationNumber']")
        # WebDriverWait(self.driver,60,2).until(EC.presence_of_element_located(self.loc_one))
        # sleep(2)
        self.shenqingtiaoma=self.driver.find_element(*self.loc_one)
        # 搜索自身申请
        self.sousuozishen=self.driver.find_element(By.XPATH,'//*[contains(text(),"搜索自身申请")]')
        #  搜索他人申请
        self.sousuotashen=self.driver.find_element(By.XPATH,'//*[contains(text(),"搜索他人申请")]')
        # 确定按钮
        self.queding=(By.XPATH,'//*[contains(text(),"确定")]')
        # 取消按钮
        self.quxiao=(By.XPATH,'//*[contains(text(),"取消")]')
        # 申请查询列表
        self.wenzi=(By.XPATH,'//*[contains(text(),"%s")]'% tiaoma)
        # 列表申请记录数量
        self.liebiaoshu=self.quxiao=self.driver.find_element(By.CLASS_NAME,'mat-paginator-range-label')
        # 信用决策 
        self.xinyongjuece=self.driver.find_element(By.XPATH,'/html/body/app-root/div/div[2]/app-queue-page/div[2]/div[1]/button[7]')


