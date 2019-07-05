def create_num(all_num):
  a,b = 0,1
  current_num = 0
  while current_num < all_num:
    yield a
    a,b = b, a+b
    current_num+=1
    return ok

obj2 = create_num(20)

while True:
  try:
    ret = next(obj2)
  except Exception as ret:
    print(ret.value)
    break



# ret = next(obj2)
# print("obj2",ret)
