# -*- coding: utf-8 -*-

import os
import time
import socks
from telethon import TelegramClient, events, sync

try:
    import tools.utils as tools
except:
    import sys
    sys.path.append('./')
    import tools.utils as tools


class www_telegram_org:
    # https://www.jianshu.com/p/0f61dd28d969
    def __init__(self):
        self.name = 'www.telegram.org'
        self.date = time.strftime("%Y-%m-%d", time.localtime())
        self.log_head = f'[{self.date}][{self.name}] '
        self.api_id = tools.get_environment_variables('TELEGRAM_API_ID')
        self.api_hash = tools.get_environment_variables('TELEGRAM_API_HASH')
        self.proxy = (socks.SOCKS5, '127.0.0.1', 10808)

    def checkIn(self):

        session_name = self.api_id[:]
        for num in range(len(self.api_id)):
            session_name[num] = "id_" + str(session_name[num])
            client = TelegramClient(session_name[num], self.api_id[num], self.api_hash[num]).start()
            # client = TelegramClient(session_name[num], self.api_id[num], self.api_hash[num], proxy=self.proxy).start()
            client.send_message("FreeSGKbot", '/sign')  # 第一项是机器人ID，第二项是发送的文字
            time.sleep(5)  # 延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
            client.send_read_acknowledge("FreeSGKbot")  # 将机器人回应设为已读
            print("Done! Session name:", session_name[num])

    def run(self):
        self.checkIn()


if __name__ == '__main__':
    www_telegram_org().run()
