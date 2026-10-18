#!/usr/bin/env python3
"""Brute-force check: four-vertex connector intersections vs odd selectors."""
from itertools import product,permutations
from random import Random
def orbit(n,x,i):
    a=x&~(1<<i);b=(a^((1<<n)-1))&~(1<<i)
    return (i,min(a,b)),int(a!=min(a,b))
def test(a,b,seed):
    rng=Random(seed);n=a+b;am=(1<<a)-1
    bits={}
    for i in range(a,n):
        for x in range(1<<n):
            e,s=orbit(n,x,i)
            if e not in bits:bits[e]=rng.randrange(2)
    def c(x,i):
        e,s=orbit(n,x,i)
        return bits[e]^s
    def S(x,w):
        out=set()
        for p in permutations(range(b)):
            z=w;word=[]
            for k in p:
                word.append(c(x|(z<<a),a+k));z^=1<<k
            if len(set(word))==1:out.add(word[0])
        return out
    W=tuple(w for w in range(1<<b) if rng.random()<.65) or (0,)
    C={x:set.intersection(*(S(x,w) for w in W)) for x in range(1<<a)}
    assert all(C[x^am]=={1-t for t in C[x]} for x in C)
    rm=(1<<(a-2))-1
    faces={z:[(z<<2)|u for u in range(4)] for z in range(1<<(a-2))}
    I={z:set.intersection(*(C[x] for x in face)) for z,face in faces.items()}
    feasible=all(I.values())
    reps=sorted({min(z,z^rm) for z in faces})
    brute=False
    for v in product((0,1),repeat=len(reps)):
        choices=dict(zip(reps,v))
        if all((choices[min(z,z^rm)]^int(z>z^rm)) in I[z] for z in I):
            brute=True;break
    assert feasible==brute
    if not feasible:
        assert any((not C[x]) or
                   any(C[x]=={0} and C[y]=={1} for y in face)
                   for face in faces.values() for x in face)
    return feasible
if __name__=="__main__":
    for a,b in ((3,1),(4,1),(4,2),(5,2),(3,3)):
        count=sum(test(a,b,s) for s in range(40))
        print("PASS Q%dxQ%d: 40 legal cases, %d selectors"%(a,b,count))
