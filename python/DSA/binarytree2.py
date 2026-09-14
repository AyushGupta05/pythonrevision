class Node:
    def __init__ (self,value):
        self.value = value
        self.left = None
        self.right = None


    def searchtree (node, target):

# root -    top node
# child - node below anotehr node
# parent - node above anotehr node
# leaf - node with no children
# subtree - smmaller tree inside a tree
# height - longest path from node to leaf
# depth - distance from root to node 

# tree algorithims genuinely follow this pattern

def function(node):
    if node is None:
        return

    do something with node
    function(node.left)
    function(node.right)