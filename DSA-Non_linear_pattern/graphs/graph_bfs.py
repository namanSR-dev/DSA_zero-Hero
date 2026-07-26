from collections import deque

def bfs_graph(graph, node):

    # 1. initialization 
    visited = set()
    order = []
    q = deque()

    # 2. base case: handling the first node
    visited.add(node)
    order.append(node)
    q.append(node)
    
    # 3. processing the nodes until queue is empty
    while q:

        # Optimization : If the no. of visited nodes is equal to the total number of nodes in the graph,
        # we can stop the process since we have already visited all the nodes. --- [ why: see the debug ]
        if len(visited) == len(graph):
            break
        
        # 4. take the first node out of the queue for processing it ( i.e visiting its neighbors ).
        curr = q.popleft()

        # debug: checking unnecisary node visits :- 
        # print(f"current node:{curr} \n queued items : {q} \n visited set : {visited} \n traversed node so far: {order} \n#==========================#\n")
        # Result - redundand node visits are found, we don't need to process each node in the queue since only processing few node we can completely visit all the nodes in the graph.

        # 5. visiting all the neighbors and sequentially adding then into result and the processing queue and marking the visited
        for neighbor in graph.get(curr, []):
            if neighbor not in visited:
                visited.add(neighbor)
                order.append(neighbor)
                q.append(neighbor)
    
    return order
if __name__ == "__main__":

#
    graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
  }
  
print(bfs_graph(graph, "A"))

    

        

    