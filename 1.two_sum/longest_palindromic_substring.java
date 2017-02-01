// be careful when checking boundaries
// this case will not work for large input size
public class Solution {
    public String longestPalindrome(String s) {
        String result = "";
        if (s.length() == 0){
            return null;
        }else if (s.length() == 1){
            return s;
        }
        
        int middle_index = -1;
        int length = -1;
        
        String new_s = "";
        for (int i = 0; i < s.length(); i++){
            new_s = new_s + "#" + s.substring(i, i+1);
        }
        new_s = new_s + "#";
        
        int counter = 1;
        for (int j = 0; j < new_s.length(); j++){
            counter = 1;
            while (j - counter >= 0 && j + counter <= new_s.length()-1 && (new_s.charAt(j-counter) == new_s.charAt(j+counter))){
                counter++;
            }
            if (counter > length){
                length = counter - 1;
                middle_index = j;
            }
        }
        new_s = new_s.substring(middle_index - length, middle_index + length + 1);
        for (int k = 1; k < new_s.length(); k = k + 2){
            result = result + new_s.charAt(k);
        }
        return result;
    }
}