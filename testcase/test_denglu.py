

import os
import sys
path=os.getcwd()
# print(path)
sys.path.append(path)
import pytest
import allure
from business.file_processing import login
from business.file_processing import *

class Test_login(object):
    category_data = [
        
        ('add','111111', '用户不存在！'),
        ('Administrator','222222', '用户验证不通过！'),
        ('Administrator','000000', 'GBG Activate - Credit Application Management | GBG'),
    ]
    # 类级别函数
    def setup_class(self) -> None:
        self.denglu_logger=Login()
        self.logger = get_logger()
        self.logger.info('测试用户登录')

    @allure.story('登录功能')
    @allure.title('登录测试用例')
    # 登录依赖
    # @pytest.mark.dependency(depends=["admin_login"], scope="module")
    @pytest.mark.parametrize('user,pwd,jiaoyan', category_data)
    def test_login(self,user,pwd,jiaoyan):
        # denglu_logger=Login()
        # self.logger = get_logger()
        self.denglu_logger.user.clear() 
        self.denglu_logger.user.send_keys(user)
        self.logger.debug('输入用户名称：%s', user)
        self.denglu_logger.pwd.clear()
        self.denglu_logger.pwd.send_keys(pwd)
        self.logger.debug('输入用户密码：%s', pwd)
        self.denglu_logger.log_on.click()
        self.logger.debug('点击登录')
        sleep(3)
        if self.denglu_logger.driver.current_url==self.denglu_logger.jiaoyan_sc:
            jietu('登录成功',self.denglu_logger.driver)
            sleep(1)
            self.denglu_logger.driver.quit()
            # http://170.254.228.174/#/home
        else :
            assert self.denglu_logger.driver.find_element(*self.denglu_logger.jiaoyan_cw).text==jiaoyan
            sleep(1)
            jietu(jiaoyan,self.denglu_logger.driver)
            sleep(1)
                
        
# if __name__=='__main__':
    # a=Test_login
    # a.test_login()
    # pytest.main(['test_denglu.py'])
if __name__ == '__main__':
    # 这里可以跳过登录错误
    pytest.main(['-vs',r'C:\project\Activate\testcase\test_denglu.py'])




