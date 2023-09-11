import unittest
import requests
import time

from businessCommon import apiRe
from businessCommon.clearNotes import clear_notes
from common.checkCommon import CheckTools
from parameterized import parameterized
from common.ymlOperation import ReadYaml
from common.caseLogMethod import class_case_log, info, error, warn, step
from businessCommon.apiRe import ApiRe
import json


@class_case_log
class getRecyclebinLevel1(unittest.TestCase):
    envConfig = ReadYaml.env_yaml()  # 通过yaml文件读取环境配置项 config.yaml
    print(envConfig)
    apiConfig = ReadYaml().api_yaml('api.yml')
    path = apiConfig['NoteSvrSetNoteInfo']['path']
    must_key = apiConfig['NoteSvrSetNoteInfo']['must_key']
    host = envConfig['host']
    url = host + path
    user_id = envConfig['user_id']
    sid = envConfig['sid']
    apiRe = ApiRe()

    findRecyclebinListPath = apiConfig['findRecyclebinList']['path']
    find_recyclebin_list_url = host + findRecyclebinListPath
    print(find_recyclebin_list_url)

    def setUp(self) -> None:
        step('初始化清空用户便签数据')
        clear_notes(self.user_id, self.sid)

    def testCase02_input_empty_userid(self):
        """入参校验，校验入参userid为空字符串"""
        info("STEP:获取首页便签数据")
        userid = ''
        start_index = 0
        rows = 50

        #  1、接口请求体
        #  1、接口请求体
        url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/invalid/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(404, res.status_code)  # 校验状态码返回200
        expect_output = {'timestamp': str, 'status': 404, 'error': 'Not Found', 'message': 'No message available',
                         'path': str}
        CheckTools().check_output(expect_output, res.json())
        print(res.json())

    def testCase02_input_str_userid(self):
        """入参校验，校验入参userid为字符串形式的数值"""
        info("STEP:获取首页便签数据")
        userid = 'test'
        start_index = 0
        rows = 50

        #  1、接口请求体
        #  1、接口请求体
        url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/invalid/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(500, res.status_code)  # 校验状态码返回200
        expect_output = {'errorCode': -7, 'errorMsg': '参数类型错误！'}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_decimal_userid(self):
        """入参校验，校验入参userid为小数值"""
        info("STEP:获取首页便签数据")
        userid = 1.5
        start_index = 0
        rows = 50

        #  1、接口请求体
        url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/invalid/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(500, res.status_code)  # 校验状态码返回200
        expect_output = {'errorCode': -7, 'errorMsg': '参数类型错误！'}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_0_userid(self):
        """入参校验，校验入参userid为数值0"""
        info("STEP:获取首页便签数据")
        userid = 0
        start_index = 0
        rows = 50

        #  1、接口请求体
        url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/invalid/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'webNotes': list}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_minusOne_userid(self):
        """入参校验，校验入参userid为数值-1"""
        info("STEP:获取首页便签数据")
        userid = -1
        start_index = 0
        rows = 50

        #  1、接口请求体
        url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/invalid/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(412, res.status_code)  # 校验状态码返回200
        expect_output = {'errorCode': -1011, 'errorMsg': 'user change!'}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_empty_startIndex(self):
        """入参校验，校验入参startIndex为空字符串"""
        info("STEP:获取首页便签数据")
        userid = 229478081
        start_index = ''
        rows = 0

        #  1、接口请求体
        url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/invalid/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(404, res.status_code)  # 校验状态码返回200
        expect_output = {'timestamp': str, 'status': 404, 'error': 'Not Found', 'message': 'No message available',
                         'path': str}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_str_startIndex(self):
        """入参校验，校验入参startIndex为字符串形式的数值"""
        info("STEP:获取首页便签数据")
        userid = self.user_id
        start_index = 'test'
        rows = 50

        #  1、接口请求体
        url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/invalid/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(500, res.status_code)  # 校验状态码返回200
        expect_output = {'errorCode': -7, 'errorMsg': '参数类型错误！'}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_decimal_startIndex(self):
        """入参校验，校验入参startIndex为小数值"""
        info("STEP:获取首页便签数据")
        userid = self.user_id
        start_index = 1.5
        rows = 50

        #  1、接口请求体
        url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/invalid/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(500, res.status_code)  # 校验状态码返回200
        expect_output = {'errorCode': -7, 'errorMsg': '参数类型错误！'}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_minusOne_startIndex(self):
        """入参校验，校验入参startIndex为数值-1"""
        info("STEP:获取首页便签数据")
        userid = self.user_id
        start_index = -100
        rows = 50

        #  1、接口请求体
        url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/invalid/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'webNotes': list}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_empty_rows(self):
        """入参校验，校验入参rows为空字符串"""
        info("STEP:获取首页便签数据")
        userid = 229478081
        start_index = 0
        rows = ''

        #  1、接口请求体
        url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/invalid/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(404, res.status_code)  # 校验状态码返回200
        expect_output = {'timestamp': str, 'status': 404, 'error': 'Not Found', 'message': 'No message available',
                         'path': str}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_str_rows(self):
        """入参校验，校验入参rows为字符串形式的数值"""
        info("STEP:获取首页便签数据")
        userid = 229478081
        start_index = 0
        rows = 'test'

        #  1、接口请求体
        url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/invalid/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(500, res.status_code)  # 校验状态码返回200
        expect_output = {'errorCode': -7, 'errorMsg': '参数类型错误！'}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_decimal_userid(self):
        """入参校验，校验入参rows为字小数值"""
        info("STEP:获取首页便签数据")
        userid = 229478081
        start_index = 0
        rows = 1.5

        #  1、接口请求体
        url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/invalid/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(500, res.status_code)  # 校验状态码返回200
        expect_output = {'errorCode': -7, 'errorMsg': '参数类型错误！'}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_0_rows(self):
        """入参校验，校验入参rows为0"""
        info("STEP:获取首页便签数据")
        userid = 229478081
        start_index = 0
        rows = 0

        #  1、接口请求体
        url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/invalid/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'webNotes': list}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_minusOne_rows(self):
        """入参校验，校验入参rows为-1"""
        info("STEP:获取首页便签数据")
        userid = 229478081
        start_index = 0
        rows = -2

        #  1、接口请求体
        url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/invalid/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'webNotes': list}
        CheckTools().check_output(expect_output, res.json())

    