# Creating a singly-linked Linked List

from random import randint
# import pdb

class Node:

	# Initialize a node
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

	# Get the node data in string form
	def __str__(self):
		return str(self.data)


class LinkedList:

	# Initialize the linked list
	def __init__(self):
		self.head = None
		self.tail = self.head
		self.length = 0

	# Add a new node to the end of the list as the new tail while changing the "old" tail to reference the new tail as next node
	def addNode(self, data):
		# initialize a new node
		node = Node(data)
		node.data = data

		# Check if there is a head node, if not then make the new node as the head & tail. Else, assign new node as next and as the tail
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

		self.length += 1

	# Add a list of nodes to the linked list
	def addManyNodes(self, list_of_data):
		for x in list_of_data:
			self.addNode(x)

	# Turn the linked list into a string
	def __str__(self):
		if self.head != None:
			value = self.head
			node_list = [str(value.data)]
			while value.next != None:
				value = value.next
				node_list.append(str(value.data))
			return "[" + ", ".join(node_list) + "]"
		return "[]"

	# Remove a node by iterating through the linked list then make the previous node point to the following node as its next node
	def removeNode(self, node_data):
		current = self.head

		if self.length == 0:
			pass

		if current.data == node_data:
			self.head = self.head.next
			self.length = self.length - 1

		while current.next != None:
			if current.next.data == node_data:
				current.next = current.next.next
				self.length = self.length - 1
				break
			else:
				current = current.next

	# Remove a list of nodes from the linked list
	def removeManyNodes(self, list_of_data):
		for x in list_of_data:
			self.removeNode(x)

	# Check if node is in the linked list
	def hasNode(self, node_data):
		current = self.head

		while current != None:
			if current.data == node_data:
				return True
			else:
				current = current.next
		return False

	# Figure out the index of a node in the linked list. Make the head an index of 0
	def nodeIndex(self, node_data):
		current = self.head
		index_num = 0

		while current != None:
			if current.data == node_data:
				return index_num
			else:
				current = current.next
				index_num = index_num + 1
		return index_num

	# Figure out the size/length of the linked list
	def listLength(self):
		return self.length


	# Reverse a linked list non-recursively (iteratively)
	def reverseIter(self):
		current = self.head
		self.tail = self.head
		next = current.next
		# print "-->Current is %r and Next is %r." % (current.data, next.data)
		# print "-->Current.next is %r." % current.next.data
		while current.next != None:
			current = next
			next = current.next
			current.next = self.head
			self.head = current
		return linked_list

""" Functions to mess around with the linked list """

# Remove duplicates from linked list using a dictionary
def remDuplicates(linked_list):
	if linked_list.head != None:
		current = linked_list.head
		dic = {current.data: True}
		while current.next != None:
			if current.next.data in dic:
				current.next = current.next.next
				linked_list.length = linked_list.length - 1
			else:
				dic[current.next.data] = True
				current = current.next
			if current.next == None:
				linked_list.tail = current


""" Create the linked list """
if __name__ == '__main__':
	linked_list = LinkedList()
	data_list = list(range(1, 6))
	linked_list.addManyNodes(data_list)
	print "Linked List:\n" + str(linked_list)
	print "Non-Recursive Reversal:\n" + str(linked_list.reverseIter())
	# print "Size of the linked list: " + str(linked_list.listLength()
	# print "T/F: The linked list has a node with data of 6..." + str(linked_list.hasNode(6))













