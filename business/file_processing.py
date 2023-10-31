
# 文件处理
from pages.cuowuduilie import *
from pages.login import Login
from pages.shenqingchaxun import shenqingchaxun
# from pages.home import home_bnt
# from pages.shenqingchaxun import shenqingchaxun
# from pages.waibujieku_in import waibujiekou_in
from pages.cuowuduilie import cuowu
from time  import sleep
from util.fangfa import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.waibujiekou_in import waibujiekou_in
from pages.waibujiekou import waibujiekou
from pages.xinshen import xinshen
from pages.xinshen_in import xinshen_in
from pages.xinyongjuece import xinyongjuece
from pages.shishizhika import shishizhika
from pages.fenzhongxinyushen import fenzhongxinyushen

def login(user='Administrator',pwd='000000'):
    denglu_logger=Login()
    logger = get_logger()
    logger.info('申请查询页')
    denglu_logger.user.send_keys(user)
    denglu_logger.pwd.send_keys(pwd)
    jietu('登录页截图',denglu_logger.driver)
    denglu_logger.log_on.click()
    return denglu_logger.driver

    # 输入条码,点击查询,点击第一个元素,点击重新校验
def chongxinchaxun(tiaoma,driver):
    cuowu1=cuowu(tiaoma,driver)
    wait_chunzai(cuowu1.driver,cuowu1.loc_one)
    # WebDriverWait(cuowu1.driver,60,2).until(EC.presence_of_element_located(cuowu1.loc_one))
    cuowu1.shenqingtiaoma.send_keys(cuowu1.tiaoma)
    cuowu1.shousuojianyan.click()
    sleep(2)
    # wait_dianji(driver,cuowu1.loc_two)
    cuowu1.liebiao1.click()
    # sleep(2)
    # wait_dianji(driver,cuowu1.chongxinjiaoyan)
    cuowu1.driver.execute_script("arguments[0].scrollIntoView(true);", cuowu1.chongxinjiaoyan)
    wait_dianji(driver,cuowu1.chongxinjiaoyan)
    cuowu1.chongxinjiaoyan.click()
    jietu('点击重新查询',cuowu1.driver)

def chaxun(tiaoma,driver):
    sqcx=shenqingchaxun(tiaoma,driver)
    wait_dianji(driver,sqcx.shenqingtiaoma_yuanshu)
    sqcx.shenqingtiaoma.send_keys(sqcx.tiaoma)
    # 因为信审INS时候更新队列较慢所以要加等待
    sleep(1)
    sqcx.chaxunshenqing.click()
    # # 申请查询列表
    # wenzi='//*[contains(text(),%s)]'% tiaoma
    WebDriverWait(sqcx.driver,300,2).until(EC.presence_of_element_located(sqcx.liebiao_zhuangtai))
    # self.liebiao_sqtm=self.driver.find_element(By.XPATH,self.wenzi)
    # self.liebiao_sqtm.click()
    wenben=sqcx.driver.find_element(*sqcx.liebiao_zhuangtai).text
    sqcx.logger.debug('申请件状态')
    while wenben=='装载':
        sqcx.chaxunshenqing.click()
        wait_dianji(driver,sqcx.liebiao_zhuangtai)
        # sleep(1)
        wenben=sqcx.driver.find_element(*sqcx.liebiao_zhuangtai).text
    return wenben


def waibujiekou_ins(tiaoma,driver):
    wbjk_in=waibujiekou_in(tiaoma,driver)
    WebDriverWait(driver,60,2).until(EC.presence_of_element_located(wbjk_in.loc_one))
    wbjk_in.shenqingtiaoma.send_keys(tiaoma)
    wbjk_in.sousuozishen.click()
    sleep(3)
    # 判断查询到
    if wbjk_in.liebiaoshu.text=='0 of 0':
        # 点击搜索他人
        wbjk_in.sousuotashen.click()
        # # 申请查询列表
        # wenzi='//*[contains(text(),%s)]'% tiaoma
        WebDriverWait(wbjk_in.driver,60,2).until(EC.presence_of_element_located(wbjk_in.wenzi))
        wbjk_in.driver.find_element(*wbjk_in.wenzi).click()
        wbjk_in.driver.execute_script(('window.scrollBy(0,10000)'))
        wbjk_in.xinshen.click()
        # sleep(2)
        wait_dianji(driver,wbjk_in.queding)
        wbjk_in.driver.find_element(*wbjk_in.queding).click()
        sleep(0.5)
        wait_dianji(driver,wbjk_in.queding)
        wbjk_in.driver.find_element(*wbjk_in.queding).click()
        sleep(1)
    else:
        WebDriverWait(wbjk_in.driver,60,2).until(EC.presence_of_element_located(wbjk_in.wenzi))
        wbjk_in.driver.find_element(*wbjk_in.wenzi).click()
        wbjk_in.driver.execute_script(('window.scrollBy(0,10000)'))
        wbjk_in.xinshen.click()
        # sleep(2)
        wait_dianji(driver,wbjk_in.queding)
        wbjk_in.driver.find_element(*wbjk_in.queding).click()
        # sleep(7)
        sleep(0.5)
        wait_dianji(driver,wbjk_in.queding)
        wbjk_in.driver.find_element(*wbjk_in.queding).click()
        sleep(1)
 
            

