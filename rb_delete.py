from rb_tree import RBTree, Node, BLACK, RED, NIL
NIL_LEAF = RBTree.NIL_LEAF

def delete_root():

    """
      REMOVE--> __5__                     __8B__
               /     \     --Result-->   /
             3R      8R                3R
    """

    rb_tree = RBTree()
    root = Node(value=5, color=BLACK, parent=None, left=NIL_LEAF, right=NIL_LEAF)
    left_child = Node(value=3, color=RED, parent=root, left=NIL_LEAF, right=NIL_LEAF)
    right_child = Node(value=8, color=RED, parent=root, left=NIL_LEAF, right=NIL_LEAF)
    root.left = left_child
    root.right = right_child
    rb_tree.root = root
    rb_tree.remove(5)

    return list(rb_tree) == [3, 8]

def delete_root_two_nodes():

    """
            __5B__ <-- REMOVE        __8B__
                 \      Should become--^
                 8R
    """

    rb_tree = RBTree()
    root = Node(value=5, color=BLACK, parent=None, left=NIL_LEAF, right=NIL_LEAF)
    right_child = Node(value=8, color=RED, parent=root, left=NIL_LEAF, right=NIL_LEAF)
    root.right = right_child
    rb_tree.root = root
    rb_tree.remove(5)

    return list(rb_tree) == [8]

def delete_single_child_node():
    """
           5                        5B
          / \   should become      /
        1R   6R                   1R
    """
    rb_tree = RBTree()
    root = Node(value=5, color=BLACK, parent=None, left=NIL_LEAF, right=NIL_LEAF)
    left_child = Node(value=1, color=RED, parent=root, left=NIL_LEAF, right=NIL_LEAF)
    right_child = Node(value=6, color=RED, parent=root, left=NIL_LEAF, right=NIL_LEAF)
    root.left = left_child
    root.right = right_child
    rb_tree.root = root
    rb_tree.remove(6)

    return list(rb_tree) == [1, 5]

def delete_single_deep_child():

    """
            ______20______
           /              \
         10B           ___38R___
        /   \         /         \
      5R    15R      28B         48B
                    /  \        /   \
                  23R  29R     41R   49R    <--- REMOVE
    """

    rb_tree = RBTree()
    root = Node(value=20, color=BLACK, parent=None, left=NIL_LEAF, right=NIL_LEAF)
    # left subtree
    node_10 = Node(value=10, color=BLACK, parent=None, left=NIL_LEAF, right=NIL_LEAF)
    node_5 = Node(value=5, color=RED, parent=node_10, left=NIL_LEAF, right=NIL_LEAF)
    node_15 = Node(value=15, color=RED, parent=node_10, left=NIL_LEAF, right=NIL_LEAF)
    node_10.left = node_5
    node_10.right = node_15
    # right subtree
    node_38 = Node(value=38, color=RED, parent=root, left=NIL_LEAF, right=NIL_LEAF)
    node_28 = Node(value=28, color=BLACK, parent=node_38, left=NIL_LEAF, right=NIL_LEAF)
    node_48 = Node(value=48, color=BLACK, parent=node_38, left=NIL_LEAF, right=NIL_LEAF)
    node_38.left = node_28
    node_38.right = node_48
    # node_28 subtree
    node_23 = Node(value=23, color=RED, parent=node_28, left=NIL_LEAF, right=NIL_LEAF)
    node_29 = Node(value=29, color=RED, parent=node_28, left=NIL_LEAF, right=NIL_LEAF)
    node_28.left = node_23
    node_28.right = node_29
    # node 48 subtree
    node_41 = Node(value=41, color=RED, parent=node_48, left=NIL_LEAF, right=NIL_LEAF)
    node_49 = Node(value=49, color=RED, parent=node_48, left=NIL_LEAF, right=NIL_LEAF)
    node_48.left = node_41
    node_48.right = node_49

    root.left = node_10
    root.right = node_38
    rb_tree.root = root
    rb_tree.remove(49)

    return list(rb_tree) == [5, 10, 15, 20, 23, 28, 29, 38, 41, 48]

def delete_black_node_black_successor_red_child():

    """
                     ___10B___                                             ___10B___
                    /         \                                           /         \
                   5B         30B  <------- REMOVE THIS                  5B         32B  <----
                  /  \       /   \                                      /  \       /   \
                -5B  7B    20B   38R                                  -5B  7B    20B   38R
                                /   \                                                 /   \
               successor ---> 32B    41B                                       -->  35B    41B
                                 \             30B becomes 32B
                                 35R           old 32B becomes 35B
    """

    rb_tree = RBTree()
    root = Node(value=10, color=BLACK, parent=None, left=NIL_LEAF, right=NIL_LEAF)
    # left subtree
    node_5 = Node(value=5, color=BLACK, parent=root, left=NIL_LEAF, right=NIL_LEAF)
    node_m5 = Node(value=-5, color=BLACK, parent=node_5, left=NIL_LEAF, right=NIL_LEAF)
    node_7 = Node(value=7, color=BLACK, parent=node_5, left=NIL_LEAF, right=NIL_LEAF)
    node_5.left = node_m5
    node_5.right = node_7
    # right subtree
    node_30 = Node(value=30, color=BLACK, parent=root, left=NIL_LEAF, right=NIL_LEAF)
    node_20 = Node(value=20, color=BLACK, parent=node_30, left=NIL_LEAF, right=NIL_LEAF)
    node_38 = Node(value=38, color=RED, parent=node_30, left=NIL_LEAF, right=NIL_LEAF)
    node_30.left = node_20
    node_30.right = node_38
    # 38 subtree
    node_32 = Node(value=32, color=BLACK, parent=node_38, left=NIL_LEAF, right=NIL_LEAF)
    node_41 = Node(value=41, color=BLACK, parent=node_38, left=NIL_LEAF, right=NIL_LEAF)
    node_38.left = node_32
    node_38.right = node_41
    node_35 = Node(value=35, color=RED, parent=node_32, left=NIL_LEAF, right=NIL_LEAF)
    node_32.right = node_35

    root.left = node_5
    root.right = node_30

    rb_tree.root = root
    rb_tree.remove(30)

    return list(rb_tree) == [-5, 5, 7, 10, 20, 32, 35, 38, 41]


def main():

    # Sample execution of methods for deletion of nodes in different cases
    # Run rb_tree_tests.py for a thorough test
    delete_methods = [delete_root, delete_root_two_nodes, delete_single_child_node,
                      delete_single_deep_child, delete_black_node_black_successor_red_child]

    print()
    for func in delete_methods:
        print(f'Executing {func.__name__}')
        if func():
            print('Successeful deletion.\n')



if __name__ == '__main__':
    main()
