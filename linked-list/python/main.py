from linked_list import *

def main():
  linkedList = LinkedList()
  linkedList.add(1)
  linkedList.add(2)
  linkedList.add(3)
  linkedList.add(4)
  linkedList.add(5)

  print(f'the size is: {linkedList.size}')
  print(f'index of element 4: {linkedList.find(4)}')

if __name__ == '__main__':
  main()
