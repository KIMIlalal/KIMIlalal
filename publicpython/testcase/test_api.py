import json
import random
import re
import unittest

import jsonpath as jsonpath
import pytest as pytest
import requests

from comment.request_util import RequestUtil
from comment.yaml_util import read_testcase, write_yaml, read_yaml


class TestApi():
    # 创建一个类全局变量

    # 获取鉴权码
    @pytest.mark.parametrize("casedatas",read_testcase("./testcase/test_get_token.yaml"))
    def test_get_token(self, casedatas):
        print(casedatas)
        method=casedatas['request']["method"]
        url = casedatas["request"]["url"]
        datas =casedatas["request"]["params"]
        res = RequestUtil().all_send_request(method=method,url=url, params=datas)
        result = res.json()
        if "access_token" in result:
            # 提取access_token
            value = jsonpath.jsonpath(result, "$.access_token")
            datas={"access_token":value[0]}
            #读取并写入到ymal文件中
            write_yaml(datas)


    # 获取公众号已创建标签接口
    @pytest.mark.parametrize("casedatas", read_testcase("./testcase/get_select_flag.yaml"))
    def test_select_flag(self,casedatas):
        method = casedatas['request']["method"]
        url = casedatas["request"]["url"]
        # 需要用到上一个接口的返回值
        datas =casedatas["request"]["params"]
        for key,value in datas.items():
            print(key,value)
            datas[key]=read_yaml(key)
        print(datas)
        res = RequestUtil().all_send_request(method=method,url=url, params=datas)
        print(res.json())
        assert "星标组" in res.text
    #
    # # 创建标签接口
    # def test_creat_flag(self):
    #     url = "https://api.weixin.qq.com/cgi-bin/tags/create?access_token=" + read_yaml("access_token")
    #     data = {"tag": {"name": "广西" + str(random.randint(10000, 999999))}}
    #     res = RequestUtil().all_send_request(url=url, json=data)
    #     print(json.loads(json.dumps(res.json()).replace("\\\\", "\\")))
    #
    # # 文件上传路径
    # @pytest.mark.parametrize("casedatas", read_testcase("./testcase/get_file_load.yaml"))
    # def test_file_upload(self,casedatas):
    #     method = casedatas['request']["method"]
    #     url = casedatas["request"]["url"]
    #     # 需要用到上一个接口的返回值
    #     datas = casedatas["request"]["params"]
    #     for key, value in datas.items():
    #         print(key, value)
    #         datas[key] = read_yaml(key)
    #     files=casedatas["request"]["files"]
    #     for key, value in files.items():
    #         print(key, value)
    #         files[key] = open(value,"rb")
    #     res = RequestUtil().all_send_request(method=method,url=url,params=datas,files=files)


