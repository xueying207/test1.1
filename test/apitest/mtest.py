#coding=utf-8
import demjson
import hashlib
import base64
from pyDes import *


def getpar(APIName,data,key):
    #m=hashlib.md5()
    data1={}
    data2={}
    data3={}
    data1["APIName"]=str(APIName)
    data1["Parameters"] = [data]
    data3["InputData"]=[data1]
    #{'UserName': 'Androidwangpiao', 'Password': '7cPOdDWnewc=', 'Parameters': '{"InputData":[{"APIName":"GetFilmHotAndReflected","Parameters":[{"CityID":"1","Type":"1"}]}]}', 'Sign': 'c61bbf3eb72814ade804b557b8db25e3'}
    data3=demjson.encode(data3)
    #key='Wp16dY@z^F283QVj'
    m=hashlib.md5()
    x=data3+key
    #print x
    m.update(x)
    json1 = m.hexdigest()
    #print json1
    data2['UserName']= 'Androidwangpiao'
    data2[ 'Password']= '7cPOdDWnewc='
    data2[ 'Parameters']=str(data3)
    data2['Sign']= json1
    #data4={'UserName': 'Androidwangpiao', 'Password': '7cPOdDWnewc=', 'Parameters':data1,'Sign': 'c61bbf3eb72814ade804b557b8db25e3'}
    #data5=demjson.encode(data4)
    return data2

#Des_IV =  # 自定IV向量


def wpdes(str,Des_Key):
    from run import Des_IV
    k =des(Des_Key, CBC,Des_IV, padmode=PAD_PKCS5)

    EncryptStr = k.encrypt(str)
    #print "Encrypted: " , EncryptStr

    return base64.b64encode(EncryptStr) #转base64编码返回

