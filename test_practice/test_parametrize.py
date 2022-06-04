"""
@pytest.mark.parametrize
总结：当indirect为True的时候，参数为固件函数名称的，执行的时候会当做函数来执行。
当indirect为false的时候，参数为固件函数名称的，执行的时候会当做一个参数来执行。
"""
import pytest


@pytest.fixture()
def login(request):
    name = request.param
    print('name是：{}'.format(name))
    return name


# 如果需要传多个参数，需要通过字典去传
data = [
    {"username": "name1", "pwd": "pwd1"},
    {"username": "name2", "pwd": "pwd2"}
]


# ndirect=True 参数是为了把 login 当成一个函数去执行，而不是一个参数，并且将data当做参数传入函数
# @pytest.mark.flaky(reruns=5)
@pytest.mark.parametrize('login', data, indirect=True)
def test_name(login):
    # 这里的login是获取login函数返回的值

    print('测试用例的登录账号是：{}'.format(login['username']))
    print('测试用例的登录账号是：{}'.format(login['pwd']))


if __name__ == '__main__':
    pytest.main(['test_parametrize.py'])
