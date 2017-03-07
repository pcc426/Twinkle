# coding=utf-8

import requests
import unittest
import os
import sys
import ConfigParser


class LoginLogoutTest(unittest.TestCase):
    """ user/login 接口测试 """

    def setUp(self):
        base_dir = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
        file_path = base_dir + "\device.conf"
        print os.path.dirname(os.path.abspath("__file__"))
        print os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
        # print("file_path="+ file_path)

        cp = ConfigParser.ConfigParser()
        cp.read(file_path)

        host = cp.get("host_config", "host")

        self.login_url = "http://"+ host + "/user/login"
        self.logout_url = "http://"+ host + "/user/logout"
        self.headers = {'Content-Type': "application/x-www-form-urlencoded"}
        self.ios_app = cp.get("ios", "app")
        self.android_app = cp.get("android", "app")
        self.ios_version = cp.get("ios", "version")
        self.android_version = cp.get("android", "version")
        self.ios_release = cp.get("ios", "release")
        self.android_release = cp.get("android", "release")
        self.channel = cp.get("ios", "channel")
        self.token = ""

    def test_user_login_success(self):
        """已注册的手机号密码登录成功"""

        # s = requests.session()
        dataload = {'cellphone': 18601750451, 'password': '750451'}
        # r = s.post(self.login_url, data=dataload, headers=self.headers)
        r = requests.post(self.login_url, data=dataload, headers=self.headers)
        result = r.json()
        result_uni = unicode(result)
        print(result_uni)
        self.assertEqual(result['code'], 0)
        self.assertIsNotNone(result['result']['token'])
        if result['result']['token']:
            self.__class__.token = result['result']['token']

    # def test_user_logout(self):
    #     """登出成功"""
    #
    #     print("Logout Token=" + self.__class__.token)
    #     dataload = {'token': self.__class__.token}
    #     r = requests.post(self.logout_url, data=dataload, headers=self.headers)
    #     result = r.json()
    #     print unicode(result)
    #     self.assertEqual(result['code'], 0)
    #     self.assertEqual(result['result']['token'],self.__class__.token)

if __name__ == '__main__':
     unittest.main()