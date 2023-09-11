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

参数化必填校验：
1、data/api.yml 可以配置必填校验 
2、然后通过must_key = apiConfig['NoteSvrSetNoteContent']['must_key'] 获取
3、添加装饰器取到值：
parameterized.expand(must_key)
def testCase02_input_must_key(self, dic):
print(f'必填项校验的字段{dic}')
body.pop(dic['key'])
self.assertEqual(dic['code'], get_note_content_res.status_code)  # 接口是否返回500

另外一种方式：
1、类的最前面写：
must_key = ('noteId', 'title', 'summary', 'body')
must_key1 = ([{'key': 'noteId', 'code': 500}], [{'key': 'summary', 'code': 500}])
2、然后添加装饰器取到值：
parameterized.expand(must_key)
"""


@class_case_log
class getNoteLevel1(unittest.TestCase):
    must_key = ('noteId', 'title', 'summary', 'body')
    must_key1 = ([{'key': 'noteId', 'code': 500}], [{'key': 'summary', 'code': 500}])

    """
        参数化最多只能处理2个变量，比方说必填项的校验，他们的期望值是一致的，超过2个变量代码可读性会降低
    """

    envConfig = ReadYaml.env_yaml()  # 通过yaml文件读取环境配置项 config.yaml
    print(envConfig)
    apiConfig = ReadYaml().api_yaml('api.yml')
    path = apiConfig['NoteSvrSetNoteInfo']['path']
    must_key = apiConfig['NoteSvrSetNoteContent']['must_key']
    path = '/v3/notesvr/set/noteinfo'
    host = envConfig['host']
    url = host + path
    user_id = envConfig['user_id']
    sid = envConfig['sid']
    apiRe = ApiRe()
    setNoteContentPath = apiConfig['NoteSvrSetNoteContent']['path']
    get_note_content_url = host + setNoteContentPath

    # @parameterized.expand(must_key)
    # def testCase02_input_must_key(self, key):
    #     """上传/更新便签内容 必填性校验 """
    #     print(f'必填项校验的字段{key}')
    #     info("STEP:上传/更新便签信息主体")
    #     #  1、接口请求体
    #     note_id = str(int(time.time() * 1000)) + '_test_noteId'
    #     body = {
    #         'noteId': note_id
    #     }
    #     # 请求体 包含了 url、 user_id、 sid、 请求的body
    #     res = self.apiRe.note_post(self.url, self.user_id, self.sid, body)
    #
    #     # 2、断言
    #     infoVersion = res.json()['infoVersion']
    #     self.assertEqual(200, res.status_code)  # 校验状态码返回200
    #     expect_output = {'responseTime': int, 'infoVersion': int, 'infoUpdateTime': int}
    #     CheckTools().check_output(expect_output, res.json())
    #
    #     info('STEP:上传/更新便签内容')
    #     body = {
    #         'noteId': note_id,
    #         'title': 'test_title',
    #         'summary': 'test_summary',
    #         'body': 'test_body',
    #         'localContentVersion': infoVersion,
    #         'BodyType': 0
    #     }
    #     body.pop(key)
    #     get_note_content_res = self.apiRe.note_post(self.get_note_content_url, self.user_id, self.sid, body)
    #     self.assertEqual(200, get_note_content_res.status_code)  # 接口是否返回200
    #     expect_output = {'responseTime': int, 'contentVersion': int, 'contentUpdateTime': int}
    #     CheckTools().check_output(expect_output, get_note_content_res.json())

    @parameterized.expand(must_key)
    def testCase02_input_must_key(self, dic):
        """上传/更新便签内容 必填性校验 """
        print(f'必填项校验的字段{dic}')
        info("STEP:上传/更新便签信息主体")
        #  1、接口请求体
        note_id = str(int(time.time() * 1000)) + '_test_noteId'
        body = {
            'noteId': note_id
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.url, self.user_id, self.sid, body)

        # 2、断言
        infoVersion = res.json()['infoVersion']
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'infoVersion': int, 'infoUpdateTime': int}
        CheckTools().check_output(expect_output, res.json())

        info('STEP:上传/更新便签内容')
        body = {
            'noteId': note_id,
            'title': 'test_title',
            'summary': 'test_summary',
            'body': 'test_body',
            'localContentVersion': infoVersion,
            'BodyType': 0
        }
        body.pop(dic['key'])
        res = self.apiRe.note_post(self.get_note_content_url, self.user_id, self.sid, body)
        self.assertEqual(dic['code'], res.status_code)  # 接口是否返回500
        # expect_output = {'responseTime': int, 'contentVersion': int, 'contentUpdateTime': int}
        # CheckTools().check_output(expect_output, get_note_content_res.json())

    def testCase02_input_empty_str_noteId(self):
        """入参校验，校验入参noteId为空字符 """
        info("STEP:上传/更新便签信息主体")
        #  1、接口请求体
        note_id = str(int(time.time() * 1000)) + '_test_noteId'
        body = {
            'noteId': note_id
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.url, self.user_id, self.sid, body)

        # 2、断言
        infoVersion = res.json()['infoVersion']
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'infoVersion': int, 'infoUpdateTime': int}
        CheckTools().check_output(expect_output, res.json())

        info('STEP:上传/更新便签内容')
        body = {
            'noteId': '',
            'title': 'test_title',
            'summary': 'test_summary',
            'body': 'test_body',
            'localContentVersion': infoVersion,
            'BodyType': 0
        }
        res = self.apiRe.note_post(self.get_note_content_url, self.user_id, self.sid, body)
        # 2、断言
        self.assertEqual(500, res.status_code)  # 接口是否返回500
        expect_output = {'errorCode': -7, 'errorMsg': "参数不合法！"}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_special_str_noteId(self):
        """入参校验，校验入参noteId为特殊字符串 """
        info("STEP:上传/更新便签信息主体")
        #  1、接口请求体
        note_id = str(int(time.time() * 1000)) + '_test_noteId'
        body = {
            'noteId': '#@#@@##'
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.url, self.user_id, self.sid, body)

        # 2、断言
        infoVersion = res.json()['infoVersion']
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'infoVersion': int, 'infoUpdateTime': int}
        CheckTools().check_output(expect_output, res.json())

        info('STEP:上传/更新便签内容')
        body = {
            'noteId': '#@#@@##',
            'title': 'test_title',
            'summary': 'test_summary',
            'body': 'test_body',
            'localContentVersion': infoVersion,
            'BodyType': 0
        }
        res = self.apiRe.note_post(self.get_note_content_url, self.user_id, self.sid, body)
        # 2、断言
        self.assertEqual(200, res.status_code)  # 接口是否返回200
        expect_output = {'responseTime': int, 'contentVersion': int, 'contentUpdateTime': int}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_int_noteId(self):
        """入参校验，校验入参noteId为int类型 """
        info("STEP:上传/更新便签信息主体")
        #  1、接口请求体
        note_id = int(time.time() * 1000)
        body = {
            'noteId': note_id
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.url, self.user_id, self.sid, body)

        # 2、断言
        infoVersion = res.json()['infoVersion']
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'infoVersion': int, 'infoUpdateTime': int}
        CheckTools().check_output(expect_output, res.json())

        info('STEP:上传/更新便签内容')
        body = {
            'noteId': note_id,
            'title': 'test_title',
            'summary': 'test_summary',
            'body': 'test_body',
            'localContentVersion': infoVersion,
            'BodyType': 0
        }
        res = self.apiRe.note_post(self.get_note_content_url, self.user_id, self.sid, body)
        # 2、断言
        self.assertEqual(200, res.status_code)  # 接口是否返回200
        expect_output = {'responseTime': int, 'contentVersion': int, 'contentUpdateTime': int}
        CheckTools().check_output(expect_output, res.json())

    def testCase02_input_empty_body(self):
        """入参校验，校验入参body为空字符 """
        info("STEP:上传/更新便签信息主体")
        #  1、接口请求体
        note_id = str(int(time.time() * 1000)) + '_test_noteId'
        body = {
            'noteId': note_id
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.url, self.user_id, self.sid, body)

        # 2、断言
        infoVersion = res.json()['infoVersion']
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'infoVersion': int, 'infoUpdateTime': int}
        CheckTools().check_output(expect_output, res.json())

        body = ''
        info('STEP:上传/更新便签内容')
        body = {
            'noteId': note_id,
            'title': 'test_title',
            'summary': 'test_summary',
            'body': body,
            'localContentVersion': infoVersion,
            'BodyType': 0
        }
        res = self.apiRe.note_post(self.get_note_content_url, self.user_id, self.sid, body)
        # 2、断言
        self.assertEqual(412, res.status_code)  # 接口是否返回500
        expect_output = {'errorCode': -1012, 'errorMsg': "Note body Requested!"}
        CheckTools().check_output(expect_output, res.json())
