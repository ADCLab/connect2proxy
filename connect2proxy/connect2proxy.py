from pandas import read_csv
from platform import system
import os
import requests
import yaml
import pkgutil
import io

def splitString(cVal,defaultVal=None):
    try:
        val=cVal.split(',')
        if val==['']:
            val=defaultVal
    except:
        val=defaultVal
    return val
            


class MyProxy:
    def __init__(self,configFile=None,proxies=None,user=None,passwd=None,restrictCountries=None,restrictRegions=None,randomize=True,trackUsed=True):
        if proxies is None:
            allProxies=read_csv(  io.BytesIO( pkgutil.get_data(__name__, 'proxies_latest.csv')  )  )
        else:
            allProxies=read_csv(proxies)
            
        if isinstance(configFile,str):
            with open(configFile, 'r') as stream:
                config = yaml.safe_load(stream)
                
            user=config['user']
            passwd=config['passwd']
            useCountries=splitString(config['useCountries'])
            useRegions=splitString(config['useRegions'])
            trackUsed=config['passwd']
            randomize=config['randomize']

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
            
        