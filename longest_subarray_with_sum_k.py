class Solution{
    public:
    int lenOfLongSubarr(int A[],  int N, int K) 
    { 
    unordered_map<int, int> um;
    int sum = 0, max = 0;
    for (int i = 0; i < N; i++) {
        sum += A[i];
        if (sum == K)
            max = i + 1;
        if (um.find(sum) == um.end())
            um[sum] = i;
        if (um.find(sum - K) != um.end()) {
            if (max < (i - um[sum - K]))
                max = i - um[sum - K];
        }
    }
