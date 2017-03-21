#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Pcc on 3/21/17


import unittest
import requests
import os
import ConfigParser


class ProductlistTest(unittest.TestCase):
    """/user/productList API test"""

    cp = ConfigParser.ConfigParser()

    def setUp(self):
        base_dir = os.path.dirname(os.path.abspath("__file__"))
        if os.name == 'nt':
            self.file_path = base_dir + "\config.conf"    # windows系统下路径
        else:
            self.file_path = base_dir + "/config.conf"    # mac/linux下路径
        # print os.path.dirname(os.path.abspath("__file__"))
        # print os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
        # print("file_path=" + self.file_path)

        self.cp.read(self.file_path)

        host = self.cp.get("host_config", "host")
        # device_info = self.cp.get("ios", "device_info")
        self.token = self.cp.get("ios", "token")
        self.url = "http://" + host + "/user/productList"
        # self.headers = {'Content-Type': 'text/html', 'release': '0', 'channel': 'standard', 'version':
        #                 self.cp.get("ios", "version"), 'app': self.cp.get("ios", "app")}
        self.params = {'token': self.token}

    def test_product_list_success(self):
        r = requests.post(self.url, data=self.params,
                          headers={'Content-Type': "application/x-www-form-urlencoded"})
        result = r.json()
        # print r.headers
        # print('RESP:' + unicode(result))
        self.assertEqual(result['code'], 0)
        self.assertIsInstance(result['data'][0], dict)
        self.assertIsInstance(result['data'][1], dict)
        self.assertIsInstance(result['data'][2], dict)
        self.assertNotEqual(result['data'][0]['product_id'], "")
        self.assertNotEqual(result['data'][0]['product_name'], "")
        self.assertNotEqual(result['data'][0]['price'], "")


if __name__ == '__main__':
    unittest.main()
