#!/usr/bin/env python3
"""Safe free-orbit clause lifting under arbitrary odd connector colors."""
from itertools import permutations
from random import Random

def orbit(n,x,i):
    m=(1<<n)-1;a=x&~(1<<i);b=(a^m)&~(1<<i)
    return (i,min(a,b)),int(a!=min(a,b))

def clauses(n,col):
    out=set()
    for root in range(1<<(n-1)):
        for pi in permutations(range(n)):
            x=root;fr=[];fixed=[]
            for i in pi:
                e,s=orbit(n,x,i)
                if i<2:fr.append((e,s))
                else:fixed.append(col(x,i))
                x^=1<<i
            if len(set(fixed))==1:
                t=fixed[0]
                out.add(frozenset((e,t^s) for e,s in fr))
    return out

def check(a,b,seed):
    rand=Random(seed);am=(1<<a)-1
    fb={}
    for i in range(2,a):
        for x in range(1<<a):
            e,s=orbit(a,x,i)
            if e not in fb:fb[e]=rand.randrange(2)
    def f(x,i):
        e,s=orbit(a,x,i);return fb[e]^s
    hb={}
    for x in range(1<<a):
        k=min(x,x^am)
        if k not in hb:hb[k]=rand.randrange(2)
    def h(x):return hb[min(x,x^am)]^int(x>x^am)
    gb={}
    for w in range(1<<b):
        k=min(w,w^((1<<b)-1))
        if k not in gb:gb[k]=rand.randrange(2)
    def psi(w):return gb[min(w,w^((1<<b)-1))]
    def color(z,i):
        x=z&am;w=z>>a
        return f(x,i)^psi(w) if i<a else h(x)
    C=clauses(a+b,color)
    safe={}
    for i in (0,1):
        for x in range(1<<a):
            e,_=orbit(a,x,i)
            safe[e]=h(x)==h(x^(1<<i))
    U=sum(not val for val in safe.values())
    derivative=sum(h(x)!=h(x^(1<<i))
                   for i in (0,1) for x in range(1<<a))
    assert U==derivative//4
    for w in range(1<<b):
        B=clauses(a,lambda x,i:f(x,i)^psi(w))
        mapped=set()
        for clause in B:
            if not all(safe[e] for e,p in clause):continue
            target=[]
            for (i,rep),p in clause:
                v=rep if h(rep)==0 else ((rep^am)&~(1<<i))
                assert h(v)==h(v^(1<<i))==0
                _,s=orbit(a,v,i);e,t=orbit(a+b,v|(w<<a),i)
                target.append((e,p^s^t))
            mapped.add(frozenset(target))
        assert mapped<=C,(a,b,seed,w)
    return U

if __name__=="__main__":
    for a,b,N in ((3,1,10),(4,1,10),(3,2,10),(4,2,5),(5,1,5)):
        vals=[check(a,b,i) for i in range(N)]
        print("PASS Q%dxQ%d, %d odd selectors, unsafe range %d-%d"%
              (a,b,N,min(vals),max(vals)))
