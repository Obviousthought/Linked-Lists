# Creating a singly-linked Linked List

from random import randint
# import pdb

class Node(object):

	# Initialize a node
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next


	def __str__(self):
		# Node data in string form	
		return str(self.data)


class LinkedList(object):

	# Initialize the linked list
	def __init__(self):
		self.head = None
		self.tail = self.head
		self.length = 0

	# Add a new node to the end of the linked list
	def addNode(self, data):
		# Initialize a new node
		node = Node(data)
		node.data = data

		# Assign new node (check if there is a head node)
		if self.head == None:
			self.head = node
		if self.tail != None:
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

	def reverseIter(self):
		self.tail = self.head
		current = self.head.next
		temp = current.next
		self.head.next = None
		while temp.next:
			current.next = self.head
			self.head = current
			current = temp
			temp = temp.next
		current.next = self.head
		self.head = temp
		self.head.next = current

##### Functions to mess around with the linked list #####

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

# Create a randomized linked list
def randomLinkedList(length, min, max):
    linkedlist = LinkedList()
    for x in range(length):
        node_data = randint(min, max)
        linkedlist.addNode(node_data)
    return linkedlist



""" Create the linked list """

def main():
	linked_list = LinkedList()
	data_list = list(range(1, 6))
	linked_list.addManyNodes(data_list)
	print "Linked List: " + str(linked_list)
	linked_list.reverseIter()
	print "Reverse: " + str(linked_list)
	# print "Non-Recursive Reversal:\n" + str(linked_list.reverseIter())
	# print "Size of the linked list: " + str(linked_list.listLength()
	# print "T/F: The linked list has a node with data of 6..." + str(linked_list.hasNode(6))
	# random_list = randomLinkedList(100,1,100)	


if __name__ == '__main__':
	main()