# 跳过外部接口
def wbjk(tiaoma,driver):
    wbjk_s=waibujiekou(tiaoma,driver)    
    wait_dianji(driver,wbjk_s.loc_one)
    wbjk_s.driver.execute_script(('window.scrollBy(10000,0)'))
    sleep(2)
    wbjk_s.shenqingtiaoma.send_keys(tiaoma)
    wbjk_s.sousuozishen.click()
    sleep(1)
    wbjk_s.driver.find_element(*wbjk_s.wenzi).click()
    wbjk_s.tiaoguowaibujiekou.click()
    sleep(1)
    wbjk_s.driver.find_element(*wbjk_s.queding).click()
    sleep(7)
    wbjk_s.driver.find_element(*wbjk_s.queding).click()


# 信审审核到下一队列
def xinshens(tiaoma,driver):
    xs=xinshen(tiaoma,driver)
    xs.shenqingtiaoma.send_keys(tiaoma)
    xs.sousuozishen.click()
    sleep(1)
    if xs.liebiaoshu.text=='0 of 0':
        xs.sousuotashen.click()
        # 点击列表数据
        sleep(3)
        xs.driver.find_element(*xs.wenzi).click()
        # 点击信审
        xs.driver.execute_script(('window.scrollBy(0,10000)'))
        sleep(1)
        xs.driver.find_element(*xs.xinshen).click()
        # sleep(5)
        # 等待加载      
        wait_dianji(driver,xs.kehutezheng)
        xs.driver.execute_script(('window.scrollBy(10000,0)'))
        sleep(2)
        # 点击工作所在地
        xs.driver.execute_script("arguments[0].scrollIntoView();",xs.driver.find_element(*xs.kehutezheng))
        # sleep(1)
        wait_dianji(driver,xs.gongzuosuozaidi)
        sleep(1)
        xinshen_list=xs.driver.find_elements(*xs.gongzuosuozaidi)
        xinshen_list[4].click()

        # next_btn = xs.driver.find_element(By.XPATH,"//div[@class='pager_container']/span[last()]")
        xs.driver.execute_script("arguments[0].click();", xs.driver.find_element(*xs.gongzuosuozaidi_heb))
        # xs.driver.find_element(*xs.gongzuosuozaidi_heb).click()
        # 点击详细信息
        xs.driver.execute_script(('window.scrollBy(0,5000)'))
        shuoyin=0
        xs_xiangxixinxi=xs.driver.find_elements(*xs.xiangxixinxi)
        while shuoyin in range(len(xs_xiangxixinxi)-2):
         
            # if 'disabled'  not in str(xs_xiangxixinxi[shuoyin].get_property("outerHTML")) and xs_xiangxixinxi[shuoyin].text=='查询详情' or xs_xiangxixinxi[shuoyin].text=='详细信息':
            #     # if shuoyin==3:
            #     #     print(xs_xiangxixinxi[shuoyin].get_property("outerHTML"))
            try:
                xs_xiangxixinxi[shuoyin].click()

                sleep(0.5)
                # Action.move_to_element(my_error_element).perform()
                xs.driver.find_element(*xs.queding).click()
            except:
                pass
            shuoyin+=1
            if shuoyin==5:
                xs.driver.execute_script(('window.scrollBy(0,10000)'))
                sleep(1)

        # 点击客户特征
        xs.driver.execute_script(('window.scrollBy(10000,0)'))
        sleep(1)
        xs.driver.find_element(*xs.kehutezheng).click()
        # 点击行业
        xs.driver.execute_script(('window.scrollBy(0,10000)'))
        xs.driver.find_element(*xs.hangye).click()
        sleep(0.5)
        # xs.driver.execute_script("arguments[0].click();", xs.driver.find_element(*xs.hangye_A01))
        xs.driver.find_element(*xs.hangye_A01).click()
        # 点击职位
        xs.driver.find_element(*xs.zhiwei).click()
        sleep(0.5)
        xs.driver.find_element(*xs.zhiwei_A01).click()
        # 点击日志
        xs.driver.find_element(*xs.rizhi).click()
        sleep(1)
        xs.driver.execute_script(('window.scrollBy(0,10000)'))
        xs.driver.find_element(*xs.guanbi).click()
        # 点击提交
        # 点击提交
        sleep(0.5)
        xs.driver.find_element(*xs.tijiao).click()
        # sleep(5)
        # 点击确认
        wait_dianji(driver,xs.queding)
        xs.driver.find_element(*xs.queding).click()
        # sleep(25)
        # 再次确认
        sleep(0.5)
        wait_dianji(driver,xs.queding)
        xs.driver.find_element(*xs.queding).click()
        # sleep(8)
        # try:
        #     xs.driver.find_element(*xs.queding).click()
        # except:
        #     pass
     
   

    else:
        # 点击列表数据
        sleep(3)
        xs.driver.find_element(*xs.wenzi).click()
        # 点击信审
        xs.driver.execute_script(('window.scrollBy(0,10000)'))
        sleep(1)
        xs.driver.find_element(*xs.xinshen).click()
        # sleep(5)
        # 等待加载
        wait_dianji(driver,xs.kehutezheng)
        xs.driver.execute_script(('window.scrollBy(10000,0)'))
        sleep(2)
        # 点击工作所在地
        xs.driver.execute_script("arguments[0].scrollIntoView();",xs.driver.find_element(*xs.kehutezheng))
        sleep(2)
        xinshen_list=xs.driver.find_elements(*xs.gongzuosuozaidi)
        xinshen_list[4].click()

        # next_btn = xs.driver.find_element(By.XPATH,"//div[@class='pager_container']/span[last()]")
        xs.driver.execute_script("arguments[0].click();", xs.driver.find_element(*xs.gongzuosuozaidi_heb))
        # xs.driver.find_element(*xs.gongzuosuozaidi_heb).click()
        # 点击详细信息
        xs.driver.execute_script(('window.scrollBy(0,5000)'))
        shuoyin=0
        xs_xiangxixinxi=xs.driver.find_elements(*xs.xiangxixinxi)
        while shuoyin in range(len(xs_xiangxixinxi)-2):
         
            # if 'disabled'  not in str(xs_xiangxixinxi[shuoyin].get_property("outerHTML")) and xs_xiangxixinxi[shuoyin].text=='查询详情' or xs_xiangxixinxi[shuoyin].text=='详细信息':
            #     # if shuoyin==3:
            #     #     print(xs_xiangxixinxi[shuoyin].get_property("outerHTML"))
            try:
                xs_xiangxixinxi[shuoyin].click()

                sleep(0.5)
                # Action.move_to_element(my_error_element).perform()
                xs.driver.find_element(*xs.queding).click()
            except:
                pass
            shuoyin+=1
            if shuoyin==5:
                xs.driver.execute_script(('window.scrollBy(0,10000)'))
                sleep(1)

        # 点击客户特征
        xs.driver.execute_script(('window.scrollBy(10000,0)'))
        sleep(1)
        xs.driver.find_element(*xs.kehutezheng).click()
        # 点击行业
        xs.driver.execute_script(('window.scrollBy(0,10000)'))
        xs.driver.find_element(*xs.hangye).click()
        # xs.driver.execute_script("arguments[0].click();", xs.driver.find_element(*xs.hangye_A01))
        xs.driver.find_element(*xs.hangye_A01).click()
        # 点击职位
        xs.driver.find_element(*xs.zhiwei).click()
        xs.driver.find_element(*xs.zhiwei_A01).click()
        # 点击日志
        xs.driver.find_element(*xs.rizhi).click()
        sleep(1)
        xs.driver.execute_script(('window.scrollBy(0,10000)'))
        xs.driver.find_element(*xs.guanbi).click()
        # 点击提交
        sleep(0.5)
        xs.driver.find_element(*xs.tijiao).click()
        # sleep(5)
        # 点击确认
        wait_dianji(driver,xs.queding)
        xs.driver.find_element(*xs.queding).click()
        # sleep(25)
        # 再次确认
        try:
            wait_dianji(driver,xs.queding)
            xs.driver.find_element(*xs.queding).click()
            sleep(8)
        except:
            pass
        try:
            xs.driver.find_element(*xs.queding).click()
        except:
            pass
        

        
