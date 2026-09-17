# The cyclic same-slot pair-core triangle forces its middle puncture Hamiltonian and fully exits local holonomy

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-pair-core-triangle-middle-puncture-forced`

**Summary:** Exact finite theorem: in the SV31722 cyclic same-slot configuration on U={u,v,w,a,b,c}, where the three Hamilton P5s insert (a,b),(b,c),(c,a) into one common slot of T=(u,v,w), non-Hamiltonicity of U forces the middle puncture U-v to be Hamiltonian. A self-contained exact-reversal DPLL verifier checks the four insertion slots from 60 reversal-pair variables, with no external solver. Therefore the middle-puncture hypothesis of SV32787 is automatic. SV32787 then forbids quiet-or-selected-reversal-only behavior for any Hamilton path on U-v, forcing reverse-trimer or proper-cycle R435 geometry. Those outputs are already currentized by R4/SV25652 to actual or closed maximum-three-forest dynamics. Hence the pair-core triangle has no terminal quiet or selected-reversal-only residue at all; it fully exits local universal-core holonomy.


### 1. Exact six-vertex local theorem
Work in any exact-reversal tight-turn system on

  U={u,v,w,a,b,c}.

Fix the ordered common trimer

  T=(u,v,w).

Choose one of the four insertion slots of the word T. Suppose the three five-vertex orders obtained by inserting, in that SAME slot, the ordered exterior pairs

  (a,b),  (b,c),  (c,a)                                  (MP.1)

are all tight Hamilton paths on respectively

  T+{a,b}, T+{b,c}, T+{c,a}.                             (MP.2)

Assume U itself is non-Hamiltonian. Then

  U-v is Hamiltonian.                                     (MP.3)

Thus the puncture deleting the middle vertex v of the common trimer order is forced Hamiltonian. No R195 density hypothesis is needed.

### 2. Exact finite verification
The statement is an exact Boolean consequence of reversal antisymmetry. There are 60 reversal-pair variables on six vertices. For each of the four slots form the CNF consisting of:

1. the nine unit clauses certifying the three displayed Hamilton P5 orders;
2. for every permutation p of U, the clause saying at least one of its four consecutive turns is bad, encoding non-Hamiltonicity of U;
3. for every permutation p of U-v, the clause saying at least one of its three consecutive turns is bad, encoding non-Hamiltonicity of U-v.

Each of the four CNFs is UNSAT. The following standalone standard-library verifier rebuilds the exact clauses and checks UNSAT by exhaustive DPLL with unit propagation. Positive literals encode one representative of a complete-reversal pair and negative literals its reverse.

```python
from itertools import permutations

def cert(slot):
    V=range(6); T=(0,1,2)
    keys=sorted({(a,m,c) for m in V for a in V for c in V
                 if a<c and a!=m and c!=m})
    I={x:i+1 for i,x in enumerate(keys)}
    def L(t):
        a,m,c=t
        return I[(a,m,c)] if a<c else -I[(c,m,a)]
    C=[]
    for x,y in ((3,4),(4,5),(5,3)):
        p=T[:slot]+(x,y)+T[slot:]
        C += [(L(p[i:i+3]),) for i in range(3)]
    for p in permutations(V):
        C.append(tuple(-L(p[i:i+3]) for i in range(4)))
    W=(0,2,3,4,5)
    for p in permutations(W):
        C.append(tuple(-L(p[i:i+3]) for i in range(3)))
    def go(A):
        A=set(A)
        while True:
            R=[]; unit=None
            for c in C:
                if any(x in A for x in c):
                    continue
                r=[x for x in c if -x not in A]
                if not r:
                    return False
                if len(r)==1:
                    unit=r[0]; break
                R.append(r)
            if unit is None:
                break
            A.add(unit)
        if not R:
            return True
        f={}
        for c in R:
            for x in c:
                f[abs(x)]=f.get(abs(x),0)+2**(-len(c))
        z=max(f,key=f.get)
        return go(A|{z}) or go(A|{-z})
    return go(set())

for slot in range(4):
    assert not cert(slot)
```

The verifier contains no optimization solver, random choice, or external package. It exhausts both branches of every split. Hence (MP.3) is a finite exact-reversal theorem, not experimental MILP evidence.

### 3. Application to the quiet pair-core triangle
Retain the sole quiet local residue of SV31722. Its common trimer order is T=(u,v,w), its three exterior pair orders are cyclic exactly as in (MP.1), all three pairs occupy one common insertion slot, and its six-union U is non-Hamiltonian.

The theorem above therefore gives a Hamilton path R on

  U-v.                                                     (MP.4)

So the special middle-puncture hypothesis of SV32787 is automatic.

### 4. Selected-reversal-only behavior is impossible
Apply SV32787 to any actual Hamilton path R on U-v. At least one comparison of R with the three perimeter Hamilton paths must emit a reverse-trimer or proper-cycle R435 output. It cannot happen that every comparison is quiet or selected-reversal-only.

Therefore the selected-reversal branch retained in the more general fourth-puncture currentization SV32145, and its later fixed-complement/high-transition refinements for endpoint punctures, are not needed to consume the CYCLIC SAME-SLOT triangle itself: the forced middle puncture always gives the stronger output.

### 5. Full local triangle extinction
The reverse-trimer output is a proper graph-intrinsic tight path and hence is currentized by accepted R4 into an actual maximum spanning three-forest. The proper-cycle output is currentized by SV25652 into its closed movable-break family of actual maximum three-forests.

Consequently every shortest pair-core TRIANGLE produced by the universal one-extension four-set program has the following exhaustive local fate:

  an R435-nonquiet perimeter comparison already exists,
  or the quiet normal form SV31722 applies and the forced middle puncture produces reverse-trimer/proper-cycle geometry.  (MP.5)

In particular there is no terminal quiet triangle and no selected-reversal-only triangle residue. The pair-core triangle is fully exported to actual/closed maximum-three-forest holonomy.

This extinguishes the triangle as a local universal-core obstruction. It does not extinguish the resulting global maximum-forest closed classes.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```
