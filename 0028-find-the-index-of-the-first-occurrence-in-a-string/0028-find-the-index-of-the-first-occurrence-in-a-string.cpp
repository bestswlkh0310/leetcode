class Solution {
public:
    int strStr(string haystack, string needle) {
        int result = haystack.find(needle);
        return result == std::string::npos ? -1 : result;
    }
};