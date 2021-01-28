import requests


class Message(object):

    def __init__(self, api_key):
        # 账号的唯一标识
        self.api_key = api_key
        # 单条短信发送的接口
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_message(self, phone, code):
        """
        短信发送的实现
        :param phone:   接收短信的手机号
        :param code:    随机验证码
        """

        params = {
            "apikey": self.api_key,
            "mobile": phone,
            "text": "【张凯test】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        # 通过requests 发送请求
        req = requests.post(self.single_send_url, data=params)
        # 如果返回200代表成功
        print(req)


# if __name__ == '__main__':
#     message = Message("40d6180426417bfc57d0744a362dc108")
#     message.send_message("13821228537", "66666")
