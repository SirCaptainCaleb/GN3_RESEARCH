#!/usr/bin/env python3
"""Two-square four-path forcing packet and edge-orbit incidence.

Checks formula N(e_i,e_j)=k!(n-2-k)! through Q8 and verifies
four paths for every assignment of the three relevant free orbit bits
through Q12. Standard Python library only.
"""
from itertools import permutations, product
from math import factorial

def orbit(x,i,n):
    full=(1<<n)-1
    a=x&~(1<<i)
    b=(x^full)&~(1<<i)
    return (i,min(a,b)), int(a!=min(a,b))

def pair_incidence(n):
    start=0;second=list(range(1,n))
    counts={}
    for tail in permutations(second):
        v=start
        for i in (0,)+tail:
            e,s=orbit(v,i,n)
            counts[e]=counts.get(e,0)+1
            v^=1<<i
    full=(1<<n)-1
    for j in second:
        orbs={orbit(y,j,n)[0] for y in range(1<<n)}
        for e in orbs:
            y=e[1]
            if not (y&1):y^=full
            y&=~(1<<j)
            S=(y^1)&~1&~(1<<j)
            k=S.bit_count()
            assert counts[e]==factorial(k)*factorial(n-2-k),(n,e,counts[e],k)
    assert counts[(0,0)]==factorial(n-1)

def forced_paths(n):
    tail=tuple(range(3,n))
    return [
        (7,(1,2,0)+tail,0,'a0_b5_0'),
        (5,(2,0)+tail+(1,),0,'a0_b5_1'),
        (4,(2,0)+tail+(1,),1,'a1_b4_0'),
        (6,(1,2,0)+tail,1,'a1_b4_1')
    ]

def packet(n):
    rows=[]
    used_fixed=set()
    for root,order,t,tag in forced_paths(n):
        v=root;free={}
        for i in order:
            e,s=orbit(v,i,n)
            if i>=2:
                color=(v&1)^(i==2)
                assert color==t,(n,tag,i,v,color)
                used_fixed.add(e)
            else:
                free[i]=(e,s)
            v^=1<<i
        assert v==(root^((1<<n)-1))
        assert free[0]==((0,0),0)
        assert free[1][0] in ((1,4),(1,5))
        rows.append((tag,t,free))
    assert len(used_fixed)==2*(n-2)
    for a,b4,b5 in product((0,1),repeat=3):
        mono=[]
        for tag,t,f in rows:
            if f[1][0]==(1,4):b=b4
            else:b=b5
            if a==t and (b^f[1][1])==t:
                mono.append(tag)
        assert len(mono)==1,(n,a,b4,b5,mono)
    print('Q%d four-path packet PASS; constrained fixed orbits: %d'%(
        n,len(used_fixed)))

if __name__=='__main__':
    for n in range(3,9):
        pair_incidence(n)
        print('Q%d cross-direction pair-incidence PASS'%n)
    for n in range(4,13):packet(n)
