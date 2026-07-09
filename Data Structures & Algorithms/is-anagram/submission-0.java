class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        HashMap<Character,Integer> totalChars = new HashMap<>();
        for (char d: s.toCharArray()){
            totalChars.put(d,totalChars.getOrDefault(d,0)+1); 
        }
        for (char c: t.toCharArray()){
            if (totalChars.containsKey(c)){
                totalChars.put(c,totalChars.get(c)-1); 
            }
            else{
                return false;
            }
        }
        for (int count: totalChars.values()){
            if (count != 0){
                return false;
            }
        }
        return true;
    }
}
