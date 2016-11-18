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
	stack = [] #Create empty stack
	while not None: #To represent if traversal is done
		if tree is not None: #If tree has value
			stack.append(tree) #Add to the stack
			tree = tree.left #Next node is left child
		else: 
			if (len(stack) > 0): #If stack has a value
				tree = stack.pop() #Go to last value
				print(tree.value) #Ouptut
				tree = tree.right #Next node is right child
			else: #Break out when traversal is complete
				break 
  	
#def in_order(tree):
#    if(tree.left != None):
#        in_order(tree.left)
#    print(tree.value)
#    if(tree.right != None):
#        in_order(tree.right)

def tree_sort(lst):
    t = tree_insert(None, lst[0])
    for i in lst:
        tree_insert(t, i)
    in_order(t)

lst = [2, 4, 6, 8, 9, 1, 3, 0, 5, 7]       
t=tree_insert(None, 6);
tree_insert(t, 10)
tree_insert(t, 5)
tree_insert(t, 2)
tree_insert(t, 3)
tree_insert(t, 4)
tree_insert(t, 11)
in_order(t)
#tree_sort(lst)
#postorder(t)
