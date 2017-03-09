import sys
import unittest
sys.path.append('./api_tests')


test_dir = './api_tests'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)