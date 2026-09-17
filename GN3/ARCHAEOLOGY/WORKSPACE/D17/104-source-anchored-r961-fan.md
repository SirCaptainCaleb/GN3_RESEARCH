# Source-anchored R961 triangles force a fixed common-complement R435 fan

**Workspace:** D17
**State:** established
**Key:** `source-anchored-r961-fan`

**Summary:** A corrected synchronization theorem independent of the withdrawn rooted-cycle shortcut. Fix a Hamilton order X of a saturated petal Omega=X+p. Outside explicit R435 output, any R961 constant-role triangle must contain p; HHH anchors at the first two X vertices and TTT at the last two. Every further puncture path is then R435-nonquiet against at least one member of this one fixed three-path packet. In the R953 three-petal fixed point all such puncture paths are actual singleton-deletion rails with the same Hamilton pair-union complement, yielding a source-visible common-complement R435 fan but not yet an absorber.

### 1. Setup and correction target

Let Omega=X union {p}, where X=(x_1,...,x_k) is one retained Hamilton tight path, k>=4. Assume Omega is non-Hamiltonian and Omega-y is Hamiltonian for every y in Omega. Apply accepted R961. Thus either R961 already returns explicit R435 geometry, or it supplies a constant-role directed triangle A,B,C with certified puncture paths P_A,P_B,P_C and common remainder order M=Omega-{A,B,C}. In the latter branch the exact forms are

HHH:
  P_A=(B,C,M),
  P_B=(C,A,M),
  P_C=(A,B,M),

or

TTT:
  P_A=(M,C,B),
  P_B=(M,A,C),
  P_C=(M,B,A).

The aim here is to compare these ACTUAL puncture paths with the independently retained source order X. No endpoint incidence is prescribed into the R961 shortest cycle. In particular this argument does not use the rooted-cycle shortcut withdrawn in DR17.54.

### 2. A fully X-quiet R961 triangle must contain p

Assume none of P_A,P_B,P_C has explicit R435 output when compared with X. By R435 contact monotonicity, the X-vertices encountered along each P-label occur in increasing X-order.

Suppose first that A,B,C all lie in X. In the HHH case P_A=(B,C,M) forces B<C in X-order, P_B=(C,A,M) forces C<A, and P_C=(A,B,M) forces A<B. These three inequalities form the impossible cyclic order

  A < B < C < A.

In the TTT case P_A=(M,C,B) forces C<B, P_B=(M,A,C) forces A<C, and P_C=(M,B,A) forces B<A, again impossible. Therefore, outside an explicit X-relative R435 event, p belongs to the R961 triangle.

Cyclically relabel the triangle so A=p, B=a, C=b.

### 3. Exact source-anchored quiet forms

In HHH we have

  P_p=(a,b,M),
  P_a=(b,p,M),
  P_b=(p,a,M).

The first path P_p is a Hamilton path on Omega-p=X. If it is R435-quiet relative to the Hamilton order X, then every X-contact occurs in increasing X-order; since both paths use all of X, their literal orders coincide. Hence

  a=x_1,  b=x_2,  M=(x_3,...,x_k),

and the three actual puncture paths are exactly

  P_p    =(x_1,x_2,x_3,...,x_k)=X,
  P_x1   =(x_2,p,x_3,...,x_k),
  P_x2   =(p,x_1,x_3,...,x_k).

Thus the HHH quiet triangle is anchored at the first source gap.

In TTT we have

  P_p=(M,b,a),
  P_a=(M,p,b),
  P_b=(M,a,p).

Again P_p is a Hamilton path on X and X-quietness forces P_p=X. Therefore

  M=(x_1,...,x_{k-2}),  b=x_{k-1},  a=x_k,

so the exact dual packet is

  P_p       =X,
  P_xk      =(x_1,...,x_{k-2},p,x_{k-1}),
  P_x{k-1}  =(x_1,...,x_{k-2},x_k,p).

Thus the TTT quiet triangle is anchored at the final source gap. No path has been reversed or reoriented.

### 4. Every further puncture path conflicts with the same anchored packet

Consider first the HHH packet. Fix j>=3 and let K be ANY Hamilton path on Omega-x_j. Suppose K were R435-quiet against all three fixed base paths P_p,P_x1,P_x2.

Quietness against P_p=X forces x_1 to occur before x_2 along K. Quietness against P_x1=(x_2,p,x_3,...) forces x_2 before p along K. Quietness against P_x2=(p,x_1,x_3,...) forces p before x_1 along K. Hence one linear order K would satisfy

  p < x_1 < x_2 < p,

impossible. Therefore every Hamilton path on Omega-x_j is R435-nonquiet against at least one member of the SAME packet {P_p,P_x1,P_x2}.

The TTT case is the exact role-correct dual. For j<=k-2, if K on Omega-x_j were quiet against P_p=X, P_xk=(...,p,x_{k-1}), and P_x{k-1}=(...,x_k,p), then K would satisfy respectively

  x_{k-1} < x_k,
  p < x_{k-1},
  x_k < p,

again an impossible cyclic order. Thus every non-anchor puncture path is R435-nonquiet against the same fixed TTT packet.

Consequently there is an exact dichotomy for the saturated petal with retained order X: either an explicit R435 event already occurs in the R961 triangle or in one of its comparisons with X, or the triangle is source-anchored as above and EVERY remaining puncture fiber supplies explicit R435 geometry against one fixed three-path packet. This is support-wide in the sense that the conclusion holds for every actual Hamilton order chosen on the further puncture support.

### 5. R953 three-petal specialization: common-complement currentization

In the R953 same-size fixed point, write the three Hamilton petals as L,B,Z, each of order k>=4, with L+p, B+p, Z+p non-Hamiltonian deletion-Hamiltonian and all three pair unions L+B, L+Z, B+Z Hamiltonian. Apply the preceding theorem to any chosen petal X in {L,B,Z}, using one retained Hamilton order of X.

Let Q be an actual Hamilton path on the union of the other two petals. For every y in X+p, the puncture support (X+p)-y is Hamiltonian and is disjoint from Q; together they form an actual exact singleton-deletion two-cover of H-y. Hence every member of the anchored R961 packet, and every further puncture path appearing in the forced R435 fan, is current in a singleton-deletion cover with the SAME literal Hamilton complement Q.

This repairs the synchronization defect that makes anonymous R435 output useless: the events are now source-visible, puncture-labelled, and common-complement current. It still does not consume the R435 event. Accepted R483 remains the fence. The next consumer must use the named comparison and its actual reversed state / reverse trimer / proper cycle to manufacture either an R561 boundary-reversed Hamilton dimer on one fixed petal or pair union, a legal tau=1/two-ear source transfer, or a spanning two-cover.

At the three-petal fixed point any R561 boundary-reversed Hamilton dimer on a Hamilton pair union is immediately fatal: R561 Hamilton-extends that pair union by a vertex y of the third petal, while the complementary puncture of the third saturated petal is Hamiltonian, giving a spanning two-cover. Therefore R561 on a fixed pair union is a legitimate terminal target for consuming this common-complement fan. No claim is made here that the fan alone forces such a dimer.

Status: complete internal working argument from accepted R961 and R435, with the final fixed-point currentization conditional on accepted R953. It deliberately avoids the withdrawn rooted-cycle shortcut. It is not canonically reviewed and does not close Universal Source-Crossing Absorption.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R961"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "conditional_dependency",
        "revision_id": "R953"
    },
    {
        "relation": "comparison",
        "revision_id": "R561"
    }
]
```
