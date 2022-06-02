"""
将数据写入配置yaml文件
"""
import os
import yaml

login_api = {"name": "登录接口",
             "request": {"url": "http://hn216.api.yesapi.cn/?&s=App.User.login", "method": 'post'},
             "param": {"app_key": 123456, "uuid": 123456789},
             "returns": '200'}
profile_api = {"name": "获取个人资料接口",
               "request": {"url": "http://hn216.api.yesapi.cn/?&s=App.User.Profile", "method": 'post'},
               "param": {"app_key": 123456, "uuid": 123456789},
               "returns": '200'}
# test_ppc_list = ["aaa", "bbb", "ccc"]

# 获取当前脚本所在文件夹路径
path = os.path.dirname(os.path.realpath(__file__))
testpath = os.path.join(path, "generate.yaml")
print(testpath)

# 写入yaml文件
with open(testpath, 'w', encoding="utf-8")as f:
    # 如果不加 allow_unicode=True 会出现yaml文件内写入的是Unicode
    yaml.dump([login_api, profile_api], f, allow_unicode=True)


print('success')

