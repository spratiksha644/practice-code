class Solution:


	def search(self,pat, txt):
	    # code here
	    c=0
        n = len(pat)
        pattern=sorted(pat)
        m = ''.join(pattern)
        for i, item in enumerate(txt):
            if txt[i] in m:
                p = txt[i:i+n]
                sort1 = sorted(p)
                num = ''.join(sort1)
                if num == m:
                    c+=1
        return c
