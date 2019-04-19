try :
  fh = open('/fff.txt','w+')
  fh.write('这是一个测试文件')
except:
  print('ERROR')
else: 
  print('sucess')