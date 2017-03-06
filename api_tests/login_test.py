# coding=utf-8

import requests
import unittest
import os
import sys
import ConfigParser


class LoginTest(unittest.TestCase):
    """ user/login 接口测试 """

    def setUp(self):
        base_dir = os.getcwd()
        file_path = base_dir + "\device.conf"
        # print("file_path="+ file_path)

        cp = ConfigParser.ConfigParser()
        cp.read(file_path)

        host = cp.get("host_config", "host")

        self.url = "http://"+ host + "/user/login"
        self.headers = {'Content-Type': "application/x-www-form-urlencoded"}
        self.ios_app = cp.get("ios", "app")
        self.android_app = cp.get("android", "app")
        self.ios_version = cp.get("ios", "version")
        self.android_version = cp.get("android", "version")
        self.ios_release = cp.get("ios", "release")
        self.android_release = cp.get("android", "release")
        self.channel = cp.get("ios", "channel")

    def test_user_login_success(self):
        """已注册的手机号密码登录成功"""
        dataload = {'cellphone': 18601750451, 'password': '750451'}
        r = requests.post(self.url, data=dataload, headers=self.headers)
        result = r.json()
        result_uni = unicode(result)
        print(result_uni)
        self.assertEqual(result['code'], 0)
        self.assertIsNotNone(result['result']['token'])

if __name__ == '__main__':
     unittest.main()