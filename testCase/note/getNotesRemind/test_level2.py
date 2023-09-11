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
class getNoteLevel2(unittest.TestCase):
    envConfig = ReadYaml.env_yaml()  # 通过yaml文件读取环境配置项 config.yaml
    print(envConfig)
    apiConfig = ReadYaml().api_yaml('api.yml')
    path = apiConfig['NoteSvrSetNoteInfo']['path']
    must_key = apiConfig['getNotesRemind']['must_key']
    host = envConfig['host']
    url = host + path
    user_id = envConfig['user_id']
    sid = envConfig['sid']
    apiRe = ApiRe()

    getNotesRemindPath = apiConfig['getNotesRemind']['path']
    get_notes_remind_url = host + getNotesRemindPath

    @parameterized.expand(must_key)
    def testCase02_input_must_key(self, dic):
        """查看日历下便签"""
        info("STEP:查看日历下便签 必填项校验")
        print(f'必填项校验的字段{dic}')
        #  1、接口请求体
        body = {
            'remindStartTime': 1693497600000,
            'remindEndTime': 1696089600000,
            'startIndex': 0,
            'rows': 300,
            "month": '2023/09'
        }
        body.pop(dic['key'])
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.get_notes_remind_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(dic['code'], res.status_code)  # 接口是否返回500
        expect_output = {'responseTime': int, 'webNotes': list}
        CheckTools().check_output(expect_output, res.json())
