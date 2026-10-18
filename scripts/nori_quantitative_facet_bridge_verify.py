#!/usr/bin/env python3
"""Verify the quantitative facet bridge for legal antipodally odd cube colorings."""
from itertools import permutations
from random import Random

def orbit(y,i,n):
    full=(1<<n)-1
    a=y&~(1<<i);b=(a^full)&~(1<<i)
    return (i,min(a,b))

def check(n,seed):
    d=n-1;full=(1<<d)-1
    rng=Random(seed)
    f={}
    for x in range(1<<d):
        for i in range(d):
            y=x^(1<<i)
            f[tuple(sorted((x,y)))]=rng.randrange(2)
    g={}
    for x in range(1<<d):
        if x<(x^full):
            g[x]=rng.randrange(2)
            g[x^full]=1-g[x]
    c={}
    for (a,b),v in f.items():
        c[a+(1<<d),b+(1<<d)]=v
        c[tuple(sorted((a^full,b^full)))]=1-v
    for x in range(1<<d):c[x,x+(1<<d)]=g[x]
    def color(x,i):
        return c[tuple(sorted((x,x^(1<<i))))]
    counts={}
    for x in range(1<<d):
        p0=p1=0
        for pi in permutations(range(d)):
            y=x;word=[]
            for i in pi:
                z=y^(1<<i);word.append(f[tuple(sorted((y,z)))]);y=z
            p0+=all(a<=b for a,b in zip(word,word[1:]))
            p1+=all(a>=b for a,b in zip(word,word[1:]))
        counts[x]=(p0,p1)
    expected={}
    for x in range(1<<d):
        if x < (x^full):
            assert counts[x][1]==counts[x^full][0]
            expected[orbit(x,d,n)]=counts[x][g[x]]
    supports={}
    for root in range(1<<n):
        for pi in permutations(range(n)):
            y=root;es=[];ts=[]
            for k,i in enumerate(pi):
                es.append(orbit(y,i,n))
                ts.append((min(y,y^((1<<n)-1)),tuple(sorted((pi[k-1],i)))))
                y^=1<<i
            supports[frozenset(es)]=frozenset(ts)
    got={e:0 for e in expected}
    for es,ts in supports.items():
        changes=sum(color(y,i)!=color(y,j) for y,(i,j) in ts)
        if changes==1:
            v=next(e for e in es if e[0]==d)
            got[v]+=1
    assert got==expected,(n,seed,got,expected)
    paired=sum(counts[x][0]>0 and counts[x][1]>0
               for x in range(1<<d) if x<(x^full))
    used=sum(v>0 for v in got.values())
    assert used>=paired
    print('Q%d, seed %d: %d good supports, %d used bridge orbits, %d forced paired-root orbits'%
          (n,seed,sum(got.values()),used,paired))

if __name__=='__main__':
    for n in (3,4,5):
        for seed in range(7):check(n,101+n*7+seed)
