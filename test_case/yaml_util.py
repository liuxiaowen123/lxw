"""
yaml工具类，读取yaml文件
"""
import yaml


class YamlUtil:
    def __init__(self, yaml_file):
        # 通过init方法把yaml文件传入到类
        self.yaml_file = yaml_file

    # 读取yaml文件
    def read_yaml(self):
        with open(self.yaml_file, encoding='utf-8') as f:
            # 对yaml文件反序列化，就是把yaml格式转成dict格式
            value = yaml.load(f, Loader=yaml.FullLoader)  # 添加loader参数是为了去掉load warning
            return value
