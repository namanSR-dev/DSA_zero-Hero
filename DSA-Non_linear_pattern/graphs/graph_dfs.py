def dfs_graph(graph, node, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order=[]

    # we will imediately mark the node visited as soon as we reach it.
    visited.add(node)
    order.append(node)

    # In Graph unlike trees, we have more than two option (left and right) to visit,
    # Thus we use the for loop to iterate over all the neighbors of the node.
    for neighbor in graph.get(node, []):
        # we only operate over the node which is not already visited.
        if neighbor not in visited:
            dfs_graph(graph, neighbor, visited, order)
    return order


if __name__ == "__main__":

  # Adjacency list representation of graph
  graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
  }


  print("DFS traversal in the graph:- \n",dfs_graph(graph, "A"))
