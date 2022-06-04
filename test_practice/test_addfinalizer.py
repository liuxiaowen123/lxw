"""
yield与addfinalizer的区别:
1）addfinalizer可以注册多个终结函数
2）当setUp的代码执行错误，addfinalizer依旧会执行？
"""
import pytest


@pytest.fixture(scope='function', autouse=False)
def demo_fixture(request):

    print('\n这个fixture在每个case前执行一次')

    def demo_finalizer():
        print('\n在每个case完成后执行的teardown')

    def demo_finalizer1():
        print('\n在每个case完成后执行的teardown1')

    def demo_finalizer2():
        print('\n在每个case完成后执行的teardown2')

    request.addfinalizer(demo_finalizer)
    request.addfinalizer(demo_finalizer1)
    request.addfinalizer(demo_finalizer2)


# 注意:addfinalizer执行顺序与注册的顺序相反
class Test01:
    def test_01(self, demo_fixture):
        print("\n===执行了case: test_01===")

    def test_02(self, demo_fixture):
        print("\n===执行了case: test_02===")

    def test_03(self, demo_fixture):
        print("\n===执行了case: test_03===")


if __name__ == '__main__':
    pytest.main(['test_01.py'])
