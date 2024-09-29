import yaml


def read_yaml1(path):
    # 读取yaml文件
    with open(path,encoding="utf-8",mode="r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data

# if __name__=='__main__':
#     print(read_yaml("./test_get_news.yaml"))