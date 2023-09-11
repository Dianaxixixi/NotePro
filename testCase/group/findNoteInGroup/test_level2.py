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
    must_key = apiConfig['findNoteInGroup']['must_key']
    host = envConfig['host']
    user_id = envConfig['user_id']
    sid = envConfig['sid']
    apiRe = ApiRe()

    findNoteInGroupPath = apiConfig['findNoteInGroup']['path']
    find_note_in_group_url = host + findNoteInGroupPath

    @parameterized.expand(must_key)
    def testCase02_input_must_key(self, dic):
        """查看分组下便签 必填项校验"""
        print(f'必填项校验的字段{dic}')
        info("STEP:查看分组下便签")
        #  1、接口请求体
        body = {
            'groupId': '6f60c97323aa8edb576758aff8c8362a'
        }
        body.pop(dic['key'])
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.find_note_in_group_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(dic['code'], res.status_code)  # 接口是否返回500
        expect_output = {'responseTime': int, 'webNotes': list}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_empty_str_groupId(self):
        """入参校验，校验入参noteId为空字符 """
        info("STEP:查看分组下便签")
        #  1、接口请求体
        groupId = ''
        body = {
            'groupId': groupId
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.find_note_in_group_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(500, res.status_code)  # 接口是否返回500
        expect_output = {'errorCode': -7, 'errorMsg': "参数不合法！"}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_int_noteId(self):
        """入参校验，校验入参noteId为int类型 """
        info("STEP:新增分组")
        #  1、接口请求体
        groupId = int(time.time() * 1000)
        body = {
            'groupId': groupId
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.find_note_in_group_url, self.user_id, self.sid, body)
        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'updateTime': int}
        CheckTools().check_output(expect_output, res.json())