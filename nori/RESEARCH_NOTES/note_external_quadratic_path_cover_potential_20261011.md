# Archive: quadratic component-size potential for path-cover moves

- Stable ID: note_external_quadratic_path_cover_potential_20261011
- Author: unspecified; session provenance retained
- Primary home: project:nori
- Labels: historical_scope, archive
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r5005_1
- Updated session: session_nori_r5005_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Elementary potential identities for generic path-cover optimization, under explicitly specified legal moves. No established implication for current NORI goals. Pending general/path-cover toolkit relocation; the original full Toolkit text remains archived.

## Original Toolkit source: quadraticpotential01

QUADRATIC COMPONENT-SIZE POTENTIAL

For a q-component path cover C=P_1|...|P_q, put s_i=|P_i| and
Phi(C)=sum_i s_i^2.

1. VARIANCE FORM.
Since sum_i s_i=n,
Phi(C)=n^2/q+sum_i(s_i-n/q)^2.
Thus, for fixed n and q, minimizing Phi is exactly minimizing component-size variance. The integer minimum occurs when component orders differ pairwise by at most one.

2. ONE-VERTEX TRANSFER.
For a legal transfer from a component of order a to one of order b,
Delta Phi=(a-1)^2+(b+1)^2-a^2-b^2=2(b-a)+2.
Therefore:
- a>=b+2: strict descent by 2(a-b-1);
- a=b+1: Phi-neutral;
- a=b: Phi increases by 2;
- moving from smaller to larger strictly increases Phi whenever the sizes differ.

3. TWO-COMPONENT REPARTITION.
For fixed m=a+b,
a^2+b^2=(m^2+(a-b)^2)/2.
Hence among legal two-covers of one fixed union, Phi order is exactly absolute-imbalance order.

4. EXTREMAL NORMALIZATION.
Fix a class of path covers together with its specified legal moves. If C is Phi-minimal in this class, every legal repartition of any component pair has imbalance at least that of the displayed pair. If C is Phi-maximal in this class, every legal local transfer that would increase imbalance is forbidden. This yields obstruction information even when no descent is available.

5. WELL-FOUNDEDNESS.
Phi is integer-valued and every strict one-vertex descent changes it by at least 2. Hence any strict-descent sequence is finite, with length at most (Phi(start)-Phi_min)/2.

6. METHOD.
Use Phi as a primary potential in two complementary ways:
- minimize it to force pairwise imbalance-minimality and expose local obstruction or equality structure;
- maximize it inside a constrained move class to forbid imbalance-increasing moves and orient any surviving transfer toward balance.
If the specified move graph has adjacent states of equal Phi, use a secondary structural invariant to distinguish those states.

This toolkit abstracts the same mechanism appearing in pairwise repartition, balanced-cover improvement, defect compression, and contiguous-block relocation.
