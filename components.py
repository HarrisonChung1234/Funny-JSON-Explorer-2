"""
设计模式:
- 访问者模式 (Visitor Method):
    Component ：抽象元素，定义了 accept(visitor) 方法。
    Container 和 Leaf ：具体元素，继承自 Component ，实现了 accept(visitor) 方法，分别调用 visitor 的 visit_container()
                        和 visit_leaf()方法。
"""
from abc import ABC, abstractmethod
from iterators import ComponentIterator


# 抽象元素
class Component(ABC):
    def __init__(self, name, icon='', level=0, is_last=[], is_first=False):
        self.name = name
        self.icon = icon
        self.level = level
        self.is_last = is_last
        self.is_first = is_first

    @abstractmethod
    def accept(self, visitor):
        pass

    @abstractmethod
    def create_iterator(self):
        pass


# 具体元素：容器
class Container(Component):
    def __init__(self, name, icon='', level=0, is_last=[], is_first=False):
        super().__init__(name, icon, level, is_last, is_first)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def accept(self, visitor):
        visitor.visit_container(self)

    def create_iterator(self):
        return ComponentIterator(self.children)


# 具体元素：叶子
class Leaf(Component):
    def accept(self, visitor):
        visitor.visit_leaf(self)

    def create_iterator(self):
        return ComponentIterator([])
