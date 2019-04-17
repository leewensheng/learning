a = [1,2,3,2]
b = (1,2,3,4,5)
print(len(a))
print(a.count(2))
print(max(a))
print(min(a))
print(list(b))

def square(x):
  return x*x
arrmap = map(square, a)
print(list(arrmap))
print(type(33))