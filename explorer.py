from builder import Builder
from visitors import TreeVisitor, RectangleVisitor


class FunnyJsonExplorer:
    def __init__(self, icon_family=None, style='tree'):
        self.root = None
        self.max_len = 0
        self.icon_family = icon_family or {'container': ' ', 'leaf': ' '}
        self.style = style

    def _load(self, json_data):
        builder = Builder(self.icon_family)
        self.root, self.max_len = builder.build(json_data)

    def show(self, json_data):
        self._load(json_data)
        if self.root:
            if self.style == 'rectangle':
                visitor = RectangleVisitor(self.max_len)
            else:
                visitor = TreeVisitor()
            iterator = self.root.create_iterator()
            while iterator.has_next():
                iterator.next().accept(visitor)
