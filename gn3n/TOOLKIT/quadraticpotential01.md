# Quadratic component-size potential under path-cover moves

**Summary:** Quadratic component-size potential under path-cover moves

## Statement

For a path cover C=P_1|...|P_q with component orders s_i and total order n, define Phi(C)=sum_i s_i^2. For fixed n and q, Phi differs from the size-variance sum_i(s_i-n/q)^2 only by n^2/q. A one-vertex transfer a->a-1, b->b+1 changes Phi by 2(b-a)+2; hence transfers from a component at least two larger into a smaller component strictly decrease Phi, while transfers between equal components strictly increase it. More generally, for a fixed two-component union, comparing Phi is equivalent to comparing absolute component-size imbalance. Within any specified class of path covers and specified legal moves, a Phi-minimal cover admits no legal repartition with smaller imbalance on the changed pair, a Phi-maximal cover admits no legal transfer that increases Phi, and every strict Phi-descent sequence is finite.

## Body

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

## Metadata

- ID: quadraticpotential01
- Kind: toolkit
- Version: 2
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
