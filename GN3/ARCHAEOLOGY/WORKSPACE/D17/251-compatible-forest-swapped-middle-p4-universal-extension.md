# Two same-end P4 orders with swapped middle vertices force universal one-extension

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-swapped-middle-p4-universal-extension`

**Summary:** Pure five-vertex exact lemma, currently supported by a self-contained finite edge-order verification. If X={a,p,q,b} has both tight Hamilton orders (a,p,q,b) and (a,q,p,b), then every exterior d Hamilton-extends X. Indeed, if X+d were non-Hamiltonian, accepted R902 makes the five-set edge-orderable. Accepted R887 translates the two P4s into ap< pq, aq< pq, pq< pb, pq< qb. Exhaustive topological enumeration of all 120,960 total edge orders extending these four inequalities finds an increasing Hamilton P5 in every case, contradiction. Thus the swapped-middle same-end P4 reversal is a universal one-extension four-set, not a terminal same-support reversal packet. The finite verifier is exact but the section remains working/expository pending independent review or a conceptual proof.


### 1. Pure local statement
Let H be a Strong Level-(1) boundary tournament and let

  X={a,p,q,b}

be four distinct vertices. Assume both literal Hamilton P4 orders

  P=(a,p,q,b),
  P'=(a,q,p,b)                                      (SM.1)

are tight. Then for every vertex d outside X, the five-set X+d is Hamiltonian.

Equivalently, X is universally one-vertex Hamilton-extendable.

### 2. Reduction of a hypothetical bad fifth vertex to an edge order
Fix d outside X and suppose, for contradiction, that X+d has no Hamilton P5. Accepted R902 says every non-Hamiltonian five-vertex boundary tournament is edge-orderable. Thus the comparison orientation on the ten ordinary edges of K_{X+d} is realized by a strict total edge order.

By accepted R887, the four tight turns supplied by (SM.1) become the edge inequalities

  ap < pq,
  aq < pq,
  pq < qb,
  pq < pb.                                           (SM.2)

Hence it is enough to prove the following finite edge-order statement:

> Every strict total order of the ten edges of K_5 satisfying (SM.2) contains an increasing Hamilton path.

### 3. Exact finite verification
The following standard-library verifier enumerates every topological ordering of the ten K5 edges extending (SM.2). There are exactly 120960 such orders. At every leaf it checks all 5! vertex orders and asserts that at least one has strictly increasing consecutive edge labels.

```python
from itertools import combinations, permutations

V = ('a','p','q','b','d')
E = tuple(sorted(tuple(sorted(e)) for e in combinations(V,2)))

def edge(x,y):
    return tuple(sorted((x,y)))

constraints = (
    (edge('a','p'), edge('p','q')),
    (edge('a','q'), edge('p','q')),
    (edge('p','q'), edge('p','b')),
    (edge('p','q'), edge('q','b')),
)

pred = {e:set() for e in E}
for lo,hi in constraints:
    pred[hi].add(lo)

orders_checked = 0

def has_increasing_hamilton(order):
    rank = {e:i for i,e in enumerate(order)}
    for P in permutations(V):
        seq = [rank[edge(P[i],P[i+1])] for i in range(4)]
        if seq[0] < seq[1] < seq[2] < seq[3]:
            return True
    return False

def enumerate_extensions(prefix, remaining):
    global orders_checked
    if not remaining:
        orders_checked += 1
        assert has_increasing_hamilton(prefix)
        return
    available = [e for e in remaining if not (pred[e] & remaining)]
    for e in available:
        enumerate_extensions(prefix+(e,), remaining-{e})

enumerate_extensions((), frozenset(E))
assert orders_checked == 120960
```

There is no random choice, optimization solver, SAT package, or external dependency. The verification is exhaustive over precisely the edge-orderable branch supplied by R902.

### 4. Consequence
The assumed non-Hamiltonian five-set X+d would admit an edge order satisfying (SM.2), but Section 3 shows every such edge order has an increasing Hamilton P5. Under R887 that is a tight Hamilton P5 in X+d, contradiction.

Therefore every exterior d Hamilton-extends X.

### 5. Status and scope
This is a pure five-vertex exact statement. The present proof route is a complete finite edge-order verification plus accepted R887/R902. It is retained as working/expository mathematics and is not declared canonically certified by this write.

The statement is stronger than a wrap-failure conclusion: no R548 hypothesis is needed. Its intended use is as a terminal consumer for actual maximum-three-forest representatives whose same four-vertex rail appears in the two same-end swapped-middle orders (SM.1).


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R887"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    }
]
```