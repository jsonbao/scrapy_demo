#-*-coding:UTF-8-*-#
'''
Created on 2015-3-11
下载为OKB文件的再次下载
@author: wangyi
'''

#DownByDate.py sh600115 2014-12-29 2015-3-15
#DownByDate.py stock_num start_date end_date
 
#http://stock.gtimg.cn/data/index.php?appn=detail&action=download&c=sh600115&d=20141229
#sh600115_2014-12-29.txt
 
import sys
import urllib
import datetime
import os
import os.path
from os.path import getsize
import time
import socket
socket.setdefaulttimeout(20)

def listfilename(rootdir):
    fullfilename = []
    for parent,dirnames,filenames in os.walk(rootdir): 
        for filename in filenames:            
             fullfilename.append(os.path.join(parent,filename))
    return fullfilename
 
def download_date(src_url,dest_file):
    download=urllib.FancyURLopener();
    download_page=download.open(src_url);
    savefile=file(dest_file,'wb+');
    while True:
        arr = download_page.read();
        if len(arr)==0:
            break;
        savefile.write(arr);
    savefile.flush();
    savefile.close();
    return
#http://stock.gtimg.cn/data/index.php?appn=detail&action=download&c=sh002039&d=20150303#sh002039_2015-03-03.txt 
# stock_code=sys.argv[1]
# str_0='''http://stock.gtimg.cn/data/index.php?appn=detail&action=download&c='''
# str_0=str_0 + stock_code + '&d='
# date_start=datetime.datetime.strptime(sys.argv[2],'%Y-%m-%d')
# if len(sys.argv)>3:
#     date_end=datetime.datetime.strptime(sys.argv[3],'%Y-%m-%d')
# else:
#     date_end=date_start+datetime.timedelta(days=1)

str_url = "http://stock.gtimg.cn/data/index.php?appn=detail&action=download&c=%s&d=%s#%s_%s.txt" 

# str_date = ["2015-02-17"]
def kfd(currToday):
    files = listfilename("/home/wangyi/gp/DOWNCJMX/%s" % currToday)
    for filen in files:
        if getsize(filen) < 53:
            ddt = filen[-19:-11]
            ddt = '%s-%s-%s' % (ddt[:4],ddt[4:6],ddt[6:])
            fmddt = "%s%s%s" % (ddt[0:4],ddt[5:7],ddt[8:10])         
            gpdm = filen[-10:-4].lower() 
            if gpdm[0] == '0':
                gpdm = 'sz' + gpdm 
            else:
                gpdm ='sh' + gpdm
            dm = filen[-10:-4]
            url =  str_url % (gpdm,fmddt,gpdm,ddt)
            dest_file = "/home/wangyi/gp/DOWNCJMX/%s/%s-%s.txt" % (fmddt,fmddt,dm)
            try:
                download_date(url,dest_file)
            except Exception,e:
                print e
            print 'down a file: %s' % dest_file
            
if __name__ == '__main__':
#     files = listfilename("d:\\gp\\002297")
#     print files
#     print files[0]
#     print files[0][-10:-4]
#     d = files[0][-19:-11]
#     print d
#     fd = "%s-%s-%s" % (d[0:4],d[4:6],d[6:8])
#     print fd
    files = listfilename("/home/wangyi/gp/0KB")
    for filen in files:
        ddt = filen[-19:-11]
        ddt = '%s-%s-%s' % (ddt[:4],ddt[4:6],ddt[6:])
        fmddt = "%s%s%s" % (ddt[0:4],ddt[5:7],ddt[8:10])         
        gpdm = filen[-10:-4].lower() 
        if gpdm[0] == '0':
            gpdm = 'sz' + gpdm 
        else:
            gpdm ='sh' + gpdm
        dm = filen[-10:-4]
#         print fmddt
#         print ddt
#         print gpdm
#         break
        url =  str_url % (gpdm,fmddt,gpdm,ddt)
        dest_file = "/home/wangyi/gp/DOWNCJMX/%s/%s-%s.txt" % (fmddt,fmddt,dm)
#             print dest_file
#             print dm
#             break
        
        try:
            download_date(url,dest_file)
        except Exception,e:
            print e
        print 'down a file: %s' % dest_file
#             time.sleep(0.5)
        
# while date_start<date_end: 
#     str_date="date_start.strftime('%Y%02m%02d')" 
#     str_url="str_0+str_date" 
#     str_file="stock_code=" + "sz002039"  
#     date_start.strftime("%y-%02m-%02d")=""
#     download_date(str_url,str_file)
#     print date_start "date_start+datetime.timedelta(days=1)

