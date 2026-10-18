#!/usr/bin/env python3
"""Classify the 104 minima produced by nori_q5_parity_census.cpp.
Usage: python nori_q5_parity_symmetry.py census-output.txt
"""
import itertools,re,sys
from collections import Counter,defaultdict

txt=open(sys.argv[1]).read()
line=re.search(r'^MIN_MASKS=(.*)$',txt,re.M)
assert line
minima={int(x,16) for x in line.group(1).split(',') if x}
assert len(minima)==104
FULL=31
orbits=[];index={}
for d in range(2,5):
    for x in range(32):
        y=x&~(1<<d);a=min(y,(y^FULL)&~(1<<d))
        if (d,a) not in index:
            index[d,a]=len(orbits);orbits.append((d,a))
assert len(orbits)==24

def color(mask,d,x):
    y=x&~(1<<d);a=min(y,(y^FULL)&~(1<<d))
    return ((mask>>index[d,a])&1)^(y!=a)

def permute(x,pi):
    return sum(((x>>i)&1)<<pi[i] for i in range(5))

def transform(mask,pi,t,flip):
    return sum((color(mask,pi[d],permute(x,pi)^t)^flip)<<i
               for i,(d,x) in enumerate(orbits))

perms=[(0,1)+p for p in itertools.permutations((2,3,4))]
remaining=minima.copy();classes=[]
while remaining:
    mask=min(remaining)
    group={transform(mask,p,t,f) for p in perms for t in range(32) for f in range(2)}
    assert group<=minima
    remaining.difference_update(group)
    classes.append((len(group),mask))
assert sorted(s for s,_ in classes)==[2,6,24,24,48]
print('classes',[(s,hex(m)) for s,m in sorted(classes,reverse=True)])

# Independently regenerate all 1920 rooted projective full-geodesic paths.
all_orbits={};edge={}
for d in range(5):
    for x in range(32):
        y=x&~(1<<d);a=min(y,(y^FULL)&~(1<<d))
        if (d,a) not in all_orbits:all_orbits[d,a]=len(all_orbits)
        edge[x,d]=(all_orbits[d,a],int(y!=a))
paths=[]
for root in range(16):
    for order in itertools.permutations(range(5)):
        x=root;fixed=[];free=[]
        for d in order:
            idx,s=edge[x,d]
            (free if d<2 else fixed).append((idx if d<2 else idx-16,s))
            x^=1<<d
        paths.append((fixed,free))
assert len(paths)==1920
shapes=Counter()
for mask in minima:
    clauses=set()
    for fixed,free in paths:
        t=(mask>>fixed[0][0]&1)^fixed[0][1]
        if any(((mask>>k&1)^s)!=t for k,s in fixed[1:]):continue
        (a,sa),(b,sb)=free
        if a>=8:a,sa,b,sb=b,sb,a,sa
        clauses.add((a,t^sa,b-8,t^sb))
    by=defaultdict(lambda:[[],[]])
    for a,p,b,q in clauses:by[a][p].append((b,q))
    resolved=defaultdict(set)
    for a,(zero,one) in by.items():
        for b,p in zero:
            for c,q in one:
                if b==c:continue
                pair=(min(b,c),max(b,c))
                resolved[pair].add((p,q) if b<c else (q,p))
    contradiction=[pair for pair,assignments in resolved.items() if len(assignments)==4]
    assert len(contradiction)==4
    degree=Counter(v for pair in contradiction for v in pair)
    shapes[tuple(sorted(degree.values()))]+=1
assert shapes=={(2,2,2,2):96,(1,1,1,1,1,1,1,1):8}
print('contradiction graph degree patterns',dict(shapes))