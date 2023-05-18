def printFirstNegativeInteger( a,n,k):
    wstart=0
    wend=k
    res=[]
    while wend<=n:
        b=a[wstart:wend]
        c=0
        for i in b:
            if i < 0:
                res.append(i)
                c=1 
                break
        if c==0:
            res.append(0)
        wstart+=1
        wend+=1
    return res
