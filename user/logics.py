from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from common import keys
import json
import random
import os
from datetime import timedelta

from flask import session
from main import app
from common import code_status

def get_token():
    code_list = []
    for i in range(5):
        code_list.append(str(random.randint(0,9)))
    return "".join(code_list)


def send_mes(phone):
    client = AcsClient(keys.accessKeyId, keys.accessSecret, 'cn-hangzhou')

    request = CommonRequest()

    request.set_accept_format('json')

    request.set_domain('dysmsapi.aliyuncs.com')

    request.set_method('POST')

    request.set_protocol_type('https')  # https | http

    request.set_version('2017-05-25')

    request.set_action_name('SendSms')

    code = get_token()

    print('验证码：', code)

    param_msg = {
        'RegionId': "cn-hangzhou",
        'PhoneNumbers': phone,
        'SignName': "滑动弹弹",
        'TemplateCode': "SMS_181851494",
        'TemplateParam': '{\"code\":\'code\'}'
    }

    for key, value in param_msg.items():
        request.add_query_param(key, value)

    response = client.do_action_with_exception(request)

    res = json.loads(response)

    code_key = code_status.SENDMES_KEY % phone
    if res['Message'] == 'OK' and res['Code'] == 'OK':
        session['%s' % code_key]  = code
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=3)
        return True
    else:
        print(response)
        return False