import requests

url = 'https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=CWA-7700639C-B983-4F0E-B1AF-F5E664BE99C5&downloadType=WEB&format=JSON'
data = requests.get(url)   # 取得 JSON 檔案的內容為文字
data_json = data.json()    # 轉換成 JSON 格式
location = data_json['cwaopendata']['dataset']['location']   # 取出 location 的內容
for i in location:
    print(f'{i}')