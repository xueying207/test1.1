#-coding:UTF8-*-
from api import *
from excel import *
from sjjc  import *

dir1='E:/\log/'
http="http://testpj.channel.wangpiao.com/MobileTicketWebService/WebServiceV2.asmx/"
key='Wp16dY@z^F283QVj'
deskey="eltcwang"
Des_IV = "\x12\x34\x56\x78\x90\xAB\xCD\xEF" # 自定IV向量

xls=getfile(dir1)

for i in xls:
    i= i.decode("gbk")

    print i,"准备执行"
    #try:
    api,url,ruq = apidata(dir1+i,deskey)

    url1=http+url  #生成完成接口地址
    print "请求地址为："+str(url1)
    num=0

    for  j in (api ):
        #print api
        num = num + 1
        y=mtest.getpar(url, j, key)  #生成Parameters
        #print y
        x=requtest(y,url1,ruq)
        #print x
        z= i.split(".")[0]
        runtest(num,x,z,y)
        #jc(x,y)
    print i,"用例执行完成，准备执行下一个用例"
    #except:
        #print i,"文件内容出错，请检查"
print "目录下所有用例执行完成，执行结果信息请查看日志文件"


