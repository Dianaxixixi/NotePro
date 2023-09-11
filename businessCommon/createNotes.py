# 7.批量生成便签的函数  形参定义 num、sid、user_id   return noteids
import requests
import time
from common.checkCommon import CheckTools


def generate_notes(num, sid, user_id):
    note_ids = []
    if num <= 0:
        return
    for i in range(num):
        # 上传/更新便签主体
        url = 'http://note-api.wps.cn' + '/v3/notesvr/set/noteinfo'  # 上传/更新便签信息主体
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': user_id,
            'cookie': 'wps_sid=' + sid
        }

        note_id = str(int(time.time() * 1000)) + '_noteId' + str(i)
        note_ids.append(note_id)  # 把note_id加入列表
        body = {
            'noteId': note_id
        }

        res = requests.post(url=url, headers=headers, json=body)
        infoVersion = res.json()['infoVersion']
        assert (200, res.status_code)

        # 上传/更新便签内容
        get_userid_url = 'http://note-api.wps.cn' + '/v3/notesvr/set/notecontent'
        title = str(int(time.time() * 1000)) + '_title'
        summary = str(int(time.time() * 1000)) + '_summary'
        body = str(int(time.time() * 1000)) + '_body'

        body = {
            'noteId': note_id,
            'title': title,
            'summary': summary,
            'body': body,
            'localContentVersion': infoVersion,
            'BodyType': 0
        }

        get_userid_res = requests.post(url=get_userid_url, headers=headers, json=body)
        assert (200, get_userid_res.status_code)

    return note_ids


if __name__ == '__main__':
    aa = generate_notes(1, 'V02SkIJL_aWyToRT_5-ELMLvcJ1PC9c00a9f842c000dad8ec1', '229478081')
    print(aa)
