from collections import deque

def h(n, start_node, parents) -> int:
    '''
    heristic function based on number of step taken from start node to node n
    '''
    reconst_path = []
    while parents[n] != n:
        reconst_path.append(n)
        n = parents[n]
    # number of steps excluding the starting node
    return len(reconst_path)

def a_star_search(graph: dict, start, end) -> list:
    '''
    Function to find path from start node to end node by using A* Search
    '''
    # open_list is a list of nodes which have been visited, but who's neighbors
    # haven't all been inspected, starts off with the start node
    # closed_list is a list of nodes which have been visited
    # and who's neighbors have been inspected
    open_list = set([start])
    closed_list = set([])

    # g contains current distances from start_node to all other nodes
    # the default value (if it's not found in the map) is +infinity
    g = {}

    g[start] = 0

    # parents contains an adjacency map of all nodes
    parents = {}
    parents[start] = start

    while len(open_list) > 0:
        n = None

        # find a node with the lowest value of f() - evaluation function
        for v in open_list:
            if n == None or g[v] + h(v, start, parents) < g[n] + h(n, start, parents):
                n = v

        if n == None:
            print('Path does not exist!')
            return None

        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n == end:
            print(f"Total cost: {g[n] + h(n, start, parents)}")
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start)
            reconst_path.reverse()
            return reconst_path

        # for all neighbors of the current node do
        for (m, weight) in graph[n]:
            # if the current node isn't in both open_list and closed_list
            # add it to open_list and note n as it's parent
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight

            # otherwise, check if it's quicker to first visit n, then m
            # and if it is, update parent data and g data
            # and if the node was in the closed_list, move it to open_list
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_list.remove(n)
        closed_list.add(n)

    print('Path does not exist!')
    return None


def bfs(graph_to_search: dict, start: int, end: int) -> list:
    '''
    This is the function to perform breath-first search
    '''
    queue = deque([[start]])

    while queue:
        # Gets the first path in the queue
        path = queue.popleft()

        # Gets the last node in the path
        vertex = path[-1]

        # Checks if we got to the end
        if vertex == end:
            return path
        # check all adjacent nodes, construct a new path and push it into the queue
        # excluded neightbors that are already visited
        for current_neighbour in graph_to_search.get(vertex, []):
            if current_neighbour not in path:
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)


def dfs(graph_to_search: dict, start: int, end: int) -> list:
    '''
    This is the function to perform depth-first search
    '''
    queue = deque([[start]])

    while queue:
        # Gets the first path in the queue
        path = queue.pop()

        # Gets the last node in the path
        vertex = path[-1]

        # Checks if we got to the end
        if vertex == end:
            return path
        # Check all adjacent nodes, construct a new path and push it into the queue
        # excluded neightbors that are already visited
        for current_neighbour in graph_to_search.get(vertex, []):
            if current_neighbour not in path:
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)


def all_paths_search(graph_to_search: dict, start: int, end: int) -> list:
    '''
    This is the function to search for all paths from start node to end node
    '''
    queue = deque([[start]])
    all_paths = []

    while queue:
        # Gets the first path in the queue
        path = queue.popleft()

        # Gets the last node in the path
        vertex = path[-1]

        # Checks if we got to the end
        if vertex == end:
            #return path
            all_paths.append(path)
            continue
        # check all adjacent nodes, construct a new path and push it into the queue
        # excluded neightbors that are already visited
        for current_neighbour in graph_to_search.get(vertex, []):
            if current_neighbour not in path:
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)
    return all_paths