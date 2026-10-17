#!/usr/bin/env python3
"""NORI1 full-parity/zero-frequency turn Gram certificate; Python standard library."""
from itertools import combinations, permutations
from collections import Counter
from fractions import Fraction as F

def gram(n):
    E=list(combinations(range(n),2)); ix={e:k for k,e in enumerate(E)}
    U=[[0]*len(E) for _ in E]; V=[[0]*len(E) for _ in E]
    m=0
    for tail in permutations(range(1,n)):
        p=(0,)+tail
        h=[0]*len(E); a=[0]*len(E)
        for j in range(n):
            t=ix[tuple(sorted((p[j-1],p[j])))]
            h[t]=1; a[t]=(-1)**j
        for i in range(len(E)):
            for j in range(len(E)):
                U[i][j]+=h[i]*h[j]; V[i][j]+=a[i]*a[j]
        m+=1
    for i,e in enumerate(E):
        for j,f in enumerate(E):
            k=len(set(e)&set(f))
            z={2:F(2,n-1),1:F(2,(n-1)*(n-2)),0:F(4,(n-1)*(n-2))}[k]
            v={2:F(2,n-1),1:F(-2,(n-1)*(n-2)),
               0:F(4,(n-1)*(n-2)*(n-3))}[k]
            assert F(U[i][j],m)==z
            assert F(V[i][j],m)==v
    print('Gram check:',n,'orderings',m)

def color(x,i):
    if i<2: v=((x>>2)^(x>>3)^(x>>4))&1
    elif i<4: v=(x^(x>>1)^(x>>5))&1
    else: v=x&1
    return v^(i&1)

def example():
    n=6; E=list(combinations(range(n),2))
    av={e:F(0) for e in E}; bv={e:F(0) for e in E}
    h=Counter()
    for x in range(64):
        assert sum(color(x,i) for i in range(n))==3
        for i in range(n):
            assert color(x^(1<<i),i)==color(x,i)
            assert color(x^63,i)==1-color(x,i)
        for i,j in E:
            d=color(x,i)^color(x,j)
            av[i,j]+=F(d,64)
            bv[i,j]+=F(d*(-1)**x.bit_count(),64)
        for p in permutations(range(n)):
            y=x; w=[]
            for i in p:
                w.append(color(y,i));y^=1<<i
            g=sum(w[j]!=w[j+1] for j in range(n-1))+(w[-1]==w[0])
            h[g]+=1
    assert all(v%24==0 for v in h.values())
    h={g:v//24 for g,v in h.items()}
    assert h=={1:176,3:992,5:752},h
    assert sum((v-F(3,5))**2 for v in av.values())==F(3,5)
    assert sum(v*v for v in bv.values())==1
    assert all(sum(bv[tuple(sorted((i,j)))] for j in range(n) if j!=i)==0
               for i in range(n))
    L=F(2,5)*F(3,5)+F(2,3)
    mean=F(sum(g*v for g,v in h.items()),1920)
    variance=F(sum(g*g*v for g,v in h.items()),1920)-mean*mean
    assert (L,mean,variance)==(F(68,75),F(18,5),F(118,75))
    assert L>(mean-3)*(5-mean)
    print('Q6 histogram:',h,'mean',mean,'variance',variance,'L',L)

if __name__=='__main__':
    for n in (4,6,8): gram(n)
    example()
