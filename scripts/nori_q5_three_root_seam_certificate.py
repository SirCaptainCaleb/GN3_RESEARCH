#!/usr/bin/env python3
"""NORI1 Q5: 28 satisfiable seam pairs, but six paths on three roots force.
No external dependencies.
"""
from itertools import permutations, combinations
from collections import defaultdict

def orbit(x,i):
    a=x&~(1<<i);b=(a^31)&~(1<<i)
    return (i,min(a,b)),int(a!=min(a,b))

def c(x,i):
    return ((x>>1)&1) if i==2 else 1^((x>>(0 if i==3 else 1))&1)

free=sorted({orbit(x,i)[0] for x in range(32) for i in (0,1)})
fixed=sorted({orbit(x,i)[0] for x in range(32) for i in (2,3,4)})
assert len(free)==16 and len(fixed)==24
idx={e:k for k,e in enumerate(free)}
assert sum(c(rep,i)<<k for k,(i,rep) in enumerate(fixed))==0x3355cc
G=defaultdict(dict)
for root in range(16):
    for pi in permutations(range(5)):
        x=root;values=[];unknown=[];seam=None
        for i in pi:
            if i==4:seam=min(x&15,(x&15)^15)
            if i>=2:values.append(c(x,i))
            else:unknown.append(orbit(x,i))
            x^=1<<i
        if len(set(values))==1:
            clause=frozenset((e,values[0]^s) for e,s in unknown)
            G[seam].setdefault(clause,(root,pi))
assert sorted(G)==list(range(8))
def satisfies(clauses,word):
    return all(any(((word>>idx[e])&1)!=v for e,v in clause)
               for clause in clauses)
words={
(0,1):0xcc44,(0,2):0xe80f,(0,3):0xaaaa,(0,4):0xaaaa,
(0,5):0xcc70,(0,6):0xcc44,(0,7):0xcc44,
(1,2):0xe916,(1,3):0x33d0,(1,4):0x3bf0,(1,5):0x00f0,
(1,6):0xcc44,(1,7):0xcc44,
(2,3):0x3311,(2,4):0x3311,(2,5):0x3311,(2,6):0x000f,
(2,7):0xcc07,(3,4):0x3311,(3,5):0x3311,(3,6):0xb30f,
(3,7):0xaaaa,(4,5):0x3311,(4,6):0xb30d,(4,7):0xaaaa,
(5,6):0xa659,(5,7):0xccf0,(6,7):0xcc44}
assert set(words)==set(combinations(range(8),2))
for (a,b),word in words.items():
    assert satisfies(G[a],word) and satisfies(G[b],word)

paths=[
(11,(0,2,1,3,4),4), (4,(0,2,3,1,4),4),
(10,(0,4,3,1,2),4),(5,(0,4,1,2,3),4),
(1,(3,0,2,1,4),1), (15,(2,1,0,3,4),0)]
wanted=[
{((0,10),1),((1,12),1)}, {((0,4),0),((1,9),0)},
{((0,10),0),((1,12),1)}, {((0,4),1),((1,9),0)},
{((0,8),0),((1,12),0)}, {((0,8),1),((1,9),1)}]
six=[]
for (root,pi,sr),expect in zip(paths,wanted):
    x=root;values=[];free_edges=[];seam=None
    for i in pi:
        if i==4:seam=min(x&15,(x&15)^15)
        if i>=2:values.append(c(x,i))
        else:free_edges.append(orbit(x,i))
        x^=1<<i
    assert seam==sr and len(set(values))==1
    clause=frozenset((e,values[0]^s) for e,s in free_edges)
    assert clause==expect and clause in G[sr]
    six.append(clause)

var=[idx[e] for e in ((0,10),(0,4),(0,8),(1,12),(1,9))]
for m in range(32):
    word=sum(((m>>k)&1)<<v for k,v in enumerate(var))
    assert not satisfies(six,word)
print('PASS: all 28 two-root assignments; six-path irreducible triple-root certificate')


# Second triadic forcing packet on projective seam roots {3,6,7}.
# This set is disjoint from the first packet's {0,1,4}.
another=[
(3,(0,2,1,3,4),3,{((0,2),1),((1,4),1)}),
(9,(2,3,0,1,4),6,{((0,4),0),((1,4),0)}),
(0,(0,2,1,4,3),7,{((0,0),0),((1,5),0)}),
(3,(2,1,0,3,4),3,{((0,4),1),((1,5),1)}),
(2,(0,4,3,1,2),3,{((0,2),0),((1,4),1)}),
(1,(0,3,4,1,2),7,{((0,0),1),((1,5),0)})]
core=[]
for root,pi,sr,expected in another:
    x=root;fixed_colors=[];free_edges=[];seam=None
    for i in pi:
        if i==4:seam=min(x&15,(x&15)^15)
        if i>=2:fixed_colors.append(c(x,i))
        else:free_edges.append(orbit(x,i))
        x^=1<<i
    assert seam==sr and len(set(fixed_colors))==1
    clause=frozenset((e,fixed_colors[0]^s) for e,s in free_edges)
    assert clause==expected and clause in G[sr]
    core.append(clause)
var2=[idx[e] for e in ((0,2),(0,4),(0,0),(1,4),(1,5))]
for bits in range(32):
    word=sum(((bits>>k)&1)<<v for k,v in enumerate(var2))
    assert not satisfies(core,word)
print('PASS: two disjoint three-root six-path forcing packets')
