# -- coding: utf-8 --
import requests
from datetime import datetime

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        'message': msg,
        'stickerPackageId' : 2,
        'stickerId' : 520
    }
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
    return r.status_code


# 你要傳送的訊息內容
message = '@李賢輝 台南簡訊目前異常，請關心!! http://www.sinlau.org.tw/' + datetime.now()
# 將剛剛複製下來的Token取代以下''中的內容即可
token = 'oc9vps8aktycRYhcQAyvccxbeS9tGNo0FNmfu8m1g44'

lineNotifyMessage(token, message)
