
class Node:
    def __init__(self, prob=0):
        self.prob = prob
        self.letter = None
        self.left = None
        self.right = None
        self.parent = None
        self.code = None
        self.leaf = False
        self.marked = False

    def set_leaf(self, letter):
        self.leaf = True
        self.letter = letter

    def insert_parent_with(self, right_node, parent_key):
        parent = Node(parent_key)
        parent.right = right_node
        parent.left = self
        self.code = "0"
        right_node.code = "1"

        return parent

    def visit(self, node, code="", huffman_code=None):
        if huffman_code is None:
            huffman_code = {}
        if node is None:
            return
        if node.left is not None:
            code += node.left.code
            code, huffman_code = self.visit(node.left, code, huffman_code)

            code = code[:-1]

        if node.right is not None:
            code += node.right.code
            code, huffman_code = self.visit(node.right, code, huffman_code)
            code = code[:-1]

        if node.leaf:
            huffman_code[node.letter] = code

        return code, huffman_code
