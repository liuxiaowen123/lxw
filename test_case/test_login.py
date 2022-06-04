"""
执行测试用例
"""
import os
import pytest
from test_case.yaml_util import YamlUtil
from test_case.case_requests import Request
from test_case.case_assert import Assertions


@pytest.fixture(scope="session")
def open():
    # 会话前置操作setup
    print("===打开浏览器===")
    test = "测试变量是否返回"
    yield test
    # 会话后置操作teardown
    print("==关闭浏览器==")


class Test_login:

    # 读取yaml文件
    @pytest.mark.parametrize('args', YamlUtil('test_login.yaml').read_yaml())
    # @pytest.mark.xfail(raises=AssertionError)
    def test_login(self, args, open):
        url = args['request']['url']
        params = args['request']['param']
        response = Request.post_request(url, params)
        print('响应结果:')
        print(response)

        # with pytest.raises(AssertionError):
        #     # 断言状态码
        #     Assertions.assert_status_code(response['ret'], args['returns']['code'])

        Assertions.assert_status_code(response['ret'], args['returns']['code'])


if __name__ == '__main__':
    pytest.main(['test_login.py'])
    os.system('allure generate ../temp -o ../report --clean')
