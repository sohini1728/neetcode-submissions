class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Logic: Add all the element and counts of everything from string 
        #s to the hashmap and then go through every letter of string t
        #and subtract the count -- if the hashmap is empty at the end 
        #it is an anagram, otherwise it's not an anagram 
        if len(s) != len(t): 
            return False
        #forward pass
        tempMap = {}
        for tempChar in s: 
            if tempChar in tempMap: 
                tempMap[tempChar]+= 1 
            else: 
                tempMap[tempChar] = 1 
        
        #backwards pass
        for tempChar in t: 
            if tempChar in tempMap: 
                tempMap[tempChar] -= 1
            else: 
                return False
            
        for val in tempMap.values(): 
            if val != 0: 
                return False
        return True

        