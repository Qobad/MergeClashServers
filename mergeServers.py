
import requests
import time

url=['https://proxypool.laowang.me/clash/proxies',
     'https://proxypool.toshiki.top/clash/proxies',
     'https://klausvpn.posyao.com/clash/proxies',
     'https://fq.lonxin.net/clash/proxies',
     'https://proxies.bihai.cf/clash/proxies',
     'http://wxshi.top:9090/clash/proxies',
     'https://www.sdufe.tk/clash/proxies',
     'https://proxy.yugogo.xyz/clash/proxies',
     'https://free.dswang.ga/clash/proxies',
     'http://clash.3wking.com:12580/clash/proxies'
     ]

outlist=[]

urlIndex=0
for urlItem in url:
    servercount=0
    try:
        response = requests.get(urlItem,timeout=60)
    except:
        pass
    allservers = response.text
    
    Lines = allservers.split("\n")

    servercount=len(Lines)
    outlist.extend(Lines)

    urlIndex+=1

    print(" link  "  ,urlIndex," found  " , servercount ,"  servers")
    allservers=""


result = []

for item in outlist:
    try:
        servername=item.split('server":"')[1].split('"')[0]
        serverport=item.split('port":')[1].split(',')[0]
        serverpass=item.split('password":')[1].split('"')[1]
        if not any((servername in s and serverport in s and serverpass in s) for s in  result):
            result.append(item)
            servercount+=1
            print(" server no ", servercount, "--->",servername,":", serverport,"  pass : ", serverpass)
    except:
        pass
    

file1 = open("./allservers.txt", "w", encoding="utf8")
file1.write("proxies:" + "\n")
for element in result:
    file1.write(element + "\n")
file1.close()
time.sleep(10)

