#-----------------------NOT USING ANYMORE----------(i think)------------------------
import urllib2
from bs4 import BeautifulSoup

#scraping mta right now, will switch to api if needed

def url():
  f = urllib2.urlopen('http://www.mta.info/status/serviceStatus.txt')
  return f
  
def lineNamesInfo():
  f = url()
  result = BeautifulSoup(f)
  
  #---------this should return a list of all the train names?
  lineNames1 = result.service.subway.find_next_siblings("line")
  lineNames = []
  for x in lineNames1:
	lineNames.append(x.name)
  return lineNames
  
def lineStatusInfo():
  f= url()
  result = BeautifulSoup(f)
  
  #--------this should return a list of the status of those said trains?  
  lineStatus1 = result.service.subway.find_next_siblings("line")
  lineStatus = []
  for x in lineStatus1:
	lineStatus.append(x.status)
  return lineStatus
  
#-----------------------------------TRAIN LINES---------------------------------------
def ott():
  names = lineNamesInfo()
  status = lineStatusInfo()
  OTT = (names[0], status[0]);
  return OTT #the 1, 2, and 3 
  
def ffs():
  names = lineNamesInfo()
  status = lineStatusInfo()
  FFS = (names[1], status[1]);
  return FFS #the 4, 5, and 6

def seven():
  names = lineNamesInfo()
  status = lineStatusInfo()
  SEVEN = (names[2], status[2]);
  return SEVEN #the 7

def ace():
  names = lineNamesInfo()
  status = lineStatusInfo()
  ACE = (names[3], status[3]);
  return ACE #the A, C, E

def bdfm():
  names = lineNamesInfo()
  status = lineStatusInfo()
  BDFM = (names[4], status[4]);
  return BDFM #the B, D, F, M
  
def g():
  names = lineNamesInfo()
  status = lineStatusInfo()
  G = (names[5], status[5]);
  return G #the G
  
def jz():
  names = lineNamesInfo()
  status = lineStatusInfo()
  JZ = (names[6], status[6]);
  return JZ #the J, Z
  
def l():
  names = lineNamesInfo()
  status = lineStatusInfo()
  L = (names[7], status[7]);
  return L #the L
  
def nqr():
  names = lineNamesInfo()
  status = lineStatusInfo()
  NQR = (names[8], status[8]);
  return NQR #the N, Q, R
  
def s():
  names = lineNamesInfo()
  status = lineStatusInfo()
  S = (names[9], status[9]);
  return S #the S
  
def sir():
  names = lineNamesInfo()
  status = lineStatusInfo()
  SIR = (names[10], status[10]);
  return SIR #the Staten Island Railroad
  
