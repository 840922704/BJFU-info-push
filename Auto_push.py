# coding=UTF-8
import urllib.request
import sqlite3
from bs4 import BeautifulSoup
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
# 定义网址和网页编码
URL_News = "http://jwc.bjfu.edu.cn/jwkx/"
URL_Exam = "http://jwc.bjfu.edu.cn/ksxx/"
htmlCharset = "gb2312"
db_path = "/python/Auto_push/Auto_push.db"
count = 0
# 创建数据库
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS News (
              title varchar(20) NOT NULL PRIMARY KEY,  
              date  TEXT NOT NULL,              
              url   TEXT NOT NULL)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Exam (
              title varchar(20) NOT NULL PRIMARY KEY,
              date  TEXT NOT NULL,
              url   TEXT NOT NULL)''')
cursor.close()
conn.commit()
conn.close()
# 爬取信息_News
wb_data = urllib.request.urlopen(URL_News)
Page = BeautifulSoup(wb_data, features="lxml", from_encoding=htmlCharset)
title = Page.find_all("a", {"target": "_blank"})
title[:10] = []
url = Page.find_all("a", {"target": "_blank", "href": True})
url[:10] = []
date = Page.find_all("span", {"class": "datetime"})
First_title = title[0].get_text()
First_date = date[0].get_text()
First_url = url[0].get("href")
# print(First_title)
# print(type(URL_News))
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
try:
    Text_News = "<div>教务快讯：<br></div><div><%s><a href="'%s'">%s</a></div>" \
                % (First_date, "".join([URL_News, First_url]), First_title)
    cursor.execute("INSERT INTO %s (title,date,url) \
              VALUES ('%s','%s','%s')" % ("News", First_title, First_date, "".join([URL_News, First_url])))
    count += 1
except Exception:
    Text_News = "<div>教务快讯：</div><div><%s> 无更新<br></div>" % First_date
finally:
    cursor.close()
    conn.commit()
    conn.close()
    # print(Text_News)
# 爬取信息并存入数据库_Exam
wb_data = urllib.request.urlopen(URL_Exam)
Page = BeautifulSoup(wb_data, features="lxml", from_encoding=htmlCharset)
title = Page.find_all("a", {"target": "_blank"})
title[:10] = []
url = Page.find_all("a", {"target": "_blank", "href": True})
url[:10] = []
date = Page.find_all("span", {"class": "datetime"})
First_title = title[0].get_text()
First_date = date[0].get_text()
First_url = url[0].get("href")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
try:
    Text_Exam = "<div>考试信息：<br></div><div><%s><a href="'%s'">%s</a></div>" \
                % (First_date, "".join([URL_Exam, First_url]), First_title)
    cursor.execute("INSERT INTO %s (title,date,url) \
              VALUES ('%s','%s','%s')" % ("Exam", First_title, First_date, "".join([URL_Exam, First_url])))
    count += 1
except Exception:
    Text_Exam = "<div>考试信息：</div><div><%s> 无更新<br></div>" % First_date
finally:
    cursor.close()
    conn.commit()
    conn.close()

# 邮件模块


def send_email(text_news, text_exam):
    smtp_server = 'smtp.qq.com'
    smtp_port = '465'
    from_addr = '你的发送邮箱地址（默认为QQmail）'
    password = '你的发送邮箱的密码'
    to_addr = '你的接收邮箱地址'

    message = MIMEText('%s' % text_news+text_exam, 'html', 'utf-8')
    message['From'] = Header("Auto_Push", 'utf-8')
    message['To'] = Header("me", 'utf-8')
    message['Subject'] = Header("教务处信息更新", 'utf-8').encode()

    server_s = SMTP_SSL(smtp_server, smtp_port)
    # server_s.set_debuglevel(1)
    server_s.login(from_addr, password)
    server_s.sendmail(from_addr, [to_addr], message.as_string())
    server_s.quit()


if count != 0:
    send_email(Text_News, Text_Exam)
# 调用邮件模块
