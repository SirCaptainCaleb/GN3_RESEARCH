# Reproducible exact finite proof certificate for pointwise-sensitivity elimination

This standard-library Python certificate supports Item `nori_pointwise_sensitivity_elimination_even_q6_20261008`. It is a forced-implication proof, not a SAT/MILP optimization. The analytic companion lemma derives the seeded four-orientation constant block from one local exterior sensitivity. The code checks both remaining constant bits.

```python
from collections import deque
from itertools import permutations, product

V=tuple(range(6))
def face(order,ones):
    order=tuple(order)
    E=tuple(k for k in V if k not in order)
    a=(order,tuple((ones>>k)&1 for k in E))
    b=(order[::-1],tuple(1^v for v in a[1]))
    return min(a,b)
def windows(p,x):
    crossed=0
    result=[]
    for i in range(4):
        free=sum(1<<d for d in p[i:i+3])
        result.append(face(p[i:i+3],(x^crossed)&~free&63))
        crossed ^= 1<<p[i]
    return tuple(result)

for p in permutations(V):
    for x in range(64):
        assert windows(p[::-1],x)==windows(p,x)[::-1]

ids={}
paths=set()
for p in permutations(V):
    if p>p[::-1]: continue
    for x in range(64):
        paths.add(tuple(ids.setdefault(f,len(ids)) for f in windows(p,x)))
paths=tuple(paths)
touches=[[] for _ in ids]
for i,p in enumerate(paths):
    for v in p: touches[v].append(i)
bad=[w for w in product((0,1),repeat=4)
     if sum(w[j]!=w[j+1] for j in range(3))>=2]
assert (len(ids),len(paths),len(bad))==(480,23040,8)

def verify(K):
    seed={ids[face((0,1,2),0)]:0,ids[face((0,1,2),1<<3)]:1}
    for triple in [(3,4,5),(3,5,4),(5,4,3),(4,5,3)]:
        E=[i for i in V if i not in triple]
        for b in range(8):
            m=sum(((b>>j)&1)<<E[j] for j in range(3))
            i=ids[face(triple,m)]
            assert i not in seed or seed[i]==K
            seed[i]=K
    assert len(seed)==18
    known=dict(seed)
    queue=deque(i for v in known for i in touches[v])
    while queue:
        p=paths[queue.popleft()]
        options=[w for w in bad
                 if all(v not in known or known[v]==w[j]
                        for j,v in enumerate(p))]
        if not options: return len(known)
        for j,v in enumerate(p):
            if v not in known and all(w[j]==options[0][j]
                                       for w in options):
                known[v]=options[0][j]
                queue.extend(touches[v])
    raise AssertionError("No contradiction for K="+str(K))

assert verify(0)==396
assert verify(1)==228
print("PASS: 480 variables, 23040 constraints, both branches refuted")
```
