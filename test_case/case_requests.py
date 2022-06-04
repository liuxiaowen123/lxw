"""
封装request方法
"""
import json
import requests


class Request:

    @staticmethod
    def post_request(request_url, data):
        '''
        post 请求
        '''
        try:
            response = requests.post(request_url, data)
        except Exception as e:
            print(e)
            response = ''

        # 响应时间，单位为秒
        time_consume = response.elapsed.total_seconds()
        res = response.content
        res_dict = json.loads(res)
        res_dict['time_consume'] = time_consume

        return res_dict
