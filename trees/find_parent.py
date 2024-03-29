
class Node:

	def __init__(self, data):
	
		self.data = data
		self.left = None
		self.right = None

def findParent(node : Node, 
			val : int, 
			parent : int) -> None:
	if (node is None):
		return

	if (node.data == val):
	
		print(parent)
	else:
	
		# Recursive calls 
		# for the children
		# of the current node
		# Current node is now 
		# the new parent
		findParent(node.left, 
				val, node.data)
		findParent(node.right, 
				val, node.data)

# Driver code
if __name__ == "__main__":

	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	node = 4
	findParent(root, node, -1)


