class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictTotal = {}
        finalList = []

        for num in nums:
            if num in dictTotal:
                dictTotal[num] = dictTotal[num] + 1
            else:
                dictTotal[num] = 1

        def getCount(pair):
            return pair[1]

        sortedPairs = sorted(dictTotal.items(), key=getCount, reverse=True)

        for i in range(k):
            finalList.append(sortedPairs[i][0])

        return finalList