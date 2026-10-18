#!/usr/bin/env python3
"""Full arbitrary-layer seam interval formula and exterior/interior clause models."""
from itertools import permutations
from random import Random

def orbit(n,x,i):
    m=(1<<n)-1;y=x&~(1<<i);a=min(y,(y^m)&~(1<<i))
    return (i,a),int(y!=a)

def coloring(n,s):
    rng=Random(s);d={}
    for i in range(2,n):
        for x in range(1<<n):
            e,k=orbit(n,x,i)
            if e not in d:d[e]=rng.randrange(2)
    return lambda x,i:d[orbit(n,x,i)[0]]^orbit(n,x,i)[1]

def brute(n,c):
    C=set();Z=[set(),set()]
    for root in range(1<<(n-1)):
        for order in permutations(range(n)):
            x=root;fixed=[];free=[];pos={}
            for k,i in enumerate(order):
                pos[i]=k
                if i>=2:fixed.append(c(x,i))
                else:free.append(orbit(n,x,i))
                x^=1<<i
            if len(set(fixed))!=1:continue
            t=fixed[0];cl=frozenset((e,t^s) for e,s in free)
            interior=int(min(pos[0],pos[1])<pos[n-1]<max(pos[0],pos[1]))
            C.add(cl);Z[interior].add(cl)
    return C,Z

def interval(n,c):
    a=n-1;C=set();Z=[set(),set()]
    for root in range(1<<a):
        for order in permutations(range(a)):
            x=[root]
            for i in order:x.append(x[-1]^(1<<i))
            data=[(k,c(x[k],i),c(x[k],i)^c(x[k]|(1<<a),i))
                  for k,i in enumerate(order) if i>=2]
            ps=[k for k,i in enumerate(order) if i<2]
            for u in (0,1):
                for t in (0,1):
                    L,R=0,a
                    for k,alpha,d in data:
                        if not d:
                            if alpha!=t:L=a+1;break
                        elif alpha^u^t:R=min(R,k)
                        else:L=max(L,k+1)
                    for cut in range(L,R+1):
                        if c(x[cut],a)!=t:continue
                        free=[]
                        for k,i in enumerate(order):
                            if i<2:
                                y=x[k]|((u^int(k>=cut))<<a)
                                free.append(orbit(n,y,i))
                        cl=frozenset((e,t^s) for e,s in free)
                        C.add(cl)
                        Z[int(min(ps)<cut<=max(ps))].add(cl)
    return C,Z

def model(clauses,free_colors):
    return all(any(free_colors[e[0]]!=value for e,value in cl)
               for cl in clauses)

def main():
    for n,N in ((3,4),(4,256),(5,40),(6,5)):
        for seed in range(N):
            if n<=4:
                keys=sorted({orbit(n,x,i)[0] for i in range(2,n)
                             for x in range(1<<n)})
                d={e:((seed>>k)&1) for k,e in enumerate(keys)}
                c=lambda x,i:d[orbit(n,x,i)[0]]^orbit(n,x,i)[1]
            else:c=coloring(n,seed*31+2)
            a,A=brute(n,c);b,B=interval(n,c)
            assert a==b and A==B
            assert model(B[0],(0,1)) and model(B[1],(0,0))
        print(f'PASS Q{n}: {N} contexts, full clauses and two zone models')
if __name__=="__main__":main()
