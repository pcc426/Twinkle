# coding=utf-8

import requests
import unittest
import os
import sys
import ConfigParser
import json


class LoginTest(unittest.TestCase):
    """ /user/login  接口测试 """

    def setUp(self):
        # 在api_tests目录中执行.py时要改路径
        # base_dir = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
        base_dir = os.path.dirname(os.path.abspath("__file__"))
        self.file_path = base_dir + "\device.conf"    # windows系统下路径
        # self.file_path = base_dir + "/device.conf"    # mac下路径
        print os.path.dirname(os.path.abspath("__file__"))
        print os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
        print("file_path=" + self.file_path)

        cp = ConfigParser.ConfigParser()
        cp.read(self.file_path)

        host = cp.get("host_config", "host")
        device_info = cp.get("ios", "device_info")
        # print device_info

        self.app_init_url = "http://" + host + "/app/init?" + device_info
        # print self.app_init_url
        self.login_url = "http://" + host + "/user/login"
        self.headers = {'Content-Type': "application/x-www-form-urlencoded"}

        payload = {"device_id": "iPhone5,4_0_753E48F5-5FC0-43A4-B668-A1BC24F0B38C"}
        r = requests.post(self.app_init_url, data=json.dumps(payload), headers={'Content-Type': "application/raw"})
        # init接口headers与其他接口不同
        result = r.json()
        # print("APP_INIT_RESPONSE:" + unicode(result))
        self.token = result['token']

    def test_user_login_success(self):
        """ 已注册的手机号密码登录 """

        dataload = {'cellphone': 18601750451, 'password': '750451', 'token': self.token}
        r = requests.post(self.login_url, data=dataload, headers=self.headers)
        result = r.json()
        print(unicode(result))
        self.assertEqual(result['code'], 0)
        self.assertEqual(result['result']['token'], self.token)

        cp = ConfigParser.ConfigParser()
        cp.read(self.file_path)
        cp.set("ios", "token", self.token)
        cp.write(open(self.file_path, 'w'))


class LogoutTest(unittest.TestCase):
    """ /user/logout 接口测试"""

    def setUp(self):
        # 在api_tests目录中执行.py时要改路径
        # base_dir = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
        base_dir = os.path.dirname(os.path.abspath("__file__"))
        # file_path = base_dir + "\api_tests\device.conf"    # windows系统下路径
        self.file_path = base_dir + "/device.conf"    # mac下路径
        # print os.path.dirname(os.path.abspath("__file__"))
        # print os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
        # print("file_path=" + self.file_path)

        cp = ConfigParser.ConfigParser()
        cp.read(self.file_path)

        host = cp.get("host_config", "host")
        self.token = cp.get("ios", "token")
        # self.login_url = "http://" + host + "/user/login"
        self.logout_url = "http://" + host + "/user/logout"
        self.headers = {'Content-Type': "application/x-www-form-urlencoded"}

    def test_user_logout_success(self):
        """用户注销"""

        dataload = {'token': self.token}
        r = requests.post(self.logout_url, data=dataload, headers=self.headers)
        result = r.json()
        print unicode(result)
        self.assertEqual(result['code'], 20008)    # 用户注销太快易失败?先将校验开启,后续可考虑延迟实现
        # self.assertEqual(result['result']['token'], self.token)


if __name__ == '__main__':
    unittest.main()