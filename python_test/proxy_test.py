#-*-coding:utf-8-*-  
import urllib2,re,time,urllib,proxyIP,random,user_agents


def getHtml(url):
    proxy_ip =random.choice(proxyIP.proxy_list) #在proxy_list中随机取一个ip
    print proxy_ip    
    proxy_support = urllib2.ProxyHandler(proxy_ip)
    opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    request = urllib2.Request(url)
    user_agent = random.choice(user_agents.user_agents)  #在user_agents中随机取一个做user_agent
    request.add_header('User-Agent',user_agent) #修改user-Agent字段
    print user_agent
    html = urllib2.urlopen(request).read()
    return proxy_ip
urls = ['http://music.douban.com/subject/1403307/','http://music.douban.com/subject/1403832/']
count_True,count_False,count= 0,0,0
while True:
    for url in urls:
        count +=1
        try:
            proxy_ip=getHtml(url)            
        except urllib2.URLError:
            print 'URLError! The bad proxy is %s' %proxy_ip
            count_False += 1
        except urllib2.HTTPError:
            print 'HTTPError! The bad proxy is %s' %proxy_ip
            count_False += 1
        except:
             print 'Unknown Errors! The bad proxy is %s ' %proxy_ip 
             count_False += 1
        #randomTime = random.uniform(1,3) #取1-10之间的随机浮点数
        #time.sleep(randomTime) #随机等待时间
        print '%d Eroors,%d ok,总数 %d' %(count_False,count - count_False,count)
        ######################

#上面引入模块中：proxyIP、user_agents内容如下：

######################



#!/usr/bin/python
#-*- conding:utf-8 -*-



###########################



#!/usr/bin/python
