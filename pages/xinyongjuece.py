



# 信用决策

from pages.base_selenium import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from business.file_processing import login
# import util.fangfa
from util.fangfa import *
from time import sleep
from selenium import webdriver

class xinyongjuece(Base):
    def __init__(self,tiaoma,driver=webdriver.Chrome) -> None:
        super(xinyongjuece,self).__init__(driver)
        self.logger = get_logger()
        self.logger.info('信用决策')
        self.tiaoma=tiaoma
        # 首页一级菜单
        self.driver=driver
        # 申请条码
        self.loc_one=(By.CSS_SELECTOR,"input[formcontrolname='applicationNumber']")
        # WebDriverWait(self.driver,60,2).until(EC.presence_of_element_located(self.loc_one))
        sleep(2)
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
        self.xinyongjuece=self.driver.find_element(By.XPATH,'/html/body/app-root/div/div[2]/app-queue-page/div[2]/div/button[5]')
        self.kachanpin=self.driver.find_element(By.XPATH,'/html/body/app-root/div/div[2]/app-queue-page/div[2]/app-queue-page-grid/div/div[2]/table/tbody/tr[1]/td[25]')


        # 信用决策，决策结果下拉框
        self.juecejieguo=(By.XPATH,'/html/body/app-root/div/div[2]/app-decision-page/app-credit-decision-info/div/div/app-form-decision/form/div/div[1]/table/tbody/tr[1]/td[2]/app-combo-box/div/div/i')
        # 核准
        self.hezhun=(By.XPATH,'//*[contains(text(),"A-核准")]')
        #限额原因
        self.xianeyuanyin=(By.XPATH,'/html/body/app-root/div/div[2]/app-decision-page/app-credit-decision-info/div/div/app-form-decision/form/div/div[2]/table/tbody/tr[2]/td[2]/app-combo-box/div/div/i')
        # 选择限额原因
        self.xianeyuanyin_801=(By.XPATH,'//*[contains(text(),"801 - 信用违例")]')
        # 额度
        self.ed=(By.CSS_SELECTOR,'input[formcontrolname="finalLimit"]')
        # 结果
        self.jieguo=(By.XPATH,'/html/body/app-root/div/div[2]/app-decision-page/app-credit-decision-info/div/div/div/button[6]')
        

        







