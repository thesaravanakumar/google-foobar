def solution(entrances, exits, path):
    nodes = []

    for i in range(len(path)):
        nodes.append([])

    for i in range(len(path)):
        for j in range(len(path[i])):
            if i == j or path[i][j] == 0:
                continue
            a = Edge(i, j, path[i][j], 0)
            b = Edge(j, i, 0, 0)
            a.augmented = b
            b.augmented = a
            nodes[i].append(a)
            nodes[j].append(b)

    max_flow = 0
    max_flow_prev = -1
    while not max_flow_prev == max_flow:
        max_flow_prev = max_flow
        for start in entrances:
            edges = get_path(start, nodes, exits)
            bottleneck = 10000000
            if not edges:
                continue
            for edge in edges:
                bottleneck = min(bottleneck, edge.capacity - edge.flow)
            if bottleneck > 0:
                max_flow += bottleneck
                for edge in edges:
                    edge.flow += bottleneck
                    edge.augmented.flow -= bottleneck

    return max_flow


path = []


def get_path(start, nodes, exits):
    """
    :param start: start node
    :param nodes: adjacency list
    :param exits: list of exit nodes
    :return: path (edges taken to exit)
    """
    visited = []
    for i in range(len(nodes)):
        visited.append(False)

    global path
    path = []
    a = dfs_recursive(start, nodes, visited, exits)
    if a:
        return a
    else:
        return None


def dfs_recursive(node, nodes, visited, exits):
    """
    recursive depth first search
    :param node: current node
    :param nodes: adjacency list
    :param visited: list of visited nodes
    :param exits: list of exit nodes
    :return: returns path to any exit node, if path exists
    """
    for edge in nodes[node]:
        if not visited[edge.end] and edge.capacity - edge.flow > 0:
            path.append(edge)
            visited[edge.end] = True
            if edge.end in exits:
                return path
            else:
                a = dfs_recursive(edge.end, nodes, visited, exits)
                if not a:
                    path.pop()
                    visited[edge.end] = False
                else:
                    return a
    return None

def print_path(edges):
    curr = edges[0].end
    for edge in edges:
        s = str(edge.start) + " -> " + str(edge.end)
        print s


class Edge:
    def __init__(self, start, end, capacity, flow):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = flow
        self.augmented = None
