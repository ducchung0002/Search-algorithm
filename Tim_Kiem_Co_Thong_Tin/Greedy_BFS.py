from MyLib.TreeNode.Node import Node
from MyLib.MinHeap.MinHeap import MinHeap

def Gready_BFS(initial_state: Node, goal_state: Node):
    frontier = [initial_state]
    explored = []

    while frontier:
        # print('frontier', [(node.label, node.value) for node in frontier])
        # print('explored', [(node.label, node.value) for node in explored])
        # print()

        state = MinHeap.extract_min(frontier)
        explored.append(state)

        if state.label == goal_state.label:
            return explored

        for neighbor in state.get_neighbors():
            try:
                index = frontier.index(neighbor)
                # neighbor in frontier, there no exception
                # Why update?
                MinHeap.decrease_key(frontier, index, neighbor)
            except ValueError: # neighbor not in frontier
                if neighbor not in explored:
                    MinHeap.insert(frontier, neighbor)
    return None

    

if __name__ == "__main__":
    A = Node('A', 6)
    B = Node('B', 3)
    C = Node('C', 4)
    D = Node('D', 5)
    E = Node('E', 3)
    F = Node('F', 1)
    G = Node('G', 6)
    H = Node('H', 2)
    I = Node('I', 5)
    J = Node('J', 4)
    K = Node('K', 2)
    L = Node('L', 0)
    M = Node('M', 4)
    N = Node('N', 0)
    O = Node('O', 4)
    A.add_neighbors(B, C, D)
    B.add_neighbors(E, F)
    C.add_neighbors(G, H)
    D.add_neighbors(I, J)
    F.add_neighbors(K, L, M)
    H.add_neighbors(N, O)

    result = Gready_BFS(A, N)
    if result:
        s = 'explored: '
        for i in result:
            s += i.label + ' '
            print(s)

    else:
        print('404 NOT FOUND')