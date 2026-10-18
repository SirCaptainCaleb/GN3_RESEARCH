#!/usr/bin/env python3
"""Two free direction classes: independently verify bipartite 2-SAT certificates.

Standard Python only. Exhausts all fixed Q4 facet-color contexts and all
legal Q4 colorings, checking CNF truth against monochromatic geodesics.
"""
from itertools import permutations
from collections import Counter
from random import Random

def make(n):
    mask=(1<<n)-1
    orbits={}; edge={}
    for i in range(n):
        for x in range(1<<n):
            y=x&~(1<<i)
            a=min(y,(y^mask)&~(1<<i))
            if (i,a) not in orbits:orbits[i,a]=len(orbits)
            edge[x,i]=(orbits[i,a],int(y!=a))
    free=[k for (i,a),k in orbits.items() if i in (0,1)]
    fixed=[k for (i,a),k in orbits.items() if i not in (0,1)]
    fi={k:j for j,k in enumerate(free)}
    ci={k:j for j,k in enumerate(fixed)}
    paths=[]
    for x in range(1<<(n-1)):
        for p in permutations(range(n)):
            y=x; F=[]; V=[]
            for i in p:
                k,s=edge[y,i]
                (V if i in (0,1) else F).append(((fi if i in (0,1) else ci)[k],s))
                y^=1<<i
            paths.append((F,V))
    return len(free),len(fixed),paths

def clauses(paths,mask):
    out=set()
    for F,V in paths:
        t=(mask>>F[0][0]&1)^F[0][1]
        if all(((mask>>k&1)^s)==t for k,s in F[1:]):
            (a,sa),(b,sb)=V
            out.add((a,t^sa,b,t^sb))
    return out

def unsat(n,C):
    g=[[] for _ in range(2*n)]
    rg=[[] for _ in range(2*n)]
    for a,p,b,q in C:
        u,v=2*a+p,2*b+(q^1)
        g[u].append(v);rg[v].append(u)
        u,v=2*b+q,2*a+(p^1)
        g[u].append(v);rg[v].append(u)
    seen=set();order=[]
    for z in range(2*n):
        if z in seen:continue
        seen.add(z);stack=[(z,0)]
        while stack:
            x,j=stack[-1]
            if j<len(g[x]):
                y=g[x][j];stack[-1]=(x,j+1)
                if y not in seen:seen.add(y);stack.append((y,0))
            else:stack.pop();order.append(x)
    component=[-1]*(2*n)
    label=0
    for z in reversed(order):
        if component[z]>=0:continue
        todo=[z];component[z]=label
        while todo:
            x=todo.pop()
            for y in rg[x]:
                if component[y]<0:component[y]=label;todo.append(y)
        label+=1
    return any(component[2*k]==component[2*k+1] for k in range(n))

def direct_good(paths,known,free):
    for F,V in paths:
        word=[(known>>k&1)^s for k,s in F]
        word += [(free>>k&1)^s for k,s in V]
        if len(set(word))==1:return True
    return False

def audit(n):
    v,k,paths=make(n)
    sizes=Counter()
    for fixed in range(1<<k):
        C=clauses(paths,fixed)
        assert unsat(v,C)
        # Greedily strip inessential clauses, retaining a finite certificate.
        core=list(C)
        Random(fixed+16*n).shuffle(core)
        for clause in list(core):
            remaining=set(core)-{clause}
            if unsat(v,remaining):core.remove(clause)
        assert unsat(v,core)
        sizes[len(core)]+=1
        for free in range(1<<v):
            forbidden=any((free>>a&1)==p and (free>>b&1)==q for a,p,b,q in C)
            assert forbidden==direct_good(paths,fixed,free)
    print(f"Q{n}: {1<<k} contexts, {1<<(k+v)} colorings checked; core sizes {dict(sorted(sizes.items()))}")

if __name__=="__main__":
    audit(3)
    audit(4)
