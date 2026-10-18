#!/usr/bin/env python3
"""Search for a Q5 fixed coloring with every two-projective-square
induced 2-SAT problem satisfiable. SciPy/HiGHS binary MILP.

Run: python scripts/nori_two_square_q5_milp.py
Status 2 (infeasible) certifies universal two-square forcing in Q5.
"""
from itertools import combinations, permutations
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix

def generate(n=5):
    top=(1<<n)-1
    orb={}
    sides={}
    for i in range(n):
        for x in range(1<<n):
            u=x&~(1<<i)
            v=(x^top)&~(1<<i)
            a=min(u,v)
            orb.setdefault((i,a),len(orb))
            sides[x,i]=(orb[i,a],int(u!=a))
    free=[j for (i,a),j in orb.items() if i<2]
    fixed=[j for (i,a),j in orb.items() if i>=2]
    fi={j:k for k,j in enumerate(free)}
    ci={j:k for k,j in enumerate(fixed)}
    paths=[]
    for root in range(1<<(n-1)):
        for order in permutations(range(n)):
            x=root; F=[];V=[]
            for i in order:
                j,s=sides[x,i]
                (V if i<2 else F).append(((fi if i<2 else ci)[j],s))
                x^=1<<i
            paths.append((F,V))
    squares=set()
    for x in range(1<<n):
        square=frozenset((
            fi[sides[x,0][0]],fi[sides[x^2,0][0]],
            fi[sides[x,1][0]],fi[sides[x^1,1][0]]))
        assert len(square)==4
        squares.add(square)
    squares=sorted(squares,key=lambda S:min(S))
    return len(fixed),len(free),paths,squares

def solve(n=5,seconds=90):
    nf,nv,paths,squares=generate(n)
    pairs=list(combinations(range(len(squares)),2))
    index={}; count=nf
    for p in pairs:
        for x in sorted(squares[p[0]]|squares[p[1]]):
            index[p,x]=count
            count+=1
    owner={x:a for a,S in enumerate(squares) for x in S}
    rows=[];cols=[];vals=[];lo=[];hi=[]
    done=set()
    for F,V in paths:
        a=owner[V[0][0]];b=owner[V[1][0]]
        for p in pairs:
            if a not in p or b not in p:continue
            edge=tuple(F)+tuple((index[p,x],s) for x,s in V)
            if (p,edge) in done:continue
            done.add((p,edge))
            t=sum(s for x,s in edge)
            r=len(lo)
            for x,s in edge:
                rows.append(r);cols.append(x);vals.append(1-2*s)
            lo.append(1-t)
            hi.append(n-1-t)
    A=coo_matrix((np.array(vals,dtype=float),(rows,cols)),
                 shape=(len(lo),count)).tocsr()
    print(f'Q{n}: {len(squares)} projective squares, {len(pairs)} two-square tests,',
          f'{count} binary variables, {len(lo)} NAE-path constraints',flush=True)
    result=milp(np.zeros(count),integrality=np.ones(count),
                bounds=Bounds(np.zeros(count),np.ones(count)),
                constraints=LinearConstraint(A,np.array(lo),np.array(hi)),
                options={'time_limit':seconds,'disp':True})
    print('Status:',result.status,result.message)
    if result.x is not None:
        print('Fixed-color bitmask:',hex(sum(
            int(result.x[i]>0.5)<<i for i in range(nf))))
    return result

if __name__=='__main__':
    solve()
