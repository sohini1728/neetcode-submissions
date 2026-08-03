class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}                       # value -> index
        for i in range(len(nums)):
            n = nums[i]
            complement = target - n
            if complement in seen:
                return [seen[complement], i]
            seen[n] = i
        return []