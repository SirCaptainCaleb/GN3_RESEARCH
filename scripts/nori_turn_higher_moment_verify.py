#!/usr/bin/env python3
"""NORI1 all-order turn incidence and Q7 moment certificate.
Run: python scripts/nori_turn_higher_moment_verify.py
Requires Python 3.10+ and sympy.
"""
import itertools as it
import math
import random
from collections import Counter
import sympy as sp

def proj(x,n):
    return min(x,x^((1<<n)-1))

def supports(n):
    out=set()
    for x in range(1<<(n-1)):
        for order in it.permutations(range(n)):
            y=x
            turns=[]
            for k,d in enumerate(order):
                turns.append((proj(y,n),tuple(sorted((order[k-1],d)))))
                y^=1<<d
            out.add(tuple(sorted(turns)))
    return out

def multi(n,U):
    U=list(dict.fromkeys(U))
    if not U:
        return 2**(n-2)*math.factorial(n-1)
    x,(i,j)=U[0]
    full=(1<<n)-1
    cuts=[]
    for y,ab in U[1:]:
        if y==x: return 0
        d=x^y
        if (d>>i&1)==(d>>j&1):return 0
        B=d if d>>j&1 else d^full
        entering=[h for h in ab if B>>h&1]
        if len(entering)!=1:return 0
        exiting=next(h for h in ab if h!=entering[0])
        cuts.append((B,entering[0],exiting))
    cuts.sort(key=lambda v:v[0].bit_count())
    previous=0
    first=j
    answer=1
    for B,last,nextfirst in cuts+[(full,i,-1)]:
        if (B&previous)!=previous:return 0
        block=B^previous
        size=block.bit_count()
        if not size or not (block>>first&1) or not (block>>last&1):return 0
        if (size==1)!=(first==last):return 0
        if size>1:answer*=math.factorial(size-2)
        first=nextfirst
        previous=B
    return answer

def test_incidence(n):
    oo=supports(n)
    assert len(oo)==2**(n-2)*math.factorial(n-1)
    turns=sorted(set(t for O in oo for t in O))
    count=0
    for k in range(1,min(n,4)+1):
        actual=Counter(U for O in oo for U in it.combinations(O,k))
        for U,v in actual.items():
            assert multi(n,U)==v,(n,U,v,multi(n,U))
        count+=len(actual)
    rng=random.Random(n)
    for k in range(2,min(n,5)+1):
        for _ in range(1000):
            U=rng.sample(turns,k)
            assert multi(n,U)==sum(set(U)<=set(O) for O in oo)
    print('n=',n,'supports=',len(oo),'positive incidences checked=',count)

def pair(n,p,q,y):
    return multi(n,[(0,p),(proj(y,n),q)])

def spectrum7():
    n=7
    pairs=list(it.combinations(range(n),2))
    z=sp.symbols('z')
    expected={
        0:z**6*(z-840)*(z-120)**14,
        1:z**2*(z-120)**4*(z-88)**5*(z*z-480*z+20160)*(z*z-280*z+15360)**4,
        7:z**4*(z-312)*(z-216)**2*(z-120)**9*(z-72)*(z*z-312*z+18432)**2,
        31:z**6*(z-264)*(z-184)**9*(z-120)**5,
    }
    for S,poly in expected.items():
        K=sp.Matrix([[sum((1-2*((S&y).bit_count()%2))*pair(n,p,q,y) for y in range(64))
                       for q in pairs] for p in pairs])
        assert sp.expand(K.charpoly(z).as_expr()-poly)==0,S
    print('n=7 all four Fourier block characteristic polynomials verified')

def example7():
    def c(x,i):
        if i==0:return (x>>1)&1
        if i==1:return 1^(x&1)
        if i in (2,3,5):return x&1
        return 1^(x&1)
    n=7
    h=Counter()
    for x in range(1<<(n-1)):
        for p in it.permutations(range(n)):
            bits=[];v=x
            for i in p:
                bits.append(c(v,i));v^=1<<i
            k=sum(bits[j]!=bits[j+1] for j in range(n-1))
            k+=bits[-1]==bits[0]
            h[2*k]+=1
    h=Counter({E:m//(2*n) for E,m in h.items()})
    assert h=={2:1152,6:10368,10:10368,14:1152},h
    mu=sum(E*m for E,m in h.items())/23040
    variance=sum((E-mu)**2*m for E,m in h.items())/23040
    assert mu==8 and variance==36/5
    hypothetical={6:13824,10:6912,14:2304}
    assert sum(hypothetical.values())==23040
    assert sum(E*m for E,m in hypothetical)/23040==mu
    assert sum((E-mu)**2*m for E,m in hypothetical)/23040==variance
    for x in range(128):
        assert sum(c(x,i) for i in range(7)) in (3,4)
        for i in range(7):
            assert c(x,i)==c(x^(1<<i),i)
            assert c(x,i)!=c(x^127,i)
    print('n=7 balanced coloring and moment-matching zero-witness histogram verified')


def sparse_affine_example7():
    """Second balanced coloring with only 480 good coherent supports."""
    from collections import Counter
    n=7
    d=(1,0,0,6,6,1,1)
    b=(0,1,0,0,1,0,1)
    counts=Counter()
    for pi in it.permutations(range(n)):
        for x0,x1,x6 in it.product((0,1),repeat=3):
            x={0:x0,1:x1,6:x6}
            seen=set()
            seq=[]
            for i in pi:
                seq.append(b[i]^x[d[i]]^(d[i] in seen))
                seen.add(i)
            m=sum(seq[j]!=seq[j+1] for j in range(n-1))
            m+=(seq[-1]==seq[0])
            counts[2*m]+=1
    assert counts=={2:840,6:19656,10:18648,14:1176},counts
    support_counts={E:4*v//7 for E,v in counts.items()}
    assert support_counts=={2:480,6:11232,10:10656,14:672}
    assert sum(support_counts.values())==23040
    mean=sum(E*v for E,v in support_counts.items())/23040
    var=sum((E-mean)**2*v for E,v in support_counts.items())/23040
    assert mean==8 and var==28/5
    formal={6:12672,10:9216,14:1152}
    assert sum(formal.values())==23040
    assert sum(E*v for E,v in formal.items())/23040==mean
    assert sum((E-mean)**2*v for E,v in formal.items())/23040==var
    print('n=7 sparser balanced affine example verified:',support_counts)

if __name__=='__main__':
    for n in (3,4,5,6):test_incidence(n)
    spectrum7()
    example7()
    sparse_affine_example7()
