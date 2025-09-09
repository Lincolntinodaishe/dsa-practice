class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack =[]
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                prevday = stack.pop()
                res[prevday]= i - prevday
            stack.append(i)
        return res  