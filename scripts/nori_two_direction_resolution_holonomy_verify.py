#!/usr/bin/env python3
"""Two-direction paired-geodesic resolution, parity holonomy, and Q5 certificate.

Checks all 256 prescribed-color assignments in Q4, a 7-geodesic Q5
forcing packet without an ordinary four-clause orbit-pair packet, plus
sampled partial colorings in Q5 and Q6. Python standard library only.
"""
from itertools import permutations, product
from collections import defaultdict, Counter
from random import Random

def make(n):
    top=(1<<n)-1;orbits={};edge={}
    for i in range(n):
        for x in range(1<<n):
            y=x&~(1<<i);a=min(y,(y^top)&~(1<<i))
            orbits.setdefault((i,a),len(orbits))
            edge[x,i]=(orbits[i,a],int(y!=a))
    free=[k for (i,a),k in orbits.items() if i<2]
    fixed=[k for (i,a),k in orbits.items() if i>=2]
    fi={k:j for j,k in enumerate(free)}
    ci={k:j for j,k in enumerate(fixed)}
    paths=[]
    for root in range(1<<(n-1)):
        for order in permutations(range(n)):
            v=root;F=[];V=[]
            for i in order:
                k,s=edge[v,i]
                (V if i<2 else F).append(((fi if i<2 else ci)[k],s))
                v^=1<<i
            paths.append((root,order,F,V))
    return len(free),len(fixed),paths

def clauses(paths,mask,r):
    C={}
    for root,order,F,V in paths:
        t=(mask>>F[0][0]&1)^F[0][1]
        if any(((mask>>j&1)^s)!=t for j,s in F[1:]):continue
        (a,sa),(b,sb)=V
        p,q=t^sa,t^sb
        if a>=r:a,p,b,q=b,q,a,p
        assert a<r<=b
        C.setdefault((a,p,b,q),(root,order,t))
    return C

def resolve(C,r):
    by=defaultdict(lambda:[[],[]])
    for a,p,b,q in C:
        by[a][p].append((b-r,q))
    R={}
    for a,(zero,one) in by.items():
        for b,q in zero:
            for c,s in one:
                if b==c and q!=s:continue
                key=(b,q,c,s) if b<=c else (c,s,b,q)
                R.setdefault(key,((a,0,b+r,q),(a,1,c+r,s)))
    return R

def opposite_parity_pair(R):
    grouped=defaultdict(set)
    for a,p,b,q in R:
        if a!=b:grouped[a,b].add((p,q))
    for (a,b),S in grouped.items():
        if len(S)==4:return a,b
    return None

def check_q4():
    v,k,paths=make(4);r=v//2
    assert v==8 and k==8
    for mask in range(1<<k):
        C=clauses(paths,mask,r);R=resolve(C,r)
        assert opposite_parity_pair(R) is not None,mask
    print("Q4: every one of 256 fixed-color contexts has incompatible parity on a second-direction orbit pair")

def check_q5_packet():
    v,k,paths=make(5);r=v//2
    mask=0xce337b
    C=clauses(paths,mask,r);R=resolve(C,r)
    assert max(Counter((a,b) for a,p,b,q in C).values())>=4  # counting raw clauses, not patterns
    groups=defaultdict(set)
    for a,p,b,q in C:groups[a,b].add((p,q))
    assert max(map(len,groups.values()))==3
    assert opposite_parity_pair(R) is not None
    cert=[
        (1,(0,1,2,3,4),0,(0,0,8,0)),
        (15,(2,3,1,0,4),0,(0,0,9,0)),
        (0,(0,4,3,2,1),1,(0,1,8,0)),
        (2,(1,0,4,3,2),1,(0,1,8,1)),
        (8,(3,0,1,2,4),1,(0,1,9,1)),
        (3,(0,2,3,4,1),0,(1,0,9,1)),
        (8,(3,1,0,2,4),1,(1,1,8,1)),
    ]
    listed={(root,order,t):clause for root,order,t,clause in cert}
    found=defaultdict(set)
    for cl,(root,order,t) in C.items():
        found[root,order,t].add(cl)
    for (root,order,t),clause in listed.items():
        assert clause in found[root,order,t],(root,order,t,clause)
    used=sorted({a for _,_,_,(a,p,b,q) in cert}|{b for _,_,_,(a,p,b,q) in cert})
    assert used==[0,1,8,9]
    for vals in product((0,1),repeat=4):
        assignment=dict(zip(used,vals))
        assert any(assignment[a]==p and assignment[b]==q
                   for _,_,_,(a,p,b,q) in cert)
    print("Q5: mask 0xce337b has no direct 4-clause orbit-pair certificate,")
    print("but the 7 named geodesics force one for every free-color assignment.")

def check_sample(n,count):
    v,k,paths=make(n);r=v//2
    rng=Random(773*n)
    for _ in range(count):
        C=clauses(paths,rng.getrandbits(k),r);R=resolve(C,r)
        assert opposite_parity_pair(R) is not None
    print("Q%d: %d sampled partial colorings have a parity diamond" % (n,count))

if __name__=="__main__":
    check_q4()
    check_q5_packet()
    check_sample(5,200)
    check_sample(6,80)
