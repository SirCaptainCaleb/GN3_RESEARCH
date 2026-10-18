#!/usr/bin/env python3
"""Adaptive odd-seam lifting, full path clause enumeration, and strict boundary."""
from itertools import permutations
from random import Random

def orbit(n,x,i):
    z=x&~(1<<i);q=(z^((1<<n)-1))&~(1<<i)
    return (i,min(z,q)),int(z!=min(z,q))

def clauses(n,c):
    C=set()
    for root in range(1<<(n-1)):
        for order in permutations(range(n)):
            z=root;fixed=[];free=[]
            for i in order:
                e,s=orbit(n,z,i)
                (free if i<2 else fixed).append((e,s) if i<2 else c(z,i))
                z^=1<<i
            if len(set(fixed))==1:
                C.add(frozenset((e,fixed[0]^s) for e,s in free))
    return C

def test(a,b,seed):
    rand=Random(seed);A=(1<<a)-1;R=(1<<(a-2))-1
    F={}
    for i in range(2,a):
        for x in range(1<<a):
            e,_=orbit(a,x,i)
            if e not in F:F[e]=rand.randrange(2)
    def f(x,i):
        e,s=orbit(a,x,i)
        return F[e]^s
    hb={r:rand.randrange(2) for r in range(1<<(a-3))}
    def h(x):
        r=x>>2
        return hb[min(r,r^R)]^int(r>r^R)
    E={}
    for w in range(1<<b):
        p=min(w,w^((1<<b)-1))
        if p not in E:E[p]=rand.randrange(2)
    def psi(w):return E[min(w,w^((1<<b)-1))]
    def c(z,i):
        x=z&A;w=z>>a
        return f(x,i)^psi(w) if i<a else h(x)
    full=clauses(a+b,c)
    for w in range(1<<b):
        base=clauses(a,lambda x,i:f(x,i)^psi(w))
        mapped=set()
        for clause in base:
            target=[]
            for (i,rep),p in clause:
                chosen=rep if h(rep)==0 else ((rep^A)&~(1<<i))
                _,s=orbit(a,chosen,i)
                e,t=orbit(a+b,chosen|(w<<a),i)
                target.append((e,p^s^t))
            mapped.add(frozenset(target))
        assert mapped<=full,(a,b,w,seed)
    return True

def majority():
    # Depends nonlinearly on three prescribed A bits; no fixed pivot works.
    h=lambda x:int(sum((x>>i)&1 for i in (2,3,4))>=2)
    assert all(h(x)^h(x^31) for x in range(32))
    assert all(any(h(x)==h(x^(1<<k)) for x in range(32))
               for k in (2,3,4))
    f=lambda x,i:(x>>((i+1)%5))&1
    C=clauses(6,lambda z,i:f(z&31,i) if i<5 else h(z&31))
    B=clauses(5,f)
    for w in (0,1):
        lifted=set()
        for clause in B:
            target=[]
            for (i,rep),p in clause:
                a=rep if h(rep)==0 else ((rep^31)&~(1<<i))
                _,s=orbit(5,a,i);e,t=orbit(6,a|(w<<5),i)
                target.append((e,p^s^t))
            lifted.add(frozenset(target))
        assert lifted<=C

def boundary():
    f=lambda x,i:(x>>1)&1
    h=lambda x:int(x in (0,4,5,6))
    assert all(h(x)^h(x^7) for x in range(8))
    B=clauses(3,f)
    C=clauses(4,lambda z,i:f(z&7,i) if i<3 else h(z&7))
    orbs=sorted({orbit(3,x,i)[0] for x in range(8) for i in (0,1)})
    counts=[]
    for mask in range(16):
        trans={}
        for j,(i,rep) in enumerate(orbs):
            a=rep if not ((mask>>j)&1) else ((rep^7)&~(1<<i))
            _,s=orbit(3,a,i);e,t=orbit(4,a,i)
            trans[i,rep]=(e,s^t)
        target={frozenset((trans[e][0],p^trans[e][1]) for e,p in clause)
                for clause in B}
        counts.append(len(target&C))
    assert len(B)==12 and max(counts)==10
    print('Boundary: no full 12-clause copy among 16 orbit gauges')

if __name__=='__main__':
    for a,b,cases in ((3,1,10),(4,1,10),(3,2,10),(4,2,6),(3,3,5),(5,1,3)):
        for seed in range(cases):test(a,b,seed)
        print('PASS Q%d x Q%d (%d cases)'%(a,b,cases))
    majority()
    boundary()
    print('PASS adaptive seam theorem and strict boundary')
