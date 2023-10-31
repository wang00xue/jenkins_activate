


# 信审

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
class xinshen(Base):
    def __init__(self,tiaoma,driver=webdriver.Chrome) -> None:
        super(xinshen,self).__init__(driver)
        self.logger = get_logger()
        self.logger.info('信审')
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
        self.queding_h=(By.CLASS_NAME,"btn-danger")
        
        self.queding=(By.XPATH,'//*[contains(text(),"确定")]')
        # 取消按钮
        self.quxiao=(By.XPATH,'//*[contains(text(),"取消")]')
        # 申请查询列表
        self.wenzi=(By.XPATH,'//*[contains(text(),"%s")]'% tiaoma)
        # 列表申请记录数量
        self.liebiaoshu=self.quxiao=self.driver.find_element(By.CLASS_NAME,'mat-paginator-range-label')
        # 信审
        # self.xinshen=self.driver.find_element(By.XPATH,'//*[contains(text(),"信审")]')
        self.xinshen=(By.XPATH,'/html/body/app-root/div/div[2]/app-queue-page/div[2]/div[1]/button[5]')
                          
        # 工作所在地
        self.gongzuosuozaidi=(By.CLASS_NAME,'mat-select-arrow')
        # 工作所在地选择哈尔滨
        # self.gongzuosuozaidi_heb=self.driver.find_element(By.XPATH,'//*[contains(text(),"01-哈尔滨")]')
        self.gongzuosuozaidi_heb=(By.XPATH,'//*[contains(text(),"01-哈尔滨")]')
        #日志
        self.rizhi=(By.XPATH,'//*[contains(text(),"日志")]')
        #客户特征
        self.kehutezheng=(By.XPATH,'//*[contains(text(),"客户特征")]')
        # 行业
        self.hangye=(By.XPATH,'/html/body/app-root/div/div[2]/app-application-page/app-application-info/div[2]/app-customer-characteristic/form/div[4]/div[1]/div/table/tbody/tr[1]/td[2]/app-combo-box/div/div[1]/i')
        # 行业选择
        self.hangye_A01=(By.XPATH,'//*[contains(text(),"A01 - 国家党政机关及非营利性事业单位")]')
        # 职位
        self.zhiwei=(By.XPATH,'/html/body/app-root/div/div[2]/app-application-page/app-application-info/div[2]/app-customer-characteristic/form/div[4]/div[2]/div/table/tbody/tr[1]/td[2]/app-combo-box/div/div/i')
        # 职位选择
        self.zhiwei_A01=(By.XPATH,'//*[contains(text(),"A01-省部级、厅局级(或以上)")]')
        # 提交
        self.tijiao=(By.XPATH,'//*[contains(text(),"提交")]')
        # 详细信息
        self.xiangxixinxi=(By.CLASS_NAME,'btn-info')
        # 关闭
        self.guanbi=(By.XPATH,'/html/body/modal-container/div/div/app-diary-notes/div[3]/button')