# 信审_ins队列审核到下一节点
def xinshen_ins(tiaoma,driver):
    xs_in=xinshen_in(tiaoma,driver)
    xs_in.shenqingtiaoma.send_keys(tiaoma)
    xs_in.sousuozishen.click()
    xs_in.driver.execute_script(('window.scrollBy(0,10000)'))
    sleep(0.5)
    if xs_in.liebiaoshu.text=='0 of 0':
        xs_in.sousuotashen.click()
        # 点击列表数据
        sleep(1)
        xs_in.driver.find_element(*xs_in.wenzi).click()
        xs_in.xinyongjuece.click()
        wait_dianji(driver,xs_in.queding)
        xs_in.driver.find_element(*xs_in.queding).click()
        sleep(0.5)
        wait_dianji(driver,xs_in.queding)
        xs_in.driver.find_element(*xs_in.queding).click()
    else:
        # 点击列表数据
        sleep(1)
        xs_in.driver.find_element(*xs_in.wenzi).click()
        xs_in.xinyongjuece.click()
        wait_dianji(driver,xs_in.queding)
        xs_in.driver.find_element(*xs_in.queding).click()
        wait_dianji(driver,xs_in.queding)
        xs_in.driver.find_element(*xs_in.queding).click()

# 信用决策核准(额度默认30000)
def xyjc(tiaoma,driver,ed_a='50000'):
    xyjc_s=xinyongjuece(tiaoma,driver)
    xyjc_s.shenqingtiaoma.send_keys(tiaoma)
    xyjc_s.sousuozishen.click()
    sleep(2)

    # 判断列表中是否存在数据
    if xyjc_s.liebiaoshu.text=='0 of 0':
        xyjc_s.sousuotashen.click()
        sleep(0.5)
        xyjc_s.driver.find_element(*xyjc_s.wenzi).click()
        xyjc_s.driver.execute_script(('window.scrollBy(0,10000)'))
        sleep(0.5)
        xyjc_s.xinyongjuece.click()
        sleep(3)
        # 点击决策
        xyjc_s.driver.find_element(*xyjc_s.juecejieguo).click()
        # 选择核准
        xyjc_s.driver.find_element(*xyjc_s.hezhun).click()
        # 输入额度
        xyjc_s.driver.find_element(*xyjc_s.ed).clear()
        xyjc_s.driver.find_element(*xyjc_s.ed).send_keys(ed_a)
        # 选择限额原因
        xyjc_s.driver.find_element(*xyjc_s.xianeyuanyin).click()
        xyjc_s.driver.find_element(*xyjc_s.xianeyuanyin_801).click()
        # 点击结果
        xyjc_s.driver.find_element(*xyjc_s.jieguo).click()
        wait_dianji(driver,xyjc_s.queding)
        xyjc_s.driver.find_element(*xyjc_s.queding).click()
        sleep(0.5)
        try:
            wait_dianji(driver,xyjc_s.queding)
            xyjc_s.driver.find_element(*xyjc_s.queding).click()
        except:
            pass
    else:
        xyjc_s.driver.find_element(*xyjc_s.wenzi).click()
        xyjc_s.driver.execute_script(('window.scrollBy(0,10000)'))
        sleep(0.5)
        xyjc_s.xinyongjuece.click()
        sleep(3)
        # 点击决策
        xyjc_s.driver.find_element(*xyjc_s.juecejieguo).click()
        # 选择核准
        xyjc_s.driver.find_element(*xyjc_s.hezhun).click()
        # 输入额度
        
        xyjc_s.driver.find_element(*xyjc_s.ed).send_keys(ed_a)
        # 选择限额原因
        xyjc_s.driver.find_element(*xyjc_s.xianeyuanyin).click()
        xyjc_s.driver.find_element(*xyjc_s.xianeyuanyin_801).click()
        # 点击结果
        xyjc_s.driver.find_element(*xyjc_s.jieguo).click()
        sleep(4)
        xyjc_s.driver.find_element(*xyjc_s.queding).click()
        sleep(17)
        try:
            xyjc_s.driver.find_element(*xyjc_s.queding).click()
        except:
            pass
        


