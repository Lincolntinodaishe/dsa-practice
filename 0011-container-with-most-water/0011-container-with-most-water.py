class Solution:
    def maxArea(self, height: List[int]) -> int:
        # #Brute Force time:On^2
        # max_area = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         area = (j - i)*min(height[i], height[j])
        #         max_area = max(max_area, area)
        # return max_area
         
        #Optimum Solution

        max_area= 0
        l =0
        r = len(height)-1
        while l<r:
            area = (r-l)*min(height[l],height[r]) #calculate the area btwn the two points
            max_area = max(area, max_area) #updtae max area
            if height[l]<height[r]:  #move the pointer with the lower height
                l+=1
            else:
                r-=1
        return max_area