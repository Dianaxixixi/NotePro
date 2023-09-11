import unittest
from businessCommon.apiRe import ApiRe

apiRe = ApiRe()


def clear_notes(user_id, sid):
    # 获取这个用户下的所有便签数据
    start_index = 0
    userid = user_id
    rows = 999

    get_userid_url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/home/startindex/{str(start_index)}/rows/{str(rows)}/notes'
    res = apiRe.note_get_path(get_userid_url, user_id, sid)
    note_ids = []
    for item in res.json()['webNotes']:
        note_id = item['noteId']
        note_ids.append(note_id)
    print(note_ids)
    print(len(note_ids))

    if len(note_ids) == 0:
        return

    # 删除所有的便签数据
    for note_id in note_ids:
        delete_url = 'http://note-api.wps.cn/v3/notesvr/delete'
        body = {
            'noteId': note_id
        }

        apiRe.note_post(url=delete_url, user_id=user_id, sid=sid, body=body)

    # 获取回收站所有便签数据
    get_recyclebin_url = f'https://note-api.wps.cn/v3/notesvr/user/{str(userid)}/invalid/startindex/0/rows/999/notes'
    res = apiRe.note_get_path(url=get_recyclebin_url, user_id=user_id, sid=sid)
    note_ids = []
    for item in res.json()['webNotes']:
        note_id = item['noteId']
        note_ids.append(note_id)
    print(note_ids)
    print(len(note_ids))

    # 删除回收站便签数据
    delete_recyclebin_url = 'http://note-api.wps.cn/v3/notesvr/cleanrecyclebin'
    body = {
        'noteIds': note_ids
        }

    apiRe.note_post(url=delete_recyclebin_url, user_id=user_id, sid=sid, body=body)


if __name__ == '__main__':
    clear_notes(229478081, 'V02SkIJL_aWyToRT_5-ELMLvcJ1PC9c00a9f842c000dad8ec1')
