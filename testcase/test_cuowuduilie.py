
import os
import sys
path=os.getcwd()
print(path)
sys.path.append(path)
from business.file_processing import login
from business.file_processing import *
# from pages.login import Login
from pages.home import home_bnt
# from pages.shenqingchaxun import shenqingchaxun
# from pages.waibujieku_in import waibujiekou_in
from time  import sleep
from pages.home import home_bnt
# from business.file_processing import cxjy
from time import sleep
import pytest
from util.fangfa import *



category_data = [
    
    ('202304181104446'),
    # ('202304181104468'),
    # ('202304261104800'),
]
@pytest.mark.parametrize('tiaoma', category_data)
def test_chongxinjiaoyan(tiaoma):
    # aa=cxjy('202303271104021')
    # aa.cwcxjy()
    # if __name__=='__main__':
    #     pytest.main(['test_cuowuduilie.py'])  

    # def setup_class(self) -> None:
    #     self.login = login()
    #     self.categoryPage = CategoryPage(self.login)
    driver=login()
    home=home_bnt(driver)
    driver.implicitly_wait(60)
    wait_dianji(home.driver,home.loc_one)
    # WebDriverWait(home.driver,60,2).until(EC.presence_of_element_located(home.loc_one))
    assert home.zhuye.text=='主页'
    home.gongzuoliu.click()
    home.cuowuduilie.click()
    chongxinchaxun(tiaoma,driver)










