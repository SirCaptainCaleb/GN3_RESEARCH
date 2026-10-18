#!/usr/bin/env python3
"""Randomized check of the all-zero bridge-row ordered-spine completion lemma.
Self-contained; fixed seed; verifies original edge colors, not formal row bits."""
from itertools import combinations
from random import Random
rng=Random(16162026)
def coloring(n):
    table=[]
    mirror=(1<<(n-1))-1
    for i in range(n):
        bits=[rng.getrandbits(1) for _ in range(1<<(n-2))]
        vals=[]
        for x in range(1<<n):
            a=(x&((1<<i)-1))|((x>>(i+1))<<i)
            b=min(a,a^mirror)
            vals.append(bits[b] ^ (a>b))
        table.append(vals)
    return table
def audit(n,count=40000):
    accepted=spines=double=0
    for _ in range(count):
        c=coloring(n)
        T=[[False]*n for _ in range(n)]
        for i,j in combinations(range(n),2):
            T[i][j]=bool(rng.getrandbits(1))
            T[j][i]=not T[i][j]
        root=rng.randrange(1<<n)
        rows=[]
        for i in range(n):
            w=sum((1<<j) for j in range(n) if j!=i and
                  (((root>>j)&1) ^ int(T[j][i])))
            rows.append(w)
        if any(c[i][rows[i]] for i in range(n)):continue
        accepted+=1
        for k in (1,2,3):
            for K in combinations(range(n),k):
                S=[i for i in range(n) if i not in K]
                S.sort(key=lambda i:-sum(T[i][j] for j in S if j!=i))
                if any(not T[S[a]][S[b]]
                       for a in range(len(S)) for b in range(a+1,len(S))):continue
                cuts={}
                for j in K:
                    bits=[T[i][j] for i in S]
                    if any(not bits[t] and bits[t+1] for t in range(len(bits)-1)):break
                    cuts[j]=sum(bits)
                if len(cuts)!=len(K):continue
                order=[]
                for p in range(len(S)+1):
                    order.extend(sorted(j for j in K if cuts[j]==p))
                    if p<len(S):order.append(S[p])
                x=root;observed={}
                for i in order:
                    observed[i]=c[i][x];x^=1<<i
                assert x==root^((1<<n)-1)
                assert all(observed[i]==0 for i in S)
                assert sum(observed.values())<=k
                spines+=1
                if k==2:
                    a,b=K
                    if cuts[a]!=cuts[b] and T[a][b]!=(cuts[a]<cuts[b]):
                        double+=1
                        assert all(observed[i]==c[i][rows[i]^(1<<(b if i==a else a))]
                                   for i in K)
    return accepted,spines,double
for n in range(4,8):
    print(n,*audit(n))
