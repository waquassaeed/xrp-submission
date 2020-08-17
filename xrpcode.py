import requests
import json
import time
import csv
from datetime import datetime

URL = "https://s1.ripple.com:51234"
INTERVAL = 4
TotalCount = 10

def myPeriodicFunction():
    payload = "{\"method\":\"server_info\",\"params\":[{}]}"
    r = requests.get(url=URL, data=payload)
    data = r.text
    jdata = json.loads(data)
    datapoint = str(jdata['result']['info']['time']) + ',' + str(jdata['result']['info']['validated_ledger']['seq']) + '\n'
    return datapoint

def getTimeSeq():
  dataplot = ''
  fopen = open("data.csv", "r")
  read = csv.reader(fopen)
  exdata = list(read)
  for item in range(len(exdata)):
    text = str.split(exdata[item][0])[1]
    dataplot += text.split(".")[0] + ',' + exdata[item][1] + '\n'
  
  fwrite = open("dataplot.csv", "w+")
  fwrite.write(dataplot)
  print("File created for data plotting [dataplot.csv]" + '\n')
  fwrite.close()


def startTimer():
    count = 0
    datapoints = ''
    
    while count < TotalCount:
        datapoints += myPeriodicFunction()
        time.sleep(INTERVAL)
        count += 1
    
    print("Data (method: server_info): Ledger Time and Sequence Number" + '\n')
    print(datapoints)
    f = open("data.csv", "w+")
    f.write(datapoints)
    print("File created for data set [data.csv]" + '\n')
    f.close()

def dataManipulation():

  lstMinMax = []
  DupNonDup = 1
  fo = open("data.csv", "r")
  read = csv.reader(fo)
  exdata = list(read)

  for i in range(len(exdata)):
    if i == 0:
      continue

    if exdata[i][1] == exdata[i-1][1]:
      DupNonDup = 2
      continue
    else:
      time1 = datetime.strptime(exdata[i][0], '%Y-%b-%d %H:%M:%S.%f %Z')
      time2 = datetime.strptime(exdata[i-DupNonDup][0], '%Y-%b-%d %H:%M:%S.%f %Z')
      timediff = time1 - time2
      lstMinMax.append(timediff)
    
    if DupNonDup == 2:
      DupNonDup = 1


  print("Minimum Time: " + str(min(lstMinMax)) + '\n')
  print("Maximum Time: " + str(max(lstMinMax)) + '\n')

  tot = 0
  avgdata= list(lstMinMax)

  for itr in range(len(avgdata)):
    ttime = datetime.strptime(str(avgdata[itr]), '%H:%M:%S.%f')
    tot += ttime.time().second
  
  print("Average Time: " + str(tot / len(avgdata)) + '\n')
  fo.close()

startTimer()
dataManipulation()
getTimeSeq()
