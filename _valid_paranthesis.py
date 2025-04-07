class Solution:
    def isValid(self, s: str) -> bool:
        # If the string has an odd number of characters, it can't be valid
        if len(s) % 2 != 0:
            return False

        # Dictionary to match opening brackets with their corresponding closing brackets
        bracket_map = {'(': ')', '[': ']', '{': '}'}
        
        # Stack to keep track of opening brackets
        stack = []

        # Go through each character in the string
        for char in s:
            # If it's an opening bracket, push it onto the stack
            if char in bracket_map:
                stack.append(char)
            else:
                # If stack is empty or the brackets don't match, return False
                if not stack:
                    return False
                last_open = stack.pop()
                if bracket_map[last_open] != char:
                    return False

        # If stack is empty at the end, all brackets matched properly
        return not stack
