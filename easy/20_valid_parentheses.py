class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to hold the matching pairs
        matching_bracket = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        # Stack to hold the opening brackets
        stack = []

        for char in s:
            if char in matching_bracket:
                # If the stack is empty, use a dummy value '#' which will never match
                top_element = stack.pop() if stack else '#'

                # Check if the current closing bracket matches the top of the stack
                if matching_bracket[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)

        # The stack should be empty if all opening brackets have been matched
        return not stack

# Example usage:
sol = Solution()
print(sol.isValid("()"))       # Output: True
print(sol.isValid("()[]{}"))   # Output: True
print(sol.isValid("(]"))       # Output: False
