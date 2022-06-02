import pytest
import requests
from test_case.yaml_util import YamlUtil


class TestApi:
    @pytest.mark.parametrize('args', YamlUtil('test_api.yaml').read_yaml())
    def test_01(self, args):
        url = args['request']['url']
        headers = args['request']['headers']
        params = args['request']['params']
        res = requests.get(url,headers=headers,params=params)
        print(res.text)


if __name__ == '__main__':
    pytest.main(['test_api.py'])