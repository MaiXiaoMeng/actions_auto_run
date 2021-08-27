'''
Author: MaiXiaoMeng
Date: 2021-02-13 16:56:08
LastEditors: MaiXiaoMeng
LastEditTime: 2021-02-14 15:56:18
'''
import sqlite3
import requests
from requests.models import Response

try:
    import tools.utils as tools
except:
    import sys
    sys.path.append('./')
    import tools.utils as tools


class exchange_rate:
    def __init__(self):
        self.json = None
        self.rate_code = [
            'USD', 'AED', 'ARS', 'AUD', 'BGN', 'BRL', 'BSD', 'CAD', 'CHF', 'CLP', 'CNY', 'COP', 'CZK',
            'DKK', 'DOP', 'EGP', 'EUR', 'FJD', 'GBP', 'GTQ', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR',
            'ISK', 'JPY', 'KRW', 'KZT', 'MVR', 'MXN', 'MYR', 'NOK', 'NZD', 'PAB', 'PEN', 'PHP', 'PKR',
            'PLN', 'PYG', 'RON', 'RUB', 'SAR', 'SEK', 'SGD', 'THB', 'TRY', 'TWD', 'UAH', 'UYU', 'ZAR',
        ]

    def get_latest_rate(self, symbols=''):
        for _rate_code in self.rate_code:
            url = f'https://api.exchangerate-api.com/v4/latest/{_rate_code}'
            print(url)
            self.json = requests.get(url).json()
            self.save_rate_data()

    def save_rate_data(self):
        for key in list(self.json['rates'].keys()):
            try:
                self.conn.execute(
                    f'INSERT INTO "main"."库存管理_历史汇率"("日期", "本币", "外币", "汇率") VALUES ("{self.json["date"]}", "{self.json["base"]}","{key}", "{self.json["rates"][key]}")')
                self.conn.commit()
            except Exception as error:
                print(error)

    def open_database(self):
        self.conn = sqlite3.connect('scripts/exchange_rate.db')
        self.cursor = self.conn.cursor()

    def close_database(self):
        self.conn.commit()
        self.conn.close()

    def run(self):
        try:
            self.open_database()
            self.get_latest_rate()
            self.close_database()
        except Exception:
            message_context = f'运行异常,脚本又挂掉啦~'
            tools.send_message(self.log_head + message_context)


# if __name__ == '__main__':
    # exchange_rate().run()
