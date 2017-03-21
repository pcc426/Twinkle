#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Pcc on 3/21/17


import unittest
import requests
import os
import ConfigParser


class VideoRateTest(unittest.TestCase):
    """/video/video_rate API test"""

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
        self.url = "http://" + host + "/video/video_rate"
        self.headers = {'Content-Type': 'text/html', 'release': '0', 'channel': 'standard', 'version':
                        self.cp.get("ios", "version"), 'app': self.cp.get("ios", "app")}
        self.params = {'token': self.token, 'vid': self.cp.get('program', 'vid'),
                       'fdn_code': self.cp.get('program', 'fdn_code')}

    def test_video_rate_success(self):
        r = requests.get(self.url, params=self.params, headers=self.headers)
        result = r.json()
        # print r.url
        print('RESP:' + unicode(result))
        self.assertEqual(result['code'], 0)
        self.assertNotEqual(result['data']['download'], [], msg='download rate exist')
        self.assertNotEqual(result['data']['livestream'], [], msg='livestream rate exist')


if __name__ == '__main__':
    unittest.main()
