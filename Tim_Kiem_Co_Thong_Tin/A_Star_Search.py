from MyLib.TreeNode.Node import Node
from MyLib.MinHeap.MinHeap import MinHeap

def A_Start_Search(initial_state: Node, goal_state: Node):
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
            #update learned length
            if neighbor.learned_length > state.learned_length + state.get_edge_weight(neighbor):
                neighbor.learned_length = state.learned_length + state.get_edge_weight(neighbor)
            try: #
                index = frontier.index(neighbor)
                MinHeap.decrease_key(frontier, index, neighbor)
            except ValueError:
                if neighbor not in explored:
                    neighbor.value += neighbor.learned_length
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

    A.learned_length = 0
    B.learned_length = float('inf')
    C.learned_length = float('inf')
    D.learned_length = float('inf')
    E.learned_length = float('inf')
    F.learned_length = float('inf')
    G.learned_length = float('inf')
    H.learned_length = float('inf')
    I.learned_length = float('inf')
    J.learned_length = float('inf')
    K.learned_length = float('inf')
    L.learned_length = float('inf')
    M.learned_length = float('inf')
    N.learned_length = float('inf')
    O.learned_length = float('inf')


    A.add_neighbor(neighbor=B, edge_weight=2)
    A.add_neighbor(neighbor=C, edge_weight=1)
    A.add_neighbor(neighbor=D, edge_weight=3)

    B.add_neighbor(neighbor=E, edge_weight=5)
    B.add_neighbor(neighbor=F, edge_weight=4)

    C.add_neighbor(neighbor=G, edge_weight=6)
    C.add_neighbor(neighbor=H, edge_weight=3)

    D.add_neighbor(neighbor=I, edge_weight=2)
    D.add_neighbor(neighbor=J, edge_weight=4)

    F.add_neighbor(neighbor=K, edge_weight=2)
    F.add_neighbor(neighbor=L, edge_weight=1)
    F.add_neighbor(neighbor=M, edge_weight=4)

    H.add_neighbor(neighbor=N, edge_weight=2)
    H.add_neighbor(neighbor=O, edge_weight=4)

    result = A_Start_Search(A, N)
    if result:
        s = 'explored: '
        for i in result:
            s += i.label + ' '
            print(s)

    else:
        print('404 NOT FOUND')