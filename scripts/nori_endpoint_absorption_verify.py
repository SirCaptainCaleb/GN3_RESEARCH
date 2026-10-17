#!/usr/bin/env python3
"""Checks the antipodal endpoint-absorption and curved-square shortening identities.

Run: python scripts/nori_endpoint_absorption_verify.py
Python standard library only. Algebraic proofs are in the matching NORI Subsection.
"""
from itertools import combinations
from collections import deque
from random import Random


def coloring(n, requirements, seed=11):
    top = (1 << n) - 1
    bits = {}
    for u,v,a in requirements:
        assert (u^v).bit_count()==1
        e=tuple(sorted((u,v)))
        ae=tuple(sorted((u^top,v^top)))
        if e in bits: assert bits[e]==a
        if ae in bits: assert bits[ae]==1-a
        bits[e]=a
        bits[ae]=1-a
    rng=Random(seed)
    for u in range(1<<n):
        for i in range(n):
            v=u^(1<<i)
            e=tuple(sorted((u,v)))
            if e in bits:continue
            ae=tuple(sorted((u^top,v^top)))
            a=rng.randrange(2)
            bits[e]=a
            bits[ae]=1-a
    def c(u,v):
        return bits[tuple(sorted((u,v)))]
    return c


def verify_path(n,P,c):
    assert P[-1]==P[0]^((1<<n)-1)
    assert len(P)==len(set(P))
    assert all((u^v).bit_count()==1 and c(u,v)==0 for u,v in zip(P,P[1:]))


def test_terminal_ear(n,alt):
    i,j=n-1,0
    word=[n-2,i]+list(range(1,n-2))+[i,j,i]
    P=[0]
    for d in word:P.append(P[-1]^(1<<d))
    z=P[-4]
    requirements=[(u,v,0) for u,v in zip(P,P[1:])]
    requirements.append((z,P[-1],alt))
    c=coloring(n,requirements,11+alt)
    verify_path(n,P,c)
    Q=(P[:-3]+[P[-1]]) if alt==0 else ([1<<j]+P[:-3])
    verify_path(n,Q,c)
    assert len(Q)==n+1
    assert len({(u^v).bit_length() for u,v in zip(Q,Q[1:])})==n


def test_curvature(n):
    c=coloring(n,[],80+n)
    for x in range(1<<n):
        for i,j in combinations(range(n),2):
            y=x^(1<<i)^(1<<j)
            m1=c(x,x^(1<<i))^c(x^(1<<i),y)
            m2=c(x,x^(1<<j))^c(x^(1<<j),y)
            k=c(x,x^(1<<i))^c(x^(1<<i),y)^c(x,x^(1<<j))^c(x^(1<<j),y)
            assert m1^m2==k
            if k:assert m1!=m2


def dist(n,c,root,a):
    queue=deque([root])
    d={root:0}
    while queue:
        x=queue.popleft()
        for i in range(n):
            y=x^(1<<i)
            if y not in d and c(x,y)==a:
                d[y]=d[x]+1
                queue.append(y)
    return d


def test_endpoint_metric(n):
    top=(1<<n)-1
    for seed in range(10):
        c=coloring(n,[],100+seed)
        ds={(a,x):dist(n,c,x,a) for a in (0,1) for x in range(1<<n)}
        options=[(ds[a,x][x^top],a,x) for a in (0,1) for x in range(1<<n)
                 if x^top in ds[a,x]]
        if not options:continue
        L,a,root=min(options)
        target=root^top
        P=[root]
        while P[-1]!=target:
            y=P[-1]
            choices=[y^(1<<i) for i in range(n)
                     if c(y,y^(1<<i))==a
                     and ds[a,y^(1<<i)].get(target,10**9)==L-len(P)]
            assert choices
            P.append(choices[0])
        for t,v in enumerate(P):
            assert min(ds[0,root].get(v,10**9),ds[1,root].get(v,10**9))==t
            assert min(ds[0,v].get(target,10**9),ds[1,v].get(target,10**9))==L-t


if __name__=="__main__":
    for n in range(4,9):
        for alt in (0,1):test_terminal_ear(n,alt)
        print("Q%d terminal-ear shortening: both opposite colors verified" % n)
    for n in range(3,8):
        test_curvature(n)
        print("Q%d square-curvature XOR verified" % n)
    for n in range(3,7):
        test_endpoint_metric(n)
        print("Q%d two-color shortest-path endpoint distances verified" % n)
