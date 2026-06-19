From collections import deque 


def levelOrder(root)
	If root is None:
		Return []; 
	queue = deque([root])
	result = []


    while queue:
        level_size = len (queue)
        level = []
        