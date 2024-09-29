import os
import yaml

#写入到文件中
def write_yaml(data):
    with open(os.getcwd()+"/extract.yml",encoding="utf-8",mode="a+") as f:
        yaml.dump(data,stream=f,allow_unicode=True)


#读取到文件中
def read_yaml(key):
    with open(os.getcwd()+"/extract.yml",encoding="utf-8",mode="r") as f:
        value = yaml.load(f, yaml.FullLoader)
        print(value[key])
        return value[key]

#清空ymal文件
def clear_yaml():
    with open(os.getcwd() + "/extract.yml", encoding="utf-8", mode="w") as f:
        f.truncate()

#读取测试用例
def read_testcase(path):
    with open(path,encoding="utf-8",mode="r") as f:
        value = yaml.load(f, yaml.FullLoader)
        return value

# if __name__=='__main__':
#     print(read_testcase("../testcase/test_get_token.yaml"))
