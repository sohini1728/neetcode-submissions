class Solution {

    public String encode(List<String> strs) {
        String finalString = "";
        for (String str: strs){
            str = str.length() + "#" + str; 
            finalString = finalString + str;
        }
        return finalString;
    }

    public List<String> decode(String str) {
    List<String> finalList = new ArrayList<>();
    int i = 0;
    while (i < str.length()) {
        int j = i;
        while (str.charAt(j) != '#') {
            j++;
        }
        int length = Integer.parseInt(str.substring(i, j));
        String word = str.substring(j + 1, j + 1 + length);
        finalList.add(word);
        i = j + 1 + length;
    }
    return finalList;
}
}
