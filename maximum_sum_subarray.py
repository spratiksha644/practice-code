class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        wstart = 0
        wend = 0
        sum1 = 0
        ans = 0
        while(wend< len(Arr)):
            sum1 += Arr[wend]
            if((wend - wstart) + 1 == K):
                ans = max(sum1, ans)
                sum1 -= Arr[wstart]
                start += 1
            end += 1
        return ans
