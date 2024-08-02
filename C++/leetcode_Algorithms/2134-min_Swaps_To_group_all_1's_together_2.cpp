class Solution {
public:
    int minSwaps(vector<int>& nums) {
        int n = nums.size();
        int ones = 0;
        for(int i = 0; i < n; i++) {
            if(nums[i] == 1) {
                ones++;
            }
        }
        if(ones == 0) {
            return 0;
        }
        int left = 0, right = 0;
        int maxOnes = 0;
        for(int i = 0; i < n; i++) {
            if(i < ones) {
                if(nums[i] == 1) {
                    left++;
                }
            } else {
                if(nums[i] == 1) {
                    right++;
                }
            }
            maxOnes = max(maxOnes, right);
        }
        return ones - maxOnes;
    }
};