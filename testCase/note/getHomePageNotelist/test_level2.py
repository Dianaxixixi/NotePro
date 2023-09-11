import unittest
import requests
import time

from businessCommon import apiRe
from common.checkCommon import CheckTools
from parameterized import parameterized
from common.ymlOperation import ReadYaml
from common.caseLogMethod import class_case_log, info, error, warn, step
from businessCommon.apiRe import ApiRe
import json
from businessCommon.createNotes import generate_notes
from businessCommon.clearNotes import clear_notes


@class_case_log
class getNoteLevel1(unittest.TestCase):
    """便签一级用例"""
    envConfig = ReadYaml.env_yaml()  # 通过yaml文件读取环境配置项 config.yaml
    print(envConfig)
    apiConfig = ReadYaml().api_yaml('api.yml')
    must_key = apiConfig['NoteSvrSetNoteInfo']['must_key']
    user_id = envConfig['user_id']
    sid = envConfig['sid']
    user_id2 = envConfig['user_id2']
    sid2 = envConfig['sid2']
    apiRe = ApiRe()

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
        url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
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
        url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
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
        url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
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
        url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
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
        url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
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
        url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
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
        url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
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
        url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
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
        url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
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
        url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
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
        url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
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
        url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
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
        url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
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
        url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'webNotes': list}
        CheckTools().check_output(expect_output, res.json())

    def testCase01_handles(self):
        """用户存在不同的用户便签数据，创建1条便签数据"""
        step("创建用户1的便签数据")
        user1_note_id = generate_notes(num=1, sid=self.sid, user_id=self.user_id)
        # step("创建用户2的便签数据")
        # user2_note_id = generate_notes(num=1, sid=self.sid2, user_id=self.user_id2)
        step("获取首页便签数据")
        start_index = 0
        userid = self.user_id
        rows = 50
        get_userid_url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(get_userid_url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        self.assertEqual(1, len(res.json()['webNotes']))
        self.assertEqual(user1_note_id[0], res.json()['webNotes'][0]['noteId'])

    def testCase02_handles(self):
        """用户存在不同的用户便签数据，创建2条便签数据"""
        step("创建用户1的便签数据")
        user1_note_id = generate_notes(num=2, sid=self.sid, user_id=self.user_id)
        # step("创建用户2的便签数据")
        # user2_note_id = generate_notes(num=1, sid=self.sid2, user_id=self.user_id2)
        step("获取首页便签数据")
        start_index = 0
        userid = self.user_id
        rows = 50
        get_userid_url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(get_userid_url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        self.assertEqual(2, len(res.json()['webNotes']))

    def testCase03_handles(self):
        """越权场景校验，用户1查询用户2的便签数据"""
        # step("创建用户1的便签数据")
        # user1_note_id = generate_notes(num=1, sid=self.sid, user_id=self.user_id)
        step("创建用户2的便签数据")
        user2_note_id = generate_notes(num=1, sid=self.sid2, user_id=self.user_id2)
        step("获取首页便签数据")
        start_index = 0
        userid = self.user_id2
        rows = 50
        get_userid_url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(get_userid_url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(412, res.status_code)  # 校验状态码返回200
        expect_output = {'errorCode': -1011, 'errorMsg': 'user change!'}
        CheckTools().check_output(expect_output, res.json())

