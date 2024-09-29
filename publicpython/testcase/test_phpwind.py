import unittest
import re

import pytest




class TestPhpwind():
    csrf_token = ""

    # cookies关联的接口
    # @pytest.mark.smoke
    # def test_astart1(self):
    #     url = "http://47.107.116.139/phpwind/"
    #     res = RequestUtil().all_send_request(method="get", url=url)
    #     # res = requests.get(url=url)
    #     result = res.text
    #     TestPhpwind.csrf_token = re.search('name="csrf_token" value="(.*?)"', result).group(1)
    #     print(TestPhpwind.csrf_token)
    #     datas={"csrf_token":TestPhpwind.csrf_token}
    #     write_yaml(datas)
    #     # print(res.text)
    #
    # # 测试登录的接口
    # def test_blogin2(self):
    #     url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
    #     datas = {
    #         "username": "baili",
    #         "password": "baili123",
    #         "csrf_token": read_yaml("csrf_token"),
    #         "back_url": "http://47.107.116.139/phpwind/",
    #         "invite": ""
    #     }
    #     headers = {
    #         "Accept": "application/json,text/javascript,/;q=0.01",
    #         "X-Requested-With": "XMLHttpRequest"
    #     }
    #     res = RequestUtil().all_send_request(method="post", url=url, data=datas, headers=headers)
    #     # res = requests.post(url=url, data=datas, headers=headers)
    #     print(res.json())


# if __name__ == '__main__':
#     TestPhpwind().test_astart()
    # TestPhpwind.test_blogin()

