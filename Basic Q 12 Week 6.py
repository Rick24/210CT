##Week 6 Task 1

##Implement TREE_SORT algorithm in a language of your choice, but make sure
##that the INORDER function is implemented iteratively

class BinTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_insert( tree, item):
    if tree == None:
        tree = BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left == None):
                tree.left = BinTreeNode(item)
            else:
                tree_insert(tree.left, item)
        else:
            if(tree.right == None):
                tree.right = BinTreeNode(item)
            else:
                tree_insert(tree.right, item)
    return tree

def postorder(tree):
    if(tree.left != None):
        postorder(tree.left)
    if(tree.right != None):
        postorder(tree.right)
    print(tree.value)
  
def in_order(tree):
	list = []
	while not None:
		if tree is not None: #Reach left most Node
			list.append(tree) #Place pointer 
			tree = tree.left
		else: #Go to Node at top of stack, if stack is empty, DONE
			if (len(list) > 0): #Reach right mode Node
				tree = list.pop() #Add values to the end of tree
				print(tree.value)
				tree = tree.right
			else:
				break #Escape while loop when tree is done
  	
#def in_order(tree):
#    if(tree.left != None):
#        in_order(tree.left)
#    print(tree.value)
#    if(tree.right != None):
#        in_order(tree.right)
        
t=tree_insert(None, 6);
tree_insert(t, 10)
tree_insert(t, 5)
tree_insert(t, 2)
tree_insert(t, 3)
tree_insert(t, 4)
tree_insert(t, 11)
in_order(t)
#postorder(t)
