class Solution:
    def countPoints(self, rings: str) -> int:
        d = defaultdict(set)
        count = 0
        for i in range(1, len(rings), 2):
            d[rings[i]].add(rings[i-1])
        for i in d:
            if d[i] == {'R','G','B'}:
                count += 1
        return count

