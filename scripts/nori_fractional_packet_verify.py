#!/usr/bin/env python3
"""NORI1 overlapping-packet bound: full-geodesic Q7 verification, no dependencies."""
from itertools import permutations

def orbit(n,x,i):
    full=(1<<n)-1
    u=x&~(1<<i);v=(u^full)&~(1<<i)
    p=min(u,v)
    return (i,p),int(u!=p)

def clauses(n,color):
    C=set()
    for root in range(1<<(n-1)):
        for p in permutations(range(n)):
            x=root;fixed=[];free=[]
            for i in p:
                e,s=orbit(n,x,i)
                if i<2:free.append((e,s))
                else:fixed.append(color(x,i))
                x^=1<<i
            if len(set(fixed))==1:
                t=fixed[0]
                C.add(frozenset((e,t^s) for e,s in free))
    return C

a=6;n=7;am=(1<<a)-1;R=(1<<(a-2))-1;m=1<<(a-2)
def h(x):
    q=((x>>3)&1)==((x>>4)&1)==((x>>5)&1)
    return ((x>>2)&1) if q else (x&1)
assert all(h(x)^h(x^am) for x in range(1<<a))
inf=[sum(h(x)!=h(x^(1<<i)) for x in range(1<<a))/(1<<a) for i in (0,1)]
assert inf==[.75,0.]
base=clauses(a,lambda x,i:x&1)
full=clauses(n,lambda x,i:(x&1) if i<a else h(x&am))
unsafe=[set(),set()]
for i in (0,1):
    for s in range(m):
        x=s<<2;e,_=orbit(a,x,i)
        if h(x)!=h(x^(1<<i)):unsafe[i].add(e)
assert (len(unsafe[0]),len(unsafe[1]))==(12,0)

def packet(s):
    X,sx=orbit(a,s<<2,0)
    Y,sy=orbit(a,s<<2,1)
    Z,sz=orbit(a,(s^R)<<2,1)
    return {frozenset(((X,1^sx),(Y,0^sy))),
            frozenset(((X,1^sx),(Y,1^sy))),
            frozenset(((X,sx),(Z,sz))),
            frozenset(((X,sx),(Z,1^sz)))}

def lift(clause,w):
    L=[]
    for (i,rep),val in clause:
        x=rep if h(rep)==0 else (rep^am)&~(1<<i)
        _,s=orbit(a,x,i)
        e,t=orbit(n,x|(w<<a),i)
        L.append((e,val^s^t))
    return frozenset(L)

intact=[]
for s in range(m):
    if s>(s^R):continue
    opts=[packet(s),packet(s^R)]
    assert all(p<=base for p in opts)
    for p in opts:
        variables={e for clause in p for e,_ in clause}
        if any(e in unsafe[e[0]] for e in variables):continue
        for w in (0,1):
            assert {lift(c,w) for c in p}<=full
        intact.append(s);break

assert len(intact)==2
print("PASS: Q6 star + Q1, influence .75/0, 2 safe packets per layer")
print("Full Q7 clauses checked:",len(full))
