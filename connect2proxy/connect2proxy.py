from pandas import DataFrame, read_csv
from configparser import ConfigParser
from platform import system
import os
import requests

def configParserFillNone(config,section,key,defaultVal=None):
    try:
        val=config[section][key].split(',')
        if val==['']:
            val=defaultVal
    except:
        val=defaultVal
    return val
            


class MyProxy:
    def __init__(self,configFile=None,proxies='proxies_latest.csv',user=None,passwd=None,restrictCountries=None,restrictRegions=None,randomize=True,trackUsed=True):
        allProxies=read_csv(proxies)
        if isinstance(configFile,str):
            config=ConfigParser(allow_no_value=True)
            config.read(configFile)
            user=configParserFillNone(config,'login','user')[0]
            passwd=configParserFillNone(config,'login','passwd')[0]
            useCountries=configParserFillNone(config,'regions','useCountries')
            useRegions=configParserFillNone(config,'regions','useRegions')
            trackUsed=eval(configParserFillNone(config,'cycling','trackUsed',True)[0])
            randomize=eval(configParserFillNone(config,'cycling','randomize',True)[0])

        self.user=user
        self.passwd=passwd
        self.trackUsed=trackUsed
        self.randomize=randomize

        if useCountries is not None:
            self.useProxies=allProxies[allProxies['Country'].isin(useCountries)]
        elif useRegions is not None:
            self.useProxies=allProxies[allProxies['Region'].isin(useRegions)]
        else:
            self.useProxies=allProxies.copy()
        self.useableProxies=self.useProxies.copy()
        if len(self.useProxies)==0:
            raise NameError('No country or region by that name.')            
        self.os=system()
            
    def setProxyByURL(self,url,port=7070):
        proxy_http= 'http://%s:%s@%s:%d'%(self.user,self.passwd,url,port)
        proxy_https = 'https://%s:%s@%s:%d'%(self.user,self.passwd,url,port)

        # print(proxy_https)
        self.proxy_url={'http':proxy_http,'https':proxy_https}
        os.environ['http_proxy'] = proxy_http 
        os.environ['https_proxy'] = proxy_https
        if system()!='Windows':
            os.environ['HTTP_PROXY'] = proxy_http
            os.environ['HTTPS_PROXY'] = proxy_https
        
    def resetProxy(self):
        del os.environ['http_proxy'] 
        del os.environ['https_proxy']
        if system()!='Windows':
            del os.environ['HTTP_PROXY']
            del os.environ['HTTPS_PROXY']
        self.proxy_url=None
        
    def setProxyByRand(self):
        if len(self.useableProxies)==0:
            self.useableProxies=self.useProxies.copy() 
        self.currentProxy=self.useableProxies.sample()
        self.setProxyByURL(url=self.currentProxy.iloc[0]['Hostnames'])
        if self.trackUsed:
            self.useableProxies.drop(labels=self.currentProxy.index[0],inplace=True)
        
    def testIP(self):
        response = requests.get("https://api.myip.com/")
        print(response.text)
            
        