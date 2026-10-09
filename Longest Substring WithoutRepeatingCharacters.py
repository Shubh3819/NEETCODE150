class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen=set()
        max1=0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1

            seen.add(s[right])
            max1=max(max1,(right-left+1))

        return max1
