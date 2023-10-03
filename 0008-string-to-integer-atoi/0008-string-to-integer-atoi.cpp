#include <cctype>
#include <list>
#include <iostream>

class Solution {
public:
    int myAtoi(string s) {
        int l = s.size();
        int i = 0;
        
        while (s[i] == ' ') i++;
        
        int p = 0, n = 0;
        
        if(s[i] == '+'){
            p++;
            i++;
        }

        if(s[i] == '-'){
            n++;
            i++;
        }
        #include<iostream>
        
        if(n > 0 and p > 0) return 0;
        
        long long ans = 0; 

        while (i < l and '0' <= s[i] and s[i] <= '9') {
            ans = ans * 10 + (s[i] - '0');
            i++;
            std::cout << ans << std::endl;
            if(ans > INT_MAX && n < 1) return INT_MAX;

            if(-ans < INT_MIN && n > 0) return INT_MIN;
        }
        
        
        std::cout << n << std::endl;

        if(n > 0) ans = -ans;


        return ans;
    }
};