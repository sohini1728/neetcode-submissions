import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(k: int) -> int:
            return sum(math.ceil(p / k) for p in piles)

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if hours(mid) <= h:
                hi = mid          # mid works, might be the answer, keep it
            else:
                lo = mid + 1      # mid fails, so does everything below it
        return lo