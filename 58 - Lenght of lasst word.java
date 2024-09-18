#Given a string s consisting of words and spaces, return the length of the last word in the string.

class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();
        int len = 0;
        for(int n=s.length()-1;n>=0;n--){
            if(s.charAt(n)==' '){
                return len;
            }
            len++;
        }
        return len;
    }
}
