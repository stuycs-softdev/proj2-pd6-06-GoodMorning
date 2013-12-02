import urllib2
from bs4 import BeautifulSoup

#scraping mta right now, will switch to api if needed
#only have trains, no buses

def url():
  f = urllib2.urlopen('http://www.mta.info/status/serviceStatus.txt')
  return f
  
def ott(): #-------THE 1, 2, 3
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  return first_line.status.string

def ffs(): #---------THE 4, 5, 6
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,1):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def seven(): #------THE 7
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,2):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def ace(): #-----THE A, C, E
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,3):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def bdfm(): #-----THE B, D, F, M
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,4):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def g(): #--------THE G
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,5):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def jz(): #-----THE J, Z
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,6):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def l(): #-----THE L
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,7):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def nqr(): #----THE N, Q, R
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,8):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def s(): #--------THE S
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,9):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string

def sir(): #-----THE STATEN ISLAND RAILROAD
  f = url()
  result = BeautifulSoup(f)
  first_line = result.line
  for x in range (0,10):
	nextLine = first_line.find_next_sibling("line")
  return nextLine.status.string
