from binary_search_tree import BinarySearchTree, min_value_node


my_tree = BinarySearchTree()
my_tree.insert(50)
my_tree.insert(57)
my_tree.insert(46)
my_tree.insert(67)
my_tree.insert(56)
my_tree.insert(24)
my_tree.insert(13)
my_tree.insert(30)
print(min_value_node(my_tree.root).value)
print(my_tree.contains(46))
