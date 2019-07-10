import os
import io

from PIL import Image
from array import array
import deleter
from deleter import *



#images 

def sencode(path,password,rev):
  try:
    write(shift(readfile(path,False),password,rev),path)
  except:
    pass

def readimage(path,destroy):
  count = os.stat(path).st_size / 2
  with open(path, "rb") as f:
    ret = bytearray(f.read())
    f.close()
    if destroy:
      #construct(readfile('_rewrite_',False),path[:path.index('.')-1],path[path.index('.'):])
      os.remove(path)
    return ret

def shift(bytearr,password,reverse):

  key = []
  for let in list(password):
    key.append(ord(let))
  c = 0
  if reverse:
    for k in key:
      key[key.index(k)] = -k
  count = 0
  if key:
    for byte in bytearr:
      if count > 40:
        byte += key[c]
        b = byte%256
        bytearr[count] = b
        c+=1
        if c == len(key):
          c = 0
      count += 1
  return(bytearr)
    

    
def readfile(path,destroy):
  f = open(path,'rb')
  bytes = bytearray(f.read())
  f.close()
  if destroy:
    os.remove(path)
    delete_recycle(path,SID)
  return(bytes)

def write(bytes,name):
  f = open(name, 'wb')
  f.write(bytes)
  f.close()


def construct(bytes,name,end):
  image = Image.open(io.BytesIO(bytes))
  image.save(name+end)




def encim(name,password):
  failed = True
  try:
    write(shift(readimage(name+'.jpg',True),password,False),name)
    failed = False
  except:
    pass
  if failed:
    failed = True
    try:
      write(shift(readimage(name+'.png',True),password,False),name)
      failed = False
    except:
      pass
  if failed:
    failed = True
    try:
      write(shift(readimage(name+'.PNG',True),password,False),name)
      failed = False
    except:
      pass
  if failed:
    failed = True
    try:
      write(shift(readimage(name+'.JPG',True),password,False),name)
      failed = False
    except:
      pass
  if failed:
    print('Failed to encode',name)
  else:
    print('Encoded',name)

def ctojpg(name):
  encim(name)
  decim(name)
  


def decim(name,password):
  end = '.jpg'
  failed = True
  try:
    print('Decoding',name)
    construct(shift(readfile(name,False),password,True),name,end)
    failed = False
  except:
    pass
  if failed:
    print('Failed to decode',name)
  else:
    os.remove(name)
    delete_recycle(name,SID)
    print('Decoded',name)


def find(cur_files):
  ops = []
  for f in cur_files:
    if (f.lower().endswith('.png') or f.lower().endswith('.jpg')  ):#and not  f != '_rewrite_':
      file = ''
      for l in list(f)[:list(f).index('.')]:
        file += l
      ops.append(file)
  return ops

def nodot(cur_files):
  ops = []
  for f in cur_files:
    if (not '.' in f ):#and f != '__pycache__':
      ops.append(f)
  return ops

def notpy(cur_files):
  ops = []
  for f in cur_files:
    if( not '.py' in f ):#and f != '__pycache__' and f != '_rewrite_':
      ops.append(f)
  return ops

        
def menu(SID):
  cur_files = os.listdir(os.path.dirname(os.path.realpath(__file__)))
  s = '\\$Recycle.Bin\\'+SID
  inp = input('(E)ncode, (D)ecode, {E}ncode {A}ll, {D}ecode {A}ll, (C)lear folder or (S)afe_delete [removes all recycling bin]? ')
  if inp == 'E':
    ops = find(cur_files)
    if ops:
      print('Files that can be encoded:')
      for op in ops:
        print(op)
      nam = input()
      if nam != '_rewrite_':
        encim(nam,input())
      else:
        print('No can do, chum')
    else:
      print('No possible files')
  elif inp == 'DS':
    ops = nodot(cur_files)
    if ops:
      print('Files that can be re-encoded:')
      for op in ops:
        print(op)
      nam = input()
      rev = False
      r = input('If reversing, type any string in. Otherwise, leave blank')
      if r:
        rev = True
      if nam != '_rewrite_':
        sencode(nam,input(),rev)
    else:
      print('No possible files')

  elif inp == 'DSA':
    ops = nodot(cur_files)
    if ops:
      print('Files that can be re-encoded:')
      for op in ops:
        print(op)
      rev = False
      r = input('If reversing, type any string in. Otherwise, leave blank    ')
      if r:
        rev = True
      pas = input('Password:  ')
      for op in ops:
        if op != '_rewrite_':
          sencode(op,pas,rev)
        else:
          print('No can do, chum')
    else:
      print('No possible files')

  elif inp == 'D':
    ops = nodot(cur_files)
    if ops:
      print('Files that can be decoded:')
      for op in ops:
        print(op)
      nam = input()
      if nam != '_rewrite_':
        decim(nam,input())
      else:
        print('No can do, chum')
    else:
      print('No possible files')
  elif inp == 'EA':
    ops = find(cur_files)
    print('Files that can be encoded:')
    for op in ops:
      print(op)
    password = input('Enter a password to encode all files:  ')
    for op in ops:
      encim(op,password)
  elif inp == 'DA':
    ops = nodot(cur_files)
    print('Files that can be decoded:')
    for op in ops:
      print(op)
    password = input('Enter a password to decode all files:  ')
    for op in ops:
      if op != '_rewrite_':
        decim(op,password)
  elif inp == 'De':
    for f in s:
      try:
        delete_recycle(f,SID)
      except:
        pass
  elif inp == 'ctj':
    ops = find(cur_files)
    if ops:
      print('Files that can be encoded:')
      for op in ops:
        print(op)
      nam = input()
      if nam != '_rewrite_':
        ctojpg(nam)
      else:
        print('No can do, chum')
    else:
      print('No possible files')
  elif inp == 'C':
    ops = notpy(cur_files)
    for op in ops:
      if op != '_rewrite_' and op != '__pycache__':
        if op.endswith('.png') or op.endswith('.jpg'):
          write(readfile('_rewrite_',False),op)
        elif '.' not in op:
          write(readfile('_rewrite_',False),op)
        try:
          os.remove(op)
        except:
          pass
    for f in s:
      try:
        delete_recycle(f,SID)
      except:
        pass
  inp = input('(B)reak or press enter to stay;  ')
  if not inp == 'B':
    menu(SID)

decim('_rewrite_','allow717')

#write(readimage('_rewrite_.png',True),'_rewrite_')
#construct(readfile('_rewrite_',False),'test','.png')
SID = 'S-1-5-21-99293853-716088001-3749604325-1001'
#menu(SID)

