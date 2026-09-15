class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]

        for i,temp in enumerate(temperatures):
            while stack and temp>stack[-1][1]:#[1]is here to get the value(1,72) gives only value:72 not index:1
                prev_index,prev_temp=stack.pop()
                result[prev_index]=i-prev_index

            stack.append((i,temp))

        return result
