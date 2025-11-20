"""
LeetCode 141 - Linked List Cycle
Detect cycle using Floyd's Tortoise and Hare algorithm
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


# Simple test (manual linked list with a cycle)
if __name__ == "__main__":
    # Create nodes
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)

    # Link nodes
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # cycle here

    solution = Solution()
    print(solution.hasCycle(n1))  # Output: True
