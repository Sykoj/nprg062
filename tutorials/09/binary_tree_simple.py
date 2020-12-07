def evaluate(node):
    if node.value == '*':
        return evaluate(node.left) * evaluate(node.right)
    elif node.value == '+':
        return evaluate(node.left) + evaluate(node.right)
    elif node.value == '-':
        return evaluate(node.left) - evaluate(node.right)
    elif node.value == '/':
        return evaluate(node.left) / evaluate(node.right)
    else:
        return node.value

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left=  left
        self.right = right

# Expression: * + 2 3 4 = 20
expression = Node('*', Node('+', Node(2), Node(3)), Node(4))

print(evaluate(expression))