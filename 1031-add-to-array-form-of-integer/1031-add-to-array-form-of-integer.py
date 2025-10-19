class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # you have to convert the numbers to a string then add them like you are adding on paper
        carry =0
        fin = []
        noo = ""
        for i in num:
            noo += str(i)
        k = str(k)
        i = len(noo)-1
        j = len(k)-1
        while i >=0 or j>=0 or carry != 0:
            digit1 = int(noo[i]) if i>=0 else 0
            digit2 = int(k[j]) if j>=0 else 0
            total = (digit1) + (digit2) + carry
            fin.append(total % 10)
            carry = total // 10
            i -= 1
            j -= 1
        return fin[::-1]

        