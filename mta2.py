import urllib2
from bs4 import BeautifulSoup

#scraping mta right now, will switch to api if needed

def url():
  f = urllib2.urlopen('http://www.mta.info/status/serviceStatus.txt')
  return f
  
def ott():
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  return first_line.status.string

def ffs():
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,1):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def seven():
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,2):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def ace():
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,3):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def bdfm():
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,4):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def g():
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,5):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def jz():
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,6):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def l():
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,7):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def nqr():
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,8):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def s():
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,9):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def sir():
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,10):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string