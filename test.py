import os
from encoder import *
import time

def testSpeed():
  cur_files = os.listdir(os.path.dirname(os.path.realpath(__file__)))
  test = 'abcdefghijhijklmnopqrstuvwxyz'
  decode_times = []
  for i in range(20):
    now = time.time()
    ops = nodot(cur_files)
    if ops:
      #print('Files that can be decoded:')
      #for op in ops:
      #  print(op)
      try:
        nam = 'secretImage'#input()
        if nam != '_rewrite_':
          decim(nam,test[:i])#input())
        else:
          print('No can do, chum')
      except:
        pass
    else:
      print('No possible files')
    later = time.time()
    print('Atempted decode time for',i+1,'letter code',later-now)
    decode_times.append(later-now)
  tot = 0
  for val in decode_times:
    tot += val
  av = tot/20
  print('Average',av)

testSpeed()
