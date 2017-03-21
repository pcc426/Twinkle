#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Pcc on 3/21/17


import unittest
import requests
import os
import ConfigParser


class VideoRecommendTest(unittest.TestCase):
    """/video/recommend API test"""

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
        self.url = "http://" + host + "/video/recommend"
        self.headers = {'Content-Type': 'text/html', 'release': '0', 'channel': 'standard', 'version':
                        self.cp.get("ios", "version"), 'app': self.cp.get("ios", "app")}
        self.params = {'token': self.token, 'vid': self.cp.get('program', 'vid')}

    def test_video_recommend_success(self):
        r = requests.get(self.url, params=self.params, headers=self.headers)
        result = r.json()
        # print r.url
        # print('RESP:' + unicode(result))
        self.assertEqual(result['code'], 0)
        self.assertNotEqual(result['total'], 0)
        self.assertNotEqual(result['data'][0]['id'], "", msg='recommend vid is not null')
        self.assertNotEqual(result['data'][0]['title'], "", msg='recommend title is not null')
        self.assertNotEqual(result['data'][0]['small_image1'], "", msg='recommend small_image1 is not null')

    def test_video_recommend_no_related_videos(self):
        'vid=2401050 should not have any related videos'
        r = requests.get(self.url, params={'token': self.token, 'vid': '2401050'}, headers=self.headers)
        result = r.json()
        self.assertEqual(result['code'], 20050, msg='not any related videos')


if __name__ == '__main__':
    unittest.main()

