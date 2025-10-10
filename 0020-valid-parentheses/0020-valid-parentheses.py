class Solution:
    def isValid(self, s: str) -> bool:
        #Brute
        #  check if a combination is in the list of the pranhtess
        # in a valid parenthis, thers always one true combination
        # replace that combination with empty
        # return s ==""
        # each time replace runs it is O(n) time and it ends up being o(n2+)
        # while "()" in s or "{}" in s or "[]" in s:
        #   s = s.replace("()", "")
        #   s = s.replace("{}", "")
        #   s = s.replace("[]", "")
        # return s == ""
        

        # Optimal
        dict1 = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            if i in ')}]' :
                if not stack or dict1[i] != stack[-1]:
                    return False
                stack.pop()
        return not stack


