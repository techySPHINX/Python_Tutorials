# remove from the first of linked list
def remove_first_node(self):
    if(self.head == None):
        return
     
    self.head = self.head.next

#remove last node
def remove_last_node(self):

	if self.head is None:
		return

	current_node = self.head
	while(current_node.next.next):
		current_node = current_node.next

	current_node.next = None



# Method to remove at given index
def remove_at_index(self, index):
		if self.head == None:
			return

		current_node = self.head
		position = 0
		if position == index:
			self.remove_first_node()
		else:
			while(current_node != None and position+1 != index):
				position = position+1
				current_node = current_node.next

			if current_node != None:
				current_node.next = current_node.next.next
			else:
				print("Index not present")
				


# method to delete ndoe at given data point
def remove_node(self, data):
	current_node = self.head

	# Check if the head node contains the specified data
	if current_node.data == data:
		self.remove_first_node()
		return

	while current_node is not None and current_node.next.data != data:
		current_node = current_node.next

	if current_node is None:
		return
	else:
		current_node.next = current_node.next.next
			

	
