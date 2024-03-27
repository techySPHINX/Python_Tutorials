
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



# insertion at the beginnning
        
def insertAtBegin(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    else:
        new_node.next = self.head
        self.head = new_node


# insertion at the end
        
  
def inserAtEnd(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
 
    current_node = self.head
    while(current_node.next):
        current_node = current_node.next
 
    current_node.next = new_node    


 #insertion at the position
    
def insertAtIndex(self, data, index):
    new_node = Node(data)
    current_node = self.head
    position = 0
    if position == index:
        self.insertAtBegin(data)
    else:
        while(current_node != None and position+1 != index):
            position = position+1
            current_node  = current_node.next

        if current_node != None:
            new_node.next = current_node.next
            current_node.next  = new_node
        else:
            print("Index not present")


  
