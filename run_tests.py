import sys
import unittest
import HtmlTestRunner
sys.path.append('./api_tests')


test_dir = './api_tests'
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='login_test.py')
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == '__main__':
    # 如果需要html格式输出测试报告,可用下面的html_runner
    # html_runner = HtmlTestRunner.HTMLTestRunner(output='../../api_test_results', verbosity=2)
    # html_runner.run(discover)

    # 普通报告输出
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(discover)
