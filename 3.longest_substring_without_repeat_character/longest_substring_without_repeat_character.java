import java.util.ArrayList;
import java.util.HashMap;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int earlest_repeat_index = 0;
        int result = 0;
        HashMap<Character, ArrayList<Integer>> hm = new HashMap<Character, ArrayList<Integer>>();
        for (int i = 0; i < s.length(); i++){
            char ptr = s.charAt(i);
            if (!hm.containsKey(ptr)){
                ArrayList<Integer> al = new ArrayList<Integer>();
                al.add(0);
			    al.add(i);
                hm.put(ptr, al);
                if (i > result){
                    result = i;
                }
            }else{
                ArrayList<Integer> al = new ArrayList<Integer>();
                int latest = hm.get(ptr).get(1);
                al.add(hm.get(ptr).get(1));
                al.add(i);
                hm.put(ptr, al);
                if (i - latest > result){
                    result = i - latest;
                }
            }
        }
        
        return result;
    }
}