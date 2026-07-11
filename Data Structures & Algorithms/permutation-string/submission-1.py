class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        left = 0

        for right in range(len(s2)):
            # character entering the window
            ch = s2[right]
            window[ch] = window.get(ch, 0) + 1

            # once window is wider than len(s1), shrink from the left
            if right - left + 1 > len(s1):
                left_ch = s2[left]
                window[left_ch] -= 1
                if window[left_ch] == 0:
                    del window[left_ch]
                left += 1

            if window == need:
                return True

        return False