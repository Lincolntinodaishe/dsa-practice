class Solution:
    import math
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for i in s:
            if i == letter:
                count += 1
        per = count / len(s) * 100
        per = math.floor(per) # math flooring importing math lib
        return per
        