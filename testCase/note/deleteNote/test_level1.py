import unittest
import requests
import time

from businessCommon import apiRe
from businessCommon.clearNotes import clear_notes
from businessCommon.createNotes import generate_notes
from common.checkCommon import CheckTools
from parameterized import parameterized
from common.ymlOperation import ReadYaml
from common.caseLogMethod import class_case_log, info, error, warn, step
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
    must_key = apiConfig['deleteNote']['must_key']
    path = '/v3/notesvr/set/noteinfo'
    host = envConfig['host']
    url = host + path
    user_id = envConfig['user_id']
    sid = envConfig['sid']
    apiRe = ApiRe()

    deleteNotePath = apiConfig['deleteNote']['path']
    delete_note_url = host + deleteNotePath

    def setUp(self) -> None:
        step('初始化清空用户便签数据')
        clear_notes(self.user_id, self.sid)

    def testCase01_major(self):
        """删除便签"""
        info("STEP:删除便签")

        info('创建用户1的便签数据')
        user1_note_id = generate_notes(num=1, sid=self.sid, user_id=self.user_id)
        # 下面的noteid从接口1返回取出来
        note_id = user1_note_id[0]  # 1693318482398_noteId
        info('删除便签数据')
        #  1、接口请求体
        body = {
            'noteId': note_id
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_post(self.delete_note_url, self.user_id, self.sid, body)

        # 2、断言
        #  noteId = res.json()['noteId']
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        expect_output = {'responseTime': int}
        CheckTools().check_output(expect_output, res.json())

        step("获取首页便签数据")
        start_index = 0
        userid = self.user_id
        rows = 50
        get_userid_url = f'http://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(get_userid_url, self.user_id, self.sid)
        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        self.assertEqual(0, len(res.json()['webNotes']))
