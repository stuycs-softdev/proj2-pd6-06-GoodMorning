import urllib2
from bs4 import BeautifulSoup

#scraping mta right now, will switch to api if need be

def url():
  f = urllib2.urlopen('http://www.mta.info/status/serviceStatus.txt')
  return f
  
def info():
  f = url()
  result = BeautifulSoup(f)
  
  #---------this should return a list of all the train names?
  lineNames = soup.service.subway.findNextSibling('line').name

  #--------this should return a list of the status of those said trains?  
  lineStatus = soup.serive.subway.findNextSibling('line').status

  
  #--------thinking about buses, but that will be for later
  
