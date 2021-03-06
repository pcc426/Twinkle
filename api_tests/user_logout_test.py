# coding=utf-8

import requests
import unittest
import os
import sys
import ConfigParser
import json


class LogoutTest(unittest.TestCase):
    """ /user/logout API test"""

    def setUp(self):
        # 在api_tests目录中执行.py时要改路径
        # base_dir = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
        base_dir = os.path.dirname(os.path.abspath("__file__"))
        if os.name == 'nt':
            self.file_path = base_dir + "\config.conf"    # windows系统下路径
        else:
            self.file_path = base_dir + "/config.conf"    # mac/linux下路径

        cp = ConfigParser.ConfigParser()
        cp.read(self.file_path)

        host = cp.get("host_config", "host")
        self.token = cp.get("ios", "token")
        self.logout_url = "http://" + host + "/user/logout"
        self.headers = {'Content-Type': "application/x-www-form-urlencoded"}

    def test_user_logout_success(self):
        """ User Logout success"""

        dataload = {'token': self.token}
        r = requests.post(self.logout_url, data=dataload, headers=self.headers)
        result = r.json()
        print("LOGOUT_RESP=" + unicode(result))
        self.assertEqual(result['code'], 0)

if __name__ == '__main__':
    unittest.main()
