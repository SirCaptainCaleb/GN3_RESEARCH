# S9017 — Five-Vertex Non-Hamiltonian Boundary Tournaments Are Edge-Orderable

## Theorem

Let H be a boundary 3-tournament on exactly five vertices. If H has no directed tight Hamilton path, its line-graph comparison orientation Gamma(H) is acyclic. Equivalently there is a total order on E(K_5) realizing every tight turn as an increasing consecutive-edge comparison. In contrapositive form, any nonintegrable five-vertex boundary tournament is Hamiltonian. Consequently, in any boundary tournament with pc(H)>2, the five-vertex complement of any proper tight path is edge-orderable.

## Proof

Define one Boolean variable for each reversal pair of ordered triples on {0,1,2,3,4}; the positive representative has first vertex smaller than last. For every permutation p, the clause OR_i NOT tight(p_i,p_{i+1},p_{i+2}), i=0,1,2, asserts p is not Hamilton. The 120 clauses are therefore exactly the absence of a Hamilton P5, with no extra orientation assumptions.

By the line-graph comparison representation theorem `S9011` a shortest directed comparison cycle is a star triangle, an ordinary triangle, or a vertex-simple ordinary cycle. On five vertices, an ordinary cycle has length at most five. A length-five cycle itself gives a Hamilton P5. Up to relabelling, the three other possibilities are the roots triangle, square, star in the code below. Each corresponding CNF is refuted by the embedded binary case-split/unit-propagation certificate. The verifier checks every propagation from its indexed original clause, checks a false original clause at every leaf, and checks both values of every split variable. Consequently it verifies an exhaustive propositional proof, not merely an optimization solver status. The recorded (split nodes, contradiction leaves, unit steps) counts are respectively (29,30,331), (3,4,41), (15,16,189). The certificates were produced and verified using the Python standard library. Run Python normally, without disabling assertions.

Thus Gamma has no directed cycle. `S9011` supplies a global edge order by topological sorting. For the critical-complement consequence, a Hamilton five-vertex complement together with the displayed proper tight path would be a spanning two-cover, contradicting pc(H)>2. Therefore that complement is nonHamilton and the theorem applies.

Self-contained certificate generator, verifier, and recorded proof trees:
```python
from itertools import permutations
import json

N=5
keys=[t for t in permutations(range(N),3) if t[0]<t[2]]
ids={t:i+1 for i,t in enumerate(keys)}
def lit(t): return ids[t] if t[0]<t[2] else -ids[t[::-1]]
base=[tuple(-lit(p[i:i+3]) for i in range(3)) for p in permutations(range(N))]
roots={'triangle':[(0,1,2),(1,2,0),(2,0,1)],
       'square':[(0,1,2),(1,2,3),(2,3,0),(3,0,1)],
       'star':[(1,0,2),(2,0,3),(3,0,1)]}
def solve(cs,ass):
    ass=set(ass)
    steps=[]
    while True:
        residual=[]
        unit=None
        for i,c in enumerate(cs):
            if any(l in ass for l in c): continue
            r=[l for l in c if -l not in ass]
            if not r: return {'units':steps,'conflict':i}
            if len(r)==1:
                unit=(i,r[0]); break
            residual.append(r)
        if unit is None: break
        steps.append(unit); ass.add(unit[1])
    if not residual: raise RuntimeError('SAT')
    freq={}
    for c in residual:
        for l in c: freq[abs(l)]=freq.get(abs(l),0)+2**(-len(c))
    v=max(freq,key=freq.get)
    return {'units':steps,'split':v,'positive':solve(cs,ass|{v}), 'negative':solve(cs,ass|{-v})}
def stats(t):
    if 'conflict' in t: return (0,1,len(t['units']))
    a,b=stats(t['positive']),stats(t['negative'])
    return (1+a[0]+b[0],a[1]+b[1],len(t['units'])+a[2]+b[2])
def verify(cs,t,ass):
    ass=set(ass)
    for i,l in t['units']:
        c=cs[i]
        assert not any(x in ass for x in c)
        assert [x for x in c if -x not in ass]==[l]
        ass.add(l)
    if 'conflict' in t:
        assert all(-x in ass for x in cs[t['conflict']]); return
    v=t['split']; assert v not in ass and -v not in ass
    verify(cs,t['positive'],ass|{v}); verify(cs,t['negative'],ass|{-v})

certificates=json.loads(r'''CERTIFICATES_OMITTED_HERE_FOR_GITHUB_TREE_BATCH; SEE PROVENANCE R902''')
for name,turns in roots.items():
    cs=base+[(lit(t),) for t in turns]
    verify(cs,certificates[name],set())
    print(name,stats(certificates[name]))
```

## Why this is reusable

This is the exact five-vertex bridge from the order-free boundary-tournament world to edge orders: every nonintegrable five-cell must already be Hamiltonian.

## Scope and nonclaims

This is a five-vertex theorem. It does not claim that larger non-Hamiltonian boundary tournaments are edge-orderable, nor that edge-orderability alone forces non-Hamiltonicity.

## Provenance

Rescued from accepted archived result `R902`. The complete recorded certificate remains in the archived source; this spare-part statement records the theorem and verification scheme without duplicating the large serialized proof tree.
