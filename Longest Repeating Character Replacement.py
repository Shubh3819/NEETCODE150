class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=[0]*26
        left=0
        max_len=0
        max_freq=0

        for right in range(len((s))):
            idk=ord(s[right])-ord('A')
            freq[idk]+=1
            max_freq=max(max_freq,freq[idk])

            if (right-left+1)-max_freq>k:
                freq[ord(s[left])-ord('A')]-=1
                left+=1

            max_len=max(max_len,(right-left+1))

        return max_len
