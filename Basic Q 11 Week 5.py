##Week 5 Task 2

##Implement the node delete function in the programming language of your choice based on the template provided

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoubleList(object):
	def __init__(self):
		self.head = None
		self.tail = None
		
	def RemoveNode(self, node):
		if node.prev != None:
			node.prev.next = node.next
		else:
			self.head = node.next
		if node.next != None:
			node.next.prev = node.next
		else:
			self.tail = node.prev
		
	def PrintList(self):
		node = self.head
		
		while node != None:
			print(node.data)
			node = node.next
			
	def AddNode(self, node, x):
		if node != None:
			x.next = node.next
			node.next = x
			x.prev = node
			if x.next != None:
				x.next.prev = x
		if self.head == None:
			self.head = self.tail = x
			x.prev = x.next = None
		elif self.tail == None:
			self.tail = x.range
	

N1 = Node(23)
N2 = Node(45)
N3 = Node(66)
list = DoubleList()
list.AddNode(None, N1)
list.AddNode(list.head, N2)
list.AddNode(list.head, N3)
list.RemoveNode(N2)
list.PrintList()
