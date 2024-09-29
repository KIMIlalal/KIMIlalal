import pytest
import requests

from comment.yaml_util import read_yaml
from testcase.readyanm_util import read_yaml1


class TestGetNew:


    @pytest.mark.parametrize('agrs',read_yaml1("./test_get_news.yaml"))
    def test_get_new(self,agrs):
        print(agrs)
        # *获取网页新闻的接口
        url=agrs["api_request"]["url"]
        print(url)
        method=agrs["api_request"]["method"]
        headers=agrs["api_request"]["headers"]
        params=agrs["api_request"]["params"]
        vidate=agrs["api_validate"]
        print(vidate[0]["eq"]["code"])
        if method=="get":
            requests.get()
        else:
            res = requests.post(url=url,json=params,headers=headers)
        # print(res.json())

if __name__=='__main__':
    pytest.main(['-vs','test_get_news.py'])
