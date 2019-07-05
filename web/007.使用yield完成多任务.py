import time

def task_1():
  while True:
    print("---1----")
    time.sleep(0.1)
    yield

def task_2():
  while True:
    print("---2----")
    time.sleep(0.1)


def main():
  #此时并非函数调用，而是创建生成器
  t1 = task_1()
  t2 = task_2()
  while True:
    next(t1)
    next(t2)



if __name__ == '__main__':
    main()

#并行（真多任务）：多个任务，一个任占一个 核
#并行（假多任务）：多个任务，只有四个核，假体执行

