# A quiet pair-core triangle is a single-slot cyclic insertion holonomy

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-pair-core-triangle-quiet-insertion-holonomy`

**Summary:** Let T be the fixed three-vertex core in a shortest pair-core triangle a,b,c from SV29868, so T+ab, T+bc, T+ca are Hamiltonian five-supports. Choose one Hamilton path on each support. If any neighboring comparison is R435-nonquiet, explicit Reverse-Ear geometry is already present. If all three comparisons are R435-quiet and U=T+{a,b,c} is non-Hamiltonian, then the three paths induce one common linear order on T, each exterior label has a well-defined insertion slot in that order, all three labels use the same slot, and their pairwise orders form a directed 3-cycle. Indeed, if the slots are not all equal, merging the three compatible orders gives a Hamilton P6 on U. If all slots agree but the pair-order tournament on a,b,c is transitive, four short R3 dichotomies, one for each possible slot, force a Hamilton P6. Thus the only pairwise-quiet non-Hamiltonian triangle is a literal one-gap cyclic insertion defect. This compresses the triangle nucleus from three path comparisons to one physical slot carrying a 3-cycle; it does not yet consume that cyclic defect.

### 1. Pair-core triangle setup
Retain a shortest pair-core triangle from `universal-one-extension-four-set-girth-four-compression` SV29868. Write the fixed three-vertex core as T and the exterior triangle labels as a,b,c. Thus the three five-supports

  T+{a,b},   T+{b,c},   T+{c,a}

are Hamiltonian. Choose and retain actual Hamilton paths

  P_ab on T+{a,b},
  P_bc on T+{b,c},
  P_ca on T+{c,a}.                                      (QT.1)

Put U=T+{a,b,c}. If U is Hamiltonian, its Hamilton P6 is already a fresh proper path representative for the global maximum-three-forest program by smallest-counterexample minimality, so the only local residue of interest is the case that U is non-Hamiltonian.

If any pair among (P_ab,P_bc),(P_bc,P_ca),(P_ca,P_ab) is R435-nonquiet, retain the explicit R435 output and leave the present quiet analysis. Assume from now on that all three comparisons are R435-quiet.

### 2. Quietness produces three compatible insertion coordinates
Because P_ab and P_bc are R435-quiet, their common four vertices T+{b} occur in one common linear order. The same holds for T+{c} in P_bc,P_ca and for T+{a} in P_ca,P_ab. In particular the three paths induce one common linear order

  K=(u,v,w)                                               (QT.2)

on T. Each exterior label x in {a,b,c} therefore occupies one well-defined insertion slot sigma(x) among the four gaps

  before u,   u|v,   v|w,   after w,                     (QT.3)

and it occupies that same slot in both Hamilton paths containing x. Whenever two labels have the same slot, their relative order in their common Hamilton path is also retained.

### 3. Distinct slots glue to a Hamilton six-path
Suppose the three slots are not all equal. Merge a,b,c into K according to their slot positions and, when exactly two labels share a slot, use their retained relative order from the Hamilton path containing that pair. Since not all three labels occupy one slot, every consecutive triple of the resulting six-vertex word omits at least one of {a,b,c}. Hence that consecutive triple lies in one of the supports of (QT.1), and its relative order is exactly the retained order there. Every consecutive triple is therefore tight. The merged word is a Hamilton P6 on U, contradiction.

Consequently any pairwise-quiet non-Hamiltonian survivor has

  sigma(a)=sigma(b)=sigma(c).                             (QT.4)

### 4. A transitive pair order in the common slot also forces P6
The three retained pair orders in the common slot define a tournament on {a,b,c}. Suppose it is transitive. Relabel so that

  a<b<c                                                    (QT.5)

in the sense that P_ab places a before b, P_bc places b before c, and P_ac places a before c. We show directly that every possible common slot forces a P6.

If the slot is before u, the retained paths include

  a,b,u,v,w ;  b,c,u,v,w ;  a,c,u,v,w.

The two six-orders

  b,a,c,u,v,w
  c,a,b,u,v,w

have every required turn certified except respectively (b,a,c) and (c,a,b), which are complete reversals. By R3 exactly one is tight, so one order is a P6.

If the slot is u|v, use

  a,u,b,c,v,w
  b,u,a,c,v,w.

All turns are certified except respectively (a,u,b) and (b,u,a), again complete reversals; R3 gives a P6.

If the slot is v|w, use

  u,v,a,b,w,c
  u,v,a,c,w,b.

All turns are certified except respectively (b,w,c) and (c,w,b); R3 gives a P6.

If the slot is after w, use

  u,v,w,a,c,b
  u,v,w,b,c,a.

All turns are certified except respectively (a,c,b) and (b,c,a); R3 again gives a P6.

Thus the pair-order tournament cannot be transitive.

### 5. Quiet triangle normal form
Every tournament on three vertices is transitive or cyclic. Therefore a pairwise-R435-quiet pair-core triangle with non-Hamiltonian six-union U has exactly one possible local form:

1. the three Hamilton five-paths share one literal order K=(u,v,w) on T;
2. a,b,c all occupy one common insertion slot of K;
3. their retained pair orders form a directed 3-cycle.       (QT.6)

Hence a quiet pair-core triangle is not diffuse path-order ambiguity. It is one physical insertion gap carrying a cyclic three-label holonomy. Any failure of (QT.6) yields either explicit R435 geometry or a Hamilton P6 and therefore a fresh global representative.

No claim is made here that the cyclic same-slot defect itself is impossible. Accepted R195 supplies additional Hamilton punctures of U, but local six-vertex density alone does not automatically extinguish this cyclic insertion cell; its remaining consumption should use the simultaneous donor/portal complement geometry of the pair-core nucleus.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```
