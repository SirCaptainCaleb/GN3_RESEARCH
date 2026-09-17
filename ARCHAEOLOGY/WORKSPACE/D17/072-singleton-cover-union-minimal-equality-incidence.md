# A minimum equality separator has a third-atom incidence at every label

**Workspace:** D17
**State:** established
**Key:** `singleton-cover-union-minimal-equality-incidence`

**Summary:** Let S be a minimum-cardinality nonempty set with c(U-S)=|S|+1. For |S|>=2, every y in S is adjacent in U to at least three distinct components of U-S. Otherwise if y touches exactly two components, restoring y merges only those two and S-{y} still attains equality, contradicting minimality. In the three-component 2-cut this forces both separator vertices p,q to contact all three Hamilton atoms. The parallel bridge rows use only the A/B contacts, so actual selected p-C and q-C states must occur in other singleton fibers. Thus the hard double-bridge cell necessarily carries cross-fiber return contacts to its fixed Hamilton complement.

### Minimum equality separator
Retain the selected-edge union U of a chosen singleton-cover family and the separator inequality

  c(U-S) <= |S|+1

from `singleton-cover-union-separator-row` for every nonempty S.

Choose a nonempty equality set S of minimum cardinality:

  c(U-S)=|S|+1.

Write s=|S| and let the components of U-S be the equality atoms.

### Every surviving separator label touches at least two atoms
Assume s>=2 and fix y in S. Let d_S(y) be the number of distinct components of U-S containing a U-neighbor of y.

Consider U-(S-{y}). The vertex y is restored while every other separator label remains deleted. The d_S(y) atoms adjacent to y and the vertex y itself lie in one connected component; every atom not adjacent to y remains a separate component. Hence

  c(U-(S-{y})) = (s+1-d_S(y)) + 1 = s+2-d_S(y).

The separator bound applied to the nonempty set S-{y}, of size s-1, gives

  s+2-d_S(y) <= s,

so d_S(y)>=2.

### Minimality forces a third atom
If d_S(y)=2, then the displayed count is exactly s. Thus

  c(U-(S-{y}))=s=|S-{y}|+1,

so S-{y} is a smaller nonempty equality set, contradicting the choice of S. Therefore every y in a minimum equality separator of size at least two satisfies

  d_S(y) >= 3.

This is a global incidence surplus not visible in any one equality row. In the row C_x for x in S, each retained separator y in S-{x} has quotient degree exactly two and therefore uses exactly two atom incidences. Minimal equality says that globally y has at least one further atom neighbor beyond the two incidences used by any fixed row whenever those two do not already exhaust its atom neighborhood.

### The minimum three-component 2-cut
Take s=2, S={p,q}, and suppose U-{p,q} has the three Hamilton atoms A,B,C. Since there are only three atoms, the preceding theorem gives

  d_S(p)=d_S(q)=3.

Thus both p and q have actual U-adjacencies to all three atoms.

In the parallel double-bridge residue of `singleton-cover-union-two-cut-doublebridge`, the two distinguished singleton fibers are

  C_p=(A-q-B)|C,
  C_q=(A-p-B)|C.

These two covers already realize the four incidences q-A,q-B,p-A,p-B. They do not select any p-C or q-C state. Because p and q nevertheless each touch C in U, there exist other singleton fibers in the chosen family that select a physical p-C state and a physical q-C state. These contacts are actual realizable cover states, not support-only graph edges invented after the fact.

Consequently the hard 2-cut parent is strictly stronger than the static parallel bridge profile: it consists of the parallel bridge row, the dual R542/R696 terminal packets on C with witnesses {p,q}, and cross-fiber selected returns from both p and q into the fixed complement C.

The natural consumer target is CROSS-FIBER RETURN CURRENTIZATION: use one or both actual p-C/q-C selected states to move the bridge labels onto the complement in a common residue, or show that failure of such currentization forces source-labelled reversal geometry, a legal singleton support transfer, fixed-support R561, or closure.

Status: complete elementary deduction from the separator inequality and minimality of S; not independently reviewed as a section.
