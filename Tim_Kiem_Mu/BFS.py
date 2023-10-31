from MyLib.TreeNode.Node import Node
def Breadth_First_Search(initialState: Node, goalState: Node):
    frontier = [initialState]
    explored = []

    while frontier:
        state = frontier.pop(0)
        explored.append(state)

        if state.label == goalState.label:
            return explored

        for neighbor in state.get_neighbors():
            if neighbor not in frontier and explored:
                frontier.append(neighbor)

    return None


if __name__ == "__main__":
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    F = Node('F')
    G = Node('G')
    H = Node('H')
    I = Node('I')
    J = Node('J')
    K = Node('K')
    L = Node('L')
    M = Node('M')
    N = Node('N')
    O = Node('O')

    A.add_neighbors(B, C)
    B.add_neighbors(D, E)
    C.add_neighbors(F, G)
    D.add_neighbors(H, I)
    E.add_neighbors(J, K)
    F.add_neighbors(L, M)
    G.add_neighbors(N, O)

    result = Breadth_First_Search(A, O)
    if result:
        s = 'explored: '
        for i in result:
            s += i.label + ' '
            print(s);

    else:
        print('404 Not Found!')
