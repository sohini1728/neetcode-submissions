class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # sorting first, as you reasoned through
        totalList = []

        for i in range(len(nums) - 2):  # i can go up to len(nums)-3, matching your math
            # skip duplicate values for i, so we don't repeat the same triplet's first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    totalList.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicates for left and right too
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1  # sum too small, move left forward (bigger values)
                else:
                    right -= 1  # sum too big, move right backward (smaller values)

        return totalList