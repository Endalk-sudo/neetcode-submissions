class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        prod = 1
        for i in nums:
            res.append(prod)
            prod *= i
        
        prod = 1
        for j in range(len(nums) -1 ,-1,-1):
            
            res[j] *= prod
            prod *= nums[j]
            
        return res