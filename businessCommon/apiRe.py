import requests
from common.caseLogMethod import info
import json


class ApiRe:
    @staticmethod
    def note_post(url, user_id, sid, body, new_headers=None):
        if new_headers is not None:
            headers = new_headers
        else:
            headers = {
                'Content-Type': 'application/json',
                'X-user-key': str(user_id),
                'Cookie': f'wps_sid={sid}'
            }

        info(f'url: {url}')
        info(f'headers: {json.dumps(headers)}')
        info(f'body: {json.dumps(body)}')
        res = requests.post(url=url, headers=headers, json=body)
        info(f'res code: {res.status_code}')
        info(f'res body: {res.text}')
        return res

    @staticmethod
    def note_patch(url, user_id, sid, body, new_headers=None):
        if new_headers is not None:
            headers = new_headers
        else:
            headers = {
                'Content-Type': 'application/json',
                'X-user-key': str(user_id),
                'Cookie': f'wps_sid={sid}'
            }

        info(f'url: {url}')
        info(f'headers: {json.dumps(headers)}')
        info(f'body: {json.dumps(body)}')
        res = requests.patch(url=url, headers=headers, json=body)
        info(f'res code: {res.status_code}')
        info(f'res body: {res.text}')
        return res

    @staticmethod
    def note_get_path(url, user_id, sid):
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': str(user_id),
            'Cookie': f'wps_sid={sid}'
        }
        info(f'url: {url}')
        info(f'headers: {json.dumps(headers)}')
        res = requests.get(url=url, headers=headers)
        info(f'res code: {res.status_code}')
        info(f'res body: {res.text}')
        return res
