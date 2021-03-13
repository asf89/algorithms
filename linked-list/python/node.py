class Node:
  __slots__ = ('__element', '__next')

  def __init__(self, element=None, next=None):
    self.element = element
    self.next = next

  @property
  def element(self):
    return self.__element

  @element.setter
  def element(self, element):
    self.__element = element

  @property
  def next(self):
    return self.__next
  
  @next.setter
  def next(self, next):
    self.__next = next
