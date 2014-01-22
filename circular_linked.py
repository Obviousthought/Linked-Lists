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

	
	def addNode(self, data):
		# Add node to end of linked list to point to the head node to create/connect circle
		node = Node(data)
		node.data = data
		node.next = self.head
		if self.head == None:
			self.head = node
		if self.tail != None:
			self.tail.next = node
		self.tail = node
		self.length += 1

	def __str__(self):
		# String representation of circular linked list
		list_length = self.length
		node = self.head
		node_list = [str(node.data)]
		i = 1 									# head node has already been added to the list
		while i < list_length:
			node = node.next
			node_list.append(str(node.data))
			i += 1
		return "->" + "->".join(node_list) + "->"



## Function to determine if a linked list has a loop ##

def circularLink(linked_list):
	fast = linked_list.head
	slow = linked_list.head
	while fast != slow and fast != None:
		fast = fast.next.next
		slow = slow.next
	if fast == slow:
		return True
	else:
		return False



""" Create the Circular Linked List """

def main():
	circle_ll = CircleLinkedList() 				# Create empty circular linked list
	for x in range(1, 101): 					# Populate with 100 nodes
		circle_ll.addNode(x)
	print circle_ll 							# Display list as string
	

if __name__ == '__main__':
	main()