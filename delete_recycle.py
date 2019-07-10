import os

def recycle_delete(targ,SID):
  s = '\\$Recycle.Bin\\'+SID
  di = os.listdir(s)
  if targ == None:
    for file in di:
      f = s+'\\'+file
      os.remove(f)
  else:
    for file in di:
      if file == targ:
        f = s+'\\'+file
        os.remove(f)
        
#davidcantcrackthis
