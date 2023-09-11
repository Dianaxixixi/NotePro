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
from businessCommon.createNotes import generate_notes


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

    def testCase01_major(self):
        # 方法一
        info("STEP:获取首页便签数据")
        userid = self.user_id
        start_index = 0
        rows = 50

        #  1、接口请求体
        url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int, 'webNotes': list}
        CheckTools().check_output(expect_output, res.json())

    # 方法二 最原始的方法
    #     """获取首页便签列表"""
    #     info("STEP:获取首页便签列表")
    #     #  1、接口请求体
    #     userid = 229478081
    #     start_index = 0
    #     rows = 50
    #     url = f'http://note-api.wps.cn/notesvr/v2/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
    #     headers = {
    #         'Content-Type': 'application/json',
    #         'X-user-key': '229478081',
    #         'Cookie': 'wps_sid=V02SkIJL_aWyToRT_5-ELMLvcJ1PC9c00a9f842c000dad8ec1'
    #     }
    #
    #     res = requests.get(url=url, headers=headers)
    #     # 2、断言
    #     self.assertEqual(200, res.status_code)  # 校验状态码返回200
    #     expect_output = {'responseTime': int, 'webNotes': list}
    #     CheckTools().check_output(expect_output, res.json())
    #     print(res.json())
