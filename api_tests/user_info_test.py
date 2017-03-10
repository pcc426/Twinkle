# coding=utf-8

import requests
import unittest
import os
import sys
import ConfigParser
import json


class LoginTest(unittest.TestCase):
    """ /user/login interface tests """

    def setUp(self):
        # 在api_tests目录中执行.py时要改路径
        # base_dir = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
        base_dir = os.path.dirname(os.path.abspath("__file__"))
        # self.file_path = base_dir + "\device.conf"    # windows系统下路径
        self.file_path = base_dir + "/device.conf"    # mac下路径
        # print os.path.dirname(os.path.abspath("__file__"))
        # print os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
        # print("file_path=" + self.file_path)

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
        """ User Login Via Cellphone/Password """

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


class UserInfoTest(unittest.TestCase):
    """ user/info interface test """

    def setUp(self):
        # 在api_tests目录中执行.py时要改路径
        # base_dir = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
        base_dir = os.path.dirname(os.path.abspath("__file__"))
        # self.file_path = base_dir + "\device.conf"    # windows系统下路径
        self.file_path = base_dir + "/device.conf"    # mac下路径

        cp = ConfigParser.ConfigParser()
        cp.read(self.file_path)

        host = cp.get("host_config", "host")
        self.token = cp.get("ios", "token")
        self.url = "http://" + host + "/user/info"
        self.headers = {'Content-Type': "application/x-www-form-urlencoded"}

    def test_user_info_success(self):
        r = requests.get(self.url, {'token': self.token})
        result = r.json()
        print('USER_INFO_RESP:' + unicode(result))
        self.assertEqual(result['code'], 0)
        self.assertIsNotNone(result['data']['uuid'])
        self.assertIsNotNone(result['data']['is_vip'])


if __name__ == '__main__':
    unittest.main()
