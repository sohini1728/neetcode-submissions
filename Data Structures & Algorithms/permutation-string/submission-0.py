
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        window = Counter()

        left = 0
        for right in range(len(s2)):
            # character entering the window
            window[s2[right]] += 1

            # once window is wider than len(s1), shrink from the left
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]  # keep Counter clean for equality check
                left += 1

            if window == need:
                return True

        return False