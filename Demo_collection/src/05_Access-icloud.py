# -*- coding: UTF-8 -*-
"""
@Project : Ray_Pro
@File    : 05_Access-icloud
@IDE     : PyCharm
@Author  : 李睡睡
@Date    : 2023/8/24 8:39
@Scripts : pyicloud sys
@Documentation:
@Function: 通过 PyiCloud 访问 iCloud 服务。
@Tips    :不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""
import sys
from pyicloud import PyiCloudService


def login_icloud(apple_id, password):
    api = PyiCloudService(apple_id, password,china_mainland=True)

    if api.requires_2fa:
        print("Two-factor authentication required.")
        code = input("Enter the code you received of one of your approved devices: ")
        result = api.validate_2fa_code(code)
        print("Code validation result: %s" % result)

        if not result:
            print("Failed to verify security code")
            sys.exit(1)

        if not api.is_trusted_session:
            print("Session is not trusted. Requesting trust...")
            result = api.trust_session()
            print("Session trust result %s" % result)

            if not result:
                print("Failed to request trust. You will likely be prompted for the code again in the coming weeks")
    elif api.requires_2sa:
        import click
        print("Two-step authentication required. Your trusted devices are:")

        devices = api.trusted_devices
        for i, device in enumerate(devices):
            print(
                "  %s: %s" % (i, device.get('deviceName',
                                            "SMS to %s" % device.get('phoneNumber')))
            )

        device = click.prompt('Which device would you like to use?', default=0)
        device = devices[device]
        if not api.send_verification_code(device):
            print("Failed to send verification code")
            sys.exit(1)

        code = click.prompt('Please enter validation code')
        if not api.validate_verification_code(device, code):
            print("Failed to verify verification code")
            sys.exit(1)

    return api

api = login_icloud('2511248339@qq.com','030806lSr')

print(api.devices[1].location())