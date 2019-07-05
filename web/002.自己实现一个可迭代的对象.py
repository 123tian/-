from collections import Iterable
import time
class Classmate(object):
    def __init__(self):
       self.names = list()
       self.current_num = 0

    def add(self,name):
       self.names.append(name)

    def __iter__(self):
      """如果想要一个对象成为一个可以迭代的对象（即可使用for）
      那么必须实现__iter__方法"""
      # return ClassIterator(self)
      return self

      def __next__(self):
        if self.current_num < len(self.names):
          ret = self.names[self.current_num]
          self.current_num+=1
          return ret
        else:
          raise StropIteration

# class ClassIterator(object):
#
#   def __init__(self,obj):
#      self.obj = obj
#      self.current_num = 0
#   def __iter__(self):
#      pass
#
#

classmate = Classmate()
classmate.add("名振")
classmate.add("名振")
classmate.add("名振")

for name in classmate:
  print(name)
  time.sleep(1)
