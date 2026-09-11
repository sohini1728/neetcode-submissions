class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minVal = 0
        maxVal = len(nums) - 1
        while minVal <= maxVal: 
            middleVal = (minVal + maxVal) // 2
            if nums[middleVal] < target:
                minVal = middleVal + 1
            elif nums[middleVal] > target: 
                maxVal = middleVal - 1
            else: 
                return middleVal
                
                
        
        return -1