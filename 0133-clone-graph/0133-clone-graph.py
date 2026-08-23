"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone = {}
        clone[node] = Node(node.val, [])

        queue = deque([node])
        while queue:
            cur = queue.popleft()
            for neig in cur.neighbors:
                if neig not in clone:
                    clone[neig] = Node(neig.val, [])
                    queue.append(neig)
                clone[cur].neighbors.append(clone[neig])
        return clone[node]

        