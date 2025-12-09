class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1 = {}
        uniques = set()
        # use a set to check if the values are unique in constant time
        for i in arr:
            dict1[i] = dict1.get(i, 0)+1
        for i in dict1.values():
            if i in uniques:
                return False
            else:
                uniques.add(i)
        return True
        