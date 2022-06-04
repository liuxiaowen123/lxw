"""
封装assert方法
"""
import json


class Assertions:

    @staticmethod
    def assert_status_code(status_code, expected_code):
        """
        验证response状态码
        """
        try:
            assert status_code == expected_code
            return True

        except Exception:
            raise

    @staticmethod
    def assert_in_text(body, expected_results):
        """
        验证response body中是否包含预期字符串，不包含为 not in
        """
        text = json.dumps(body, ensure_ascii=False)
        try:
            # print(text)
            assert expected_results in text
            return True

        except Exception:
            raise

    @staticmethod
    def assert_time(actual_time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        """
        try:
            assert actual_time < expected_time
            return True

        except Exception:
            raise