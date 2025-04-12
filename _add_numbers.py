class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Create a dummy node to act as the starting point of the result linked list
        dummy = ListNode(0)
        # Initialize the current node to the dummy node
        current = dummy
        # Initialize the carry to 0
        carry = 0

        # Loop through both linked lists until both are exhausted
        while l1 is not None or l2 is not None:
            # Get the value of the current node of l1, or 0 if l1 is exhausted
            x = l1.val if l1 is not None else 0
            # Get the value of the current node of l2, or 0 if l2 is exhausted
            y = l2.val if l2 is not None else 0
            # Calculate the sum of the values and the carry
            sum = carry + x + y
            # Update the carry for the next iteration
            carry = sum // 10
            # Create a new node with the digit value (sum % 10) and link it to the current node
            current.next = ListNode(sum % 10)
            # Move the current node to the next node
            current = current.next

            # Move to the next node in l1 if it exists
            if l1 is not None: l1 = l1.next
            # Move to the next node in l2 if it exists
            if l2 is not None: l2 = l2.next

        # If there's a remaining carry, create a new node with the carry value
        if carry > 0:
            current.next = ListNode(carry)

        # Return the next node of dummy, which is the head of the result linked list
        return dummy.next
