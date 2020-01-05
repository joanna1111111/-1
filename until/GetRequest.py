import requests
import json
from conf.log import logger

class RequestHandler():
    def __init__(self,d):
        self.d = d

    def get_response(self):
        """获取请求结果"""
        response = self.send_request()
        return response

    def send_request(self):
        """发送数据"""
        response = requests.request(
            method = self.d.get("case_method"),
            url = self.d.get("case_url"),
            params = self.check_params(),
        )

        header = response.headers['Content-Type'].split('/')[-1].split(';')[0]
        if hasattr(self,'_check_{}_response'.format(header)):
            g = getattr(self,'_check_{}_response'.format(header))
            result = g(response)
        else:
            logger('{}'.format(__file__)).error('the type of data:{} has not defined'.format(header))
        return result


    def check_params(self):
        """校验参数"""
        pass

    def _check_json_response(self,response):
        """校验请求结果json数据"""
        response = response.json()
        expect = json.loads(self.d.get('case_expect'))
        for k in expect:
            if response[k] != expect[k]:
                return {k:response[k]} , {k:expect[k]}
        return {k: response[k]}, {k:expect[k]}

    def _check_html_response(self,response):
        """校验请求结m'l数据"""
        pass