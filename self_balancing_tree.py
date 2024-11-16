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

    def rotate_right(node: BinaryNode):
        node_left = node.left  #  node's left child  (will be made root)
        node_left_right = (
            node_left.right if node_left else None
        )  # right child of node's left child (will become node's left child)

        node.left = node_left_right
        node_left.right = node
        return node_left

    def add_node(self, new_node: BinaryNode):

        if not self.root_node:
            self.root_node = new_node
            return

        def place_node(
            curr: BinaryNode,
            node_to_add: BinaryNode,
            trace: list[tuple[BinaryNode, BinaryNode]],
        ) -> list[BinaryNode]:
            trace.append((None, curr)) if not trace else trace.append((trace[-1][1], curr))
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
        next_trace: tuple[BinaryNode, BinaryNode] = trace.pop() # (Parent, Current)
        while next_trace:
            balance_factor: int = AV_Tree.balance_factor(next_trace[1])

            # if left-heavy
            if balance_factor > 1:
                if AV_Tree.height(next_trace[1].left.left) >= AV_Tree.height(
                    next_trace[1].left.right
                ):
                    # the tree is left heavy and the left subtree of the left child is the cause
                    # do a single right rotation
                    new_subroot = AV_Tree.rotate_right(next_trace[1])
                    if next_trace[0].left == next_trace[1]:
                        next_trace[0].left = new_subroot
                    else:
                        next_trace[1].right = new_subroot
                    
                else:
                    # the tree is left heavy and the right subtree of the left child is the cause
                    # do a left-right rotation
                    pass
            # if right-heavy
            elif balance_factor < -1:
                if AV_Tree.height(next_trace[1].right.left) >= AV_Tree.height(
                    next_trace[1].right.right
                ):
                    # the tree is right heavy and the left subtree of the right child is the cause
                    pass
                else:
                    # the tree is right heavy and the right subtree of the right child is the cause
                    pass

            next_trace = trace.pop() if trace else None


tree = AV_Tree()

tree.add_node(BinaryNode(30))
tree.add_node(BinaryNode(20))
tree.add_node(BinaryNode(10))

print("done")
