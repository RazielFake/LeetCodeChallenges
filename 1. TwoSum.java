class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int n=0;n<nums.length;n++){
            if(map.containsKey(nums[n])){
                return new int[]{map.get(nums[n]),n};
            }
            map.put(target-nums[n], n);
        }
        return new int[]{0,0};
    }
}
