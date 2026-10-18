#!/usr/bin/env python3
"""Q3/Q4 census of two-projective-seam-root forcing; standard library."""
from itertools import permutations,combinations
from collections import Counter

def edge(n,x,i):
    m=(1<<n)-1;p=x&~(1<<i);b=min(p,(p^m)&~(1<<i))
    return (i,b),int(p!=b)

def groups(n,c):
    a=n-1;G={z:set() for z in range(1<<a)}
    for root in range(1<<(n-1)):
        for perm in permutations(range(n)):
            x=root;fixed=[];free=[];seam=None
            for i in perm:
                if i>=2:fixed.append(c(x,i))
                else:free.append(edge(n,x,i))
                if i==a:seam=x&((1<<a)-1)
                x^=1<<i
            if len(set(fixed))==1:
                t=fixed[0]
                G[seam].add(frozenset((e,t^s) for e,s in free))
    return G

def satisfiable(C):
    E=sorted({e for row in C for e,v in row});I={e:i for i,e in enumerate(E)}
    graph=[[] for _ in range(2*len(E))]
    for row in C:
        (e,p),(f,q)=tuple(row);a=2*I[e]+p;b=2*I[f]+q
        graph[a].append(b^1);graph[b].append(a^1)
    for k in range(len(E)):
        reach=[]
        for v in (2*k,2*k+1):
            seen={v};todo=[v]
            while todo:
                for w in graph[todo.pop()]:
                    if w not in seen:seen.add(w);todo.append(w)
            reach.append(seen)
        if 2*k+1 in reach[0] and 2*k in reach[1]:return False
    return True

for n,expected in ((3,{1:4}),(4,{2:4,4:76,5:120,6:56})):
    keys=sorted({edge(n,x,i)[0] for i in range(2,n) for x in range(1<<n)})
    mask=(1<<(n-1))-1
    roots=[x for x in range(1<<(n-1)) if x<(x^mask)]
    hist=Counter()
    for bits in range(1<<len(keys)):
        B={e:(bits>>j)&1 for j,e in enumerate(keys)}
        def color(x,i):
            e,s=edge(n,x,i);return B[e]^s
        G=groups(n,color)
        assert all(G[x]==G[x^mask] for x in G)
        assert all(satisfiable(G[x]) for x in roots)
        score=sum(not satisfiable(G[x]|G[y]) for x,y in combinations(roots,2))
        hist[score]+=1
    assert dict(hist)==expected,(n,hist)
    print(f"PASS Q{n}:",dict(hist))
