import requests
from lxml import etree
import base64
import time
import fofa
import sys
import config
from bs4 import BeautifulSoup
from urllib.parse import quote


def logo():
    print('''


             /$$$$$$$$ /$$$$$$  /$$$$$$$$ /$$$$$$                                   
            | $$_____//$$__  $$| $$_____//$$__  $$                                  
            | $$     | $$  \ $$| $$     | $$  \ $$                                  
            | $$$$$  | $$  | $$| $$$$$  | $$$$$$$$                                  
            | $$__/  | $$  | $$| $$__/  | $$__  $$                                  
            | $$     | $$  | $$| $$     | $$  | $$                                  
            | $$     |  $$$$$$/| $$     | $$  | $$                                  
            |__/      \______/ |__/     |__/  |__/                                  



                                /$$$$$$            /$$       /$$                    
                               /$$__  $$          |__/      | $$                    
                              | $$  \__/  /$$$$$$  /$$  /$$$$$$$  /$$$$$$   /$$$$$$ 
                              |  $$$$$$  /$$__  $$| $$ /$$__  $$ /$$__  $$ /$$__  $$
                               \____  $$| $$  \ $$| $$| $$  | $$| $$$$$$$$| $$  \__/
                               /$$  \ $$| $$  | $$| $$| $$  | $$| $$_____/| $$      
                              |  $$$$$$/| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$      
                               \______/ | $$____/ |__/ \_______/ \_______/|__/      
                                        | $$                                        
                                        | $$                                        
                                        |__/                                        

                                                                                version:1.01
    ''')




def checkSession():
    if config.cookie=="":
        print("请配置config文件")
        exit(0)
    print("检测cookie成功")
    return




def init():
    config.SearchKEY = input('请输入fofa搜索关键字 \n')
    

    return




def spider():
    searchWord = config.SearchKEY
    email, key = ('*********', '('*********',')
    client = fofa.Client(email, key) 
    fo = open(sys.argv[1],"w+")
    while True:
      searchbs64 = quote(str(base64.b64encode(searchWord.encode()), encoding='utf-8'))
      print("爬取页面为:https://fofa.info/result?qbase64=" + searchbs64+"&page=1000&page_size=10")
      print(searchWord)
      data = client.search(searchWord, size=10000, page=1, fields="host")
      for host in data["results"]:
        fo.write(host+"\n")
      fo.flush()
      html = requests.get(url="https://fofa.info/result?qbase64=" + searchbs64+"&page=1000&page_size=10", headers=config.headers).text
      soup = BeautifulSoup(html, 'lxml')
      for item in (soup.body.findNext('div',{'class':'contentLeft'}).findAll('span')):
        if(item.text.find("20") == 0):
          time2 = (item.text)
          searchWord = config.SearchKEY + ' && before = "'+time2+'"'
      time.sleep(30)




def main():
    checkSession()
    init()
    spider()




if __name__ == '__main__':
    main()
