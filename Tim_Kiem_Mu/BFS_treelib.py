from treelib import Tree, Node


def BFS(tree: Tree, initialState: Node, goalState):
    frontier = [initialState]
    explored = []
    while frontier:
        state = frontier.pop(0)
        explored.append(state)

        if state.tag == goalState:
            return explored
        for neighbor in tree.neighbor(state.identifier):
            if neighbor not in (frontier and explored):
                frontier.append(neighbor)

    return None


if __name__ == "__main__":
    tree = Tree()
    tree.create_node(tag='A', identifier='A')  # root
    tree.create_node(tag='B', identifier='B', parent='A')
    tree.create_node(tag='C', identifier='C', parent='A')
    tree.create_node(tag='D', identifier='D', parent='B')
    tree.create_node(tag='E', identifier='E', parent='B')
    tree.create_node(tag='F', identifier='F', parent='C')
    tree.create_node(tag='G', identifier='G', parent='C')
    tree.create_node(tag='H', identifier='H', parent='D')
    tree.create_node(tag='I', identifier='I', parent='D')
    tree.create_node(tag='J', identifier='J', parent='E')
    tree.create_node(tag='K', identifier='K', parent='E')
    tree.create_node(tag='L', identifier='L', parent='F')
    tree.create_node(tag='M', identifier='M', parent='F')
    tree.create_node(tag='N', identifier='N', parent='G')
    tree.create_node(tag='O', identifier='O', parent='G')
    result = BFS(tree, tree.get_node('A'), 'M')

    if result:
        s = 'explored: '
        for i in result:
            s += i.tag + ' '
            print(s)

    else:
        print('404 Not Found!')
