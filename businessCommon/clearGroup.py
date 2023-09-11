import unittest
from businessCommon.apiRe import ApiRe

apiRe = ApiRe()


def clear_groups(user_id, sid):
    # 获取这个用户下的所有分组数据

    get_userid_url = f'https://note-api.wps.cn/v3/notesvr/get/notegroup'
    body = {
        'lastRequestTime': 0,
        'excludeInValid': 'true'
    }

    res = apiRe.note_post(get_userid_url, user_id, sid, body)
    print(res.json())
    group_ids = []
    for item in res.json()['noteGroups']:
        group_id = item['groupId']
        group_ids.append(group_id)
    print(group_ids)
    print(len(group_ids))

    if len(group_ids) == 0:
        return

    # 删除所有的分组数据
    for group_id in group_ids:
        delete_url = 'http://note-api.wps.cn/v3/notesvr/delete/notegroup'
        body = {
            'groupId': group_id
        }
        apiRe.note_post(url=delete_url, user_id=user_id, sid=sid, body=body)


if __name__ == '__main__':
    clear_groups(229478081, 'V02SkIJL_aWyToRT_5-ELMLvcJ1PC9c00a9f842c000dad8ec1')
