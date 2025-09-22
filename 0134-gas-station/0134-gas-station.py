class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): # definitley if the sum of cost is greter than the gas we cannot compltete the loop. hence impossible
            return -1 
        total = 0
        res = 0
        for i in range(len(gas)): # iterate through each and evry number
            total += gas[i]-cost[i] # increament the total of each of gas - cost at evewry stage so that we see if the total is positive and allows us to move to thenext
            if total < 0: # once it falls to negative we ignore that point and get our total back to zero and set our result to the next position
                total = 0
                res = i + 1
        return res
        