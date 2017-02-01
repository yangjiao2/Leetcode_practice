// edge case for negative and single digit number

public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0){
            return false;
        }else if (x < 10){
            return true;
        }
        String int_str = Integer.toString(x);
        for (int i = 0; i <= (int) (int_str.length() -1)/ 2; i++){
            if (int_str.charAt(i) != int_str.charAt(int_str.length()-i-1)){
                return false;
            }
        }
        return true;
    }
}