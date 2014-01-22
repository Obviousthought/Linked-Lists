# Build a circular linked list with 100 nodes and write a function
# that removes every other node, starting with the 1st then 3rd and so on, 
# then loops through until there is one surviving node and returns it.
# Problem known as the Josephus Permutation. Can be solved with this code:
			  # def josephus_2( n ):
			  #   from math import log
			  #   return 2*(n - 2**(int(log(n,2))))+1
# But let's have fun with Circular Linked Lists, shall we?


""" Circular Linked List Class Implementation """


class Node(object):

	def __init__(self, data = None, next = None):
		# Initialize a node to contain a value (data) and a reference point (next)
		self.data = data
		self.next = next

	def __str__(self):
		# String representation of the data point
		return str(self.data)


class CircleLinkedList(object):

	def __init__(self):
		# Initialize a circular linked list
		self.head = None
		self.tail = None
		self.length = 0

	def addNode(self, data):
		# Add a node as the new tail that points to the head node to create/connect the circle
		# Since working with a sorted list to 100, no need for specific insert code
		node = Node(data)
		node.data = data
		node.next = self.head
		if self.head == None:
			self.head = node
		if self.tail != None:
			self.tail.next = node
		self.tail = node
		self.length += 1
	
	def remAltNodes(self):
		# Remove alternate nodes by removing the reference to them
		if self.length != None:
			node = self.tail 					# Pointer at tail so removals will be in correct order
			while node.next != node:
				node = node.next.next			# Skip a node
				self.tail.next = node 			# Tail reference also skips that node
				self.tail = node 				# Reassign tail to start process over
				self.length = self.length - 1 	# Downsize length for permament removal in list
			self.head = node 					
			self.tail = node 					# Reassign head and tail to re-connect the circle
			return node

		# Run time of removing alternate nodes is O(n)
		# Time complexity will be more apparent in linked lists with over 10,000 nodes



""" Run the main program """

def main():
	circle_ll = CircleLinkedList() 				# Create an empty circular linked list
	for x in range(1, 101): 					# Populate list with 100 nodes ("chairs")
		circle_ll.addNode(x)	
	print circle_ll.remAltNodes() 				# Run function and display surviving node


if __name__ == '__main__':
	main()