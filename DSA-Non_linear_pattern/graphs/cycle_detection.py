"""
this module defines the functions to detect the cycles in the graph( directed | undirected )
time complexity : O(V+E)
space complexity : O(V)
"""

def has_cycle_undirected(graph):
    visited = set()

    # helper Dfs function
    def dfs(node, parent):

        visited.add(node) # mark node visited
        
        for neighbor in graph.get(node, []):
            # if node is parent - SKIP
            if neighbor == parent:
                continue
            
            # if node is visited and not parent : CYCLE DETECTED
            if neighbor in visited:
                return True
            
            # for not visited neighbors - run dfs check
            if neighbor not in visited:
                 if dfs(neighbor, node):
                    return True
        
        # if complete for loop run without finding the cycle - NO_CYCLE
        return False
    
    # for every unvisited node - run dfs check
    for node in graph:
        if node not in visited:
            # IF 
            if dfs(node, None):
                return True
    
    # final return after checking entire graph but didn't find the CYCLE.
    return False

def has_cycle_directed(graph):
    """
    state-store approach:
        1. not_visited : 0
        2. currently visiting ( mean currently in DFS stack ): 1
        3. already visited : 2
    """
    state = {node: 0 for node in graph}

    # helper function to perform the dfs traversal and detect the cycle.
    def dfs(node):

        # marking the node in visiting state
        state[node] = 1

        for neighbor in graph.get(node, []):
            if state.get(neighbor, 0) == 1:  # if neighbor is already in visiting state,
                return True                  # return True Cycle is found here
            
            if state.get(neighbor, 0) == 0:  # if neighbor is not visited
                if dfs(neighbor):            # perform full dfs check for that neighbor, 
                    return True              # if cycle found, return True
        
        # if cycle not found for current set of neighbors, 
        # mark current node Visited i.e flag it 2
        state[node] = 2
        return False
    
    # for each unvisited node in graph check the cycle.
    for node in graph:
        if state.get(node, 0) == 0:
            if dfs(node):
                return True
        
    return False


if __name__ == "__main__":
    # Undirected Graph with a cycle
    undirected_graph_cycle = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"]
    }

    # Undirected Graph without a cycle
    undirected_graph_no_cycle = {
        "A": ["B", "C"],
        "B": ["A"],
        "C": ["A"]
    }

    print("--- Undirected Cycle Detection ---")
    print("Graph with cycle:", has_cycle_undirected(undirected_graph_cycle))
    print("Graph without cycle:", has_cycle_undirected(undirected_graph_no_cycle))
    print()

    # Directed Graph with a cycle
    directed_graph_cycle = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]
    }

    # Directed Graph without a cycle
    directed_graph_no_cycle = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": []
    }

    print("--- Directed Cycle Detection ---")
    print("Graph with cycle:", has_cycle_directed(directed_graph_cycle))
    print("Graph without cycle:", has_cycle_directed(directed_graph_no_cycle))
