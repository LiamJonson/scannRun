from socket import *
from termcolor import colored

import threading
w = 0
def connScan(host, port,tekst):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(2)
    result = s.connect_ex((str(host),int(port)))
    global w
    if result == 0:
        print(colored("Tcp {} - Port {} is open\n".format(host, port),'green'))
        with open(tekst, 'a') as worK_ip:
            worK_ip.write('{}\n'.format(host))
        w +=1
        s.close()

    else:
        print(colored("Tcp {} - Port {} is closed\n".format(host,port),'red'))
        s.close()

found_ip =[]
ports = [8000,8080,8888,7000,37000,34567]
spis =[]
#with open('111.txt','r') as gla:
#    for i in gla:
#        i = i.strip()
#        try:
#            n = ipaddress.ip_network(i)
#        except ValueError:
#            print(' детектед ошибка -',i)
#        else:
#            for ip in n:
#                spis.append(ip)
def ipRange(start_ip, end_ip):    #ip list generation function
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    temp = start
    ip_range = []
    ip_range.append(start_ip)
    while temp != end:
        start[3] += 1
        for i in (3, 2, 1):
            if temp[i] == 256:
                temp[i] = 0
                temp[i - 1] += 1
        ip_range.append(".".join(map(str, temp)))
    return ip_range
with open('111.txt') as diap: # port list format 0.0.0.0-0.0.0.0
    for i in diap:
        start,end = i.split('-')
        ip_range = ipRange(start, end)
#for port in ports:
#    for ip in spis:
#        connScan(ip,port)
while True:
    for i in ip_range:
        p1 = threading.Thread(target=connScan, args=(i, ports[0], '222.txt'))
        p2 = threading.Thread(target=connScan, args=(i, ports[1], '8080.txt'))
        p3 = threading.Thread(target=connScan, args=(i, ports[2], '8888.txt'))
        p4 = threading.Thread(target=connScan, args=(i, ports[3], '7000.txt'))
        p5 = threading.Thread(target=connScan, args=(i, ports[4], '37000.txt'))
        p6 = threading.Thread(target=connScan, args=(i, ports[5], '34567.txt'))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        print(w)





