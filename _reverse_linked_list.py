class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: If the list is empty, return None
        if not head:
            return None

        # Assume the first node is the new head initially
        newHead = head

        # If there is a next node, we keep reversing
        if head.next:
            # Recursively reverse the rest of the list
            newHead = self.reverseList(head.next)

            # Reverse the link:
            # The next node's 'next' should point back to the current node
            head.next.next = head

        # After reversal, the current node should not point to anything
        head.next = None

        # Return the new head of the reversed list
        return newHead
