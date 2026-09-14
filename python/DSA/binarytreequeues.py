From collections import deque 


def levelOrder(root)
	If root is None:
		Return []; 
	queue = deque([root])
	result = []


    while queue:
        level_size = len (queue)
        level = []

        for _ in range (level_size)
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append (node.left)
            
            if node.right 
                queue.append(node.right)

        result.append(level)
    return result