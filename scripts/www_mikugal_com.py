import time
import requests

try:
    import tools.utils as tools
except:
    import sys
    sys.path.append('./')
    import tools.utils as tools


class www_mikugal_com:
    def __init__(self):
        self.session = requests.session()
        self.name = 'www.mikugal.com'
        self.sign_token = None
        self.date = time.strftime("%Y-%m-%d", time.localtime())
        self.log_head = f'[{self.date}][{self.name}] '
        self.email = tools.get_environment_variables('MKGAL_EMAIL')
        self.password = tools.get_environment_variables('MKGAL_PASSWORD')

    def get_mkgal_sign(self):
        url = 'https://www.mikugal.com/sign'
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://www.mikugal.com',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Referer': 'https://www.mikugal.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'}
        data = {
            'email': self.email,
            'password': self.password
        }
        response = self.session.post(url=url, headers=headers, data=data)
        response_json = response.json()['obj']
        message_context = f'用户名:{response_json["nickname"]} 当前金币:{response_json["jf"]}'
        tools.send_message(self.log_head + message_context)
        self.sign_token = response_json["token"]

    def get_mkgal_addJf(self):
        url = 'https://www.mikugal.com/addJf'
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'X-Auth-Token': self.sign_token,
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Referer': 'https://www.mikugal.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'}
        response = self.session.get(url=url, headers=headers).json()
        if response['code'] == 0:
            message_context = f'每日签到成功'
        else:
            message_context = f'每日签到失败'
        tools.send_message(self.log_head + message_context)

    def run(self):
        try:
            self.get_mkgal_sign()
            self.get_mkgal_addJf()
        except Exception as error:
            message_context = f'运行异常,脚本又挂掉啦~'
            tools.send_message(self.log_head + message_context)
            print(error)


if __name__ == "__main__":
    www_mikugal_com().run()
