import requests
import json


def loadBaseMap(url):
    return

def autoNavigation():
    url='http://restapi.amap.com/v3/ip?key=43a462f629d817bf91ca4bb95f9cd7b3&ip=202.204.105.195'
    response=requests.get(url)
    locationInfor=json.loads(response.text)

    return locationInfor

def getPreciseLocation(locationInfor):
    rec=locationInfor['rectangle']
    x1=rec[0:11]
    y1=rec[12:23]
    x2=rec[24:35]
    y2=rec[36:47]
    x=(float(x1)+float(x2))/2
    y=(float(y1)+float(y2))/2
    return x,y

