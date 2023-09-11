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


@class_case_log
class getGroupLevel1(unittest.TestCase):
    envConfig = ReadYaml.env_yaml()  # 通过yaml文件读取环境配置项 config.yaml
    print(envConfig)
    apiConfig = ReadYaml().api_yaml('api.yml')
    path = apiConfig['NoteSvrSetNoteInfo']['path']
    must_key = apiConfig['addNoteGroup']['must_key']
    host = envConfig['host']
    user_id = envConfig['user_id']
    sid = envConfig['sid']
    apiRe = ApiRe()

    addNoteGroupPath = apiConfig['addNoteGroup']['path']
    add_note_group_url = host + addNoteGroupPath

    @parameterized.expand(must_key)
    def testCase02_input_must_key(self, dic):
        """新增分组"""
        info("STEP:新增分组 必填项校验")
        print(f'必填项校验的字段{dic}')
        #  1、接口请求体
        group_id = str(int(time.time() * 1000)) + '_group_id'
        group_name = str(int(time.time() * 1000)) + '_groupName'
        body = {
            'groupId': group_id,
            'groupName': group_name,
            'order': 0
        }

        body.pop(dic['key'])
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.add_note_group_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(dic['code'], res.status_code)  # 接口是否返回500
        expect_output = {'responseTime': int, 'updateTime': int}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_empty_str_groupId(self):
        """入参校验，校验入参noteId为空字符 """
        info("STEP:新增分组")
        #  1、接口请求体
        group_id = ''
        body = {
            'groupId': group_id,
            'groupName': 'groupNameAddTest',
            'order': 0
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.add_note_group_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(500, res.status_code)  # 接口是否返回500
        expect_output = {'errorCode': -7, 'errorMsg': "参数不合法！"}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_special_str_noteId(self):
        """入参校验，校验入参noteId为特殊字符串 """
        info("STEP:新增分组")
        #  1、接口请求体
        group_id = '%%%%'
        body = {
            'groupId': group_id,
            'groupName': 'groupNameAddTest',
            'order': 0
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.add_note_group_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'updateTime': int}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_int_noteId(self):
        """入参校验，校验入参noteId为int类型 """
        info("STEP:新增分组")
        #  1、接口请求体
        group_id = int(time.time() * 1000)
        body = {
            'groupId': group_id,
            'groupName': 'groupNameAddTest',
            'order': 0
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.add_note_group_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'updateTime': int}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_empty_str_groupName(self):
        """入参校验，校验入参noteId为空字符 """
        info("STEP:新增分组")
        #  1、接口请求体
        group_id = str(int(time.time() * 1000)) + '_test_groupId'
        body = {
            'groupId': group_id,
            'groupName': '',
            'order': 0
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.add_note_group_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(500, res.status_code)  # 接口是否返回500
        expect_output = {'errorCode': -7, 'errorMsg': "参数不合法！"}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_special_str_groupName(self):
        """入参校验，校验入参noteId为特殊字符串 """
        info("STEP:新增分组")
        #  1、接口请求体
        group_id = str(int(time.time() * 1000)) + '_test_groupId'
        body = {
            'groupId': group_id,
            'groupName': '%%$$$',
            'order': 0
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.add_note_group_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'updateTime': int}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_int_noteId(self):
        """入参校验，校验入参noteId为int类型 """
        info("STEP:新增分组")
        #  1、接口请求体
        group_id = str(int(time.time() * 1000)) + '_test_groupId'
        body = {
            'groupId': group_id,
            'groupName': 123,
            'order': 0
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.add_note_group_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'updateTime': int}
        CheckTools().check_output(expect_output, res.json())
