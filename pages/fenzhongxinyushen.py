
# 分中心预审
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
class fenzhongxinyushen(Base):
    def __init__(self,tiaoma,driver=webdriver.Chrome) -> None:
        super(fenzhongxinyushen,self).__init__(driver)
        self.logger = get_logger()
        self.logger.info('分中心预审')
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
        self.liebiaoshu=self.driver.find_element(By.CLASS_NAME,'mat-paginator-range-label')
        # 预审
        self.yushen=(By.CLASS_NAME,'btn-primary')
        # 附加信息1
        self.fujia1=(By.XPATH,'//*[contains(text(),"附加信息1")]')
        # 提交
        self.tijiao=(By.XPATH,'//*[contains(text(),"提交")]')
        #重新分配队列
        self.chongxinfenpei=(By.XPATH,'//*[contains(text(),"重新分配队列")]')
        # 定位admin用户
        self.admin=(By.XPATH,'/html/body/modal-container/div/div/app-reassign/div[2]/div/div[1]/div[2]/table/tbody/tr[24]/td/i[2]')
                             