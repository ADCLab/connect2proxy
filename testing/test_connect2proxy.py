from connect2proxy import MyProxy

myproxy=MyProxy(configFile='proxyconfig.yml')
myproxy.testIP()
myproxy.setProxyByRand()
myproxy.testIP()
myproxy.resetProxy()
myproxy.testIP()