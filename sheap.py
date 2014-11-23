class SHeap:

  def getparent(self, i):
    if i==0:
      return -1
    else:
      return int(i/2)

  def __init__(self, _array=[]):
    self.array = _array[:]

  def swap(self, i, j):
    self.array[i], self.array[j] = self.array[j], self.array[i]

  def push(self, n):
    self.array.append(n)
    self.bubbleup()

  def pop(self):
    el = self.array[0]
    self.array[0] = self.array[-1]
    del self.array[-1]
    self.bubbledown()
    return el

  def __str__(self):
    return str(self.array)

  #to be implemeted in a subclass
  def get_child_pos(self, i):
    raise NotImplementedError()

  def bubbleup(self):
    raise NotImplementedError()

  def bubbledown(self):
    raise NotImplementedError()

class SMinHeap(SHeap):

  def get_child_pos(self, i):
    ch1, ch2 = 2*i, 2*i+1
    l_ok = ch1<len(self.array)
    r_ok = ch2<len(self.array)
    if l_ok and (not r_ok or (r_ok and self.array[ch1]<self.array[ch2]) )  :
      return ch1
    elif r_ok and (not l_ok or (l_ok and not self.array[ch1]<self.array[ch2])):
      return ch2
    return -1

  def bubbleup(self):
    pos = len(self.array)-1
    parent = self.getparent(pos)
    while parent!=-1 and self.array[pos] < self.array[parent]:
      self.swap(pos, parent)
      pos = parent
      parent = self.getparent(pos)

  def bubbledown(self):
    pos = 0
    child = self.get_child_pos(pos)
    while child!=-1 and self.array[pos] > self.array[child]:
      self.swap(pos, child)
      pos = child
      child = self.get_child_pos(pos)

class SMaxHeap(SHeap):

  def get_child_pos(self, i):
    ch1, ch2 = 2*i, 2*i+1
    l_ok = ch1<len(self.array)
    r_ok = ch2<len(self.array)
    if l_ok and (not r_ok or (r_ok and self.array[ch1]>self.array[ch2]) )  :
      return ch1
    elif r_ok and (not l_ok or (l_ok and not self.array[ch1]>self.array[ch2])):
      return ch2
    return -1

  def bubbleup(self):
    pos = len(self.array)-1
    parent = self.getparent(pos)
    while parent!=-1 and self.array[pos] > self.array[parent]:
      self.swap(pos, parent)
      pos = parent
      parent = self.getparent(pos)

  def bubbledown(self):
    pos = 0
    child = self.get_child_pos(pos)
    while child!=-1 and self.array[pos] < self.array[child]:
      self.swap(pos, child)
      pos = child
      child = self.get_child_pos(pos)