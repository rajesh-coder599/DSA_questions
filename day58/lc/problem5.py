# 4002. Count Valid Sequences




def countValidSequences(n,k):
    mod=1000000007
    fact=[1]*(n+1)
    for i in range(1,n+1):
        fact[i]=(fact[i-1]*i)%mod
    def ncr(N,R):
        if R<0 or R>N:
            return 0
        num=fact[N]
        dom=(fact[R]*fact[N-R])%mod
        return num*pow(dom,mod-2,mod)%mod
    totalseq=ncr(n-1,k-1)
    if (n-k)%2!=0:
        return totalseq
    oddseq=ncr((n+k-2)//2,k-1)
    return totalseq-oddseq