from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

proxy = {'address': '123.123.123.123:2345',
         'username': 'johnsmith123',
         'password': 'iliketurtles'}


capabilities = dict(DesiredCapabilities.CHROME)
capabilities['proxy'] = {'proxyType': 'MANUAL',
                         'httpProxy': proxy['address'],
                         'ftpProxy': proxy['address'],
                         'sslProxy': proxy['address'],
                         'noProxy': '',
                         'class': "org.openqa.selenium.Proxy",
                         'autodetect': False}

capabilities['proxy']['socksUsername'] = proxy['username']
capabilities['proxy']['socksPassword'] = proxy['password']

driver = webdriver.Chrome(executable_path=[path to your chromedriver], desired_capabilities=capabilities)
dirver.get(https://wieistmeineip.de/)
