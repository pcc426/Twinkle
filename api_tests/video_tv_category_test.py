#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Pcc on 3/13/17

import unittest
import requests
import os
import ConfigParser


class TvCateTest(unittest.TestCase):
    """/video/tv_category API test"""

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

        # cp = ConfigParser.ConfigParser()
        self.cp.read(self.file_path)

        host = self.cp.get("host_config", "host")
        # device_info = self.cp.get("ios", "device_info")
        self.token = self.cp.get("ios", "token")
        self.url = "http://" + host + "/video/tv_category"
        self.headers = {'Content-Type': 'text/html', 'release': '0', 'channel': 'standard', 'version':
                        self.cp.get("ios", "version"), 'app': self.cp.get("ios", "app")}
        self.params = {'token': self.token, 'app': self.cp.get('ios', 'app')}

    def test_tv_category_success(self):
        r = requests.get(self.url, params=self.params, headers=self.headers)
        result = r.json()
        cid = result['data'][0]['id']
        # print r.url
        # print('INDEX_V2 RESP:' + unicode(result))
        self.assertEqual(result['code'], 0)
        self.assertNotEqual(result['data'], [])

        if cid != "":
            self.cp.set("tv_program", "cid", value=cid)
            self.cp.write(open(self.file_path, "w"))
        else:
            print("Cid is null!")

if __name__ == '__main__':
    unittest.main()
