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
class getRecyclebinLevel1(unittest.TestCase):
    envConfig = ReadYaml.env_yaml()  # 通过yaml文件读取环境配置项 config.yaml
    print(envConfig)
    apiConfig = ReadYaml().api_yaml('api.yml')
    path = apiConfig['NoteSvrSetNoteInfo']['path']
    must_key = apiConfig['restoreRecyclebinNote']['must_key']
    host = envConfig['host']
    url = host + path
    user_id = envConfig['user_id']
    sid = envConfig['sid']
    apiRe = ApiRe()

    restoreRecyclebinNotePath = apiConfig['restoreRecyclebinNote']['path']
    restore_recyclebin_note_url = host + restoreRecyclebinNotePath

    cleanRecyclebinPath = apiConfig['cleanRecyclebin']['path']
    clean_Recyclebin_url = host + cleanRecyclebinPath

    deleteNotePath = apiConfig['deleteNote']['path']
    delete_note_url = host + deleteNotePath

    def setUp(self) -> None:
        step('初始化清空用户便签数据')
        clear_notes(self.user_id, self.sid)

    def testCase01_major(self):
        """恢复回收站的便签"""
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

        info("STEP:查看回收站下便签列表")
        userid = self.user_id
        start_index = 0
        rows = 50
        #  1、接口请求体
        url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/invalid/startindex/{str(start_index)}/rows/{str(rows)}/notes'
        res = self.apiRe.note_get_path(url, self.user_id, self.sid)

        note_ids = []
        for item in res.json()['webNotes']:
            note_id = item['noteId']
            note_ids.append(note_id)
        print(note_ids)
        print(len(note_ids))

        if len(note_ids) == 0:
            return

        info('STEP:删除/清空回收站便签')
        # body = {
        #     'noteIds': ['-1']
        # }

        body = {
            'noteIds': note_ids
        }

        res = self.apiRe.note_post(self.clean_Recyclebin_url, self.user_id, self.sid, body)
        self.assertEqual(200, res.status_code)  # 接口是否返回200
        expect_output = {'responseTime': int}
        CheckTools().check_output(expect_output, res.json())

        info("STEP:恢复回收站的便签")
        #  1、接口请求体
        body = {
            'userId': self.user_id,
            'noteIds': note_ids
        }
        # 请求体 包含了 url、 user_id、 sid、 请求的body
        res = self.apiRe.note_patch(self.restore_recyclebin_note_url, self.user_id, self.sid, body)

        # 2、断言
        self.assertEqual(200, res.status_code)  # 校验状态码返回200
        # expect_output = {'responseTime': int, 'infoVersion': int, 'infoUpdateTime': int}
        # CheckTools().check_output(expect_output, res.json())

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