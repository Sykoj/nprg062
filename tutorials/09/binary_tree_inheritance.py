from abc import ABC, abstractmethod

class ExpressionNode(ABC):

    @abstractmethod
    def eval(self):
        pass
    
class MultiplyNode(ExpressionNode):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.right.eval() * self.left.eval()


class ValueNode(ExpressionNode):

    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

print(MultiplyNode(ValueNode(3), ValueNode(4)).eval())