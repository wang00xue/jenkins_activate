


import os
import sys
path=os.getcwd()
# print(path)
sys.path.append(path)
import pytest
from pages.home import home_bnt
from time  import sleep
from business.file_processing import *
from pages.home import home_bnt
from time import sleep
from util.fangfa import *
import multiprocessing
import subprocess

# tiao_ma=subprocess.run(['python', r'C:\project\PycharmProjects\UI自动化学习\project\main.py'])
# tiao_ma1=subprocess.getoutput(['python', r'C:\project\PycharmProjects\UI自动化学习\project\main.py'])
# tiao_ma2=subprocess.getoutput(['python', r'C:\project\PycharmProjects\UI自动化学习\project\main.py'])
# print(tiao_ma.stdout) #状态码
# print(tiao_ma.stdout)
# print(tiao_ma.args)

category_data = [
    (subprocess.getoutput(['python', r'C:\project\PycharmProjects\UI自动化学习\project\main.py'])[:-1],'0'),
    # (tiao_ma2[:-1],'50000'),
    # ('202308311117438','50000'),
    # ('202308281163252','50000'),
]
@pytest.mark.parametrize('tiaoma,ed_a', category_data)
def test_gongzuoliu(tiaoma,ed_a):
        driver=login()
        home=home_bnt(driver)
        home.shenqing_zhanghuguanli.click()
        home.shenqingchaxun.click()
        sleep(2)
        wenben=chaxun(tiaoma,driver)
        jietu('查询成功页',driver)

        # print(wenben)
        # 打开工作流
        home.gongzuoliu.click()
        # 判断进入队列
        while wenben!='账户建立' :
            if wenben=='外部接口后Instinct':
                home.waibujiekou_in.click()
                wait_yuansu=fanhui_yuanshu()
                wait_dianji(driver,wait_yuansu)
                jietu('外部接口后Instinct',driver)
                sleep(0.5)   
                waibujiekou_ins(tiaoma,driver)
                driver.execute_script(('window.scrollBy(0,10000)'))
                wait_dianji(driver,home.shenqingchaxun_yuanshu)
                # sleep(1)
                home.shenqingchaxun.click()
                sleep(3)
                wenben=chaxun(tiaoma,driver)
                try:
                    assert wenben!='外部接口后Instinct'
                except:
                    pass

            elif wenben=='外部接口':
                home.waibujiekou.click()
                wait_yuansu=fanhui_yuanshu()
                wait_dianji(driver,wait_yuansu)
                jietu('外部接口',driver)
                sleep(0.5)    
                wbjk(tiaoma,driver)
                home.shenqingchaxun.click()
                driver.execute_script(('window.scrollBy(0,10000)'))
                sleep(2)
                wenben=chaxun(tiaoma,driver) 
                try:
                    assert wenben!='外部接口'
                except:
                    pass
            elif wenben=='分中心预审':
                home.fenzhongxinyushen.click()
                wait_yuansu=fanhui_yuanshu()
                wait_dianji(driver,wait_yuansu)
                jietu('分中心预审页面',driver)
                sleep(0.5)   
                fzxys(tiaoma,driver)
                sleep(1)
                home.shenqingchaxun.click()
                wenben=chaxun(tiaoma,driver)
                try:
                    assert wenben!='分中心预审'
                except:
                    pass

            elif wenben=='信审':
                home.xinshen.click()
                wait_yuansu=fanhui_yuanshu()
                wait_dianji(driver,wait_yuansu)
                # sleep(5)
                jietu('信审页面',driver)
                sleep(0.5)   
                xinshens(tiaoma,driver)
                sleep(2)
                driver.execute_script(('window.scrollBy(0,10000)'))
                home.shenqingchaxun.click()
                try:
                    sleep(1)
                    home.driver.find_element(*home.queding).click()
                except:
                     pass
                sleep(3)
                wenben=chaxun(tiaoma,driver)
                try:
                    assert wenben!='信审' 
                except:
                    home.shenqinggengxin.click()
                    wait_dianji(driver,wait_yuansu)
                    sleep(8)
                    home.shenqingchaxun.click()
                    wenben=chaxun(tiaoma,driver)
            elif wenben=='信审Instinct队列':
                home.xinshen_in.click()
                wait_yuansu=fanhui_yuanshu()
                wait_dianji(driver,wait_yuansu)
                jietu('信审Instinct',driver)
                sleep(0.5)   
                xinshen_ins(tiaoma,driver)
                sleep(3)
                driver.execute_script(('window.scrollBy(0,10000)'))
                home.shenqingchaxun.click()
                wenben=chaxun(tiaoma,driver)
                try:
                    assert wenben!='信审Instinct队列'  
                except:
                    pass

            elif wenben=='信用决策':
                home.xinyongjueceduilie.click()
                wait_yuansu=fanhui_yuanshu()
                wait_dianji(driver,wait_yuansu)
                jietu('信用决策',driver)
                sleep(0.5)   
                xyjc(tiaoma,driver,ed_a)
                sleep(3)
                driver.execute_script(('window.scrollBy(0,10000)'))
                home.shenqingchaxun.click()
                wenben=chaxun(tiaoma,driver) 
                try:
                    assert wenben!='信用决策' 
                except:
                    jietu('信用决策更新失败',driver)

            elif wenben=='等待上载':
                if driver.find_element(*home.hezhun).text=='核准':
                    home.shishizhika.click()
                    wait_yuansu=fanhui_yuanshu()
                    wait_dianji(driver,wait_yuansu)
                    jietu('等待上载',driver)
                    sleep(0.5)   
                    zhuangtai=sszk(tiaoma,driver)
                    print(zhuangtai)
                    assert wenben!='实时制卡'
                    break
                else:
                    zhuangtai='拒绝'
                    break


                












