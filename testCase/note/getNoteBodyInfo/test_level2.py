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
class getNoteLevel1(unittest.TestCase):
    envConfig = ReadYaml.env_yaml()  # 通过yaml文件读取环境配置项 config.yaml
    print(envConfig)
    apiConfig = ReadYaml().api_yaml('api.yml')
    must_key = apiConfig['getNoteBodyInfo']['must_key']
    path = '/v3/notesvr/set/noteinfo'
    host = envConfig['host']
    url = host + path
    user_id = envConfig['user_id']
    sid = envConfig['sid']
    apiRe = ApiRe()
    getNoteBodyInfopath = apiConfig['getNoteBodyInfo']['path']
    get_note_body_info_url = host + getNoteBodyInfopath

    @parameterized.expand(must_key)
    def testCase02_input_must_key(self, dic):
        """获取便签内容 必填项校验"""
        print(f'必填项校验的字段{dic}')
        info("STEP:获取便签内容")
        #  1、接口请求体
        body = {
            'noteIds': ['1693477063044_test_noteId', '1693476864368_test_noteId']
        }
        body.pop(dic['key'])
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.get_note_body_info_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(dic['code'], res.status_code)  # 接口是否返回500
        expect_output = {'errorCode': -7, 'errorMsg': "参数不合法！"}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_empty_str_noteId(self):
        """入参校验，校验入参noteId为空字符 """
        info("STEP:获取便签内容")
        #  1、接口请求体
        noteIds = ''
        body = {
            'noteIds': noteIds
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.get_note_body_info_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(500, res.status_code)  # 校验状态码返回200
        expect_output = {'errorCode': -7, 'errorMsg': str}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_int_noteId(self):
        """入参校验，校验入参noteId为int类型 """
        info("STEP:获取便签内容")
        #  1、接口请求体
        noteIds = [1, 2]
        body = {
            'noteIds': noteIds
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.get_note_body_info_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'noteBodies': list}
        CheckTools().check_output(expect_output, res.json())
