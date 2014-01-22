""" Implement a circular linked list """

class Node(object):

	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

	def __str__(self):
		# Node data in string form	
		return str(self.data)

class CircleLinkedList(object):

	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	# Add node to end of linked list to point to the head node
	def addNode(self, data):
		node = Node(data)
		node.data = data
		node.next = self.head
		if self.head == None:
			self.head = node
		if self.tail != None:
			self.tail.next = node
		self.tail = node
		self.length += 1

	# String representation of the circular linked list
	def __str__(self):
		list_length = self.length
		node = self.head
		node_list = [str(node.data)]
		i = 1
		while i < list_length:
			node = node.next
			node_list.append(str(node.data))
			i += 1
		return "[" + ", ".join(node_list) + "]"


def main():
	circle_ll = CircleLinkedList()
	for x in range(1, 11):
		circle_ll.addNode(x)
	print circle_ll
	

if __name__ == '__main__':
	main()