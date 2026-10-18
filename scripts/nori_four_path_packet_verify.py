#!/usr/bin/env python3
"""Dimension-uniform four-geodesic packet for two free direction classes.

Prints the unique monochromatic path for each assignment of the two selected
edge-orbit variables in every dimension Q4--Q10. Standard library only.
"""
from itertools import product

def orbit(n,x,i):
    mask=(1<<n)-1
    y=x&~(1<<i)
    z=(y^mask)&~(1<<i)
    return (i,min(y,z)),int(y!=min(y,z))

def packet(n):
    extra=list(range(4,n))
    m=sum(1<<k for k in extra)
    return [
        (4|m,(*extra,1,0,2,3),'00'),
        (4,(1,0,*extra,3,2),'11'),
        (6,(0,2,*extra,3,1),'01'),
        (6,(0,3,*extra,2,1),'10')]

def fixed(x,i):
    if i==2:return x>>3&1
    if i==3:return x>>2&1
    assert i>=4
    return (x&1)^int((x&15) in (3,12))

def check(n):
    lines=[]
    for start,order,label in packet(n):
        vertex=start
        free=[]
        for i in order:
            e,sign=orbit(n,vertex,i)
            if i>=2:
                assert fixed(vertex,i)==int(label[0]),(n,label,vertex,i)
            else:
                free.append((i,e,sign))
            vertex ^= 1<<i
        assert vertex==start^((1<<n)-1)
        assert len(free)==2
        lines.append((label,free))
    iorbits={e for _,F in lines for i,e,s in F if i==0}
    jorbits={e for _,F in lines for i,e,s in F if i==1}
    assert len(iorbits)==len(jorbits)==1
    iorb=next(iter(iorbits));jorb=next(iter(jorbits))
    assert iorb==(0,6) and jorb==(1,4)
    for a,b in product((0,1),repeat=2):
        witnesses=[]
        for label,F in lines:
            bit=int(label[0])
            vals=[(a if i==0 else b)^s for i,e,s in F]
            if vals==[bit,bit]:witnesses.append(label)
        assert witnesses==[str(a)+str(b)],(n,a,b,witnesses)
    print('Q%d: two common free orbits, four colors, four forcing paths, PASS'%n)

if __name__=='__main__':
    for n in range(4,11):check(n)
