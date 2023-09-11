# 7.批量生成便签的函数  形参定义 num、sid、user_id   return noteids
import requests
import time
from common.checkCommon import CheckTools


def generate_groups(num, sid, user_id):
    group_ids = []
    if num <= 0:
        return
    for i in range(num):
        # 新增分组
        url = 'http://note-api.wps.cn' + '/v3/notesvr/set/notegroup'  # 新增分组url
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': user_id,
            'cookie': 'wps_sid=' + sid
        }
        group_id = str(int(time.time() * 1000)) + '_group_id' + str(i)
        group_name = str(int(time.time() * 1000)) + '_groupName'
        group_ids.append(group_id)  # 把group_ids加入列表
        body = {
            'groupId': group_id,
            'groupName': group_name,
            'order': 0
        }

        res = requests.post(url=url, headers=headers, json=body)
        assert (200, res.status_code)
    return group_ids


if __name__ == '__main__':
    aa = generate_groups(1, 'V02SkIJL_aWyToRT_5-ELMLvcJ1PC9c00a9f842c000dad8ec1', '229478081')
    print(aa)
