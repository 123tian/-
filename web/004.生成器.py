def create_num(all_num):
  print("------1-----")
  a,b = 0,1

  current_num = 0
  while current_num < all_num:
    print("------2-----")
    # print(a)
    yield a #如果函数当中有yield语句，那么这个就不再是函数，而是一个生成器的模板
    a,b = b, a+b
    current_num+=1
    print("------3-----")

#如果在调用函数的时候，发现函数中与yield，那么此时不再是调用函数，而是创建一生成器
obj = create_num(10)
obj2 = create_num(2)

ret = next("obj:",ret)
print(ret)

ret = next(obj)
print("obj:",ret)

# for num in obj:
#   print(num)
