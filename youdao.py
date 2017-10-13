from bs4 import BeautifulSoup
import urllib.parse
import re
import requests
import time

index = 0
session = requests.session()
f = open('C:\\Users\\Administrator\\Desktop\\dictionary\\words.txt','r',encoding='gb2312')
output = open("C:\\Users\\Administrator\\Desktop\\dictionary\\output.txt", "w")
for line in f.readlines():
  time.sleep(10)
  if(line != '\n'):
    m = re.match(r'([a-zA-Z ]+)', line)
    if m:
      index += 1
      url = 'http://dict.youdao.com/example/blng/eng/'+ m.group(1) + '/#keyfrom=dict.main.moreblng'
      s =  '(' + str(index) + ')、' + line + "\n\r"
      print("%s"% (s) ,file = output)
      soup = BeautifulSoup(session.get(url).text)
      blingual = soup.findAll(id = 'bilingual')
      if blingual:
        ol = blingual[0].ul
        if ol:
          ul = ol.findAll('li')
          if(len(ul)<6):
            num = len(ul)
          else:
            num = 6
          for i in range(num):
            li = ul[i]
            if li.p:
              if li.p.a:
                if li.p.a.get('data-rel'):
                  s1 = urllib.parse.unquote(li.p.a['data-rel'].replace('+',' ').split('.')[0])
                  print(s1+"\n\r")
                  print("%s" % (s1), file = output)
              if len(li.findAll('p')) > 1:
                s2 = urllib.parse.unquote(li.findAll('p')[1].get_text().split()[0]).encode("gb18030").decode('gbk','ignore')
                print("%s" % (s2), file = output)
      print("\n\r\n\r", file = output)

