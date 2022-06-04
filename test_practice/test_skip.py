"""
pytest.mark.skip
可以标记无法在某些平台上运行的测试功能，或者您希望失败的测试功能
希望满足某些条件才执行某些测试用例，否则pytest会跳过运行该测试用例
实际常见场景：跳过非Windows平台上的仅Windows测试，或者跳过依赖于当前不可用的外部资源（例如数据库）的测试
"""
import os
import sys
import pytest


@pytest.fixture(autouse=True)
def login():
    print("====登录====")


def test_case01():
    print("我是测试用例11111")


@pytest.mark.skip(reason="不执行该测试用例22222，因为没写好！！")
def test_case02():
    print("我是测试用例22222")


class Test1:
    # 参数化，标记数据
    @pytest.mark.parametrize("input,expect", [(1, 1), pytest.param(1, 2, marks=pytest.mark.xfail)])
    def test_1(self, input, expect):
        print("== 我是类测试用例1111 ==")
        # 1=1 测试通过 1=2 xfail
        assert input == expect

    @pytest.mark.skip(reason="不想执行")
    def test_2(self):
        print("== 我是类测试用例2222 ==")

    # pytest.skip()函数基础使用
    # 类似于在Python的循环里面，满足某些条件则break 跳出循环
    def test_3(self):
        n = 1
        print("== 我是类测试用例3333 ==")
        while True:
            print("该用例一共执行了{}次".format(n))
            n += 1
            if n == 5:
                pytest.skip('这是执行第{}次，结束该用例执行'.format(n))

    # 希望有条件地跳过某些测试用例，条件为true时才跳过
    @pytest.mark.skipif(sys.platform == 'win32', reason="does not run on windows")
    def test_function(self):
        print("不能在window上运行")


@pytest.mark.skip(reason="类也可以跳过不执行")
class TestSkip:
    def test_1(self):
        print("== 不会执行 ==")


if __name__ == '__main__':
    pytest.main(['test_skip.py', '-s', '--alluredir', '../report/tmp'])
    os.system('allure generate ../report/tmp -o ../report/html --clean')
