#!/usr/bin/env python3
"""NORI1: odd co-singleton covariance and Q7 forcing, rational verification."""
from itertools import combinations, permutations
from collections import Counter
from fractions import Fraction as F
from math import factorial

def alt_mean(N, R):
    total = 0
    for p in permutations(range(N)):
        total += sum((-1)**j * R[tuple(sorted((p[j-1],p[j])))]
                     for j in range(1,N))**2
    return F(total, factorial(N))

def predicted(N, R):
    edge = list(combinations(range(N),2))
    norm = sum(R[e]**2 for e in edge)
    degrees = [sum(R[tuple(sorted((i,j)))]
                   for j in range(N) if j!=i) for i in range(N)]
    add = F(sum(d*d for d in degrees),N-2)-F(sum(degrees)**2,(N-2)*(2*N-2))
    return F(2,N*(N-1))*norm+F(2*(N-2),N*(N-3))*(norm-add)

for N in (4,6,8):
    for seed in range(4):
        R={e:((e[0]+2*e[1]+3*seed)**2%11)-5
           for e in combinations(range(N),2)}
        assert alt_mean(N,R)==predicted(N,R)
    print('Alternating-path Gram verified on',N,'labels')

n=7
masks=[98,25,16,98,110,16,21]
offset=[1,1,1,1,0,1,0]
full=(1<<n)-1
pairs=list(combinations(range(n),2))

def color(x,i):
    return offset[i]^((x&masks[i]).bit_count()&1)

for x in range(1<<n):
    for i in range(n):
        assert color(x,i)==color(x^(1<<i),i)
        assert color(x,i)+color(x^full,i)==1

def chi(x,S):
    return (-1)**((x&S).bit_count()&1)

a={ij:F(sum(color(x,ij[0])!=color(x,ij[1])
             for x in range(64)),64) for ij in pairs}
b={z:{ij:F(sum(chi(x,full^(1<<z))*
                   (color(x,ij[0])!=color(x,ij[1]))
                   for x in range(64)),64) for ij in pairs} for z in range(n)}

def proj_W_norm(ids,R):
    N=len(ids)
    norm=sum(v*v for v in R.values())
    deg=[sum(R[tuple(sorted((i,j)))] for j in ids if i!=j)
         for i in ids]
    add=F(sum(d*d for d in deg),N-2)-F(sum(deg)**2,(N-2)*(2*N-2))
    return norm,norm-add

mu=F(2,n-1)*sum(a.values())
_,w0=proj_W_norm(tuple(range(n)),a)
L0=F(2,n-1)*w0
high={}
for z in range(n):
    ids=tuple(i for i in range(n) if i!=z)
    R={(i,j):b[z][i,j]-b[z][tuple(sorted((z,i)))]
         -b[z][tuple(sorted((z,j)))] for i,j in combinations(ids,2)}
    norm,w=proj_W_norm(ids,R)
    high[z]=F(2,(n-1)*(n-2))*norm+F(2*(n-3),(n-1)*(n-4))*w
Lhigh=sum(high.values())
L=L0+Lhigh
cap=(mu-3)*(n-mu)
assert (mu,L0,Lhigh,L,cap,L-cap)==(
    F(19,6),F(11,90),F(19,30),F(34,45),F(23,36),F(7,60))
assert high=={0:F(2,15),1:F(0),2:F(47,180),3:F(43,180),
             4:F(0),5:F(0),6:F(0)}
print('mu,L0,Lhigh,L,cap,gap:',mu,L0,Lhigh,L,cap,L-cap)

hist=Counter()
for x in range(64):
    for p in permutations(range(n)):
        y=x
        w=[]
        for i in p:
            w.append(color(y,i));y^=1<<i
        g=sum(w[j]!=w[j+1] for j in range(n-1))+(w[-1]==w[0])
        assert g in (1,3,5,7)
        hist[g]+=1
assert all(z%14==0 for z in hist.values())
counts={g:v//14 for g,v in hist.items()}
assert counts=={1:4200,3:13000,5:5560,7:280}
var=F(sum(g*g*v for g,v in counts.items()),23040)-mu*mu
assert var==F(67,36)
assert F(L-cap,2*(n-1))*23040==224
print('Support histogram:',dict(sorted(counts.items())))
print('Variance:',var,'witness lower bound:',224)
