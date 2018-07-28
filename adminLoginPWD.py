import zmail
import sys


def main1():
    pwd = sys.argv[1]
    subject = {
        "subject": "登录验证码",
        "content": pwd
    }

    server = zmail.server("896834344@qq.com", "gkyommydyiozbbec")
    server.send_mail("896834344@qq.com", subject)


def main():
    arg = sys.argv[1]
    print(arg)


if __name__ == '__main__':
    main1()
