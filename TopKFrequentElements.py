class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}# count up the frequencies of each number: # O(n)
        for n in nums:
            counts[n] = 1 + counts.get(n, 0) # add one to the count, default if not found is 0

        
        # create our buckets: O(n)
        freq_buckets = [[] for i in range(len(nums) + 1)]

        # add the counts to each of the buckets
        for num, count in counts.items():
            # for that specific frequency, add this num to the list of 
            # numbers occurring at that frequency
            freq_buckets[count].append(num)

        # hold our k most frequent
        most_frequent = []
        # iterate from most frequent to least frequent
        for i in range(len(freq_buckets) - 1, 0, -1): # O(n): loop 3
            for num in freq_buckets[i]: # O(n): loop 4
                most_frequent.append(num)

                # break when we have k most frequent
                if len(most_frequent) == k:
                    return most_frequent
