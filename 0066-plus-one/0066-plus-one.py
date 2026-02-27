class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list1 =[]
        ans = ''
        for i in digits:
            ans += str(i)
        ans = int(ans)+1
        num = str(ans)
        for i in num:
            list1.append(int(i))
        return list1

        