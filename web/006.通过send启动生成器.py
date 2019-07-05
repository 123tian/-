def create_num(all_num):

  a,b = 0,1

  current_num = 0
  while current_num < all_num:
    ret = yield a
    print("---ret------",ret)

    yield a
    a,b = b, a+b
    current_num+=1

#如果在调用函数的时候，发现函数中与yield，那么此时不再是调用函数，而是创建一生成器
obj = create_num(10)
#如果已创建生成器就send会报错，yeild,也没有ret去接受
obj.send(None)

ret = next(obj)
print("obj:",ret)

ret = obj.send(None)
print(ret)
