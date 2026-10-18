#!/usr/bin/env python3
"""Q6xQ1 sparse selector perturbation; seven of eight star packets survive."""
from nori_sparse_selector_verify import clauses,orbit

a=6;b=1;n=a+b;A=(1<<a)-1;R=(1<<(a-2))-1
h=lambda x:((x>>2)&1)^int(x in (0,A))
f=lambda x,i:x&1
c=lambda z,i:f(z&A,i) if i<a else h(z&A)
C=clauses(n,c);B=clauses(a,f)
assert all(h(x)^h(x^A) for x in range(1<<a))
assert sum(h(x)!=h(x^(1<<i)) for i in (0,1) for x in range(1<<a))==8
packets=[]
for s in range(1<<(a-2)):
    if s>s^R:continue
    X,sx=orbit(a,s<<2,0)
    Y,sy=orbit(a,s<<2,1)
    Z,sz=orbit(a,(s^R)<<2,1)
    packet={frozenset(((X,1^sx),(Y,0^sy))),
            frozenset(((X,1^sx),(Y,1^sy))),
            frozenset(((X,0^sx),(Z,0^sz))),
            frozenset(((X,0^sx),(Z,1^sz)))}
    assert packet<=B
    safe=all(h(rep)==h(rep^(1<<i)) for i,rep in (X,Y,Z))
    if safe:
        for w in (0,1):
            lifted=set()
            for clause in packet:
                row=[]
                for (i,rep),p in clause:
                    v=rep if h(rep)==0 else ((rep^A)&~(1<<i))
                    _,old=orbit(a,v,i);e,new=orbit(n,v|(w<<a),i)
                    row.append((e,p^old^new))
                lifted.add(frozenset(row))
            assert lifted<=C
    packets.append((s,safe))
assert len(packets)==8 and sum(ok for _,ok in packets)==7
print("PASS: two unsafe free orbits, seven of eight orbit-disjoint forcing packets lift per layer")
