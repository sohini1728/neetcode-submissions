class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}  # dictionary: sorted signature -> list of original strings

        for s in strs:
            key = "".join(sorted(s))  # sort letters, join back into a string

            if key not in groups:
                groups[key] = []  # first time seeing this signature, start a new list

            groups[key].append(s)  # add the original word to its group

        return list(groups.values())  # drop the keys, just return the groups