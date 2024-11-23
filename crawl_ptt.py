import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/'
web = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', cookies={'over18':'1'})
web.encoding='utf-8'       # 避免中文亂碼
soup = BeautifulSoup(web.text, "html.parser")
titles = soup.find_all('div', class_='title')
output = ''           # 建立 output 變數
for i in titles:
    if i.find('a') != None:
        # 將資料一次記錄到 output 變數裡
        output = output + i.find('a').get_text() + '\n' + url + i.find('a')['href'] + '\n\n'
print(output)

f = open('八卦.txt','w',encoding="utf-8")   # 建立並開啟純文字文件 
f.write(output)     # 將資料寫入檔案裡
f.close()