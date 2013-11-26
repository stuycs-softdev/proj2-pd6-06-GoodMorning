import urllib2
from bs4 import BeautifulSoup

def url():
  f = urllib2.urlopen('http://www.mta.info/status/serviceStatus.txt')
  return f
  
def test():
  f = url()
  result = BeautifulSoup(f)
