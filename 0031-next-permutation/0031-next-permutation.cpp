class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        for (int i = nums.size() - 1; i > 0; i--) {
            if (nums[i - 1] < nums[i]) {
                
                int mn = INT_MAX;
                int k = 0;
                
                for (int j = i; j < nums.size(); j++) {
                    if (mn > nums[j] && nums[i - 1] < nums[j]) {
                        mn = nums[j];
                        k = j;
                    }
                }
                
                std::cout << k;
                
                // i -> 
                int temp = nums[i - 1];
                nums[i - 1] = nums[k];
                nums[k] = temp;
                
                sort(nums.begin() + i, nums.end());
                
                return;
            }
        }
        
        sort(nums.begin(), nums.end());
    }
};


// 4 2 0 2 3 2 0

// 1 2 3
// 1 3 2
// 2 1 3
// 2 3 1
// 3 1 2
// 3 2 1