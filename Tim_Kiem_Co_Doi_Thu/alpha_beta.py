from MyLib.TreeNode.Node import Node


def Max_Value(state: Node, alpha=float('-inf'), beta=float('inf')):
    neighbors = state.get_neighbors()
    if len(neighbors) == 0:
        # is leaf
        state.next_state = None
        return state.value

    state.value = float('-inf')

    for neighbor in neighbors:
        min_value = Min_Value(neighbor, alpha, beta)
        if state.value < min_value:
            state.value = min_value
            state.next_state = neighbor
        if neighbor.value >= beta:
            return neighbor.value
        if neighbor.value > alpha:
            alpha = neighbor.value

    return state.value


def Min_Value(state: Node, alpha=float('-inf'), beta=float('inf')):
    neighbors = state.get_neighbors()
    if len(neighbors) == 0:
        # is leaf
        state.next_state = None
        return state.value

    state.value = float('inf')

    for neighbor in neighbors:
        max_value = Max_Value(neighbor, alpha, beta)
        if state.value > max_value:
            state.value = max_value
            state.next_state = neighbor
        if neighbor.value <= alpha:
            return neighbor.value
        if neighbor.value < beta:
            beta = neighbor.value

    return state.value


def MiniMax_Search(strategy, state: Node):
    strategy(state)


if __name__ == "__main__":
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    F = Node('F')
    G = Node('G')
    H = Node('H', 2)
    I = Node('I', 9)
    J = Node('J', 7)
    K = Node('K', 4)
    L = Node('L', 8)
    M = Node('M', 9)
    N = Node('N', 3)
    O = Node('O', 5)

    A.add_neighbors(B, C)
    B.add_neighbors(D, E)
    C.add_neighbors(F, G)
    D.add_neighbors(H, I)
    E.add_neighbors(J, K)
    F.add_neighbors(L, M)
    G.add_neighbors(N, O)

    MiniMax_Search(Max_Value, A)
    print(A.value)
    state = A
    while True:
        print(state.label, end='')
        state = state.next_state
        if state:
            print('->', end='')
        else:
            break
