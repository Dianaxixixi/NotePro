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
class getRecyclebinLevel1(unittest.TestCase):
    envConfig = ReadYaml.env_yaml()  # 通过yaml文件读取环境配置项 config.yaml
    print(envConfig)
    apiConfig = ReadYaml().api_yaml('api.yml')
    path = apiConfig['NoteSvrSetNoteInfo']['path']
    must_key = apiConfig['cleanRecyclebin']['must_key']
    host = envConfig['host']
    url = host + path
    user_id = envConfig['user_id']
    sid = envConfig['sid']
    apiRe = ApiRe()

    cleanRecyclebinPath = apiConfig['cleanRecyclebin']['path']
    clean_Recyclebin_url = host + cleanRecyclebinPath

    @parameterized.expand(must_key)
    def testCase02_input_must_key(self, dic):
        """删除/清空回收站便签"""
        info('STEP:删除/清空回收站便签')
        print(f'必填项校验的字段{dic}')
        body = {
            'noteIds': ['-1']
        }
        body.pop(dic['key'])
        res = self.apiRe.note_post(self.clean_Recyclebin_url, self.user_id, self.sid, body)
        self.assertEqual(dic['code'], res.status_code)  # 接口是否返回500
        expect_output = {'errorCode': -7, 'errorMsg': '参数不合法！'}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_empty_str_noteIds(self):
        """入参校验，校验入参noteIds为空字符 """
        info("STEP:获取便签内容")
        #  1、接口请求体
        noteIds = ''
        body = {
            'noteIds': noteIds
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.clean_Recyclebin_url, self.user_id, self.sid, body)

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
        res = self.apiRe.note_post(self.clean_Recyclebin_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'noteBodies': list}
        CheckTools().check_output(expect_output, res.json())
