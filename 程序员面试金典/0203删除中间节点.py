class Solution:
    def delete_node(self, node):
        node.val = node.next.val
        node.next = node.next.next
