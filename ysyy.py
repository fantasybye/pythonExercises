import requests
import json
import time

url = "http://ehallapp.nju.edu.cn/qljfwapp/sys/lwAppointmentBathroom/api/appointmentSave.do"
# url = 'http://ehallapp.nju.edu.cn/qljfwapp/sys/lwAppointmentBathroom/api/appointmentValidate.do'

today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
beginTime = today + " 20:30"
endTime = today + " 21:10"
formData = {"USER_ID":"MF20320214","USER_NAME":"张帆",
            "DEPT_CODE":"4270","DEPT_NAME":"软件学院","PHONE_NUMBER":"15850566780","PALCE_ID":"f881e8c2aa6f4190bc3efa13408143af",
            "BEGINNING_DATE": beginTime,"ENDING_DATE": endTime,
            "SCHOOL_DISTRICT_CODE":"02","SCHOOL_DISTRICT":"鼓楼校区","LOCATION":"鼓楼男浴室","PLACE_NAME":"鼓楼男浴室","IS_CANCELLED":0}

payload = {'formData': json.dumps(formData)}
# payload = {'beginTime': '2020-09-07 14:30', 'end_time': '2020-09-07 15:00', 'palce_id': 'f881e8c2aa6f4190bc3efa13408143af'}
headers = {
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mi 10 Pro Build/QKQ1.191117.002; wv) AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36 yiban/8.2.1 cpdaily/8.2.1 '
                  'wisedu/8.2.1',
    'X-Requested-With': 'com.wisedu.cpdaily.nju',
    'Origin': 'http://ehallapp.nju.edu.cn',
    # 'Host': 'ehallapp.nju.edu.cn',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'Cookie: _WEU=pU4MhiL7RjLw8ZZ*nGVuh6zyBA2SU7aj1YuL8b6NnwLYfZYMkxNo*W*MG7d3n0_roYYvL5HeEEQmFjIClxllU82ORRVPHq*0rJVlwrxVrFuLV*5BdIVIueSERZouW33TCCqHi0QO3RvU9kOsPFNNrO5lzvchTjLJyXw5XNgUC3l6pq_bTrutnvfQs8e9iCcj; iPlanetDirectoryPro=SBfnaP1znGZPTZ2smFQJye; MOD_AUTH_CAS=MOD_AUTH_ST-868201-GeCjtp3FNTRUkAbzFgke1599441283175-JsFF-cas',
    'Referer': 'http://ehallapp.nju.edu.cn/qljfwapp/sys/lwAppointmentBathroom/*default/index.do'
}

response = requests.request("POST", url, headers=headers, params=payload)

print(response.text)

