class Solution {
    public int[] twoSum(int[] nums, int target) {
        int [] result = new int[2];
        
        if(nums.length==0){
            return null;
        }
        for(int i =0;i< nums.length-1;i++){
            for(int j = i+1; j< nums.length;j++){
                if(nums[j]+nums[i]==target){
                    result[0] = i;
                    result [1] = j;
                    break;
                }
            }
        }
        
        return result;
        
    }
}