#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Pcc on 3/21/17


import unittest
import requests
import os
import ConfigParser


class HotKeywordsTest(unittest.TestCase):
    """/video/hot_keywords API test"""

    def setUp(self):
        base_dir = os.path.dirname(os.path.abspath("__file__"))
        if os.name == 'nt':
            self.file_path = base_dir + "\config.conf"    # windows系统下路径
        else:
            self.file_path = base_dir + "/config.conf"    # mac/linux下路径
        # print os.path.dirname(os.path.abspath("__file__"))
        # print os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
        # print("file_path=" + self.file_path)

        cp = ConfigParser.ConfigParser()
        cp.read(self.file_path)

        host = cp.get("host_config", "host")
        device_info = cp.get("ios", "device_info")
        self.token = cp.get("ios", "token")
        self.url = "http://" + host + "/video/hot_keywords?" + device_info
        self.headers = {'Content-Type': 'text/html', 'release': '0', 'channel': 'standard', 'version':
                        cp.get("ios", "version"), 'app': cp.get("ios", "app")}
        self.params = {'token': self.token}

    def test_hot_keywords_success(self):
        r = requests.get(self.url, params=self.params, headers=self.headers)
        result = r.json()
        # print r.url
        # print('INDEX_V2 RESP:' + unicode(result))
        self.assertEqual(result['code'], 0)
        self.assertNotEqual(result['total'], 0)
        self.assertNotEqual(result['data'], [])
        self.assertNotEqual(result['ad_mplus']['btu'], "", msg='ad_mplus is not null')


if __name__ == '__main__':
    unittest.main()
