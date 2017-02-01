
// first fail: forgot to think about integer overflow
// solve: 1. check if returned integer is within integer bound
// NEED TO TRAUNCATE TO LONG TYPE FIRST!!

import java.lang.*;

public class Solution {
    public int reverse(int x) {
        int result = 0;
        while ( x != 0){
            int y = x % 10;
            x = (x - y) / 10;
            result = result * 10 + y;
            if (result < Integer.MIN_VALUE || result > Integer.MAX_VALUE){
                return 0;
            }
        }

        return result;
    }
}