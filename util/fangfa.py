


from selenium import webdriver
import os
import time
import logging
import logging.handlers
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 多元素定位到指定元素,适用于class和name
def positioning(text,element_list):
    for i in range(len(element_list)-1):
        print(element_list[i].text)
        if element_list[i].text==text:
            return element_list[i]






def makedirs():
    #生成年月日时分秒时间
    # picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    directory_time = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    # print(picture_time)
    # print(directory_time)
    # 打印文件目录
    # print(os.getcwd())
    #获取到当前文件的目录，并检查是否有 directory_time 文件夹，如果不存在则自动新建 directory_time 文件
    try:
        File_Path = os.getcwd() + '\\img\\' + directory_time +'\\'
        if not os.path.exists(File_Path):
            os.makedirs(File_Path)
            # print("目录新建成功: %s" % File_Path)
        else:
            pass
            # print("目录已存在!!!")
    except BaseException as msg:
        print("新建目录失败: %s"% msg)



def jietu(picture,driver=webdriver.Chrome):
    try:
        picture_time = time.strftime("%H_%M_%S", time.localtime(time.time()))
        directory_time = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        url=driver.save_screenshot(os.getcwd()+'\\img\\' + directory_time + '\\' + picture+picture_time + '.png')
        # print("%s : 截图成功!!!"% url)
    except BaseException as pic_msg:
        # print("截图失败:%s"% pic_msg)
        pass




def get_logger():

    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)
    path=os.getcwd()
    rf_handler = logging.handlers.TimedRotatingFileHandler(path+'\\logs\\all.log', when='midnight', interval=1, backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0),encoding='utf-8')
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    f_handler = logging.FileHandler(path+'\\logs\\error.log',encoding='utf-8')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger


def wait_chunzai(driver,yuansu,cs=60,jg=1):
    # 判断元素存在
    WebDriverWait(driver,cs,jg).until(EC.presence_of_element_located(yuansu))


def wait_dianji(driver,yuansu,cs=300,jg=1):
    # 判断某个元素中是否可见并且可点击
    WebDriverWait(driver,cs,jg).until(EC.element_to_be_clickable(yuansu))


def wait(driver,yuansu,cs=60,jg=1):
    if yuansu.is_enabled() and yuansu.is_displayed():
        pass
    else:
        WebDriverWait(driver,cs,jg).until(EC.presence_of_element_located(yuansu))


def fanhui_yuanshu():
    return   (By.CSS_SELECTOR,"input[formcontrolname='applicationNumber']")








