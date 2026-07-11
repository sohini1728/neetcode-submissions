class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)

        # if s1 is longer than s2, there's no way a chunk of s2 can match it
        if window_size > len(s2):
            return False

        # step 1: count how many of each letter s1 has
        # example: s1 = "abc" -> s1_letter_counts = {'a': 1, 'b': 1, 'c': 1}
        s1_letter_counts = {}
        for letter in s1:
            s1_letter_counts[letter] = s1_letter_counts.get(letter, 0) + 1

        # this will hold the letter counts for whatever chunk of s2
        # we're currently looking at (the "window")
        current_window_counts = {}

        window_start = 0  # left edge of our window

        # window_end walks through s2 one letter at a time (this is "right")
        for window_end in range(len(s2)):

            # step 2: the new letter at window_end just entered our window
            # so add it to our tally
            entering_letter = s2[window_end]
            current_window_counts[entering_letter] = current_window_counts.get(entering_letter, 0) + 1

            # step 3: if our window has grown bigger than s1's length,
            # we have one extra letter we don't want anymore -
            # it's the oldest one, sitting at window_start
            current_window_size = window_end - window_start + 1
            if current_window_size > window_size:
                leaving_letter = s2[window_start]
                current_window_counts[leaving_letter] -= 1

                # if that letter's count hits 0, remove it entirely
                # (so comparing dictionaries later works correctly)
                if current_window_counts[leaving_letter] == 0:
                    del current_window_counts[leaving_letter]

                window_start += 1  # shrink the window from the left

            # step 4: now our window is guaranteed to be exactly window_size wide
            # (once we've slid far enough) - check if it's a permutation of s1
            if current_window_counts == s1_letter_counts:
                return True

        # went through all of s2, never found a match
        return False