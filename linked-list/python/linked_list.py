from node import *

class LinkedList:
  __slots__ = ('__first', '__size')

  def __init__(self, first=None, size=0):
    self.first = first
    self.size = size

  @property
  def first(self):
    return self.__first
  
  @first.setter
  def first(self, value):
    self.__first = value

  @property
  def size(self):
    return self.__size
  
  @size.setter
  def size(self, value):
    self.__size = value

  def add(self, value):
    '''This implementation adds an element to the end
    of the list'''
    new = Node(value)
    if (self.first == None):
      self.first = new
      self.size += 1
      return
    else:
      last = self.first
      while (last.next != None):
        last = last.next
      last.next = new
      self.size += 1

  def find(self, element):
    if (self.size == 0):
      return 'element not found'
    else:
      curr = self.first
      i = 0
      while (curr != None):
        if (curr.element == element):
          return i
        else:
          i += 1
          curr = curr.next
      return 'element not found'
