class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = Count()
        l, r = 0, 0
        ans = 0
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            while len(count) == 3:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]] 
                l += 1
            ans = max(ans, r + 1 - l)
        return ans
