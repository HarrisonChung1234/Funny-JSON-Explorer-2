"""
设计模式:
- 建造者模式 (Builder Pattern): 通过Builder类解析和构建组件树。
"""

import copy
from components import Container, Leaf


class Builder:
    def __init__(self, icon_family):
        """
        初始化Builder类。

        :param icon_family: 一个字典，包含用于不同类型节点的图标。
        """
        self.icon_family = icon_family
        self.max_level = 0  # 记录最大层级深度
        self.max_name_len = 0  # 记录最长名称长度
        self.root = None  # 根节点

    def build(self, json_data):
        """
        构建组件树并计算最大长度。

        :param json_data: 要解析的JSON数据
        :return: 根节点和最大长度
        """
        self.root = self.parse(json_data, 'root', level=0)
        max_len = self.max_level * 3 + self.max_name_len + 5  # 计算最大长度
        return self.root, max_len

    def parse(self, data, name, level=0, is_last=[], is_first=False):
        """
        递归解析JSON数据，构建组件树。

        :param data: 当前解析的数据
        :param name: 当前节点的名称
        :param level: 当前节点的层级
        :param is_last: 一个布尔列表，指示节点是否是其父节点的最后一个子节点
        :param is_first: 一个布尔值，指示节点是否是其父节点的第一个子节点
        :return: 解析后的Container或Leaf对象
        """
        # 更新最大层级深度
        self.max_level = max(self.max_level, level)

        if isinstance(data, dict):
            # 创建Container对象
            container = Container(
                name,
                icon=self.icon_family.get('container', ''),
                level=level,
                is_last=is_last,
                is_first=is_first
            )
            # 更新最长名称长度
            self.max_name_len = max(self.max_name_len, len(name))

            for i, (key, value) in enumerate(data.items()):
                tmp_islast = copy.deepcopy(is_last)
                tmp_islast.append(i == len(data) - 1)  # 更新is_last列表

                if isinstance(value, dict):
                    # 递归解析子字典并添加到容器中
                    container.add(self.parse(
                        value,
                        key,
                        level=level + 1,
                        is_last=tmp_islast,
                        is_first=(i == 0 and name == 'root')
                    ))
                else:
                    # 创建Leaf对象并添加到容器中
                    container.add(Leaf(
                        f"{key}: {value}",
                        icon=self.icon_family.get('leaf', ''),
                        level=level + 1,
                        is_last=tmp_islast,
                        is_first=(i == 0 and name == 'root')
                    ))
                    # 更新最长名称长度
                    self.max_name_len = max(self.max_name_len, len(f"{key}: {value}"))

            return container
        else:
            # 创建Leaf对象
            self.max_name_len = max(self.max_name_len, len(f"{name}: {data}"))
            return Leaf(
                f"{name}: {data}",
                icon=self.icon_family.get('leaf', ''),
                level=level
            )
