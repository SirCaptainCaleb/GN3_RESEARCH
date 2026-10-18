#!/usr/bin/env python3
"""Independently check star parity-diamond formula and Cartesian clause lifting.

Standard-library verifier. Star cases Q3-Q6; product cases Q4 x Q2.
"""
from itertools import permutations
from random import Random

def make(n):
    full=(1<<n)-1
    keys={};edge={}
    for i in range(n):
        for x in range(1<<n):
            a=x&~(1<<i);rep=min(a,(a^full)&~(1<<i))
            if (i,rep) not in keys:keys[i,rep]=len(keys)
            edge[x,i]=(keys[i,rep],int(a!=rep))
    return keys,edge,{v:k for k,v in keys.items()}

def clauses(n,c):
    keys,edge,inv=make(n)
    h=1<<(n-2)
    C=set()
    for x in range(1<<(n-1)):
        for order in permutations(range(n)):
            z=x;fixed=[];free=[]
            for i in order:
                a,sign=edge[z,i]
                (free if i<2 else fixed).append((a,sign) if i<2 else c(z,i))
                z^=1<<i
            if len(set(fixed))!=1:continue
            t=fixed[0]
            (a,sa),(b,sb)=free
            if a>=h:a,b=b,a;sa,sb=sb,sa
            C.add((a,t^sa,b-h,t^sb))
    return C,keys,edge,inv

def test_star(n):
    C,keys,edge,inv=clauses(n,lambda z,i:z&1)
    h=1<<(n-2)
    X={};Y={}
    for s in range(h):
        a,ga=edge[s<<2,0]
        b,gb=edge[s<<2,1]
        X[a]=(s,ga);Y[b-h]=(s,gb)
    actual={(X[a][0],p^X[a][1],Y[b][0],q^Y[b][1])
            for a,p,b,q in C}
    expected={(s,p,r,0) for s in range(h) for r in range(h) for p in (0,1)}
    expected|={(s,1,s,1) for s in range(h)}
    expected|={(s,0,s^(h-1),1) for s in range(h)}
    assert actual==expected
    print("Q%d star: %d clauses; D=%d; full clause formula verified" %
          (n,len(C),h//2))

def test_product():
    rng=Random(809)
    _,e4,inv4=make(4)
    _,e6,_=make(6)
    for trial in range(4):
        mask=rng.randrange(256)
        ga,gb=rng.randrange(2),rng.randrange(2)
        def f(z,i):
            a,s=e4[z&15,i]
            return ((mask>>(a-8))&1)^s
        def product(z,i):
            if i<4:return f(z,i)
            return ((z>>5)&1)^ga if i==4 else ((z>>4)&1)^gb
        B,_,_,_=clauses(4,f)
        F,_,_,_=clauses(6,product)
        roots=(0,3) if ga!=gb else (1,2)
        copies=[]
        for w in roots:
            maps=[{},{}]
            for a,(i,rep) in inv4.items():
                if i>=2:continue
                b,sign=e6[rep|(w<<4),i]
                maps[i][a-(4 if i else 0)]=(b-(16 if i else 0),sign)
            lifted=set()
            for a,p,b,q in B:
                A,sa=maps[0][a];D,sb=maps[1][b]
                lifted.add((A,p^sa,D,q^sb))
            assert lifted<=F
            copies.append({x for group in maps for x,_ in group.values()})
        assert copies[0].isdisjoint(copies[1])
        print("Q4xQ2 product trial %d: %d clauses lifted to each disjoint orbit layer" %
              (trial,len(B)))

if __name__=="__main__":
    for n in range(3,7):test_star(n)
    test_product()
