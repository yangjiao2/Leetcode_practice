class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i in range(len(nums)):

            if nums[i] not in d.keys():
                d[nums[i]] = i
            if target - nums[i] in d.keys() and d[target - nums[i]] != i:
                return [i, d[target - nums[i]]]
        return [-1, -1]


"""
1st fail: misleading by example thinking that the list is increasing

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int right = 0;
        int left = 0;
        int [] result = new int[2];;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] > target / 2){
                left = i;
                right = i;
            }
        }
        
        while (left > 0 && right < nums.length && right < target){
            
            if (nums[left] + nums[right] == target){
                result = [left, right];
            }else if (nums[left] + nums[right] < target){
                left = left - 1;
            }else{
                right = right + 1;
            }
        }
    }
}


2nd fail: Line 14
first time failed because I did not check if the second's index is the same as index
"""