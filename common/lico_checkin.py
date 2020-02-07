import requests
from django.http import HttpResponse

from checkin_everyday.models import Lico_user


def login_lico_ssr():
    url ="https://www.lico.world/auth/login"
    users = Lico_user.objects.all()
    for user in users:
        if all([user.email,user.password]): continue
        data = {
            "email": user.email,
            "passwd": user.password,
            "code":""
        }
        response_login =requests.post(url,data)
        if eval(response_login.content.decode('utf-8'))['ret']=='0':
            return HttpResponse('登录失败,请手动查看')
        headers = response_login.headers['set-cookie']
        # uid=99; expires=Fri, 07-Feb-2020 13:24:38 GMT; Max-Age=86400;
        # path=/, email=1270806234%40qq.com; expires=Fri, 07-Feb-2020 13:24:38 GMT; Max-Age=86400;
        # path=/, key=0765451a8b4c3b24e0f1d0c179e5b2d8d4c8edbaf7d4b; expires=Fri, 07-Feb-2020 13:24:38 GMT; Max-Age=86400;
        # path=/, ip=3511895beffba393fe25f58874b40486; expires=Fri, 07-Feb-2020 13:24:38 GMT; Max-Age=86400;
        # path=/, expire_in=1581081878; expires=Fri, 07-Feb-2020 13:24:38 GMT; Max-Age=86400; path=/
        header_dict = dict()
        for i in headers.split('path=/,'):
            for j in i.split(';'):
                try:
                    if j.split('=')[0] not in header_dict:
                        header_dict[j.split('=')[0]] = j.split('=')[1]
                except:
                    pass
        get_checkin = requests.post('https://www.lico.world/user/checkin',cookies = header_dict)
        if eval(get_checkin.content.decode('utf-8'))['ret']=='1':
            return HttpResponse('签到成功')
        elif eval(get_checkin.content.decode('utf-8'))['msg']=='您似乎已经签到过了...':
            return HttpResponse('签到成功')
        return HttpResponse('签到可能失败,请手动查看')