# 实时制卡
def sszk(tiaoma,driver):
    sszk_s=shishizhika(tiaoma,driver)
    sszk_s.shenqingtiaoma.send_keys(tiaoma)
    sszk_s.driver.find_element(*sszk_s.chaxunshishizhika).click()
    sleep(0.5)
    # print(sszk_s.driver.find_elements(*sszk_s.chulijieguo)[1].text)
    if sszk_s.driver.find_elements(*sszk_s.wenzi)=='':
        return '非快发卡'
    chishu=0
    if sszk_s.driver.find_elements(*sszk_s.chulijieguo)[1].text!='处理成功' and chishu<4:
        while chishu<4 and sszk_s.driver.find_elements(*sszk_s.chulijieguo)[1].text!='处理成功':
            sszk_s.driver.find_element(*sszk_s.chaxunshishizhika).click()
            sleep(1)
            sszk_s.driver.find_element(*sszk_s.wenzi).click()
            sszk_s.driver.find_element(*sszk_s.chongdiao).click()
            sleep(1)
            sszk_s.driver.find_element(*sszk_s.queding).click()
            sleep(1)
            # sszk_s.driver.find_element(*sszk_s.queding)
            sszk_s.driver.find_element(*sszk_s.chaxunshishizhika).click()
            chishu+=1
            sleep(1)
        if chishu>3:
            return '制卡失败'
        else:
            return '制卡成功'


