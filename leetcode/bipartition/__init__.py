from typing import List
from collections import deque

def isBipartite(self, graph: List[List[int]]) -> bool:
    root = graph[0]
    colors = {root: 0}
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if colors.node[]

