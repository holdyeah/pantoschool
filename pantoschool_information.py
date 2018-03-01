# -*- coding: utf-8 -*-

# Import the module
import requests
import os
from bs4 import BeautifulSoup
from lxml import etree

# header browser
headers = {
    'Accept': 'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN',
    'Cache-Control': 'no-',
    'Connection': 'Keep-Alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)'
    }

# Constructs a payload field
payload = {
        '__EVENTVALIDATION': '',
        '__VIEWSTATE':'',
        '__VIEWSTATEGENERATOR': 'B1CEE7C8',
        'txtUserName': '',
        'txtUserPwd': '',
        'rdoSelect': '',
        'btnLogin.x': '',
        'btnLogin.y': '',
        }

# Basic parameters
student = 'student'
txtUserName = '000000' # this is studentId
txtUserPwd = '8888'
value3 = 'B1CEE7C8'
x = '32'
y = '10'

# The first line using the requests.Session () session
# object allows you to hold certain parameters across requests
url = "http://*******/pantoschool/XT/Accounts/login2.aspx?ReturnUrl=%2fpantoschool%2fDefault.aspx"
s = requests.Session()
index = s.get(url, headers=headers)
soup = BeautifulSoup(index.content, 'lxml')
value1 = soup.find('input', id='__VIEWSTATE')['value']
value2 = soup.find('input', id='__EVENTVALIDATION')['value']

payload['txtUserName'] = txtUserName
payload['txtUserPwd'] = txtUserPwd
payload['rdoSelect'] = student
payload['btnLogin.x'] = x
payload['btnLogin.y'] = y

payload['__VIEWSTATEGENERATOR'] = value3
# The following value1 and value2 do not need transcoding,
#  you can post directly in the past. Wasted a long time here
payload['__VIEWSTATE'] = value1  # value1
payload['__EVENTVALIDATION'] = value2  # value2

# Landing home page
post1 = s.post(url, data=payload, headers=headers)
html = post1.content.decode("gb2312")
selector1 = etree.HTML(html)

# Determine whether to obtain login status
content = selector1.xpath('//div[@id="welcome"]/span/text()')
if len(content) == 1:
    print 'OK',
else:
    print 'ON',

# Get personal basic information page
StuCardEditUrl = "http://*******/pantoschool/Student/StudentInform/StuCardEdit.aspx"
response = s.get(StuCardEditUrl, headers=headers)
html1 = response.content.decode("gb2312")
selector2 = etree.HTML(html1)
content2 = selector2.xpath('//table[@class="table-border"]/tr/td/span/text()')

# Output data
for each3 in content2:
    print(each3),

# Close the website
logout_url = 'http://*******/pantoschool/XT/Accounts/Logout.aspx'
re = s.get(logout_url, headers=headers)
html4 = re.content.decode("gb2312")
selector111 = etree.HTML(html4)
content22 = selector111.xpath('//div[@id="welcome"]/span/text()')
if len(content22) == 1:
    print 'OK',
else:
    print 'ON',

