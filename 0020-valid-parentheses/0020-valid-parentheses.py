class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {')': "(",
                '}' :'{',
                "]" : '['  }
        stack = []
        for i in s: # ON
            if i in '({[':
                stack.append(i)
            if  i in ')}]':
                if not stack or stack[-1] != dict1[i]:
                    return False
                else: stack.pop()
        return not stack

        # O(N) time
        # o(n) space
      
          



          