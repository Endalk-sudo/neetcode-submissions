class Solution:
    def search(self, nums: List[int], target: int) -> int:
            left = 0 
            right = len(nums) - 1
            
            while left <= right:
                idx = (left + right) // 2
                print(idx)
                
                if nums[idx] == target:
                    return idx
                elif nums[idx] < target:
                    left = idx + 1
                else:
                    right = idx - 1 
            
            return -1