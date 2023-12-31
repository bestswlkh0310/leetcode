class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int result = 0;
        while (left < right) {
            int v = (right - left) * std::min(height[left], height[right]);
            if (result < v) {
                result = v;
            }
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return result;
    }
};