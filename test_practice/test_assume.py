"""
pytest.assume 第一次即使断言失败，后面的断言还是会继续执行
"""
import pytest


# @pytest.mark.parametrize(['a', 'b'], [(1, 2), (3, 4)])
# def test_simple_assume(a, b):
#     assert a == b
#     assert 1 == 1


@pytest.mark.parametrize(['a', 'b'], [(1, 2), (3, 4)])
def test_simple_assume1(a, b):
    pytest.assume(a == b)
    pytest.assume(1 == 1)


if __name__ == '__main__':
    pytest.main(['test_assume.py'])
