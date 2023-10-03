class Solution {
public:
    double myPow(double x, int n) {
        return pow(x, n);
        // double s = 1.0;
        // if (x == 1) return 1;
        // if (n > 0) {
        //     for (long long i = 0; i < n; i++) {
        //         s *= x;
        //     }
        // } else {
        //     for (long long i = 0; i < -(long long)n; i++) {
        //         s /= x;
        //     }
        // }
        // return s;
    }
};