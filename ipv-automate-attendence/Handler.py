'''
Created on Feb 10, 2017

@author: mdshihabuddin
'''
from httplib2 import debuglevel
url = "https://www.facebook.com/"
username = "+8801914288017"
password = "01914288017"

import urllib
import urllib2
import cookielib

class LoginHandler():
    def __init__(self, url, username, password):
        self.url = url
        self.values = { 'email' : username,
                        'pass' : password
                        }
    
    def login(self):
        data = urllib.urlencode(self.values)
        cookies = cookielib.CookieJar()
        opener = urllib2.build_opener(
                   urllib2.HTTPRedirectHandler(),
                   urllib2.HTTPHandler(debuglevel = 0),
                   urllib2.HTTPSHandler(debuglevel=0),
                   urllib2.HTTPCookieProcessor(cookies))
        response = opener.open(self.url, data)
        page = response.read()
        http_headers = response.info()
        
        print page
        print "//////////////////////////print header //////////////////////"
        print http_headers
# opener = urllib2.build_opener(
#     urllib2.HTTPRedirectHandler(),
#     urllib2.HTTPHandler(debuglevel=0),
#     urllib2.HTTPSHandler(debuglevel=0),
#     urllib2.HTTPCookieProcessor(cookies))
# 
# response = opener.open(url, data)
# the_page = response.read()
# http_headers = response.info()
    
if __name__ == '__main__':
    loginObj = LoginHandler(url, username, password)
    loginObj.login()
    pass