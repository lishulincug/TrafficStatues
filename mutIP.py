# -*- coding: utf-8 -*-
# IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用

from bs4 import BeautifulSoup
import requests
import random,json
# from USA import *
def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies

def getip():
    url = 'http://www.xicidaili.com/nn/'
    # url ='http://restapi.amap.com'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    # }
    headers = {'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch, br',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               }
    ip_list = get_ip_list(url, headers=headers)
    proxies = get_random_ip(ip_list)
    print(proxies)
    return proxies
# proxies=getip()


def get_ip_listtxt( ipstr):
    # file = open(file)
    file=ipstr.split('\n')
    ip_list = []
    for line in file:
        try:
            ip_list.append(json.loads(line.strip()))
        except:
            pass
    return ip_list

ipstr='''{"https": "https://113.221.46.165:8888"}
{"https": "https://27.40.149.95:61234"}
{"https": "https://112.114.94.125:8118"}
{"https": "https://112.114.96.18:8118"}
{"http": "http://125.211.202.26:53281"}
{"https": "https://116.249.222.96:8118"}
{"https": "https://222.182.53.69:8118"}
{"http": "http://122.114.31.177:808"}
{"https": "https://113.109.53.3:8118"}
{"https": "https://219.138.58.27:3128"}
{"https": "https://112.114.99.83:8118"}
{"https": "https://223.150.8.36:8888"}
{"https": "https://219.138.58.21:3128"}
{"https": "https://123.185.131.236:8118"}
{"https": "https://112.114.97.158:8118"}
{"https": "https://219.138.58.63:3128"}
{"https": "https://118.254.142.42:53281"}
{"https": "https://223.241.116.212:8010"}
{"https": "https://180.115.12.214:28471"}
{"https": "https://112.114.94.76:8118"}
{"https": "https://221.233.85.23:3128"}
{"http": "http://219.138.58.130:3128"}
{"https": "https://113.221.44.206:8888"}
{"https": "https://112.114.98.131:8118"}
{"http": "http://123.56.169.22:3128"}
{"https": "https://110.73.50.12:8123"}
{"https": "https://211.159.171.58:80"}
{"https": "https://221.233.85.113:3128"}'''

ip_list=get_ip_listtxt(ipstr)
# proxies=random.choice(ip_list)
if __name__ == '__main__':
    proxies = getip()
    # keys = rds.hkeys("hash_xila")
    # key = random.choice(keys)
    # proxy = rds.hget("hash_xila", key)
    # ip = eval(proxy)["ip"]
    # proxies = {"http": ip}