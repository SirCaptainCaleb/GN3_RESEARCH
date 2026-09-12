# Stationary quiet recurrence needs two common crosses; double-p punctures are the exceptional fragmentation cell

**Workspace:** D17
**State:** working
**Key:** `stationary-common-cross-multiplicity`

**Summary:** Corrected stationary two-cross ledger. Every quiet exact cover has at least two common crosses, and p-Z is impossible. For c=2 the exact excess-block identity is e_A+e_B+e_Z=m_A+m_B. A single p-incidence with a class forces one extra block there. Two p-incidences with the same class require only one extra block when the full class+p segment is the exact quiet final-gap puncture order; the previous stronger b_C>=1+m_C claim was false. Thus Z is full except in one double-same-class final-gap exceptional family. This corrected unit replaces the DR17.78 overclaim and is not yet a subthreshold-cover consumer.

### Setup and retained conclusions
Retain `stationary-two-seam-common-cross`. Thus A=X-{u_X}, B=Y-{u_Y}, |A|=|B|=k-1, |Z|=k, and W=A disjoint-union B disjoint-union Z disjoint-union {p}. Every exact two-cover T of W has a selected common-cross state of type A-B, A-Z, B-Z, or p-Z. The saturated petal punctures A+p and B+p are Hamiltonian, while X+p,Y+p,Z+p are non-Hamiltonian.

For T let c(T) count selected transitions of types A-B,A-Z,B-Z,p-Z, and let d(T) count selected p-A or p-B transitions. These exhaust interclass transitions. Call the cell QUIET only relative to the exact terminal-puncture/source-anchored packets on A+p and B+p.

The preceding argument that c(T)=1 forces either Z+p Hamiltonian or explicit source-visible R435 geometry remains valid. Therefore every quiet T satisfies c(T)>=2.

### Correct exact block identity for c(T)=2
Assume T is quiet and c(T)=2. Contract maximal A-,B-,Z-, and {p}-blocks along the two T rails. Write b_A,b_B,b_Z for the class-block counts and put

  e_A=b_A-1,  e_B=b_B-1,  e_Z=b_Z-1.

Let m_A,m_B be the numbers of selected p-A,p-B incidences, so d=m_A+m_B<=2. The contracted cover has b=(b_A+b_B+b_Z+1) vertices and theta=c+d=2+d edges, and consists of two paths. Hence

  e_A+e_B+e_Z=d.                                      (1)

This identity is exact.

### Quiet fragmentation forced by p-incidences
If m_A=1 and e_A=0, then all of A is one block adjacent to p. Thus A+p is a contiguous Hamilton endpoint segment of a T rail. Its order is either p followed by all of A or all of A followed by p. The first is outside the quiet terminal-puncture forms, while the second is the tail form and is R435-nonquiet against the retained source-anchored puncture packet. Hence in a quiet cover

  m_A=1 => e_A>=1.

The same holds for B.

If m_A=2, then p lies between two A-blocks, so e_A>=1. Here the previous DR17.78 argument incorrectly claimed e_A>=2. There is one legitimate equality case: if e_A=1, the two A-blocks exhaust A and A+p is a contiguous Hamilton path with p internal. By `terminal-puncture-last-gap`, quietness then forces this full puncture path to be exactly the retained final-gap order

  (x_1,...,x_{k-2},p,x_{k-1})

for the retained A-order (up to the exact common dual orientation). Thus

  m_A=2 and e_A=1 => A+p is the exact quiet final-gap puncture path.    (2)

If that exact order is absent, e_A>=2. Dually for B. This is the only correction needed to the p-incidence lower bounds.

### p-Z is still impossible
Suppose T selects a p-Z transition. Since p has path-cover degree at most two, d<=1. If d=0, (1) gives e_A=e_B=e_Z=0. If d=1, the unique p-A or p-B incidence forces one extra block in that class by the preceding paragraph, and (1) again gives e_Z=0. Hence Z is one full block whenever a p-Z transition occurs. The selected p-Z state then makes Z+p a contiguous Hamilton subpath, contradicting the fixed-point non-Hamiltonicity of Z+p. Therefore

  no quiet c=2 cover contains p-Z.

So the two common crosses are chosen from A-B,A-Z,B-Z.

### Complete corrected fragmentation list
Equation (1), p-Z exclusion, and the quiet p-incidence rules give the following exhaustive block-count possibilities.

(0) d=0. Then A,B,Z are each one full block and p is an isolated rail vertex. The other T rail is a three-block Hamilton path through A,B,Z using exactly two of the three cross types.

(1) d=1. Up to A/B duality, m_A=1. Then e_A=1 and e_B=e_Z=0. Thus A has exactly two blocks, while B and Z are full blocks; p is an endpoint adjacent to one A-block.

(2a) d=2 with m_A=m_B=1. Then e_A=e_B=1 and e_Z=0. Thus A and B each have exactly two blocks and Z is full; p is internal with one A and one B incidence.

(2b) d=2 with m_A=2,m_B=0, or the B-dual. If e_A=2, then e_B=e_Z=0: A has three blocks and B,Z are full. If e_A=1, then A+p is forced to be the exact quiet final-gap puncture path by (2), and exactly one further excess block remains. Hence precisely one of B or Z has two blocks and the other is full.

In particular the earlier DR17.78 conclusion b_Z=1 in every quiet c=2 cover was too strong. Z can fragment only in the exceptional double-same-class cell where p uses both incidences on A (or both on B), that class+p is the exact quiet final-gap puncture path, and the unique remaining excess block is spent on Z.

### Current consumer target
Outside the exceptional final-gap cell, Z is a single full Hamilton block. The literal stationary seams u_X-Z and u_Y-Z can then be tested directly against the end at which this Z-block sits. If restoring either omitted terminal produces a rail of size at most 2k-1, the complementary singleton-cover rail is automatically below 2k and `subminimum-source-saturation` closes the branch.

The exceptional cell is more rigid rather than generic: it retains an exact final-gap puncture path on A+p or B+p and a two-block Z fragmentation. It should be consumed separately using the retained reverse terminal turn from `terminal-puncture-last-gap`, not folded into a false universal full-Z assertion.

Status: corrected working exposition. The c=1 reduction and p-Z exclusion are retained; the DR17.78 universal b_Z=1 claim is withdrawn. No subthreshold singleton cover is yet claimed for the surviving c=2 cells.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R953"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R961"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    }
]
```
