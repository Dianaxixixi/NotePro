import unittest
import requests
import time

from businessCommon import apiRe
from common.checkCommon import CheckTools
from parameterized import parameterized
from common.ymlOperation import ReadYaml
from common.caseLogMethod import class_case_log, info, error, warn
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
    must_key = apiConfig['NoteSvrSetNoteInfo']['must_key']
    host = envConfig['host']
    user_id = envConfig['user_id']
    sid = envConfig['sid']
    apiRe = ApiRe()

    getNoteGroupPath = apiConfig['getNoteGroup']['path']
    get_note_group_url = host + getNoteGroupPath

    def testCase01_major(self):
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
        expect_output = {'requestTime': int, 'noteGroups': list}
        CheckTools().check_output(expect_output, res.json())
