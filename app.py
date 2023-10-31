
from pages.home import home_bnt
# from business.file_processing import cxjy
from time import sleep
from testcase.test_cuowuduilie import  test_chongxinjiaoyan
from testcase.test_gongzuoliu import  *
from testcase.test_denglu import  Test_login
import pytest
import time
import subprocess

if __name__=='__main__':
    
    # tiao_ma=subprocess.run(['python', r'C:\project\PycharmProjects\UI自动化学习\project\main.py'])
    # print(tiao_ma.stdout)
    # print(tiao_ma[1])
    # test_chongxinjiaoyan('202303241000003')
    # testdl=Test_login()
    # testdl.setup_class()
    # testdl.test_login()

    # test01=Test_gongzuoliu()
    # test01.test_gongzuoliu('202308311110842','30000')

    # test_gongzuoliu('202310241108735','0')

    # test_gongzuoliu('202310261108907','30000')
    # test_gongzuoliu('202310081128649','50000')
    # test_gongzuoliu('202309121000006','50000')
    # test_gongzuoliu('202309071107998','30000')
    # test_gongzuoliu('202309071107999','30000')

    # pytest.main(['test_cuowuduilie.py'])
    # pytest.main(['-vs','test_denglu.py'])
    # pytest.main(['test_gongzuoliu.py'])
    # pytest.main(['-vs',r'C:\project\Activate\testcase'])

    
    directory_time = time.strftime("%Y-%m-%d-%H-%S-%M",time.localtime(time.time()))   
    pytest.main(['--alluredir','report\%s'%directory_time,r'C:\project\Activate\testcase'])

    # directory_time = time.strftime("%Y-%m-%d-%H-%S-%M",time.localtime(time.time()))       
    # pytest.main(['--alluredir','report\%s'%directory_time,r'C:\project\Activate\testcase\test_gongzuoliu.py'])
    # # 出测试报告
    # 
    # sleep(3)
    
    















