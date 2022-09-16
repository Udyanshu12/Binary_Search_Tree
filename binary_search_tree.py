from node import Node


def min_value_node(current_node):
    while current_node.left:
        current_node = current_node.left
    return current_node


class BinarySearchTree:
    def __init__(self):

        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while True:
                if value > temp.value:
                    if temp.right is None:
                        temp.right = new_node
                    temp = temp.right
                elif value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                    temp = temp.left
                else:
                    return False

    def contains(self, value):
        temp = self.root
        while temp:
            if value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
            else:
                return True
        return False

    def bfs(self):
        current_node = self.root
        results = []
        queue = [current_node]
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return results

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results
