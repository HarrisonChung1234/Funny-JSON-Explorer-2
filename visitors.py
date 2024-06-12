"""
设计模式:
- 访问者模式 (Visitor Method):
    Visitor：抽象访问者，定义了 visit_container(container) 和 visit_leaf(leaf) 方法，用于处理不同类型的元素。
    TreeVisitor和RectangleVisitor：具体访问者，实现了 Visitor 接口，定义了具体的访问行为。
"""
from abc import ABC, abstractmethod


# 抽象访问者
class Visitor(ABC):
    @abstractmethod
    def visit_container(self, container):
        pass

    @abstractmethod
    def visit_leaf(self, leaf):
        pass


# 具体访问者：树状风格
class TreeVisitor(Visitor):
    def visit_container(self, container):
        if container.level > 0:
            is_last = container.is_last
            prefix = ''.join(['   ' if last else '│  ' for last in is_last])
            prefix = prefix[:-3] if container.level > 0 else prefix
            prefix += '└─ ' if is_last[-1] else '├─ '
            prefix = prefix[:-1]
            print(prefix + container.icon + container.name)
        iterator = container.create_iterator()
        while iterator.has_next():
            iterator.next().accept(self)

    def visit_leaf(self, leaf):
        is_last = leaf.is_last
        name = leaf.name.split(":")[0] if 'None' in leaf.name else leaf.name
        prefix = ''.join(['   ' if last else '│  ' for last in is_last])
        prefix = prefix[:-3] if leaf.level > 0 else prefix
        prefix += '└─ ' if is_last[-1] else '├─ '
        prefix = prefix[:-1]
        print(prefix + leaf.icon + name)


# 具体访问者：矩形风格
class RectangleVisitor(Visitor):
    def __init__(self, max_len):
        self.max_len = max_len

    def visit_container(self, container):
        is_first = container.is_first
        is_last = container.is_last
        if is_first:
            print(f"┌─{container.icon}{container.name} ─"
                  f"{'─' * (self.max_len - len(str(container.name)) - len(container.icon))}┐")
        else:
            print(f"{'│  ' * (container.level - 1)}├─{container.icon}{container.name} ─"
                  f"{'─' * (self.max_len - len(str(container.name)) - 3 * (container.level - 1) - len(container.icon))}|")
        iterator = container.create_iterator()
        while iterator.has_next():
            child = iterator.next()
            child.accept(self)

    def visit_leaf(self, leaf):
        is_last = leaf.is_last
        max_len = self.max_len
        name = leaf.name.split(":")[0] if 'None' in leaf.name else leaf.name
        label = all(is_last)
        if label:
            prefix = '└──' + '┴──' * max(0, leaf.level - 2) + ('┴─' if leaf.level > 1 else '')
            suffix = '─' * (max_len - 3 * (leaf.level - 1) - len(name)) + '┘'
        else:
            prefix = '│  ' * (leaf.level - 1) + '├─'
            suffix = '─' * (max_len - 3 * (leaf.level - 1) - len(name)) + '|'
        print(f"{prefix}{leaf.icon}{name} {suffix}")
