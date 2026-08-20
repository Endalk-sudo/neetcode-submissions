class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i , v in enumerate(nums):
            if i != v :
                return i

            if v == len(nums) - 1:
                return v + 1
            
        