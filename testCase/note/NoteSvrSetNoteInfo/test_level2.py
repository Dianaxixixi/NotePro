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
    """便签一级用例"""
    envConfig = ReadYaml.env_yaml()  # 通过yaml文件读取环境配置项 config.yaml
    print(envConfig)
    apiConfig = ReadYaml().api_yaml('api.yml')
    path = apiConfig['NoteSvrSetNoteInfo']['path']
    must_key = apiConfig['NoteSvrSetNoteInfo']['must_key']
    path = '/v3/notesvr/set/noteinfo'
    host = envConfig['host']
    url = host + path
    user_id = envConfig['user_id']
    sid = envConfig['sid']
    apiRe = ApiRe()

    @parameterized.expand(must_key)
    def testCase01_major_must_key(self, dic):
        """上传/更新便签信息主体" 必填性校验 """
        print(f'必填项校验的字段{dic}')
        info("STEP:上传/更新便签信息主体")
        #  1、接口请求体
        note_id = str(int(time.time() * 1000)) + '_test_noteId'
        body = {
            'noteId': note_id
        }
        body.pop(dic['key'])
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(dic['code'], res.status_code)  # 接口是否返回500
        expect_output = {'errorCode': -7, 'errorMsg': "参数不合法！"}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_empty_str_noteId(self):
        """入参校验，校验入参为空字符 """
        print(f'校验入参noteId 为空')
        info("STEP:上传/更新便签信息主体")
        #  1、接口请求体
        note_id = ''
        body = {
            'noteId': note_id
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(500, res.status_code)  # 接口是否返回500
        expect_output = {'errorCode': -7, 'errorMsg': "参数不合法！"}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_special_str_noteId(self):
        """入参校验，校验入参noteId为特殊字符串 """
        print(f'校验入参noteId 为空')
        info("STEP:上传/更新便签信息主体")
        #  1、接口请求体
        note_id = '@###JJHJJ'
        body = {
            'noteId': note_id
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'infoVersion': int, 'infoUpdateTime': int}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_int_noteId(self):
        """入参校验，校验入参noteId为特殊字符串 """
        print(f'校验入参noteId 为空')
        info("STEP:上传/更新便签信息主体")
        #  1、接口请求体
        note_id = 233323
        body = {
            'noteId': note_id
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'infoVersion': int, 'infoUpdateTime': int}
        CheckTools().check_output(expect_output, res.json())