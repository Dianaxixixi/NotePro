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

    def testCase01_major(self):
        """删除/清空回收站便签"""
        info('STEP:删除/清空回收站便签')
        body = {
            'noteIds': ['-1']
        }
        res = self.apiRe.note_post(self.clean_Recyclebin_url, self.user_id, self.sid, body)
        self.assertEqual(200, res.status_code)  # 接口是否返回200
        expect_output = {'responseTime': int}
        CheckTools().check_output(expect_output, res.json())
