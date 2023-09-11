import unittest
import requests
import time

from businessCommon import apiRe
from businessCommon.clearGroup import clear_groups
from businessCommon.clearNotes import clear_notes
from businessCommon.createGroup import generate_groups
from common.checkCommon import CheckTools
from parameterized import parameterized
from common.ymlOperation import ReadYaml
from common.caseLogMethod import class_case_log, info, error, warn, step
from businessCommon.apiRe import ApiRe
import json

"""
学习点：
ApiRe   封装 url、 headers、 body 、 res code 、res body 在apiRe文件中
data包 api.yml封装所有的接口
"""


@class_case_log
class getGroupLevel1(unittest.TestCase):
    envConfig = ReadYaml.env_yaml()  # 通过yaml文件读取环境配置项 config.yaml
    print(envConfig)
    apiConfig = ReadYaml().api_yaml('api.yml')
    path = apiConfig['NoteSvrSetNoteInfo']['path']
    must_key = apiConfig['deleteGroup']['must_key']
    host = envConfig['host']
    user_id = envConfig['user_id']
    sid = envConfig['sid']
    apiRe = ApiRe()

    deleteGroupPath = apiConfig['deleteGroup']['path']
    delete_group_url = host + deleteGroupPath

    getNoteGroupPath = apiConfig['getNoteGroup']['path']
    get_note_group_url = host + getNoteGroupPath

    def setUp(self) -> None:
        step('初始化清空用户下面分组数据')
        clear_groups(self.user_id, self.sid)

    def testCase01_major(self):
        """删除分组"""
        info('STEP:创建用户1的分组数据')
        user1_group_id = generate_groups(num=1, sid=self.sid, user_id=self.user_id)
        # 下面的noteid从接口1返回取出来
        group_id = user1_group_id[0]  # 1693318482398_groupId

        info("删除分组")
        #  1、接口请求体
        body = {
            'groupId': group_id
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.delete_group_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int}
        CheckTools().check_output(expect_output, res.json())

        """获取分组列表"""
        info('STEP:获取分组列表')
        #  1、接口请求体
        body = {
            'lastRequestTime': 0,
            'excludeInValid': 'true'
        }
        res = self.apiRe.note_post(self.get_note_group_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(200, res.status_code)  # 接口是否返回200
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        self.assertEqual(0, len(res.json()['noteGroups']))