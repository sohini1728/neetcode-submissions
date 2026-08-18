class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempSet = set()
        for i in nums: 
            if (i not in tempSet): 
                tempSet.add(i)
            else:
                return True
        return False