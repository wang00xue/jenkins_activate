
# 首页标签
from pages.base_selenium import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from business.file_processing import login
import util.fangfa
from time import sleep
from selenium import webdriver
# 需要调用util方法直接定位到指定元素,传TXET
class home_bnt(Base):
    def __init__(self,driver=webdriver.Chrome) -> None:
        super(home_bnt,self).__init__(driver)
        # 首页一级菜单
        self.driver=driver
        # self.loc_one=(By.XPATH, "//*[contains(text(),'主页')]")
        self.loc_one=(By.XPATH,"/html/body/app-root/div/app-side-nav/div/ul/div[1]/li[1]/a")
        WebDriverWait(self.driver,60,2).until(EC.presence_of_element_located(self.loc_one))
        # sleep(3)#需要改成等待元素
        self.zhuye=self.driver.find_element(*self.loc_one)
        self.gongzuoliu=self.driver.find_element(By.XPATH, "//*[contains(text(),'工作流队列')]")
        self.shenqing_zhanghuguanli=self.driver.find_element(By.XPATH, "//*[contains(text(),'申请/账户管理')]")


        
        # 首页二级菜单--工作流
        self.cuowuduilie=self.driver.find_element(By.XPATH, "//*[contains(text(),'校验失败队列')]")
        self.yushenduilie=self.driver.find_element(By.XPATH, "//*[contains(text(),'预审队列')]")
        self.waibujiekou=self.driver.find_element(By.XPATH, "//*[contains(text(),'外部接口队列')]")
        self.waibujiekou_in=self.driver.find_element(By.XPATH, "//*[contains(text(),'外部接口后Instinct队列')]")
        self.xinshen=self.driver.find_element(By.XPATH, "//*[contains(text(),'信审')]")
        self.xinshen_in=self.driver.find_element(By.XPATH, "//*[contains(text(),'信审Instinct队列')]")
        self.bujianduilie=self.driver.find_element(By.XPATH, "//*[contains(text(),'补件队列')]")
        self.xinyongjueceduilie=self.driver.find_element(By.XPATH, "//*[contains(text(),'信用决策队列')]")
        self.xitongsuojianduilie=self.driver.find_element(By.XPATH, "//*[contains(text(),'系统锁定队列')]")
        self.fenzhongxinyushen=self.driver.find_element(By.XPATH, "//*[contains(text(),'分中心预审')]")
        self.yizhijianchaxun=self.driver.find_element(By.XPATH, "//*[contains(text(),'已质检查询')]")


        # 首页二级菜单--申请查询
        self.shenqingchaxun_yuanshu=(By.XPATH,"//*[contains(text(),'申请查询')]")
        self.shenqingchaxun=self.driver.find_element(By.XPATH,"//*[contains(text(),'申请查询')]")
        self.shenqinggengxin=self.driver.find_element(By.XPATH,"//*[contains(text(),'申请更新')]")
        self.yichikazhanghuchaxun=self.driver.find_element(By.XPATH,"//*[contains(text(),'已持卡账户查询')]")
        self.shishizhika=self.driver.find_element(By.XPATH,"//*[contains(text(),'实时制卡账户')]")
        self.queding=(By.XPATH,"//*[contains(text(),'确定')]")


        # 备用数据
        # 申请查询中核准
        self.hezhun=(By.XPATH, "/html/body/app-root/div/div[2]/app-list-page/div[2]/app-list-page-grid/div/div[2]/table/tbody/tr[1]/td[17]")

        



# 完全匹配
# driver.find_element(By.XPATH, "//a[text()='新闻']")
# 模糊匹配
# driver.find_element(By.XPATH, "//*[contains(text(),'新闻')]")

        # 首页一级菜单
        # loc_one=(By.CLASS_NAME,'nav-header')
        # WebDriverWait(driver,60,2).until(EC.presence_of_element_located(loc_one))
        # self.name_one=driver.find_elements(*loc_one)
        # 首页二级菜单
        # loc_two=(By.CLASS_NAME,'fa-caret-right')
        # WebDriverWait(driver,60,2).until(EC.presence_of_element_located(loc_two))
        # self.name_two=driver.find_elements(*loc_two)
        # self.xinshen=driver.find_element(By.XPATH,'/html/body/app-root/div/app-side-nav/div/ul/div[2]/li[2]/ul/li[5]/a')
        # self.two=driver.find_elements(By.CLASS_NAME,'collapse')

        
    # def ceshi(self):
    #     util.fangfa.positioning('工作流队列',self.name_one).click()
        # util.fangfa.positioning('信审队列',self.name_two).click()
        # self.xinshen.click()
        # self.erji('信审').click()


# body > app-root > div > app-side-nav > div > ul > div:nth-child(2) > li.collapse.in.show > ul > li:nth-child(1) > a
    # def erji(self,text):
    #     for i in range(len(self.two)-1):
    #         erji=self.two[i].find_elements(By.CSS_SELECTOR,'a[]')
    #         for ii in range(len(erji)-1):
    #             if erji[ii].text==text:
    #                 return self.two[i][ii]



