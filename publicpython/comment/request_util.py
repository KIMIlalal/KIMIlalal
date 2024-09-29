import requests


class RequestUtil:
    sess = requests.Session()

    #统一发请求
    def all_send_request(self,**kwargs):
        res = RequestUtil.sess.request(**kwargs)
        print(res.text)
        return res

