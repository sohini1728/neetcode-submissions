class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False

        counts = {}

        # Count each character in s
        for char in s:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1

        # Subtract counts using t
        for char in t:
            if char not in counts:
                return False

            counts[char] -= 1

            if counts[char] < 0:
                return False

        return True