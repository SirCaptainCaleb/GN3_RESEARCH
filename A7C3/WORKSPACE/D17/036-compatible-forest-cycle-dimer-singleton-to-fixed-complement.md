# The remaining cycle-dimer singleton branch exports to a two-row fixed-complement puncture cylinder

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-cycle-dimer-singleton-to-fixed-complement`

**Summary:** Let Q be a movable tight cycle rail, D={x,y} a dimer rail, and V the third rail of a maximum three-forest. Apply the cycle-dimer paired-gate analysis with common tested endpoint x and again with x,y swapped. By SV29294 the coherent fan alternative in either run already yields a universally one-extendable four-set, while SV27921 consumes paired DOUBLE. Hence if no universal one-extension core is produced, the x-run must contain a singleton-producing SLIDE with singleton y, yielding an exact singleton-deletion cover H-y=P_x|V where P_x is Hamilton on Q union {x} and x is a boundary endpoint; the swapped run similarly yields H-x=P_y|V with P_y Hamilton on Q union {y} and the same literal complement V. The active support Omega=V(Q) union {x,y} is non-Hamiltonian, since a Hamilton Omega together with V would two-cover H. Thus the residual cycle-dimer branch is an actual two-row live puncture cylinder on Omega with live labels {x,y} and fixed complement V, directly eligible for neighboring-support R435/currentization machinery. No Hamilton-order synchronization between P_x and P_y is assumed.

### 1. Setup and the completed one-endpoint analysis
Let H be a hypothetical smallest Strong Level-(1) counterexample and retain a literal maximum spanning three-forest

  Q | D | V,

where Q is the support of a proper tight cycle, D={x,y} is a dimer component, V is a nonempty third rail, and every cyclic break of Q is available through the movable-break/CYCLE-ROTATE family.

Fix the common tested dimer endpoint x and apply the paired cycle-edge/dimer analysis of SV27921, SV28505 and SV29294. These three sections together give the following exhaustive outputs for this x-run:

1. a paired DOUBLE yields a universally one-extendable four-set, in fact a universal Hamilton four-core in SV27921;
2. a coherent non-singleton growth fan yields a universally one-extendable four-set by SV29294; or
3. some paired rim edge has a singleton-producing SLIDE, whose singleton is y.

Therefore, under the standing assumption that no universally one-extendable four-set has yet been produced, outcome (3) must occur.

### 2. The x-run gives an exact H-y cover with fixed complement V
A singleton-producing SLIDE in the x-run has one of the two literal forms recorded in SV28505:

  (Q_i,x) | (y) | V,                                  (SF.1)

or

  (x,Q_i) | (y) | V,                                  (SF.2)

for some cyclic break Q_i of Q, after the corresponding choice of orientation/index. In either form the non-singleton rail P_x is a literal Hamilton path on

  V(Q) union {x}.

Delete the singleton y from (SF.1) or (SF.2). Then

  H-y = P_x | V                                       (SF.3)

is a literal spanning two-path cover. It is exact: if H-y were Hamiltonian, adjoining the singleton y would not by itself close H, but more directly H is a smallest counterexample and hence pc(H-y)<=2, while (SF.3) already supplies two nonempty rails; if a one-path cover existed, that Hamilton path together with the vacuous singleton y would be a spanning two-cover of H, contradiction. Thus pc(H-y)=2.

The path P_x retains x as a boundary endpoint and the entire Q-support in its inherited cyclic order with one break. The other rail is literally the same V as in the source maximum three-forest.

### 3. Swap x and y
Now rerun exactly the same paired-gate analysis with the dimer labels exchanged: take y as the common tested endpoint and x as its mate. The hypotheses are symmetric because the dimer component has no turn constraint and may be oriented freely.

Again, if a paired DOUBLE or coherent fan occurs, the previous sections produce a universally one-extendable four-set. Excluding that output, a singleton-producing SLIDE must occur, now with singleton x. Hence there is a literal Hamilton path P_y on

  V(Q) union {y}

such that

  H-x = P_y | V                                       (SF.4)

is an exact two-cover, with y a boundary endpoint of P_y. The complement rail is the SAME literal path V, with the same support, order, and selected states as in (SF.3).

No relation is asserted between the cyclic break used by P_x and the one used by P_y, and no Hamilton-order synchronization of their common Q vertices is assumed.

### 4. The active support is non-Hamiltonian
Put

  Omega = V(Q) union {x,y}.                            (SF.5)

If Omega had a Hamilton tight path, that path together with the disjoint literal rail V would be a spanning two-cover of H, contradicting pc(H)>2. Therefore

  Omega is non-Hamiltonian.                            (SF.6)

Combining (SF.3)-(SF.6), the no-core residue contains two neighboring Hamilton puncture rows on the same non-Hamiltonian active support Omega:

  Omega-y : P_x,
  Omega-x : P_y,

and both rows carry the identical fixed Hamilton complement V in H.

### 5. Fixed-complement puncture-cylinder export
Thus the last cycle+dimer singleton output is not an isolated singleton state. It is a genuine two-row live puncture cylinder:

  active support: Omega=V(Q) union {x,y},
  live labels: {x,y},
  puncture paths: P_x on Omega-y and P_y on Omega-x,
  fixed complement: V.

This is exactly the representative structure needed for neighboring-support comparison by accepted R435 and for the current fixed-complement currentization machinery. If the P_x/P_y comparison emits a reverse trimer, adjacent selected reversal, or proper cycle, the corresponding current D17 consumers may be invoked with their hypotheses checked; if the comparison is quiet, its actual common-order/insertion-slot data must be retained rather than assumed.

Consequently the full cycle+dimer branch now exports as follows:

- paired DOUBLE or coherent fan -> universal one-extension core -> SV26947 pair-core holonomy;
- singleton-producing SLIDE -> two-row fixed-complement puncture holonomy (SF.3)-(SF.6).

No claim is made here that the two-row cylinder itself closes H or that one R435 output is guaranteed to be productive. The result is an exact parent-level export of the formerly isolated singleton branch.
