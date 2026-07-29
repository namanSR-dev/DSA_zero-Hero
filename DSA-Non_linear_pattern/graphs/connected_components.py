def connected_components(graph):
    visited = set()
    component_count = 0

    # Helper to populate the visited set
    def populate_visited(graph, node):
      visited.add(node)
      for neighbor in graph.get(node, []):
        if neighbor not in visited:
            populate_visited(graph, neighbor)

    # check each node in the graph
    for node in graph:
        if node not in visited:
            populate_visited(graph, node)
            component_count += 1
    
    return component_count
   



if __name__ == "__main__":

  # Adjacency list representation of graph
  graph = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["E"],
    "E": ["D"],
    "F": []
  }


  print("connnected components in the graph:- \n",connected_components(graph))
