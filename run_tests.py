#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Pcc on 3/13/10

import sys
import unittest
import HTMLTestRunner
import datetime
sys.path.append('./api_tests')


test_dir = './api_tests'
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='login_test.py')
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == '__main__':
    
    # 如果需要html格式输出测试报告,可用下面的html_runner
    str_time = datetime.datetime.now().strftime('%b_%d_%y_%H_%M_%S')
    fp = file('results/api_test_report_' + str_time + '.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='Api_Test_Report',
        description='This demonstrates the report output by HTMLTestRunner.',
        verbosity=2
    )
    runner.run(discover)

    # 普通报告输出
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(discover)