# 分中心预审
def fzxys(tiaoma,driver):
    fzxys_s=fenzhongxinyushen(tiaoma,driver)
    wait_dianji(driver,fzxys_s.loc_one)
    fzxys_s.shenqingtiaoma.send_keys(tiaoma)
    fzxys_s.sousuozishen.click()
    sleep(2)
    # 判断列表中是否存在数据
    if fzxys_s.liebiaoshu.text=='0 of 0':
        fzxys_s.sousuotashen.click()
        sleep(1)
        fzxys_s.driver.find_element(*fzxys_s.wenzi).click()
        fzxys_s.driver.execute_script(('window.scrollBy(0,10000)'))
        fzxys_s.driver.find_element(*fzxys_s.chongxinfenpei).click()
        sleep(1)
        # fzxys_s.driver.execute_script(('window.scrollBy(0,4000)'))
        fzx_admin=fzxys_s.driver.find_element(*fzxys_s.admin)
        fzxys_s.driver.execute_script("arguments[0].scrollIntoView();",fzx_admin)
        sleep(1)
        # 选择admin
        fzx_admin.click()
        sleep(1)
        fzxys_s.driver.find_element(*fzxys_s.queding).click()
        sleep(1)
        fzxys_s.driver.find_element(*fzxys_s.queding).click()
        sleep(1)
        fzxys_s.sousuozishen.click()
        sleep(1)
        fzxys_s.driver.find_element(*fzxys_s.wenzi).click()
        yushen=fzxys_s.driver.find_elements(*fzxys_s.yushen)[5].click()
        # sleep(0.5)
        # fzxys_s.driver.find_element(*fzxys_s.yushen).click()
        fzxys_s.driver.execute_script(('window.scrollBy(10000,0)'))
        wait_dianji(driver,fzxys_s.fujia1)
        fzxys_s.driver.find_element(*fzxys_s.tijiao).click()
        # sleep(13)
        wait_dianji(driver,fzxys_s.queding)
        fzxys_s.driver.find_element(*fzxys_s.queding).click()
        sleep(1)
    else:
        sleep(1)
        fzxys_s.driver.find_element(*fzxys_s.wenzi).click()
        yushen=fzxys_s.driver.find_elements(*fzxys_s.yushen)[5].click()
        # sleep(0.5)
        # fzxys_s.driver.find_element(*fzxys_s.yushen).click()
        fzxys_s.driver.execute_script(('window.scrollBy(10000,0)'))
        wait_dianji(driver,fzxys_s.fujia1)
        fzxys_s.driver.find_element(*fzxys_s.tijiao).click()
        wait_dianji(driver,fzxys_s.queding)
        # sleep(13)
        fzxys_s.driver.find_element(*fzxys_s.queding).click()
        sleep(1)
        



















