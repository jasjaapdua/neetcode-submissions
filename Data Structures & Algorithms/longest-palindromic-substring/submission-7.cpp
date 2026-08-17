class Solution {
public:
    string longestPalindrome(string s) {
        int max_len = 0;
        string result = "";
        for(int i = 0; i < s.length(); i++){
            string odd = checkPalindrome(s, i, i);
            string even = checkPalindrome(s, i, i + 1);
            if (max_len < odd.length()){
                max_len = odd.length();
                result = odd;
            }
            if (max_len < even.length()){
                max_len = even.length();
                result = even;
            }
        }
        return result;
    }
    string checkPalindrome(string& s, int l, int r){
        if(l >= 0 && r < s.length() && s[l] == s[r]){
            return checkPalindrome(s, l - 1, r + 1);
        }
        else{
            l++;
            r--;
            return s.substr(l, r - l + 1);
        }
    }
};
