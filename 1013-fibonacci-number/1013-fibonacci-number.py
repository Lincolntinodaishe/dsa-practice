class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        prev_prev = 0
        prev = 1

        for i in range(2, n+1):
            temp = prev_prev 
            prev_prev = prev
            prev = prev + temp
        
        return prev
       #( if n == 2:
        #   return 1
        #if n == 1:
         #   return 0

        #fibb = [0]*(n+1)
        #fibb[0]= 0
        #fibb[1]=1
  
        #for i in range(2, n+1):
         #   fibb[i] = fibb[i-1] + fibb[i-2]
        #return fibb[n])
