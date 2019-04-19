# 简单for循环
a = [1, 2, 3, 4]
for num in a :
  print(num)
for s in 'abcd':
  print(s)
# 使用range创建list
for index in range(len(a)):
  print(index)

# 嵌套for循环
for i in range(5):
  for j in range(10):
    print('双层循环' + str(i) + str(j))
# 循环终止 
# break 跳出
# pass 占位
# continue 跳过