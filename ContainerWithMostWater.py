class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        left=0
        right=len(heights)-1

        while left<right:
            area=max(area,(right-left)*(min(heights[left],heights[right])))

            if heights[left]<heights[right]:
                left+=1
            elif heights[right]<heights[left]:
                right-=1

            else:
                left+=1

        return area
