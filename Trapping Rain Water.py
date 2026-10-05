class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        lMax = 0
        rMax = 0
        total = 0

        while left < right:
            if height[left] <= height[right]:
                if lMax > height[left]:
                    total += lMax - height[left]
                    
                else:
                    lMax = height[left]

                left += 1

            else:
                if  rMax> height[right]:
                    total += rMax - height[right]
                    
                else:
                    rMax = height[right]

                right -= 1

        return total
