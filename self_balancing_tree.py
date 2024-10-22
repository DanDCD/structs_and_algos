class BinaryNode:
    def __init__(
        self, value: any = None, left: "BinaryNode" = None, right: "BinaryNode" = None
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


class AV_Tree:
    def __init__(self, root_node: BinaryNode = None) -> None:
        self.root_node = root_node


    def height(node: BinaryNode) -> int:
        if not node:
            return 0
        return max(
            1 + AV_Tree.height(node.left) if node.left else 0,
            1 + AV_Tree.height(node.right) if node.right else 0,
        )


    def balance_factor(node: BinaryNode) -> int:
        return AV_Tree.height(node.right) - AV_Tree.height(node.left)


    def add_node(self, new_node: BinaryNode):

        if not self.root_node:
            self.root_node = new_node
            return

        def place_node(
            curr: BinaryNode, node_to_add: BinaryNode, trace: list[BinaryNode]
        )->list[BinaryNode]:
            trace.append(curr)
            if node_to_add.value <= curr.value:
                if not curr.left:
                    curr.left = node_to_add
                else:
                    place_node(curr.left, node_to_add, trace) 
            else:
                if not curr.right:
                    curr.right = node_to_add
                else:
                    place_node(curr.right, node_to_add, trace)

        trace = []
        place_node(self.root_node, new_node, trace)
        
        # we need to check if the nodes in trace need rebalancing
        # we need to go backwards up the trace
        next_trace = trace.pop()
        while next_trace:
            # ...
            next_trace = trace.pop()


tree = AV_Tree()

tree.add_node(BinaryNode(10))
tree.add_node(BinaryNode(30))
tree.add_node(BinaryNode(4))
tree.add_node(BinaryNode(8))
tree.add_node(BinaryNode(18))
tree.add_node(BinaryNode(80))

print("done")
