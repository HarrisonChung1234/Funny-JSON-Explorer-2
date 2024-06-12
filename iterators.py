"""
设计模式:
- 迭代器模式 (Iterator Pattern) :
    Iterator：抽象迭代器，定义了 hasnext() 和 next() 方法，用于遍历集合。
    ComponentIterator：具体迭代器，实现了 Iterator 接口，负责遍历 Component 集合中的元素。
"""
from abc import ABC, abstractmethod


# 抽象迭代器
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


# 具体迭代器
class ComponentIterator(Iterator):
    def __init__(self, components):
        self._components = components
        self._index = 0

    def has_next(self):
        return self._index < len(self._components)

    def next(self):
        component = self._components[self._index]
        self._index += 1
        return component
