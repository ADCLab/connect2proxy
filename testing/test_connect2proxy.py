from connect2proxy import MyProxy

myproxy=MyProxy(configFile='proxyconfig.cfg')
myproxy.testIP()
myproxy.setProxyByRand()
myproxy.testIP()
myproxy.resetProxy()
myproxy.testIP()