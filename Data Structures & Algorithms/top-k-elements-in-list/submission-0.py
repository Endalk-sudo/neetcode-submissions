class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # {num: fre }
        freq = [[] for n in range(len(nums) + 1)]

        for n in nums:
                count[n] = 1 + count.get(n,0)

        for key, val in count.items():
            freq[val].append(key)

        topk = []
        for list in freq[::-1]:
            for i in list:
                topk.append(i)
                if len(topk) == k:
                    return topk