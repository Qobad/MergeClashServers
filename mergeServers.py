



import requests

url=['https://proxypool.laowang.me/clash/proxies',
     'https://proxypool.toshiki.top/clash/proxies',
     'https://klausvpn.posyao.com/clash/proxies',
     'https://fq.lonxin.net/clash/proxies',
     'https://proxies.bihai.cf/clash/proxies'    
     ]

outlist=[]

urlIndex=0
for urlItem in url:
    response = requests.get(urlItem,timeout=60)
    allservers = response.text
    
    Lines = allservers.split("\n")


    outlist.extend(Lines)

    urlIndex+=1

    print(" link  "  ,urlIndex," done ")
    allservers=""







result = []

for item in outlist:
    try:
        servername=item.split('server":"')[1].split('"')[0]
        serverport=item.split('port":')[1].split(',')[0]

        if not any((servername in s and serverport in s ) for s in  result):
            result.append(item)
            print("----->",servername,":",serverport)
    except:
        pass
        




file1 = open("./allservers.txt", "w", encoding="utf8")
file1.write("proxies:" + "\n")
for element in result:
    file1.write(element + "\n")
file1.close()

