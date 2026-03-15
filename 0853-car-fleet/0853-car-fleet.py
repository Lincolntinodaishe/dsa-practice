class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {}
        for i, n in zip(position, speed):
            time = (target - i)/ n
            d[i] = time
        position.sort(reverse = True)
        stack = []
        for i in position:
            if not stack:
                stack.append(i)
            else:
                if d[stack[-1]] >= d[i]:
                    continue
                else:
                    stack.append(i)
        return len(stack)
        
                
# 853. Car Fleet
# -------------------------------------------------
# KEY INSIGHT:
# - A faster car behind a slower car will merge into the slower car's fleet
# - Once merged, the fleet moves at the SLOWER car's speed
# - We only care about TIME-TO-TARGET: (target - position) / speed
#   This single number captures both position and speed
#
# APPROACH (Stack):
# 1. Sort cars by position DESCENDING (closest to target first)
# 2. Calculate time-to-target for each car
# 3. Use a stack to track fleet "leaders" (the slowest car in each fleet)
#    - If current car's time <= stack top → it merges (caught up), skip it
#    - If current car's time > stack top → new fleet, push it
# 4. Return stack size = number of fleets
#
# WHY SORT DESCENDING?
# - A car can only be blocked by a car AHEAD of it (closer to target)
# - Processing front-to-back lets us compare each car against the fleet ahead
#
# WHY COMPARE TIMES?
# - time behind <= time ahead → behind car is faster, catches up → MERGE
# - time behind > time ahead → behind car is slower, never catches up → NEW FLEET
#
# COMPLEXITY:
# - Time: O(n log n) for sorting, O(n) for stack pass → O(n log n)
# - Space: O(n) for the stack
#
# EDGE CASES:
# - One car → one fleet
# - All same speed → all unique positions = all unique times = n fleets
# - All cars merge → one fleet (stack size 1)
        