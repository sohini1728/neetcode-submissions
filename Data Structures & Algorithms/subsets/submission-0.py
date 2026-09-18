class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i):
            if i == len(nums):
                res.append(path[:])
                return

            # include nums[i]
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

            # skip nums[i]
            backtrack(i + 1)

        backtrack(0)
        return res