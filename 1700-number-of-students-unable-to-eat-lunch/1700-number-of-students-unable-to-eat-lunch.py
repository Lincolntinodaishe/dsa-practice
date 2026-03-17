class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        d = {}
        for i in students:
            d[i] = d.get(i, 0)+1
        for s in sandwiches:
            if d.get(s, 0) > 0: #safe lookup 
                d[s]-= 1
                res -= 1
            else:
                return res
        return res

        
        